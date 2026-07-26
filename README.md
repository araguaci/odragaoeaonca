# O Dragão e a Onça

Investigação documental sobre captura econômico-eleitoral no federalismo brasileiro: como governadores negociam ativos estratégicos com capital estrangeiro (chinês, americano, europeu, japonês, sul-coreano) e convertem esses ativos em capital político pessoal — frequentemente sem que o benefício chegue à população das regiões afetadas.

**Licença:** CC0 1.0 — Domínio Público · série *lawfare-timeline*  
**Hub:** https://odragaoeaonca.vercel.app/ · **Corpus:** T-228 → T-243 · atualizado 25/jul/2026

---

## Tese central

> **Nenhum vetor — chinês, americano, europeu ou sul-coreano — chega ao beneficiário final.**

A União negocia marcos amplos (tratados, MoUs, cúpulas). Quem assina o contrato específico, enfrenta a comunidade atingida e responde eleitoralmente é o **governador estadual** — com nuance (T-243): o padrão confirma-se em extração mineral com custo ambiental local; enfraquece em infraestrutura/manufatura por mercado (SP, PR); contraria-se na Bahia (captura com benefício) e no par RS/ES (logística > diplomacia).

---

## Estrutura do repositório

```
odragaoeaonca/
├── artigos/                    # X Articles (.md) + heroes 1024×600
├── public/                     # Capas webp + relatórios estaduais (MD/PDF)
├── docs/                       # Dossiês-fonte, imagens, notas
├── dragao-onca-*.html          # 16 dossiês interativos
├── index.html                  # Dashboard (ordem CEBC + eixos)
└── vercel.json                 # Deploy estático (@vercel/static)
```

---

## Ordem de importância / assunto

Publicar nesta sequência (≤2 posts/dia). **Eixos transversais primeiro** → **UFs pelo ranking CEBC 2007-2025** → **sínteses por último**.

| Ordem | Prioridade | Artefato | Assunto | T-ID |
|------:|------------|----------|---------|------|
| 0 | Hub | Índice da série | Mapa completo + tese | — |
| 1 | Crítico | Brasil (Federal) | Pano de fundo 1993–2026 | T-229 |
| 2 | Crítico | Braço Diplomático | WAICO + Serra Verde + alinhamento duplo | T-236 |
| 3 | Alto | São Paulo | Variante “mercado” — CRRC/COFCO | T-238 |
| 4 | Alto | Goiás | Pivô China→EUA/Japão, terras raras | T-228 |
| 5 | Alto | Minas Gerais | Contraste ocidental (Sigma/Nasdaq) | T-232 |
| 6 | Alto | Bahia | Caso de controle — padrão falha | T-237 |
| 7 | Alto | Pará | Ferrovia + COP30 + 39 mortes | T-230 |
| 8 | Alto | Amazonas | Taboca/MPF/PF — mais grave | T-231 |
| 9 | Médio | Paraná | Coordenação estado–união (TCP) | T-239 |
| 10 | Médio | RS · ES · Ranking | Par de controle + CEBC | T-240–242 |
| 11 | Consolidação | Síntese v1 | 5 UFs originais | T-233 |
| 12 | Legislativo | PL 2.780/2024 | FGAM R$ 2 bi | T-235 |
| 13 | Transversal | Braço Jurídico | STF, marco temporal, ADI 7919 | T-234 |

**URL base dos dossiês:** `https://odragaoeaonca.vercel.app`

---

## Índice completo — X Articles

| Ordem | Capítulo | Markdown | Hero (1024×600) | HTML |
|------:|----------|----------|-----------------|------|
| 0 | Índice | `artigos/odragaoeaonca-xarticle.md` | `public/dragao-onca.webp` | `index.html` |
| 1 | Federal | `artigos/brasil-federal-xarticle.md` | `public/dragao-onca-brasil-federal.webp` | `dragao-onca-brasil-federal.html` |
| 2 | Diplomático | `artigos/braco-diplomatico-xarticle.md` | `artigos/braco-diplomatico-xarticle-hero.png` | `dragao-onca-braco-diplomatico.html` |
| 3 | São Paulo | `artigos/sao-paulo-xarticle.md` | `artigos/sao-paulo-xarticle-hero.png` | `dragao-onca-sao-paulo.html` |
| 4 | Goiás | `artigos/goias-xarticle.md` | `public/dragao-onca-goias.webp` | `dragao-onca-goias.html` |
| 5 | Minas Gerais | `artigos/minas-gerais-xarticle.md` | `public/dragao-onca-minas-gerais.webp` | `dragao-onca-minas-gerais.html` |
| 6 | Bahia | `artigos/bahia-xarticle.md` | `artigos/bahia-xarticle-hero.png` | `dragao-onca-bahia.html` |
| 7 | Pará | `artigos/para-xarticle.md` | `public/dragao-onca-para.webp` | `dragao-onca-para.html` |
| 8 | Amazonas | `artigos/amazonas-xarticle.md` | `public/dragao-onca-amazonas.webp` | `dragao-onca-amazonas.html` |
| 9 | Paraná | `artigos/parana-xarticle.md` | `public/dragao-onca-parana.webp` | `dragao-onca-parana.html` |
| 10 | RS · ES · Ranking | `artigos/rs-es-ranking-xarticle.md` | `public/dragao-onca-rs-es.webp` | `dragao-onca-rs-es-ranking-nacional.html` |
| 11 | Síntese v1 | `artigos/sintese-xarticle.md` | `public/dragao-onca-sintese.webp` | `dragao-onca-sintese.html` |
| 12 | PL 2.780 | `artigos/pl2780-xarticle.md` | `public/dragao-onca-pl2780.webp` | `dragao-onca-pl2780.html` |
| 13 | Braço Jurídico | `artigos/braco-juridico-xarticle.md` | `public/dragao-onca-braco-juridico.webp` | `dragao-onca-braco-juridico.html` |

**Sem X Article ainda:** `dragao-onca-sintese-final-cross-state.html` (T-243) — gerar a partir do HTML quando publicar.

---

## Prompt base — hero image (1024×600)

Usar em todo artigo. Substituir `[TÍTULO]`, `[CONCEITO]` e `[CORES]`.

```
Hero image para artigo X.com "[TÍTULO]".
Dimensões exatas: 1024×600 pixels (share card / preview do artigo).
Composição wide 5:2: bloco editorial central com título "[TÍTULO]" em destaque;
conteúdo importante centrado, margens seguras para recorte em feed.
Tema visual: [CONCEITO]. Paleta: fundo #080c10, vermelho dragão #d4342c, dourado onça #e8b23d, acentos [CORES].
Estilo: documentário investigativo, data journalism, tipografia editorial bold.
Grain sutil, sem emojis, sem clipart, sem fundo branco flat.
```

Se o modelo não respeitar 1024×600, redimensionar antes do upload no X.

---

## Como publicar no X Articles

Requer conta **X Premium**.

1. Acesse **x.com/compose/article**
2. Cole o `.md` de `artigos/`
3. Upload da hero (**1024×600 px**, composição 5:2) como capa
4. Publique — link **interno** ao X; URLs externas no **primeiro reply**

---

## Regras de promoção v2.1 (X.com)

| Prioridade | Regra |
|------------|-------|
| **Crítico** | Primeiros **~30 min**: responder todos os replies; rebater comentários próprios |
| **Alto** | Artigo nativo + hero — não publicar só link seco |
| **Alto** | **URLs externas no primeiro reply**, nunca no tweet principal |
| **⚠️** | Máx. **~2 posts/dia** por conta |
| **⚠️** | CTAs específicos — evitar "O que você acha?" |

**Referência:** [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm)

---

## Planos de promoção por artigo

Fluxo: **tweet de abertura** (sem URL externa) → **primeiro reply** (dossiê + fontes) → **janela 30 min**.

---

### 0. Índice da série

**Título:** *O Dragão e a Onça: oito capítulos sobre quem realmente negocia a soberania mineral do Brasil*

**Arquivos:** `artigos/odragaoeaonca-xarticle.md` · `public/dragao-onca.webp` · `index.html`

**Prompt hero:**
```
[TÍTULO] = O Dragão e a Onça
[CONCEITO] = mapa do Brasil fragmentado em estados, linhas geopolíticas Brasil×China, 16 capítulos
[CORES] = roxo #b07aff para dados
```

**Tweet de abertura:**

> 16 dossiês. 9 UFs. 4 eixos transversais.
>
> Pequim assina MoUs. Brasília eleva a relação. Mas quem assina o contrato, enfrenta a comunidade e leva o crédito eleitoral é o governador estadual.
>
> *O Dragão e a Onça* — investigação verificável, CC0.
>
> Artigo completo abaixo.

**Primeiro reply:**

> Dashboard da série (16 dossiês):
> https://odragaoeaonca.vercel.app/
>
> Ordem sugerida: Federal → Diplomático → SP → GO → … → Síntese → PL 2.780 → Jurídico
>
> Qual capítulo priorizar — Taboca, ferrovia do Pará ou terras raras de Goiás?

**Janela 30 min:** explicar ordem CEBC vs. ordem de leitura; reforçar que Minas quebra tese “só China”.

---

### 1. Brasil (Federal)

**Título:** *Brasil-China desde 1993: não é escolha de um governo — é desenho institucional*

**Arquivos:** `artigos/brasil-federal-xarticle.md` · `public/dragao-onca-brasil-federal.webp` · `dragao-onca-brasil-federal.html`

**Prompt hero:**
```
[TÍTULO] = Brasil-China desde 1993
[CONCEITO] = timeline 1993–2026, US$ 171 bi comércio, parceria estratégica institucional
[CORES] = azul diplomático #4a9eff
```

**Tweet de abertura:**

> A Parceria Estratégica Brasil-China existe desde 1993 — antes de Lula.
>
> US$ 171 bi de comércio. US$ 6,1 bi de IED chinês em 2025. Maior destino global.
>
> Tratar isso como escolha de um presidente é erro estrutural.
>
> Capítulo 1. Artigo completo abaixo.

**Primeiro reply:**

> Dossiê interativo (CC0):
> https://odragaoeaonca.vercel.app/dragao-onca-brasil-federal.html
>
> Próximo: Braço Diplomático — WAICO jul/2026 e Serra Verde abr/2026 no mesmo semestre.
>
> Salve a série se quiser acompanhar capítulo a capítulo.

**Janela 30 min:** correção Doria-Sinovac (vacina jun/2020, não 2019); MoU de mineração sem salvaguardas sociais.

---

### 2. Braço Diplomático

**Título:** *Brasil assina governança de IA com a China e vende terras raras aos EUA — no mesmo semestre*

**Arquivos:** `artigos/braco-diplomatico-xarticle.md` · `artigos/braco-diplomatico-xarticle-hero.png` · `dragao-onca-braco-diplomatico.html`

**Prompt hero:**
```
[TÍTULO] = Alinhamento assimétrico duplo
[CONCEITO] = bifurcação Pequim (WAICO, IA) vs. Washington (Serra Verde, terras raras), sem estratégia nacional
[CORES] = teal #2ecfb0 + vermelho EUA implícito
```

**Tweet de abertura:**

> Jul/2026: Brasil entra na WAICO — governança de IA liderada pela China. 29 países. EUA fora.
>
> Abr/2026: USA Rare Earth compra Serra Verde por US$ 2,8 bi. Produção deixa de ir 100% para a China.
>
> Dois movimentos. Duas potências. Zero estratégia nacional de captura de valor.
>
> Artigo abaixo.

**Primeiro reply:**

> Dossiê interativo:
> https://odragaoeaonca.vercel.app/dragao-onca-braco-diplomatico.html
>
> Corpus lawfare-timeline: IDs 1713–1718
>
> WAICO ou minerais críticos: qual eixo federal você monitora em agosto/2026?

**Janela 30 min:** conectar PL 2.780 parado no Senado; explicar “alinhamento assimétrico duplo”.

---

### 3. São Paulo

**Título:** *São Paulo: leilão “neutro”, monopólio chinês no material rodante*

**Arquivos:** `artigos/sao-paulo-xarticle.md` · `artigos/sao-paulo-xarticle-hero.png` · `dragao-onca-sao-paulo.html`

**Prompt hero:**
```
[TÍTULO] = São Paulo: variante mercado
[CONCEITO] = trilhos de trem/metrô, CRRC, terminal COFCO Santos, leilão técnico sem diplomacia pessoal
[CORES] = cinza industrial + dourado onça
```

**Tweet de abertura:**

> Tarcísio não foi à China negociar trem.
>
> Mesmo assim a CRRC consolidou domínio no material rodante paulista. COFCO triplicou capacidade em Santos. R$ 22 bi+ rastreados.
>
> É a variante “mercado” do padrão — leilão neutro, vencedor com escala estatal.
>
> #1 no ranking CEBC (151 projetos). Artigo abaixo.

**Primeiro reply:**

> Dossiê interativo:
> https://odragaoeaonca.vercel.app/dragao-onca-sao-paulo.html
>
> Contraste: Bahia (diplomacia com Xi) vs. SP (leilão técnico). Mesmo país, mecanismos diferentes.
>
> CRRC ou COFCO: qual vetor você auditou em contratos públicos paulistas?

**Janela 30 min:** rebater “anti-China” — mecanismo é mercado/concessão; citar BNDES R$ 5 bi+.

---

### 4. Goiás

**Título:** *Goiás: de Pequim a Washington em 18 meses — e terras raras viram bandeira presidencial*

**Arquivos:** `artigos/goias-xarticle.md` · `public/dragao-onca-goias.webp` · `dragao-onca-goias.html`

**Prompt hero:**
```
[TÍTULO] = Goiás: pivô China → EUA
[CONCEITO] = mina Pela Ema, terras raras, seta Pequim→Washington, Caiado 2026
[CORES] = roxo campanha #b07aff
```

**Tweet de abertura:**

> Nov/2023: Caiado assina com a China em Xangai.
> Abr/2026: USA Rare Earth compra a Serra Verde por US$ 2,8 bi.
> 31/mar/2026: deixa o governo para disputar a Presidência.
>
> Termos do contrato de 15 anos com entidades dos EUA não são públicos.
>
> Capítulo 4. Artigo abaixo.

**Primeiro reply:**

> Dossiê interativo:
> https://odragaoeaonca.vercel.app/dragao-onca-goias.html
>
> Qual lacuna priorizar — incentivos fiscais de Itumbiara ou identidade da SPV dos EUA?

**Janela 30 min:** pivô carne 55% excedente vs. acordo mineral EUA.

---

### 5. Minas Gerais

**Título:** *Minas Gerais prova que o padrão não é a China — é o mecanismo*

**Arquivos:** `artigos/minas-gerais-xarticle.md` · `public/dragao-onca-minas-gerais.webp` · `dragao-onca-minas-gerais.html`

**Prompt hero:**
```
[TÍTULO] = Minas: o padrão não é a China
[CONCEITO] = Sigma Lithium Nasdaq, Vale do Lítio, capital ocidental/coreano, Zema
[CORES] = azul ocidental #4a9eff
```

**Tweet de abertura:**

> Minas quebra a tese de que o padrão é só China.
>
> Sigma Lithium na Nasdaq. R$ 3 bi no Jequitinhonha. Mina parada 5 meses depois do lançamento.
> Zema abandonou o lítio quando as pesquisas não colaboraram.
>
> Capítulo de contraste. Artigo abaixo.

**Primeiro reply:**

> Dossiê interativo:
> https://odragaoeaonca.vercel.app/dragao-onca-minas-gerais.html
>
> Zema pivotou para o STF. Caiado manteve terras raras. Qual estratégia de descarte de ativo você monitora em 2026?

**Janela 30 min:** rebater leituras “anti-China”.

---

### 6. Bahia

**Título:** *Jerônimo negociou com Xi Jinping — e a TIR chinesa caiu de 13% para 10,88%*

**Arquivos:** `artigos/bahia-xarticle.md` · `artigos/bahia-xarticle-hero.png` · `dragao-onca-bahia.html`

**Prompt hero:**
```
[TÍTULO] = Bahia: caso de controle
[CONCEITO] = Ponte Salvador-Itaparica, Baía de Todos-os-Santos, Jerônimo × Xi, TIR 13%→10,88%
[CORES] = verde confirmação #3ecb6f (padrão falha com benefício)
```

**Tweet de abertura:**

> Caso de controle da série: aqui o padrão dominante **não se confirma**.
>
> Jerônimo negociou com Xi Jinping. PPP da ponte subiu para R$ 10,6 bi.
> Mas a TIR dos acionistas chineses **caiu** de 13% para 10,88%.
>
> Captura com benefício ao estado — raro na série. Artigo abaixo.

**Primeiro reply:**

> Dossiê interativo:
> https://odragaoeaonca.vercel.app/dragao-onca-bahia.html
>
> Contraste com Pará (exclusão comunitária) e SP (mercado). Bahia muda sua leitura da tese?

**Janela 30 min:** explicar “caso de controle” metodológico; Windey Camaçari + estaleiro São Roque.

---

### 7. Pará

**Título:** *Pará: ferrovia chinesa, COP30 e 39 mortes que ninguém menciona nos anúncios*

**Arquivos:** `artigos/para-xarticle.md` · `public/dragao-onca-para.webp` · `dragao-onca-para.html`

**Prompt hero:**
```
[TÍTULO] = Pará: ferrovia e COP30
[CONCEITO] = corredor mineral, ferrovia CCCC/Vale, COP30 Belém, 39 mortes T.I. Mãe Maria
[CORES] = verde floresta escuro + vermelho alerta
```

**Tweet de abertura:**

> 2019: protocolo com a CCCC. Traçado definido.
> 2023: MoU em Pequim — R$ 10 bi, Vale entra.
> 2026: audiências públicas começam. Sete anos depois.
>
> Na mesma região, trem da Vale matou 39 pessoas em 8 anos.
>
> Capítulo mais denso. Artigo abaixo.

**Primeiro reply:**

> Dossiê interativo:
> https://odragaoeaonca.vercel.app/dragao-onca-para.html
>
> COP30 + Ferrovia + Norsk Hydro — três vetores, mesmo padrão de exclusão comunitária.

**Janela 30 min:** timeline 2019→2026; Programa Estrutura (dívida Vale → obra pública).

---

### 8. Amazonas

**Título:** *Amazonas: estatal chinesa, rio contaminado e R$ 12,3 mi dois dias depois da desconfiança*

**Arquivos:** `artigos/amazonas-xarticle.md` · `public/dragao-onca-amazonas.webp` · `dragao-onca-amazonas.html`

**Prompt hero:**
```
[TÍTULO] = Amazonas: Taboca e Waimiri-Atroari
[CONCEITO] = rio Alalaú, estanho Taboca, China Nonferrous, 22 aldeias, investigação MPF/PF
[CORES] = vermelho crítico intenso #ff6b5f
```

**Tweet de abertura:**

> O capítulo mais grave da série.
>
> China Nonferrous controla a Taboca ao lado da TI Waimiri Atroari.
> MPF reabriu inquérito. PF abriu investigação criminal em jul/2026.
> R$ 12,3 mi à ACWA — 2 dias depois da desconfiança total da comunidade.
>
> 22 aldeias dependem do rio Alalaú. Artigo abaixo.

**Primeiro reply:**

> Dossiê interativo:
> https://odragaoeaonca.vercel.app/dragao-onca-amazonas.html
>
> Taboca ou ZFM: qual eixo merece investigação mais profunda na sua região?

**Janela 30 min:** prioridade máxima — datas FUNAI, MPF, PF.

---

### 9. Paraná

**Título:** *Paraná: acordos gêmeos na China — estado e união, dois dias de diferença*

**Arquivos:** `artigos/parana-xarticle.md` · `public/dragao-onca-parana.webp` · `dragao-onca-parana.html`

**Prompt hero:**
```
[TÍTULO] = Paraná: acordos gêmeos
[CONCEITO] = porto Paranaguá, CMPort 90%, calendário 3/nov vs 5/nov 2025 Shenzhen/Xangai
[CORES] = azul portuário + dourado
```

**Tweet de abertura:**

> 3/nov/2025: APPA assina com CMPort em Shenzhen.
> 5/nov/2025: Ministério de Portos assina R$ 1,5 bi em Xangai — mesmo terminal.
>
> Único capítulo da série com coordenação explícita estado + união com a **mesma** estatal chinesa.
>
> CMPort controla 90% do TCP desde 2018. Artigo abaixo.

**Primeiro reply:**

> Dossiê interativo:
> https://odragaoeaonca.vercel.app/dragao-onca-parana.html
>
> SP não mostra articulação equivalente na COFCO. Paraná mostra. Isso muda o desenho federal?

**Janela 30 min:** comparar com São Paulo (Cap. 3) — mercado vs. coordenação.

---

### 10. RS · ES · Ranking CEBC

**Título:** *RS perdeu, ES ganhou — e o ranking CEBC explica por que diplomacia não basta*

**Arquivos:** `artigos/rs-es-ranking-xarticle.md` · `public/dragao-onca-rs-es.webp` · `dragao-onca-rs-es-ranking-nacional.html`

**Prompt hero:**
```
[TÍTULO] = RS perdeu, ES ganhou
[CONCEITO] = mapa RS vs ES, fábrica GWM Aracruz, ranking CEBC tabela, BYD Shenzhen
[CORES] = teal ranking #2ecfb0
```

**Tweet de abertura:**

> Leite foi pessoalmente a Shenzhen. Reuniu-se com BYD. Imprensa gaúcha: "balde de água fria".
>
> A GWM escolheu o Espírito Santo — proximidade portuária de Aracruz, não cortejo mais intenso.
>
> RS: 6º no ranking CEBC (20 projetos). ES: 17º (3 projetos). Mesma disputa, desfechos opostos.
>
> Artigo abaixo.

**Primeiro reply:**

> Dossiê + ranking completo CEBC 2007-2025:
> https://odragaoeaonca.vercel.app/dragao-onca-rs-es-ranking-nacional.html
>
> US$ 85,5 bi · 355 projetos · SP líder com 151
>
> Próximo estado a documentar: SC, RJ ou MA?

**Janela 30 min:** explicar que ranking histórico ≠ vitória pontual; par de controle metodológico.

---

### 11. Síntese v1

**Título:** *Soberania na conta do governador: o que 5 capítulos revelam juntos*

**Arquivos:** `artigos/sintese-xarticle.md` · `public/dragao-onca-sintese.webp` · `dragao-onca-sintese.html`

**Prompt hero:**
```
[TÍTULO] = Soberania na conta do governador
[CONCEITO] = quadro comparativo 4 governadores, KPIs cross-estaduais, alertas críticos
[CORES] = roxo síntese #b07aff
```

**Tweet de abertura:**

> 5 capítulos. 4 governadores. 5 blocos geopolíticos.
>
> Caiado, Barbalho, Wilson Lima, Zema — mesma sequência:
> negociar → excluir comunidade → converter ativo em campanha.
>
> Síntese v1 (GO, PA, AM, MG + federal). Artigo abaixo.

**Primeiro reply:**

> Dossiê interativo:
> https://odragaoeaonca.vercel.app/dragao-onca-sintese.html
>
> Síntese final (9 UFs): https://odragaoeaonca.vercel.app/dragao-onca-sintese-final-cross-state.html

**Janela 30 min:** reforçar tese “nenhum vetor chega ao beneficiário final”; indicar síntese final T-243.

---

### 12. PL 2.780/2024

**Título:** *PL 2.780/2024: R$ 2 bi para o investidor, zero para a comunidade — e o INESC confirma Goiás*

**Arquivos:** `artigos/pl2780-xarticle.md` · `public/dragao-onca-pl2780.webp` · `dragao-onca-pl2780.html`

**Prompt hero:**
```
[TÍTULO] = PL 2.780/2024
[CONCEITO] = FGAM R$ 2 bi, streaming mineral, Senado, INESC Serra Verde
[CORES] = roxo legislativo
```

**Tweet de abertura:**

> PL 2.780/2024: aprovado na Câmara (mai/2026). 21 → 51 artigos em dias.
>
> R$ 2 bi de fundo garantidor para investidores privados.
> Zero mecanismo equivalente para comunidades afetadas.
>
> INESC cita Serra Verde (Goiás) para explicar risco de streaming.
>
> Aguarda o Senado. Artigo abaixo.

**Primeiro reply:**

> Dossiê dedicado:
> https://odragaoeaonca.vercel.app/dragao-onca-pl2780.html
>
> Nota INESC: https://inesc.org.br/wp-content/uploads/2026/05/nt-substitutivo-pl-minerais-criticos.pdf
>
> Se sancionado, monitorar Taboca, Ferrovia do Pará ou Sigma Lithium?

**Janela 30 min:** FGAM vs. ausência de fundo comunitário; streaming + USA Rare Earth.

---

### 13. Braço Jurídico

**Título:** *Braço Jurídico: a arquitetura legal que viabiliza os capítulos estaduais*

**Arquivos:** `artigos/braco-juridico-xarticle.md` · `public/dragao-onca-braco-juridico.webp` · `dragao-onca-braco-juridico.html`

**Prompt hero:**
```
[TÍTULO] = Braço Jurídico
[CONCEITO] = balança STF, marco temporal 9×1, PL Devastação pós-COP30, ADI 7919
[CORES] = roxo jurídico + dourado
```

**Tweet de abertura:**

> Os capítulos estaduais documentam execução.
> Este documenta a arquitetura legal que viabiliza tudo.
>
> Marco temporal: STF 9×1, mas lei permanece em vigor.
> Vetos derrubados 6 dias após a COP30.
> Taboca/ACWA: R$ 12,3 mi sem mediação do MPF.
>
> Artigo abaixo.

**Primeiro reply:**

> Dossiê interativo:
> https://odragaoeaonca.vercel.app/dragao-onca-braco-juridico.html
>
> ADI 7919 em tramitação — ponte com lawfare-timeline.
>
> Execução (governadores) ou arquitetura (Congresso/STF): qual frente priorizar?

**Janela 30 min:** marco temporal → Taboca → Cinta Larga.

---

## Calendário sugerido (14 dias)

| Dia | Artigo | Motivo |
|----:|--------|--------|
| 0 | Índice | Porta de entrada da série |
| 1 | Federal | Contexto histórico |
| 2 | Braço Diplomático | Eixo federal atual (WAICO + terras raras) |
| 3 | São Paulo | #1 CEBC, variante mercado |
| 4 | Goiás | Pivô geopolítico + eleição 2026 |
| 5 | Minas Gerais | Contraste ocidental |
| 6 | Bahia | Caso de controle metodológico |
| 7 | Pará | Densidade máxima |
| 8 | Amazonas | Gravidade máxima (MPF/PF) |
| 9 | Paraná | Coordenação estado–união |
| 10 | RS · ES · Ranking | Dados transversais CEBC |
| 11 | Síntese v1 | Consolidação parcial |
| 12 | PL 2.780 | Urgência legislativa |
| 13 | Braço Jurídico | Fechamento arquitetural |

---

## Checklist pós-publicação

- [ ] Hero 1024×600 como capa do Article
- [ ] Tweet de abertura (sem URL externa)
- [ ] Primeiro reply com dossiê HTML + fontes
- [ ] Monitorar replies nos **primeiros 30 min**
- [ ] Conta dentro do limite **≤2 posts/dia**
- [ ] CTAs específicos — sem iscas genéricas

---

## Corpus e metodologia

- **Dossiês HTML:** 16 · **X Articles:** 14 (+ T-243 pendente)
- **Entradas:** 126 posts Jekyll · 110 entradas lawfare.json · IDs 1639–1748
- **CEBC abr/2026:** US$ 85,5 bi · 355 projetos · ranking por UF
- **Níveis de evidência:** `ev-confirmed` · `ev-alleged` · `ev-inference` · `lacuna_investigativa`
- **Padrões:** P05 · P09 · P10 · P04b · P11 (ranking/mercado)
- **Atualização:** jul/2026

---

## Contribuir / reutilizar

Conteúdo em **domínio público (CC0)**. Citar a série *O Dragão e a Onça* / *lawfare-timeline*.

Para novos X Articles: ler dossiê HTML → formatar `.md` → gerar hero 1024×600 (prompt acima) → salvar em `artigos/[slug]-xarticle.md` + hero.
