# Dr. Hemant Jain website
Open index.html directly or run `python3 -m http.server 8000`.
18 static pages, shared CSS/JS, build-time reusable header and footer. Edit components/ or src/ then run `python3 build.py`. No framework or pip dependencies needed for rebuilding.

## Images
Place doctor-hero.jpg, knee.jpg, shoulder.jpg, ankle.jpg, elbow.jpg, fracture.jpg, replacement.jpg in the project root. news.jpg is included from the provided press archive. Use authorised photographs only. Missing specialty images fall back to diagrams.

## Before launch
Have Dr. Jain review all medical content, services, qualifications, press permissions and contact details. Confirm existing external academic links and consultation times. No fake rankings or ratings. Run `python3 build.py --domain https://YOUR-ACTUAL-DOMAIN` replacing the example with the real HTTPS origin; this generates canonical URLs and sitemap.xml. Deploy root HTML, assets, images, robots.txt, sitemap.xml; keep src, components and build.py locally. Set preferred HTTPS host redirects. Submit sitemap in Google Search Console; verify Google Business Profile and consistent clinic name, address, phone. Test mobile menu and phone links on real devices. Check Search Console indexing and Core Web Vitals. Do not create duplicate city or keyword doorway pages. No ranking guarantee.

Google guidance: https://developers.google.com/search/docs/fundamentals/creating-helpful-content ; https://developers.google.com/search/docs/essentials/spam-policies ; https://developers.google.com/search/docs/appearance/structured-data/local-business
