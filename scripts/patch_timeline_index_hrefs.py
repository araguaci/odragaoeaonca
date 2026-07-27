#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).resolve().parent.parent / "timeline" / "index.html"
t = p.read_text(encoding="utf-8")
repls = {
    "../dragao-onca-brasil-federal.html": "./timeline-brasil-federal.html",
    "../dragao-onca-braco-diplomatico.html": "./timeline-braco-diplomatico.html",
    "../dragao-onca-sao-paulo.html": "./timeline-sao-paulo.html",
    "../dragao-onca-goias.html": "./timeline-goias.html",
    "../dragao-onca-minas-gerais.html": "./timeline-minas-gerais.html",
    "../dragao-onca-bahia.html": "./timeline-bahia.html",
    "../dragao-onca-para.html": "./timeline-para.html",
    "../dragao-onca-amazonas.html": "./timeline-amazonas.html",
    "../dragao-onca-parana.html": "./timeline-parana.html",
    "../dragao-onca-rio-grande-do-sul.html": "./timeline-rio-grande-do-sul.html",
    "../dragao-onca-rs-es-ranking-nacional.html": "./timeline-rs-es-ranking.html",
    "../dragao-onca-sintese.html": "./timeline-sintese.html",
    "../dragao-onca-pl2780.html": "./timeline-pl2780.html",
    "../dragao-onca-braco-juridico.html": "./timeline-braco-juridico.html",
    "../dragao-onca-sintese-final-cross-state.html": "./timeline-sintese-final.html",
    "../dragao-onca-amapa.html": "./timeline-amapa.html",
    "../dragao-onca-rj.html": "./timeline-rj.html",
}
for a, b in repls.items():
    t = t.replace(f'href="{a}"', f'href="{b}"')
t = t.replace(
    "Cards apontam ao dossiê HTML",
    "Cards apontam à timeline condensada (dossiê no topo de cada página)",
)
t = t.replace("<b>17</b> dossiês HTML</span>", "<b>17</b> timelines + dossiês</span>")
p.write_text(t, encoding="utf-8")
print("updated", p)
