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

## Funding / Incorporation

- [ ] **Creative BC — Video Games Early Stage Growth** — SKIPPED 2026/27
  intake (deadline was Nov 2, 2026). Not ready to incorporate yet. Revisit
  for a future intake (the 2026/27 round opened mid-September, so watch for
  the next one around then). It's a pilot program, so check it still exists.
  - Up to $50K, non-repayable, competitive. For studios with ≤1 released game.
  - Must be an **incorporated** for-profit BC/Canadian company, head office in
    BC, majority owned by BC residents. A sole proprietorship doesn't qualify.
  - Company must own 100% of the game IP. 75%+ of spending must be in BC.
  - Needs: 4-page business plan, 10-page pitch deck + video, budget,
    shareholder/director info, team bios, incumbency certificate.
  - Program page: https://creativebc.com/funding-program/interactive-digital-media/video-games-early-stage-growth/
  - Contact: Nicholas Klassen, nklassen@creativebc.com
- [ ] **Incorporate the studio** — prerequisite for the grant above, and for
  the BC Interactive Digital Media Tax Credit / most other game funding.
  - Online at bcregistry.gov.bc.ca. ~$350 to incorporate. Numbered company
    skips the name wait; "Open Meadow Games Inc." needs a Name Request
    ($30 regular ~5 business days, $130 priority ~1–2 days).
  - After: issue shares to self, business bank account, assign game IP from
    me to the company, new GST number if needed, close the sole prop.
  - Talk to an accountant first about moving the IP/assets over (Section 85
    rollover) and the yearly corporate tax return cost.
  - Start this a few weeks before any grant deadline, not days.

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
