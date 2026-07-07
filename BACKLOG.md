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
