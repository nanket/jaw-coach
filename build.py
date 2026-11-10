#!/usr/bin/env python3
"""Builds the Jaw Coach website (static HTML for GitHub Pages).

    python3 build.py

Writes index.html, support/, privacy/, terms/, 404.html, sitemap.xml and
robots.txt next to this file. Edit the copy here, not in the HTML.
"""
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
BASE = "https://nanket.github.io/jaw-coach/"
APP_STORE = "https://apps.apple.com/app/id6823648145"
EMAIL = "nanket.dev@gmail.com"
UPDATED = "2026-11-10"
EULA = "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"
AAO = "https://aaoinfo.org/whats-trending/is-mewing-bad-for-you/"


def page(path, title, description, body, *, nav="", jsonld=None):
    """path: '' for home or 'support/' etc. Asset links are relative."""
    depth = path.count("/")
    up = "../" * depth
    url = BASE + path
    links = [("support/", "Support"), ("privacy/", "Privacy"), ("terms/", "Terms")]
    current = ' aria-current="page"'
    navhtml = "".join(
        f'<a href="{up}{href}"{current if href == nav else ""}>{label}</a>'
        for href, label in links
    )
    ld = ""
    for block in jsonld or []:
        ld += f'<script type="application/ld+json">{json.dumps(block, ensure_ascii=False)}</script>\n'
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#f2f2f7" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#000000" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Jaw Coach">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="apple-itunes-app" content="app-id=6823648145">
<link rel="icon" href="{up}favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="{up}favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="{up}apple-touch-icon.png">
<link rel="stylesheet" href="{up}assets/style.css">
{ld}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="wrap">
<a class="brand" href="{up or './'}"><img src="{up}assets/icon-512.png" alt="" width="28" height="28">Jaw Coach</a>
<nav class="top" aria-label="Site">{navhtml}</nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="site"><div class="wrap">
<span>Jaw Coach by Inkstroke · For adults 18+ · A wellness app, not a medical device.</span>
<nav aria-label="Footer"><a href="{up}support/">Support</a><a href="{up}privacy/">Privacy</a><a href="{up}terms/">Terms</a><a href="mailto:{EMAIL}">{EMAIL}</a></nav>
</div></footer>
</body>
</html>
"""
    out = ROOT / path / "index.html" if path else ROOT / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc)


# ---------------------------------------------------------------- home

MOVES = [
    ("Slow Close", "Open within comfort, then close slowly and smoothly."),
    ("Side Glide", "Glide your jaw side to side: slow, mid-range, never forced."),
    ("Forward Glide", "Ease your lower jaw forward and back, slowly."),
    ("Open Hold", "Hold a steady, comfortable opening, not your maximum."),
    ("Chin Tuck", "Glide your head straight back, eyes level, then relax."),
    ("Rest Reset", "Lips together, teeth apart, slow breathing through your nose."),
    ("Open, Forward and Side Press", "Light resistance in each direction. Nothing moves."),
    ("Rhythm Chew", "An easy, even chewing rhythm. Steadiness, not speed."),
    ("O–E Vowels", "Alternate round and wide lip shapes to wake up your face."),
]

FAQ = [
    ("How does Jaw Coach count reps?",
     "It uses your iPhone's front camera to follow your jaw and counts a rep only when the "
     "movement is real. It also checks tempo and steadiness. The camera frames are processed "
     "on your phone and are never saved or sent anywhere."),
    ("Will jaw exercises change how my jawline looks?",
     "Jaw Coach doesn't promise that. It trains what can actually be trained: slow, controlled "
     "movement, a comfortable range, steadiness and a daily habit, with an honest record of "
     "what you did."),
    ("Is Jaw Coach a mewing app?",
     "No. Jaw Coach coaches guided jaw movement exercises. The American Association of "
     "Orthodontists says there is no evidence for mewing."),
    ("Is it safe?",
     "There's a short safety check before you start, a Hurts button in every exercise, and a "
     "gentle Comfort track for sensitive jaws. Pain changes the plan to lighter days or rest. "
     "Jaw Coach is not a medical device; if you have a jaw problem, ask a professional first."),
    ("How much does it cost?",
     "The safety tools, the Comfort track and Level 1 are free. Premium unlocks the full "
     "program: $7.99 a month, $29.99 a year with a one-week free trial, or $59.99 once for "
     "lifetime access (US prices; your store shows local prices)."),
    ("Is there an Android version?",
     "Jaw Coach is on iPhone first. An Android version for Google Play is on the way."),
]

faq_html = "".join(
    f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}"
    + (f' <a href="{AAO}" rel="noopener">Read the AAO article</a>.' if "mewing" in q else "")
    + "</p></details>"
    for q, a in FAQ
)

home_body = f"""
<div class="wrap">
<section class="hero">
<img class="icon" src="assets/icon-512.png" alt="Jaw Coach app icon" width="112" height="112">
<h1>Jaw exercises,<br>counted live.</h1>
<p class="lead">Jaw Coach uses your front camera to count every rep and coach tempo, control and a comfortable range. A few minutes a day, with pain rules built in.</p>
<div class="cta">
<a class="btn" href="{APP_STORE}">Download on the App Store</a>
<a class="btn secondary" href="#how">How it works</a>
</div>
<p class="note">Free to start · iPhone · For adults 18+ · Android coming soon</p>
</section>
</div>

<div class="shots" role="list" aria-label="App screenshots">
<img role="listitem" src="assets/screens/01-counted.webp" width="240" height="520" alt="Session complete: every rep counted for tempo and control" loading="lazy">
<img role="listitem" src="assets/screens/02-today.webp" width="240" height="520" alt="Today: a few minutes a day, planned for you" loading="lazy">
<img role="listitem" src="assets/screens/03-progress.webp" width="240" height="520" alt="Progress: a Control Score, streaks and levels you earn" loading="lazy">
<img role="listitem" src="assets/screens/04-safety.webp" width="240" height="520" alt="Pain rules built in: tap Hurts at any time" loading="lazy">
<img role="listitem" src="assets/screens/05-dark.webp" width="240" height="520" alt="Light or dark: private by design" loading="lazy">
</div>

<div class="wrap">

<section id="how">
<h2>A jaw workout that knows when a rep counts</h2>
<p class="sub">Most jaw exercise apps play a video and hope you follow along. Jaw Coach watches the movement and coaches it.</p>
<div class="grid">
<div class="card"><div class="step">1 · Set up</div><h3>A short safety check</h3><p>Answer a few questions. If anything needs a professional first, the app says so plainly.</p></div>
<div class="card"><div class="step">2 · Train</div><h3>Live rep counting</h3><p>Prop your phone at eye level. The camera counts clean reps and a voice coach cues tempo.</p></div>
<div class="card"><div class="step">3 · Progress</div><h3>Levels you earn</h3><p>Level 1 Control, then Glide, Stability and Mastery. You move up on control, never on how far you can open.</p></div>
</div>
</section>

<section id="exercises">
<h2>The exercises</h2>
<p class="sub">Short daily doses adapted from guidance written for adults. More isn't better for your joints.</p>
<div class="moves">
{"".join(f"<div><strong>{html.escape(n)}</strong><span>{html.escape(t)}</span></div>" for n, t in MOVES)}
</div>
</section>

<section id="safety">
<h2>Safety first, privacy always</h2>
<div class="grid">
<div class="card"><h3>Pain rules built in</h3><p>A Hurts button in every exercise. Pain makes the plan lighter, adds rest, or suggests seeing someone.</p></div>
<div class="card"><h3>A gentle Comfort track</h3><p>For sensitive jaws, free for everyone, with a summary you can share with a dentist or physio.</p></div>
<div class="card"><h3>Your data stays on your phone</h3><p>No account, no ads, no health analytics. Video never leaves your phone. <a href="privacy/">Privacy policy</a></p></div>
<div class="card"><h3>A habit without pressure</h3><p>A forgiving streak with rest days built in, flare days that still count, and no guilt messages.</p></div>
</div>
</section>

<section id="pricing">
<h2>Free to start</h2>
<p class="sub">The safety tools, the Comfort track and Level 1 are free. Premium unlocks the full program.</p>
<div class="grid">
<div class="card"><h3>Annual</h3><div class="price">$29.99<span class="meta"> / year</span></div><p>One-week free trial. Cancel at least 24 hours before it ends and you won't be charged.</p></div>
<div class="card"><h3>Monthly</h3><div class="price">$7.99<span class="meta"> / month</span></div><p>Renews monthly. Cancel any time in your App Store settings.</p></div>
<div class="card"><h3>Lifetime</h3><div class="price">$59.99<span class="meta"> once</span></div><p>One payment, nothing to renew.</p></div>
</div>
<p class="note">US prices. The App Store shows your local price before you buy.</p>
</section>

<section id="faq">
<h2>Questions</h2>
{faq_html}
</section>

<section class="hero" style="padding-top:24px">
<h2>Start your first session</h2>
<p class="lead">About three minutes. Every rep counted.</p>
<div class="cta"><a class="btn" href="{APP_STORE}">Download on the App Store</a></div>
</section>
</div>
"""

app_ld = {
    "@context": "https://schema.org",
    "@type": "MobileApplication",
    "name": "Jaw Coach: Live Jaw Trainer",
    "alternateName": "Jaw Coach",
    "description": "Jaw exercises with live rep counting from your front camera, tempo coaching and pain rules built in.",
    "operatingSystem": "iOS 15.0 or later",
    "applicationCategory": "HealthApplication",
    "url": BASE,
    "downloadUrl": APP_STORE,
    "image": BASE + "assets/icon-512.png",
    "screenshot": [BASE + f"assets/screens/{n}.webp" for n in ("01-counted", "02-today", "03-progress")],
    "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
    "author": {"@type": "Organization", "name": "Inkstroke", "email": EMAIL},
    "contentRating": "Ages 18+",
}
faq_ld = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
        for q, a in FAQ
    ],
}

page("", "Jaw Coach: Jaw Exercises with Live Rep Counting",
     "Jaw Coach counts your jaw exercise reps live with your iPhone's front camera and coaches "
     "tempo, control and comfort. A few minutes a day, pain rules built in, data on your phone.",
     home_body, jsonld=[app_ld, faq_ld])

# ---------------------------------------------------------------- support

support_body = f"""
<div class="wrap narrow doc">
<h1>Jaw Coach support</h1>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a>. For purchase help, include your app version and whether you use iPhone or Android. Please don't email camera recordings, health logs, passwords or payment details.</p>
<h2>Restore Premium</h2>
<p>Open Settings → Premium → Restore purchases, signed in with the store account that made the purchase.</p>
<h2>Manage or cancel a subscription</h2>
<p>Use Manage subscription in the app, or your App Store or Google Play subscription settings. Cancel at least 24 hours before the end of the current period (or the free trial) to avoid the next charge.</p>
<h2>Refunds</h2>
<p>Refunds are handled by Apple or Google under their own policies. On iPhone, request one at <a href="https://reportaproblem.apple.com" rel="noopener">reportaproblem.apple.com</a>.</p>
<h2>Camera and counting tips</h2>
<ul>
<li>Prop your phone at eye level, about an arm's length away.</li>
<li>Keep your face evenly lit, without a bright window behind you.</li>
<li>Each move starts by learning your relaxed jaw and a comfortable range, so counting fits you.</li>
</ul>
<h2>Your data</h2>
<p>Use Settings → Your data to export or delete your on-device data. Inkstroke can't access your health records; they stay on your phone. See the <a href="../privacy/">privacy policy</a>.</p>
<h2>Health concerns</h2>
<p>Jaw Coach is a wellness app, not a medical device. Stop if anything hurts, catches or locks, and tap Hurts. For health concerns, contact a qualified health professional.</p>
</div>
"""
page("support/", "Support · Jaw Coach",
     "Help with Jaw Coach: restore Premium, manage or cancel a subscription, camera tips, and how to export or delete your data.",
     support_body, nav="support/")

# ---------------------------------------------------------------- privacy

privacy_body = f"""
<div class="wrap narrow doc">
<h1>Privacy policy</h1>
<p class="meta">Version 1.0 · October 2026 · Last updated {UPDATED}</p>
<p>Your health records and camera data stay on this phone. Apple or Google and RevenueCat process purchase information for Premium.</p>
<h2>What Jaw Coach keeps, and where</h2>
<p>To run your program, Jaw Coach saves on this phone: your profile (goals and birth year), safety-screen outcomes (never your individual answers), pain and feel logs, sessions and sets, Jaw Check results, your level and streak, and your settings.</p>
<p>Health information is kept in a private folder inside the app that is excluded from iCloud and device backups. Settings and purchase status live in the app's standard preferences.</p>
<h2>The camera</h2>
<p>Camera frames are processed in memory, on this phone, to find face landmarks and count reps. Frames are never saved, recorded or sent anywhere. Only the numbers a set produces, such as rep timing, are kept.</p>
<h2>What we collect</h2>
<p>Jaw Coach has no account, no analytics of your health or exercise activity, no advertising and no attribution SDKs. Nothing about your jaw, your pain or your face leaves this phone unless you share it yourself. Purchase processing is described below.</p>
<h2>Purchases</h2>
<p>If you buy Premium, the purchase is handled by Apple or Google, and by RevenueCat, which manages subscriptions for us. They receive purchase information only, such as the product, price, date and an anonymous app user ID. This is used to validate purchases, manage Premium access and provide purchase reports. They never receive jaw, pain, face, level or program data.</p>
<h2>Notifications</h2>
<p>Reminders are scheduled on this phone. Jaw Coach asks for permission only when you turn a reminder on.</p>
<h2>Sharing, export and deletion</h2>
<ul>
<li>Export: Settings › Your data › Export my data makes a file you can save or send. You choose where it goes.</li>
<li>The summary for a dentist or physio is shared only when you share it.</li>
<li>Delete everything: Settings › Your data removes all health data from this phone straight away. Deleting the app does the same.</li>
</ul>
<h2>Consumer health data notice</h2>
<p>Some laws, such as Washington's My Health My Data Act, give you rights over consumer health data. Jaw Coach's health data stays on your device and is not collected, shared or sold by Inkstroke, so there is nothing for us to access, correct or delete on our side. You can see (export) and delete your data yourself at any time in Settings.</p>
<h2>Age</h2>
<p>Jaw Coach is for adults aged 18 and over. Setup stops if you are under 18.</p>
<h2>Changes and contact</h2>
<p>If this policy changes, the new version will be in the app with a new date. Questions: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<h2>This website and support email</h2>
<p>This website is hosted on GitHub Pages and has no analytics scripts, advertising, cookies or account forms. GitHub processes connection information, such as IP addresses, to serve and secure the pages. If you email support, your email provider and ours process the message, and we receive the information you choose to send. Please do not send health records or camera recordings. Contact us to request deletion of support correspondence.</p>
</div>
"""
page("privacy/", "Privacy policy · Jaw Coach",
     "Jaw Coach keeps your health records and camera data on your phone. No account, no ads, no health analytics. Read what is stored and how purchases are processed.",
     privacy_body, nav="privacy/")

# ---------------------------------------------------------------- terms

terms_body = f"""
<div class="wrap narrow doc">
<h1>Terms of use</h1>
<p class="meta">Version 1.0 · October 2026 · Last updated {UPDATED}</p>
<p>The plain-language terms for using Jaw Coach.</p>
<h2>Wellness use only</h2>
<p>Jaw Coach is not a medical device and does not diagnose, treat, cure, or prevent any medical condition. Nothing in it is medical advice. Talk to a professional about any health concern.</p>
<h2>Your part</h2>
<ul>
<li>You're 18 or older.</li>
<li>You follow the pain rule: stop if it hurts, catches or locks, and tap Hurts.</li>
<li>You get a professional check if Jaw Coach suggests one, or if anything worries you.</li>
<li>Measurements are camera estimates and can be wrong. Don't rely on them for health decisions.</li>
</ul>
<h2>Premium and subscriptions</h2>
<ul>
<li>Premium is optional. The safety tools, the Comfort track, Level 1 and everything on the always-free list stay free.</li>
<li>Prices are shown in the app before you buy and are charged to your App Store or Google Play account when you confirm.</li>
<li>Subscriptions renew automatically unless cancelled at least 24 hours before the end of the current period. Manage or cancel them in your App Store or Google Play account settings.</li>
<li>If a plan starts with a free trial, you won't be charged if you cancel at least 24 hours before the trial ends.</li>
<li>Lifetime is a single payment for Premium features, with nothing to renew.</li>
<li>Refunds are handled by Apple or Google under their own policies.</li>
</ul>
<h2>The app</h2>
<ul>
<li>Jaw Coach is provided as is. We work hard to keep it accurate and safe, but we can't promise it will always be available or free of errors.</li>
<li>You may use it for your own personal, non-commercial training.</li>
<li>As far as the law allows, Inkstroke isn't liable for indirect losses from using the app. Nothing here limits your rights under consumer law.</li>
<li>We may update these terms; the current version is always in the app.</li>
</ul>
<h2>Apple's standard app licence</h2>
<p>On iPhone, your use of Jaw Coach is also covered by <a href="{EULA}" rel="noopener">Apple's Licensed Application End User License Agreement</a>.</p>
<h2>Contact</h2>
<p>Questions about these terms: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div>
"""
page("terms/", "Terms of use · Jaw Coach",
     "The plain-language terms for Jaw Coach: wellness use only, subscriptions and free trials, refunds and your part in training safely.",
     terms_body, nav="terms/")

# ---------------------------------------------------------------- 404, sitemap, robots

(ROOT / "404.html").write_text(
    (ROOT / "support/index.html").read_text()
    .replace("<title>Support · Jaw Coach</title>", "<title>Page not found · Jaw Coach</title>")
    .replace('href="../', f'href="{BASE}').replace('src="../', f'src="{BASE}')
    .replace("<h1>Jaw Coach support</h1>", f'<h1>Page not found</h1><p><a href="{BASE}">Go to the Jaw Coach home page</a>.</p><h2>Support</h2>')
    .replace(f'<link rel="canonical" href="{BASE}support/">', '<meta name="robots" content="noindex">')
)

urls = ["", "support/", "privacy/", "terms/"]
(ROOT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{BASE}{u}</loc><lastmod>{UPDATED}</lastmod></url>\n" for u in urls)
    + "</urlset>\n"
)
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
(ROOT / ".nojekyll").write_text("")
print("built", len(urls), "pages")
