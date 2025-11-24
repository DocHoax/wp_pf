# Sitemap & Search Console — Quick Guide

This README shows how to verify your site in Google Search Console and submit your sitemap (step-by-step). It also suggests where to capture screenshots during verification.

Site used in examples: https://your-domain.example
Files created in this repo:

- `sitemap.xml` — basic sitemap with main anchors
- `robots.txt` — references the sitemap

---

## 1) Verify ownership in Google Search Console

1. Open: https://search.google.com/search-console
2. Click "Add property" → choose **URL prefix** and enter your site's URL (for example `https://your-domain.example`).
3. Choose one of the verification methods:
   - **HTML file upload (recommended for Netlify)**: download the verification file provided by Google and commit it to the root of your repo (same place as `gg.html`) then deploy to Netlify. After deployment, click "Verify" in Search Console.
     - Screenshot tip: capture the "HTML file" instruction page and the confirmation "Ownership verified" page.
   - **DNS record**: add the TXT record to your domain provider's DNS. Use this if you control the domain (faster for Domain-scoped properties).
   - **Google Analytics / Tag Manager**: if already installed, use it to verify.

## 2) Submit your sitemap

1. In Search Console, open the property you verified.
2. Navigate to **Indexing → Sitemaps** (left sidebar).
3. Under "Add a new sitemap", enter: `sitemap.xml` and press Submit.
4. Wait a few minutes and refresh — Search Console will report success or list problems.

Screenshot tip: capture the Sitemaps page after submission showing your sitemap URL and status.

## 3) Check robots.txt

Visit https://your-domain.example/robots.txt and ensure it contains the `Sitemap:` line pointing to your sitemap. If you changed the repo, redeploy and verify again.

## 4) Deploy & continuous updates

- For Netlify deployments from Git, commit `sitemap.xml` and `robots.txt` to your repo root so they are served automatically.
- If your site gains new pages often, consider generating a sitemap during your build and committing it.

## 5) Troubleshooting & tips

- If Search Console reports unreachable URLs, ensure Netlify deployment completed and there are no redirects blocking the sitemap URL.
- Use the URL Inspection tool in Search Console to fetch and render any URL.
- To test robots rules, use the robots.txt tester in Search Console (if available in your account) or visit the `robots.txt` URL directly.

---

If you'd like, I can:

- Commit a Google verification HTML file to this repo (you'll need to paste the token from Search Console), or
- Add additional pages to `sitemap.xml` if you provide their URLs, or
- Create a CI step to generate sitemaps automatically for future builds.
