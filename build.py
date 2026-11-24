from pathlib import Path
import json, html, argparse
p=Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('--domain',default='');domain=parser.parse_args().domain.rstrip('/')
if domain and not domain.startswith('https://'): parser.error('Use final https:// domain')
header=(p/'components/header.html').read_text();footer=(p/'components/footer.html').read_text();pages=json.loads((p/'src/pages.json').read_text())
for slug,title,desc in pages:
 url=domain+('/' if slug=='index' else '/'+slug+'.html') if domain else ''
 clinic={'@type':'MedicalClinic','name':'Bone and Joint Clinic','telephone':'+919672445102','medicalSpecialty':'https://schema.org/Musculoskeletal','address':{'@type':'PostalAddress','streetAddress':'Quarter No. 2/4, Medical College Campus, Shastri Nagar','addressLocality':'Jodhpur','addressRegion':'Rajasthan','addressCountry':'IN'}}
 if domain: clinic.update({'@id':domain+'/#clinic','url':domain+'/'})
 schema={'@context':'https://schema.org','@graph':[clinic,{'@type':'WebPage','name':title,'description':desc,**({'url':url} if url else {})}]}
 if domain and slug!='index': schema['@graph'].append({'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Home','item':domain+'/'},{'@type':'ListItem','position':2,'name':title,'item':url}]})
 canonical=f'<link rel="canonical" href="{html.escape(url)}"><meta property="og:url" content="{html.escape(url)}">' if domain else ''
 body=(p/f'src/{slug}.body.html').read_text()
 (p/f'{slug}.html').write_text(f'<!doctype html><html lang="en-IN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc,quote=True)}"><meta property="og:title" content="{html.escape(title,quote=True)}"><meta property="og:description" content="{html.escape(desc,quote=True)}"><meta property="og:type" content="website">{canonical}<link rel="stylesheet" href="assets/css/style.css"><script type="application/ld+json">{json.dumps(schema)}</script><script defer src="assets/js/main.js"></script></head><body>{header}{body}{footer}</body></html>')
if domain:
 (p/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+html.escape(domain+('/' if s=='index' else '/'+s+'.html'))+'</loc></url>' for s,_,_ in pages)+'</urlset>')
 (p/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+domain+'/sitemap.xml\n')
else:
 (p/'robots.txt').write_text('User-agent: *\nAllow: /\n')
