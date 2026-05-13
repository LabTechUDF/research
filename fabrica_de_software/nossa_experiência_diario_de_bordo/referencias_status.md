# Status das Referências — `artigo-cadernos.tex`

Documento de auditoria das referências do `referencias.bib` em três dimensões:
(1) presença de PDF salvo no repositório, (2) uso atual no artigo e (3)
recomendação sobre incluir/excluir entradas atualmente não utilizadas.

Atualizado em: **2026-05-12**.
Total de entradas no `.bib`: **28**.

---

## 1. Referências citadas no artigo (18 entradas)

| Chave | PDF salvo | Localização do PDF |
|---|---|---|
| `agenciapib2020` | — (web) | https://agenciabrasilia.df.gov.br/2020/03/11/gdf-recebe-grupos-do-setor-de-tecnologia-da-informacao/ |
| `ander-egg1978` | ❌ não | livro Humanitas (Buenos Aires, 7ª ed.) |
| `bacigalupo2016entrecomp` | ❌ não | https://publications.jrc.ec.europa.eu/repository/handle/JRC101581 |
| `bardin2011` | ❌ não | livro Edições 70 (São Paulo) |
| `bernardi2017learning` | ✅ sim | `referencias/fichamento/Learning-by-Doing-em-Fábrica-de-Software-...pdf` |
| `cusumano1991japan` | ❌ não | livro Oxford University Press (1991) |
| `dcncomputacao2016` | ✅ sim | `referencias/DCNs eng software.pdf` |
| `ebctecnologia2024` | — (web) | https://agenciabrasil.ebc.com.br/.../empregos-ligados-tecnologia-cresceram-95-em-10-anos-diz-pesquisa |
| `fernandes2004fabrica` | ❌ não | livro Atlas (São Paulo, 2004) |
| `kerlla` | ✅ sim | `kerlla/analysis_of_learning_assessment_role_using_active_methodologies_in_KAA_perspective.pdf` |
| `mattos2011etnografia` | ✅ sim | `referencias/fichamento/Etnografia-e-educação-conceitos-e-usos.pdf` |
| `mineiro2022pesquisa` | ✅ sim | `referencias/fichamento/PESQUISA-QUALITATIVA-E-QUANTITATIVA.pdf` |
| `oliveira2017conduccao` | ✅ sim | `referencias/Conducao-de uma Fabrica de Software....pdf` |
| `perides2021competencias` | ✅ sim | `referencias/fichamento/GESTORES-DE-PROJETOS-QUE-ATUAM-COM-MÉTODOS-ÁGEIS-E-TRADICIONAIS.pdf` |
| `santos2021experiencia` | ✅ sim | `referencias/fichamento/Experiencia-do-Projeto-Fabrica-de-Software-em-um-Curso-de-Engenharia-de-Software.pdf` |
| `sherer1982gse` | ❌ não | https://journals.sagepub.com/doi/10.2466/pr0.1982.51.2.663 |
| `udfppc2023` | ✅ sim | `referencias/PPC Ciencia da Computacão_UDF (2).pdf` (e PPCs ADS/SI) |
| `wef:2025` | ✅ sim | `referencias/WEF_Future_of_Jobs_Report_2025.pdf` |

> **Total citado**: 18 chaves (13 com PDF salvo, 5 sem PDF — todos verificáveis online ou em biblioteca).

---

## 2. Referências NÃO citadas atualmente (10 entradas)

### 2.1 Citações adicionadas em 2026-05-12 (5 entradas, antes não-citadas)

| Chave | Local de inserção | Conteúdo agregado |
|---|---|---|
| `cusumano1991japan` | Introdução (parágrafo 2) | "conceito originalmente cunhado por Cusumano (1991) para descrever a sistematização do desenvolvimento no modelo industrial japonês" |
| `wef:2025` | Introdução (novo parágrafo) | Future of Jobs Report 2025 — pensamento analítico, liderança, aprendizagem contínua e alfabetização tecnológica até 2030 |
| `oliveira2017conduccao` | Introdução (junto com bernardi) | Reforça base brasileira para Fábricas de Software acadêmicas |
| `fernandes2004fabrica` | Metodologia § Procedimentos do LabTech | Definição clássica brasileira de Fábrica de Software como processo estruturado e controlado |
| `mattos2011etnografia` | Metodologia § Abordagem Qualitativa e Quantitativa | Sustenta a observação direta e situada das práticas cotidianas |

### 2.2 Recomendado **manter no `.bib`** sem citar agora

Manter como reserva para versões futuras ou para o TCC/monografia:
`marconi2022metodologia`, `matias2016manual`, `bunge1997epistemologia` — boas referências de método científico; o artigo já cita Ander-Egg para esse fim.

### 2.3 Recomendado **remover** (ou mover para o `.bib` da monografia)

| Chave | Motivo |
|---|---|
| `iso2017` | Fora de escopo do artigo de extensão. |
| `gartner2023` | Fonte cinza, não usada. |
| `ferreira2018` | Não usada e periódico difícil de validar. |
| `lacerda2020` | Não usada; soft skills já cobertas por Perides 2021. |
| `martins2021` | Não usada e tópico já coberto. |
| `sommerville2019` | Manual canônico mas sem necessidade direta no relato. |
| `ibge2025` | Não usada; dados do DF já vêm de Agência Brasília. |

> **Nota**: a remoção é opcional — entradas não citadas não aparecem no PDF compilado quando se usa BibTeX. O .bib atual produz exatamente as referências usadas, sem ruído.

---

## 3. Referências citadas mas SEM PDF salvo (5 entradas)

Vale baixar para o repositório:

| Chave | Onde obter | Prioridade |
|---|---|---|
| `bacigalupo2016entrecomp` | PDF aberto no JRC: https://publications.jrc.ec.europa.eu/repository/handle/JRC101581 | 🔴 alta — instrumento central do artigo |
| `sherer1982gse` | SAGE (paywall) ou cópia ResearchGate de Mark Sherer | 🟠 média — segundo instrumento central |
| `bardin2011` | livro físico ou PDF acadêmico (acesso restrito por direitos) | 🟢 baixa — clássico bem conhecido |
| `ander-egg1978` | Google Books snippets, Humanitas / 7ª ed. | 🟢 baixa — citação pontual |
| `cusumano1991japan` | livro Oxford University Press; biblioteca ou via interlibrary loan | 🟢 baixa — citação histórica |
| `fernandes2004fabrica` | livro Atlas; biblioteca | 🟢 baixa — referência conceitual brasileira |

---

## 4. Correções aplicadas no `.bib` (2026-05-12)

| Chave | Correção |
|---|---|
| `bernardi2017learning` | `pages={XX--XX}` → `pages={203--212}`; adicionado `doi={10.5753/eres.2017.10098}` e `url`; address corrigido para "Porto Alegre". |
| `ander-egg1978` | título: "investigacions" → "investigacion social". |

---

## 5. Citações obrigatórias adicionadas no artigo (2026-05-12)

| Chave | Local |
|---|---|
| `dcncomputacao2016` | Metodologia § Lócus da Pesquisa (enquadra os cursos do UDF nas DCN); Análise/Discussão § Aspectos Educacionais e § Andaimagem Institucional. |
| `kerlla` | Análise/Discussão § Aspectos Educacionais (perspectiva KAA da aprendizagem ativa em engenharia) e § Andaimagem Institucional. |

---

## 6. Resumo executivo

- **18 chaves** efetivamente citadas no artigo, **13 com PDF salvo** no repositório.
- **5 referências sem PDF** — destas, três são centrais (EntreComp, Sherer GSE, Bardin); recomenda-se baixar pelo menos a do EntreComp (acesso aberto).
- **5 chaves antes não-citadas** foram integradas em 2026-05-12: `cusumano1991japan`, `wef:2025`, `oliveira2017conduccao`, `fernandes2004fabrica`, `mattos2011etnografia` --- todas com PDF salvo (3 das 5).
- **7 entradas** podem ser removidas do `.bib` (não usadas e fora de escopo do artigo de extensão); manutenção apenas se servirem ao TCC/monografia paralela.
