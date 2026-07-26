# Changelog — O Dragão e a Onça

Registro de alterações em **fontes** do subsite/submódulo `odragaoeaonca/`.  
Não inclui espelhos em `docs/odragaoeaonca/` (artefato de build Jekyll no repositório principal).

Formato: data (ISO) → resumo → arquivos de fonte.

---

## 2026-07-25 (h) — síntese v1 com novos artefatos

| Ação | Arquivo | Descrição |
|------|---------|-----------|
| **Alterado** | `dragao-onca-sintese.html` | Tese com nuance (BA, SP, PR, RS/ES, Diplomático); KPIs 9 UFs / ~R$78bi / CEBC; quadro 9 estados; gráficos e alertas atualizados; horizontes marcando entregas 25/jul; ponte para T-243. |

---

## 2026-07-25 (g) — nav scroll-spy nos artefatos novos

| Ação | Arquivo | Descrição |
|------|---------|-----------|
| **Alterado** | `dragao-onca-sao-paulo.html`, `bahia`, `parana`, `rs-es-ranking-nacional`, `braco-diplomatico`, `sintese-final-cross-state` | Nav deixou de ser tabs (show/hide). Agora mostra todo o conteúdo, destaca a seção ativa via `IntersectionObserver` (padrão MG) e `#gotop` fixo no canto inferior direito. |

---

## 2026-07-25 (f) — series-nav em todos os dossiês

| Ação | Arquivo | Descrição |
|------|---------|-----------|
| **Alterado** | 8× `dragao-onca-*.html` (GO, BR, PA, AM, MG, síntese v1, PL 2.780, jurídico) | `#serie` atualizado: 15 artefatos na ordem README; `is-current` no capítulo da página. |
| **Criado** | 6× `dragao-onca-*.html` (diplomático, SP, BA, PR, RS/ES/ranking, síntese final) | CSS `series-nav` + seção `#serie` antes do rodapé (mesmo padrão). |

---

## 2026-07-25 (e) — series-nav federal (ordem README)

| Ação | Arquivo | Descrição |
|------|---------|-----------|
| **Alterado** | `dragao-onca-brasil-federal.html` | `#serie` / `series-nav`: 15 artefatos na ordem de importância do README (0 Hub → 14 T-243); card atual T-229 com `is-current`. |

---

## 2026-07-25 (d) — README + promo X.com

| Ação | Arquivo | Descrição |
|------|---------|-----------|
| **Alterado** | `README.md` (repo principal) | Seção série Dragão e a Onça, IDs 1748/T-243, tabelas de artefatos |
| **Criado** | `promo/x-posts-promocao.md` | 32 posts X (hub, corpus, 16 dossiês, 14 X Articles) + calendário 15 dias |

---

| Ação | Arquivo | Descrição |
|------|---------|-----------|
| **Alterado** | `index.html` | 16 dossiês: eixos transversais → UFs por ranking CEBC → sínteses; badge **25/jul** nos novos artefatos; seção X Articles. |

---

Posts e capítulos temáticos gerados a partir dos batches mergeados; xarticle SP já publicável em `artigos/`.

| Ação | Descrição |
|------|-----------|
| **Repo principal** | 43 posts novos em `_posts/dragao-onca/`, lawfare.json e sync atualizados |
| **HTML** | Dossiês `dragao-onca-*.html` na raiz do submódulo (SP, Bahia, etc.) |
| **X Articles** | `artigos/sao-paulo-xarticle.md` + hero (Cap. 11) |
| **Pendente editorial** | Heroes regionais base (webp); artes dedicadas por UF opcionais; `jekyll build` pausado |
| **X Articles** | `parana-xarticle.md`, `rs-es-ranking-xarticle.md` (+ sao-paulo, bahia existentes) |

---

Artigo longo para X.com a partir do dossiê HTML `dragao-onca-sao-paulo.html` (CRRC, COFCO, variante “mercado”, IDs 1726–1730, T-238).

### Fontes

| Ação | Arquivo | Descrição |
|------|---------|-----------|
| **Criado** | `artigos/sao-paulo-xarticle.md` | X Article: leilões/concessões, domínio CRRC, terminal COFCO Santos, tese T-238, lacunas, fontes. |
| **Criado** | `artigos/sao-paulo-xarticle-hero.png` | Capa share card X, 1024×600 px, composição wide 5:2. |
| **Fonte** | `dragao-onca-sao-paulo.html` | Dossiê interativo Cap. 11 (5 entradas + 1 vaga, fev/2024–2026). |

### Publicação X (referência)

- Compositor: **x.com/compose/article**
- Link externo do dossiê no **primeiro reply** (não no tweet principal): `https://gosurf.site/dragao-onca-sao-paulo`

---

## 2026-07-25 — Convenção de caminhos (repositório principal)

Regra Cursor no projeto pai documenta que **esta pasta** (`odragaoeaonca/` na raiz) é a fonte canônica — não `docs/odragaoeaonca/`.

| Ação | Arquivo (repo principal) | Descrição |
|------|--------------------------|-----------|
| **Criado** | `.cursor/rules/odragaoeaonca-paths.mdc` | X Articles, heroes e HTML sempre em `odragaoeaonca/artigos/` e `odragaoeaonca/*.html`. |

---

## Estrutura esperada de `artigos/`

```
artigos/
├── [capitulo]-xarticle.md      # texto para X Articles
└── [capitulo]-xarticle-hero.png # capa 1024×600 (quando gerada)
```

Capítulos com xarticle na pasta (jul/2026): amazonas, bahia, braco-diplomatico, braco-juridico, brasil-federal, goias, minas-gerais, odragaoeaonca (série), **parana**, para, pl2780, **rs-es-ranking**, sao-paulo, sintese.
