"""Génère les pages HTML à partir des fragments du dossier content/.
Usage : python3 build.py   (les pages sont écrites à la racine, prêtes pour GitHub Pages)"""
from pathlib import Path
PAGES = [("index","Accueil"),("biographie-ecrivain","Repères biographiques"),("romans","Romans"),
("nouvelles","Nouvelles"),("poemes-et-chansons","Poèmes et chansons"),("presse","Presse"),
("etudes-de-loeuvre","Etudes de l'oeuvre"),("temoignages","Témoignages"),("galerie","Galerie"),
("liens","Liens"),("credits-et-remerciements","Crédits et remerciements"),("contact","Contact"),
("mentions-legales","Mentions légales")]
DESC = "Bertrand de Robillard : romans, nouvelles, chansons, articles de presse, études de l'oeuvre, en français et créole, à Maurice."
T = Path("template.html").read_text(encoding="utf-8")
for slug, title in PAGES:
    nav = "\n".join(f'<a href="{"index" if s=="index" else s}.html"{" aria-current=\"page\"" if s==slug else ""}>{t}</a>' for s,t in PAGES)
    body = Path(f"content/{slug}.html").read_text(encoding="utf-8")
    page_title = "Bertrand de Robillard" if slug=="index" else f"{title} | Bertrand de Robillard"
    html = T.replace("{{title}}",page_title).replace("{{desc}}",DESC).replace("{{nav}}",nav).replace("{{body}}",body)
    Path(f"{slug}.html").write_text(html, encoding="utf-8")
print(len(PAGES),"pages générées")
