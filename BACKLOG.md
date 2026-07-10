# Website Backlog — openmeadowgames.com

Running list of improvements for the studio site. Ordered roughly by impact.
(Last groomed: July 7, 2026 — after the big site polish session.)

## High Priority

- [ ] **Email list** — the one big strategic item left. Embed a signup form
  (Buttondown or MailerLite free tier) in the Connect section and on the
  Park & Hide page. This is the audience we own; it converts to Steam
  wishlists on announcement day.

## When the Time Comes

- [ ] **Steam wishlist button** — when the Steam page exists, swap the
  "Follow the Devlog" hero CTA on `/park-and-hide/` for a big
  "Wishlist on Steam" button. Also update the homepage card.
- [ ] **Press kit page** — factsheet, logo pack, screenshots, GIFs, contact.
  Wait until marketing ramps up / name announcement settles.
- [ ] **Copyright year** — bump "© 2026" to "© 2026–2027" in January
  (or automate with a small script).

## Steam / Store

- [ ] **Register "Park & Hide" as a Steam app** — PAUSED (July 10, 2026).
  Started the Steamworks signup but stopped — no benefit yet since wishlists
  only start once the public page (needs art) is live, and app registration is
  NOT legal name protection (that's a trademark). Revisit when capsule art +
  demo plan are closer.
  - When resuming: sign up at partner.steamgames.com under the studio email
    → "I'm a developer or publisher" → sign SDA + NDA (free) → tax interview
    (W-8BEN, use SIN for Canada–US treaty rate) → bank/payout → identity
    verification (takes days). The **$100 Steam Direct fee is only charged
    when you create the app** — that's the stopping point. Optionally finish
    the FREE onboarding early to get the slow verification out of the way, but
    hold the $100 app creation until art is ready.
- [ ] **Publish the public Coming Soon page** — only once real capsule art +
  5 screenshots are ready (and Walter/lore names are settled). This is the
  wishlist-collecting page; don't rush it out with a placeholder capsule.
- [ ] **Commission capsule / key art** — artist brief is drafted (held until
  character names finalized). Work-for-hire, full copyright assignment.
- [ ] **Consider trademarking "Park & Hide"** — someday item, only if the name
  becomes precious. Real legal protection, unlike a Steam page.

## Studio Consolidation (personal → studio identity)

Goal: everything business-facing lives under the studio identity
(`openmeadowgames@gmail.com` / the `OpenMeadowGames` GitHub org), not personal
accounts. Not urgent — a "clean up before the studio grows" pass.

- [ ] **Transfer game repo to the org** — the game source repo is under a
  personal GitHub account (`djsheepy@gmail.com`). Move it into the
  `OpenMeadowGames` org via repo Settings → Danger Zone → Transfer ownership.
  Preserves history/issues/stars and sets up redirects. Stays private if it
  already is.
- [ ] **Confirm org admin access** — after transfer, ensure the studio
  account/your login has Admin on the org so control isn't lost.
- [ ] **Audit remaining personal-email accounts** — list anything game/studio
  related still tied to `djsheepy@gmail.com` and migrate or re-own under the
  studio email (socials, itch, Discord, mailing tool, domain, etc.).
  (GA is already under the studio email — no action needed there.)
- [ ] **Lock down the studio email** — 2FA (authenticator, not SMS), recovery
  email + phone, saved backup codes. It's the single point of failure once
  everything hangs off it.

## Maintenance / Tech Debt

- [ ] **Shared stylesheet** — every page duplicates ~200 lines of identical
  CSS. Extract to `/style.css` so site-wide tweaks are one edit instead of
  eight. Do this before adding more pages.
- [ ] **Blog post template** — a `_template.html` with head meta placeholders,
  share buttons, and footer pre-wired, so new posts are fill-in-the-blanks.
- [ ] **Git remote URL** — remote still points at old repo capitalization
  (`OpenMeadowGames` → `openmeadowgames`); works via redirect but prints a
  warning on every push. One-line fix:
  `git remote set-url origin https://github.com/openmeadowgames/OpenMeadowGames.github.io.git`
- [ ] **Web app manifest** — `favicon-512.png` is already in the repo; add a
  `site.webmanifest` for Android "Add to Home Screen" support. Low value
  until there's a reason people pin the site.

## Routine (every new blog post)

1. Create the post page (meta tags, share buttons, favicon links).
2. Add the card to `blog/index.html` (thumbnail + excerpt + Read More).
3. Add an `<item>` to `feed.xml`.
4. Keep post videos lean (~1–5 MB) — they live in git history forever.

## Done (this session, July 7, 2026)

- [x] Ocean water blog post + video
- [x] Copyright notices on every page
- [x] Open Graph / Twitter Card meta tags site-wide
- [x] Working share buttons (X, Bluesky, Copy Link)
- [x] Game renamed to Park & Hide across the site
- [x] Favicon set (ico/svg/png + apple-touch-icon)
- [x] Blog archive completed (pages for all five posts, thumbnails)
- [x] RSS feed (`/feed.xml`) + discovery tags
- [x] Dedicated game page (`/park-and-hide/`) + nav integration
