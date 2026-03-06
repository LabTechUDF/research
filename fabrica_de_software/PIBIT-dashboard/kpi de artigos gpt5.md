perfeito! Vou usar os PDFs que você anexou para (OE1) sintetizar o que a literatura recomenda medir e (OE2) propor um conjunto enxuto de KPIs “prontos para o dashboard” — com foco em GitHub e contexto de Fábricas de Software Acadêmicas.

# 1) Revisão de literatura (OE1) — o que medir

**GitHub (nativo + complementares propostos na literatura)**

* Nativos do GitHub: *commits por semana*, *sazonalidade de código* (épocas com mais adições/remoções), *punch card* (horas/dias com mais commits), e *network* de commits por branches.&#x20;
* Complementares (AMP.br + PyNdicators): *rótulos de issues mais comuns (RIC)*, *issues abertas vs fechadas (IAF)*, *issues com/sem responsável (NIA)*, *tempo para fechamento de issues (TFI)*, *nº de issues por mês/ano (NIC)*, *commits por mês/ano (CMA)*, *linhas incluídas vs excluídas por autor (IEA)*, *% de commits por autor (PCA)* e *ranking de colaborador por mês (RCM)*.  &#x20;
* A própria API do GitHub viabiliza isso (Issues, Commits, Statistics; JSON), com campos para estados, responsáveis, datas, linhas adicionadas/removidas, etc.&#x20;

**Projetos acadêmicos com Git/GitHub (ênfase em avaliação justa e engajamento)**

* Métricas brutas úteis: *commits*, *merges/PRs*, *churn* (adições/remoções), e *frequência diária* (commits/merges por dia).&#x20;
* Medidas agregadas para justiça/risco: índices de **desigualdade** (*Gini*, *Theil*, *Hoover*, *inter-decile ratios*) para revelar concentração de contribuições (herói/“bus factor”).&#x20;
* Cautela: métricas quantitativas **não são** proxy perfeito de desempenho de equipe; devem complementar avaliação qualitativa.&#x20;

**Dashboards e arquitetura de dados**

* ETL → DW/BD central → dashboard (ex.: Power BI, QuickSight) para métricas em tempo (quase) real. &#x20;
* Coletas **diárias ou semanais** atendem bem ao acompanhamento pedagógico.&#x20;
* (Opcional) Qualidade de código (Sonar): linhas, arquivos, métodos, **complexidade ciclomática**, incidentes — útil em nível equipe/projeto. Limitação comum: difícil mapear com precisão para indivíduos. &#x20;

# 2) KPIs propostos (OE2) — prontos para o seu dashboard

Abaixo, cada KPI vem com **o que mede** e **como calcular** (do GitHub). Todos se aplicam a **projeto/equipe/indivíduo** salvo indicado.

## Progresso & Capacidade (throughput)

* **CMA — Commits por mês/ano**: `COUNT(commits)` por período e autor/projeto. Ajuda a ver cadência e picos/vales.&#x20;
* **PRs/Merges por período**: `COUNT(pull_requests merged_at in [t0,t1])`. Pareado com CMA, indica entrega integrada.&#x20;
* **IEA — Inclusões vs Exclusões por autor (churn)**: `SUM(additions), SUM(deletions)` semanal/mensal por autor. Sinaliza retrabalho/refatorações. &#x20;

## Fluxo & Tempo

* **TFI — Tempo para Fechamento de Issues**: `median(closed_at - created_at)` (por tipo/gravidade). Base para SLOs pedagógicos.&#x20;
* **Lead time de PR** *(proposto)*: `median(merged_at - created_at)`; pode ser de **commit→deploy** se integrarem CI/CD depois. Viável via timestamps do endpoint de PRs e events.&#x20;
* **Tempo até 1ª resposta (Issues/PRs)** *(proposto)*: `median(first_comment_at - created_at)`; proxie de **responsividade**. Viável com endpoints de comentários e review comments.&#x20;

## Saúde do Backlog

* **IAF — Issues abertas vs fechadas**: razão `closed/open` no período, com *aging* de abertas por faixas de dias.&#x20;
* **NIC — Issues por mês/ano** (por label/tipo): detecta “tempestades” de defeitos ou sobrecarga.&#x20;
* **NIA — Issues com/sem responsável**: qualidade do processo de triagem/atribuição.&#x20;

## Colaboração & Engajamento

* **PCA — % de commits por autor**: participação relativa no período (equilíbrio da carga).&#x20;
* **RCM — Ranking de colaborador por mês**: ranking por commits/PRs fechados; útil para feedback e balanceamento.&#x20;
* **Rede revisor↔autor (grau/densidade)** *(proposto)*: construa grafo com arestas `author → reviewer/commenter` em PRs/issues; meça **grau médio**/**densidade** como proxy de colaboração.&#x20;

## Desigualdade & Risco (justiça e “bus factor”)

* **Índice de Gini / Theil / Hoover / Inter-decile** sobre distribuição de *commits/merges/churn* por pessoa no time; evidencia dependência em “heróis” e desigualdade de carga. &#x20;

> **Observação pedagógica**: use esses KPIs **como feedback formativo**; a própria literatura ressalta que métricas quantitativas não substituem avaliação qualitativa de colaboração e aprendizagem.&#x20;

# 3) Campos & endpoints do GitHub (para a coleta automática – OE3)

* **Issues API**: estados, labels, `assignee`, timestamps de abertura/fechamento → TFI, IAF, NIC, NIA.&#x20;
* **Commits API**: autor, mensagem, data → CMA, PCA, RCM.&#x20;
* **Statistics API**: linhas adicionadas/removidas por semana/autor → IEA (churn).&#x20;
* **Pull Requests/Reviews/Comments** *(para KPIs novos)*: contagens, `created_at`, `merged_at`, comentários e reviewers → PR throughput, lead time de PR, tempo até 1ª resposta, rede revisor↔autor. (viável; a literatura mostra que podemos ir além dos nativos criando métricas personalizadas com a API).&#x20;

# 4) Forma de visualização sugerida (OE4)

* **Séries temporais** (CMA, NIC, PRs/merges) e **histogramas** (TFI/lead time).
* **KPI cards** com alvo/meta (ex.: TFI ≤ 7 dias por defeito) e **heatmaps** para *punch card*. &#x20;
* **Gráfico de Pareto** e **grafos de colaboração** para desigualdade e rede. &#x20;

# 5) Ameaças e cuidados

* **Atribuição individual em métricas de qualidade de código** (ex.: Sonar) pode ser frágil; prefira nível equipe/projeto.&#x20;
* **Métricas ≠ desempenho pedagógico**: triangule com avaliações qualitativas/peer review.&#x20;

---

## Próximo passo prático

Se você curtir esse recorte, eu já organizo um **dicionário de dados** (nome do KPI, fórmula, endpoint/fields do GitHub, granularidade, periodicidade de coleta, visualização sugerida) e um **esquema de tabelas** para o seu ETL (diário/semanal), alinhado à proposta do PIBIT. &#x20;

Quer que eu já gere esse dicionário com as fórmulas e colunas (CSV/Markdown) com base nos KPIs acima?

