# 📋 Próximas Ações - Dashboard Fábrica de Software Acadêmica

## ✅ Concluído

### Etapa 1: Melhoramento do Artigo
- [x] Integração literatura sobre co-development e métricas
- [x] Atualização do arquivo `artigo.bib` com novas referências  
- [x] Incorporação das métricas implementadas (20 visualizações)
- [x] Refinamento da seção arquitetura medalhão com foco open source

### Etapa 2: Diagramas de Arquitetura
- [x] Diagrama de topologia geral (`topologia_dashboard.mmd` - corrigido)
- [x] Diagrama de sequência ETL (`sequencia_etl.mmd`)
- [x] DAG da arquitetura medalhão (`dag_medalhao.mmd` - corrigido)  
- [x] Diagrama de arquitetura completa (`arquitetura_geral.mmd` - corrigido)
- [x] Diagramas ASCII alternativos (`topologia_ascii.txt`, `etl_flow_ascii.txt`)

### Etapa 3: Atualização dos Documentos
- [x] Atualização do relatório parcial com estado real do projeto
- [x] Inclusão de 4 gráficos representativos no relatório parcial
- [x] Correção das inconsistências sobre implementação
- [x] Clarificação do próximo passo: organizar repositório GPL3

## 📊 Estado Atual Real do Projeto

### Artefatos Implementados
- **`extrair-dados-github.py`**: Script Python funcional que:
  - Coleta dados via GitHub API com cache inteligente
  - Implementa rate limiting e retry logic
  - Filtra organizações, repositórios, issues, PRs, commits
  - Gera `github-data.json` (2.7MB) com dados reais da LabTechUDF

- **`gerar_graficos_github.ipynb`**: Notebook Jupyter que:
  - Processa o JSON coletado 
  - Gera 20 visualizações organizadas por categoria
  - Implementa métricas técnicas, colaborativas e comportamentais
  - Salva gráficos PNG na pasta `coops/out/`

### Dados Disponíveis
- **Bronze layer**: `github-data.json` (real data from LabTechUDF)
- **Gold layer**: 20 visualizações PNG prontas
- **Silver layer**: Processamento no notebook (não persistido)

### Documentação Produzida
- Diagramas Mermaid da arquitetura alvo (corrigidos)
- Diagramas ASCII para documentação
- Artigo científico atualizado com literatura
- Relatório parcial com estado real do projeto

## 🎯 Próximas Ações Recomendadas

### 1. Organização do Repositório (Prioridade Alta)
- [ ] **Estruturar repositório open source com licença GPL3**
  - Organizar scripts Python em estrutura limpa
  - Criar documentação README para replicação
  - Definir estrutura de pastas data/bronze/, data/silver/, data/gold/
  - Configurar .gitignore apropriado

### 2. Implementação Técnica (Prioridade Média)
- [ ] **Configurar GitHub Actions workflows**
  - Criar `.github/workflows/etl-daily.yml` para coleta diária
  - Implementar scripts Python para Bronze→Silver→Gold
  - Configurar rate limiting e cache para GitHub API

- [ ] **Desenvolver frontend React/D3.js**  
  - Setup do projeto React com Vite
  - Integração da biblioteca D3.js para visualizações
  - Implementação do GitHub API client
  - Configuração do Firebase Hosting

### 2. Estrutura de Dados (Prioridade Alta)
- [ ] **Implementar camadas da arquitetura medalhão**
  - Definir estrutura de pastas `data/bronze/`, `data/silver/`, `data/gold/`
  - Criar schemas para as tabelas Silver (dim/fact)
  - Implementar versionamento e linhagem dos dados
  - Configurar armazenamento em formato Parquet/CSV

### 3. KPIs e Visualizações (Prioridade Média)
- [ ] **Implementar KPIs prioritários**
  - Slope_8w (ritmo inicial) baseado nos Apêndices A/B
  - Clones_W1-W2 (intenção de participação)
  - Índices de desigualdade (Gini, Theil, Hoover)
  - Métricas de centralidade em grafos

- [ ] **Criar dashboards interativos**
  - Visão por projeto/repositório
  - Visão por equipe/membro  
  - Análise temporal com filtros
  - Grafos de colaboração interativos

### 4. Testes e Validação (Prioridade Média)
- [ ] **Conduzir testes-piloto**
  - Testar com dados reais da organização LabTechUDF
  - Coletar feedback de docentes/gestores
  - Validar usabilidade do dashboard
  - Medir performance da pipeline ETL

### 5. Documentação e Disseminação (Prioridade Baixa)
- [ ] **Documentação técnica**
  - README detalhado para replicação por outras fábricas
  - Documentação da API e endpoints
  - Guia de instalação e configuração
  - Troubleshooting e FAQ

- [ ] **Publicação acadêmica**
  - Finalizar artigo com resultados dos testes-piloto
  - Preparar apresentação para conferências
  - Criar demo online para divulgação
  - Disponibilizar código sob licença GPL3

## 🏗️ Arquitetura Técnica Sugerida

### Estrutura de Repositório
```
PIBIT-dashboard/
├── .github/workflows/          # GitHub Actions
├── src/                        # Frontend React
├── scripts/                    # Python ETL scripts  
├── data/
│   ├── bronze/                # Raw JSON from GitHub API
│   ├── silver/                # Normalized tables
│   └── gold/                  # Ready-to-consume KPIs
├── docs/                      # Documentation
└── tests/                     # Unit/integration tests
```

### Stack Tecnológico
- **ETL**: Python + pandas + requests
- **Frontend**: React + Vite + D3.js + Material-UI
- **Hosting**: Firebase Hosting (free tier)
- **CI/CD**: GitHub Actions (free para repos públicos)
- **Armazenamento**: Próprio repositório GitHub (sem custos)

## 💡 Ideias Adicionais

### Integração com Outras Plataformas
- [ ] Suporte a GitLab como fonte de dados alternativa
- [ ] Integração com Notion para documentação de projetos
- [ ] Conexão com Slack/Teams para notificações automatizadas

### Analytics Avançados  
- [ ] Machine learning para predição de sucesso de projetos
- [ ] Análise de sentiment em comentários de PRs/issues
- [ ] Detecção automática de padrões de colaboração

### Gamificação Educativa
- [ ] Sistema de badges baseado em métricas de colaboração
- [ ] Rankings semanais por equipe (com foco pedagógico)
- [ ] Challenges de código colaborativo

## 🎓 Contribuição Acadêmica

Este trabalho contribui para:
- **Democratização** de analytics em ambientes acadêmicos
- **Padronização** de métricas para fábricas de software acadêmicas  
- **Open source** e reusabilidade entre instituições
- **Metodologia** mista (quantitativa + qualitativa) para interpretação de métricas
- **Inovação** em arquiteturas serverless para educação

---
*Documento gerado automaticamente em: 2025-01-XX*
