"""Vee's sinkhole pool for a top-down pixel-art lake.
pip install numpy pillow     then:  python sinkhole.py [seed] [I|J|L] [--steps]
Writes sinkhole_<look>_<seed>.png (transparent outside the pool) and a 4x preview on lake colour."""
import sys
import numpy as np
from PIL import Image, ImageFilter, ImageDraw

ARGS = [a for a in sys.argv[1:] if not a.startswith("--")]
STEPS = "--steps" in sys.argv          # also save one picture per step (handy for a video)
SEED = int(ARGS[0]) if len(ARGS) > 0 else 7
LOOK = ARGS[1] if len(ARGS) > 1 else "L"
W, H = 220, 180
rng = np.random.default_rng(SEED)
yy, xx = np.mgrid[0:H, 0:W]

LAKE = (70, 146, 76)
# shallow -> deep, each step one value darker (tops), plus the wall faces and lit lips for each step
TOPS = [(62, 142, 80), (42, 128, 80), (22, 106, 70), (4, 82, 56)]
FACES = [(30, 114, 74), (12, 92, 62), (2, 74, 50)]
LITS = [(72, 152, 88), (52, 138, 86), (32, 120, 78)]
CREVICE, CAST, CORE = (0, 60, 42), (8, 86, 60), (0, 66, 46)
MOSS, MOSS_LIT, MOSS_SHADE, ROOT = (58, 150, 84), (86, 172, 100), (24, 112, 72), (40, 92, 64)


def noise(cell, amp):
    """smooth value noise: random grid, blown up with bicubic"""
    g = rng.random((H // cell + 2, W // cell + 2))
    img = Image.fromarray((g * 255).astype(np.uint8)).resize((W + 2 * cell, H + 2 * cell), Image.BICUBIC)
    return (np.asarray(img)[:H, :W] / 255.0 - 0.5) * 2 * amp


def distance_in(mask):
    """px from each pool pixel to the nearest outside pixel (two-pass chamfer, good enough for art)"""
    big = 10 ** 6
    dist = np.where(mask, big, 0).astype(float)
    a, b = 1.0, 1.4142
    for y in range(H):
        for x in range(W):
            if dist[y, x]:
                v = dist[y, x]
                if x: v = min(v, dist[y, x - 1] + a)
                if y: v = min(v, dist[y - 1, x] + a)
                if x and y: v = min(v, dist[y - 1, x - 1] + b)
                if y and x < W - 1: v = min(v, dist[y - 1, x + 1] + b)
                dist[y, x] = v
    for y in range(H - 1, -1, -1):
        for x in range(W - 1, -1, -1):
            if dist[y, x]:
                v = dist[y, x]
                if x < W - 1: v = min(v, dist[y, x + 1] + a)
                if y < H - 1: v = min(v, dist[y + 1, x] + a)
                if x < W - 1 and y < H - 1: v = min(v, dist[y + 1, x + 1] + b)
                if y < H - 1 and x: v = min(v, dist[y + 1, x - 1] + b)
                dist[y, x] = v
    return dist


def snap(name, rgb, mask):
    if STEPS:
        bg = np.zeros((H, W, 3), np.uint8)
        bg[:] = LAKE
        bg[mask] = rgb[mask]
        Image.fromarray(bg).resize((W * 3, H * 3), Image.NEAREST).save(f"step_{name}.png")


def shift(m, dx, dy):
    return np.roll(np.roll(m, dy, 0), dx, 1)


# 1. the outline: two overlapping blobs, softened and wobbled (in a game, start from the hole's own tiles)
blob = np.zeros((H, W))
for cx, cy, r in ((80, 85, 52), (145, 100, 42)):
    blob = np.maximum(blob, 1 - np.hypot(xx - cx, (yy - cy) * 1.15) / r)
pool = (blob + noise(18, 0.18) + noise(6, 0.05)) > 0.15
pool = np.asarray(Image.fromarray((pool * 255).astype(np.uint8)).filter(ImageFilter.MedianFilter(5))) > 0  # no specks
pool[[0, -1], :] = False
pool[:, [0, -1]] = False
m = Image.fromarray((pool * 255).astype(np.uint8)).copy()            # keep one piece: flood-fill from the blob centre
sy, sx = np.unravel_index(np.argmax(blob * pool), pool.shape)
ImageDraw.floodfill(m, (int(sx), int(sy)), 128)
pool = np.asarray(m) == 128

snap("1_outline", np.full((H, W, 3), (40, 120, 70), np.uint8), pool)

# 2. depth: 0 at the rim .. 1 at the deepest point
d = distance_in(pool)
D = d.max()
ang = np.arctan2(yy - yy[pool].mean(), xx - xx[pool].mean())


def lopsided():
    # the ledge width changes round the pool: a wide shelf on one side, a steep wall on the other
    k = rng.random(3) * 2 - 1
    ph = rng.random(3) * 6.28
    wave = sum(k[i] * np.sin((i + 1) * ang + ph[i]) / (i + 1) for i in range(3))
    return np.clip(d / (D * 0.9 * np.clip(1 + 0.55 * wave, 0.45, 1.6)), 0, 1)


def two_wells():
    # the deepest pixel, plus a second deep spot far enough away to read as its own well
    ys, xs = np.nonzero(pool)
    dv = d[ys, xs]
    i = dv.argmax()
    far = np.hypot(xs - xs[i], ys - ys[i])
    score = np.where(far > D * 1.6, dv * np.minimum(far / (D * 2.5), 1), 0)
    pits = np.clip(1 - np.hypot(xx - xs[i], (yy - ys[i]) * 1.1) / (D * 1.9), 0, 1)
    j = score.argmax()
    if score[j] > D * 0.35:
        pits = np.maximum(pits, 0.85 * np.clip(1 - np.hypot(xx - xs[j], (yy - ys[j]) * 1.1) / (D * 1.9), 0, 1))
    return pits


if LOOK == "I":
    t = lopsided()
elif LOOK == "J":
    t = np.minimum(np.clip(d / (D * 0.5), 0, 1), two_wells() * 1.15)
else:
    t = np.minimum(lopsided() * 1.1, two_wells() * 1.2)
t = np.clip(t + noise(9, 0.04), 0, 1)
snap("2_depth", np.repeat((255 - t * 230)[..., None], 3, 2).astype(np.uint8), pool)

# 3. terraces: cut the depth into a few flat steps
lv = np.digitize(t, [0.14, 0.40, 0.66])             # 0 shallow shelf .. 3 basin
out = np.zeros((H, W, 3), np.uint8)
for k in range(4):
    out[pool & (lv == k)] = TOPS[k]
snap("3_terraces", out, pool)

# 4. walls, light from the top-left: each step casts a shadow down-right onto the next one, and the riser
#    only shows on the far (north) wall, because the camera looks down and slightly north
for k, face_h in enumerate((5, 7, 9)):
    shallow, deeper = pool & (lv <= k), pool & (lv > k)
    sh = np.zeros_like(shallow)
    for s in range(1, 9):
        sh |= shift(shallow, round(4 * s / 8), s)
    out[deeper & sh] = CAST
    f = np.zeros_like(shallow)
    for s in range(1, face_h + 1):
        f |= shift(shallow, 0, s)
    face = deeper & f
    out[face] = FACES[k]
    out[face & ~shift(face, 0, -1)] = CREVICE      # dark foot of the face
    edge = shallow & (shift(deeper, -1, 0) | shift(deeper, 0, -1)) & ~f
    out[edge & (ang > np.radians(-30)) & (ang < np.radians(150))] = LITS[k]   # lit lips on the south/east sides
out[pool & (t > 0.88)] = CORE
snap("4_walls_and_shadows", out, pool)

# 5. soft rim: one step under the lake colour, with broken lit bits facing the light
rim = pool & (d < 2.2)
out[rim] = (66, 146, 80)
facing = np.cos(ang) * 0.6 + np.sin(ang) * 0.8
out[rim & (facing > 0.3) & (noise(5, 1) > 0)] = (80, 158, 90)

snap("5_rim", out, pool)
img = np.zeros((H, W, 4), np.uint8)
img[pool, :3] = out[pool]
img[pool, 3] = 255

# 6. moss mats over the lip (mostly the shaded far side) and a few roots hanging down the far wall
ys, xs = np.nonzero(pool & (d < 1.5))
north = (ang[ys, xs] < np.radians(-15)) & (ang[ys, xs] > np.radians(-165))
picks = []
for i in rng.permutation(len(xs)):
    gap = 16 if north[i] else 24
    if all(np.hypot(xs[i] - a, ys[i] - b) >= gap for a, b in picks):
        picks.append((xs[i], ys[i]))
for x0, y0 in picks[:10]:
    mat = np.zeros((H, W), bool)
    for _ in range(rng.integers(3, 6)):
        cx, cy, r = x0 + rng.uniform(-6, 6), y0 + rng.uniform(-2, 2), rng.uniform(2, 3.8)
        mat |= (xx - cx) ** 2 + ((yy - cy) / 0.8) ** 2 <= r * r
    under = shift(mat, 1, 2) & ~mat & pool
    img[under, :3] = MOSS_SHADE
    img[mat, :3] = MOSS
    img[mat & ~shift(mat, 1, 1), :3] = MOSS_LIT
    img[mat | under, 3] = 255
for x0, y0 in [p for p in picks if ang[p[1], p[0]] < np.radians(-30) and ang[p[1], p[0]] > np.radians(-150)][:4]:
    x, y = float(x0), float(y0) + 1
    for s in range(int(rng.uniform(12, 22))):
        x += rng.uniform(-0.6, 0.6)
        y += 1
        if 0 <= int(y) < H and 0 <= int(x) < W - 1 and pool[int(y), int(x)]:
            img[int(y), int(x):int(x) + (2 if s < 9 else 1), :3] = ROOT

snap("6_moss_and_roots", img[..., :3], img[..., 3] > 0)
name = f"sinkhole_{LOOK}_{SEED}"
Image.fromarray(img, "RGBA").save(name + ".png")
bg = Image.new("RGBA", (W, H), LAKE + (255,))
bg.alpha_composite(Image.fromarray(img, "RGBA"))
bg.resize((W * 4, H * 4), Image.NEAREST).save(name + "_preview.png")
print("wrote", name + ".png")
