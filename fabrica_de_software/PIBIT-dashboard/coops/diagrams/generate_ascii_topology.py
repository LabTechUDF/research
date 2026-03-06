#!/usr/bin/env python3
"""
Gerador de Topologia ASCII - Dashboard para Fábricas de Software Acadêmicas
Arquitetura GitHub Actions + Firebase + React/D3.js

Este script gera uma representação em texto ASCII da arquitetura proposta.
"""

def generate_ascii_topology():
    """Gera representação ASCII da topologia da aplicação"""
    
    topology = """
    ╔══════════════════════════════════════════════════════════════════════════════════╗
    ║                     🎓 STAKEHOLDERS (Ambiente Acadêmico)                        ║
    ╠══════════════════════════════════════════════════════════════════════════════════╣
    ║  👨‍🏫 Docentes/Gestores    👨‍🎓 Estudantes    🔬 Pesquisadores/Analistas           ║
    ║         │                      │                      │                        ║
    ║         └──────────────────────┼──────────────────────┘                        ║
    ║                                │ HTTPS                                          ║
    ╚═══════════════════════════════┬┴══════════════════════════════════════════════════╝
                                    │
    ╔═══════════════════════════════┴══════════════════════════════════════════════════╗
    ║                        🌐 FRONTEND & HOSTING                                    ║
    ╠══════════════════════════════════════════════════════════════════════════════════╣
    ║              ☁️ Firebase Hosting ──► ⚛️ React + D3.js                           ║
    ║                                      │                                          ║
    ║                                      │ GitHub API                               ║
    ║                                      │ (Read Data)                              ║
    ╚═══════════════════════════════════════┼══════════════════════════════════════════╝
                                           │
    ╔══════════════════════════════════════┴══════════════════════════════════════════╗
    ║                         📦 REPOSITÓRIO CENTRAL                                  ║
    ╠══════════════════════════════════════════════════════════════════════════════════╣
    ║                      🗂️ Dashboard Repository                                   ║
    ║                              │                                                  ║
    ║  ┌───────────────────────────┼───────────────────────────────────────────────┐  ║
    ║  │                🗄️ CAMADAS DE DADOS                                        │  ║
    ║  │                                                                           │  ║
    ║  │  🥉 Bronze          🥈 Silver           🥇 Gold                           │  ║
    ║  │  Raw JSON     ──►   Normalized   ──►   KPIs & Metrics                   │  ║
    ║  │  (GitHub API)       (dim/fact)         (Dashboard Ready)                 │  ║
    ║  │                                                                           │  ║
    ║  └───────────────────────────────────────────────────────────────────────────┘  ║
    ║                              ▲                                                  ║
    ╚══════════════════════════════║══════════════════════════════════════════════════╝
                                   ║ Store Data
    ╔══════════════════════════════║══════════════════════════════════════════════════╗
    ║                    ⚙️ PROCESSAMENTO AUTOMATIZADO                               ║
    ╠══════════════════════════════════════════════════════════════════════════════════╣
    ║              🔄 GitHub Actions ──► 🐍 Python Scripts                            ║
    ║              (Daily ETL)           (Bronze→Silver→Gold)                          ║
    ║                    ▲                                                            ║
    ╚════════════════════║════════════════════════════════════════════════════════════╝
                         ║ GitHub API
    ╔════════════════════║════════════════════════════════════════════════════════════╗
    ║                 📊 FONTES DE DADOS                                              ║
    ╠══════════════════════════════════════════════════════════════════════════════════╣
    ║  📁 Repositórios     📋 Issues/PRs     💻 Commits/Events                        ║
    ║  da Organização                                                                  ║
    ║                                                                                  ║
    ║            LabTechUDF Organization (GitHub)                                      ║
    ╚══════════════════════════════════════════════════════════════════════════════════╝

    ═══════════════════════════════════════════════════════════════════════════════════════
                                    📋 FLUXO DE DADOS

    1️⃣ EXTRAÇÃO:     GitHub Actions coleta dados via API (daily cron)
    2️⃣ BRONZE:       Armazenamento raw JSON no repositório (append-only)
    3️⃣ SILVER:       Normalização em tabelas dim/fact com linhagem
    4️⃣ GOLD:         Agregação em KPIs prontos para dashboard
    5️⃣ CONSUMO:      React app acessa dados via GitHub API
    
    🔗 ACESSO DIRETO: Pesquisadores podem acessar Bronze/Silver para análises avançadas
    ⚖️ LICENÇA:      GPL3 - democratização e reutilização por outras fábricas acadêmicas
    
    """
    
    return topology

def generate_etl_flow():
    """Gera representação ASCII do fluxo ETL"""
    
    etl_flow = """
    ╔══════════════════════════════════════════════════════════════════════════════════╗
    ║                           📊 FLUXO ETL DETALHADO                                ║
    ╚══════════════════════════════════════════════════════════════════════════════════╝

    ⏰ TRIGGER (Daily: 0 6 * * *)
    │
    ├─► 🔄 GitHub Actions Workflow
        │
        ├─► 🐍 Python ETL Scripts
            │
            ┌─► 📡 FASE 1: EXTRAÇÃO (Bronze)
            │   ├─► Get Organization Data
            │   ├─► Get Repositories  
            │   ├─► Get Issues/PRs
            │   ├─► Get Commits/Events
            │   └─► Store Raw JSON ──► 🥉 Bronze Layer
            │
            ├─► ⚙️ FASE 2: TRANSFORMAÇÃO (Silver)
            │   ├─► Parse JSON payloads
            │   ├─► Normalize to dim/fact tables
            │   ├─► Add lineage columns
            │   └─► Store structured data ──► 🥈 Silver Layer
            │
            ├─► 📈 FASE 3: AGREGAÇÃO (Gold)
            │   ├─► Calculate KPIs
            │   ├─► Generate metrics
            │   ├─► Create visualizations data
            │   └─► Store dashboard-ready data ──► 🥇 Gold Layer
            │
            └─► ✅ CONSUMO
                ├─► Dashboard reads Gold via GitHub API
                └─► Researchers access Silver/Bronze directly

    ══════════════════════════════════════════════════════════════════════════════════════
                                   🛡️ ERROR HANDLING

    • 🚦 Rate Limiting: Intelligent backoff and retry
    • 💾 Caching: Avoid unnecessary API calls  
    • 📝 Logging: Comprehensive audit trail
    • 🔔 Notifications: GitHub Issues for failures
    """
    
    return etl_flow

def main():
    """Gera os diagramas ASCII e salva em arquivos"""
    
    # Gerar topologia
    topology = generate_ascii_topology()
    with open('topologia_ascii.txt', 'w', encoding='utf-8') as f:
        f.write(topology)
    
    # Gerar fluxo ETL
    etl_flow = generate_etl_flow()
    with open('etl_flow_ascii.txt', 'w', encoding='utf-8') as f:
        f.write(etl_flow)
    
    print("✅ Diagramas ASCII gerados:")
    print("   📁 topologia_ascii.txt")
    print("   📁 etl_flow_ascii.txt")
    
    # Exibir topologia no terminal
    print("\n" + "="*80)
    print("🏗️ TOPOLOGIA DA APLICAÇÃO")
    print("="*80)
    print(topology)

if __name__ == "__main__":
    main()
