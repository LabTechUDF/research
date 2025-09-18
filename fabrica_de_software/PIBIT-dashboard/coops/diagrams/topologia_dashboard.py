#!/usr/bin/env python3
"""
Topologia da Aplicação - Dashboard para Fábricas de Software Acadêmicas
Arquitetura GitHub Actions + Firebase + React/D3.js

Este diagrama ilustra a arquitetura serverless proposta onde:
- GitHub Actions realiza ETL dos dados da organização
- Dados são armazenados no próprio repositório (Bronze/Silver/Gold)
- Frontend React/D3 consume dados via GitHub API
- Firebase Hosting serve a aplicação estática
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.github.actions import Actions
from diagrams.github.objects import Repository, Issue, PullRequest
from diagrams.programming.language import Python, JavaScript
from diagrams.programming.framework import React
from diagrams.firebase.hosting import Hosting
from diagrams.onprem.client import Client
from diagrams.generic.storage import Storage
from diagrams.generic.database import Database
from diagrams.generic.compute import Rack
from diagrams.generic.blank import Blank

def create_topology_diagram():
    """Cria diagrama de topologia da aplicação"""
    
    with Diagram("Topologia Dashboard - Fábrica Software Acadêmica", 
                 filename="topologia-dashboard", 
                 show=False,
                 direction="TB"):
        
        # Usuários finais
        with Cluster("👥 Stakeholders"):
            docentes = Client("Docentes/\nGestores")
            estudantes = Client("Estudantes")
            pesquisadores = Client("Pesquisadores")
            users = [docentes, estudantes, pesquisadores]
        
        # Frontend e Hosting
        with Cluster("🌐 Frontend & Hosting"):
            firebase = Hosting("Firebase\nHosting")
            react_app = React("React +\nD3.js")
            firebase >> react_app
        
        # Repositório central e dados
        with Cluster("📦 Repositório Central"):
            main_repo = Repository("Dashboard\nRepository")
            
            with Cluster("🗂️ Camadas de Dados"):
                bronze = Storage("Bronze\n(Raw JSON)")
                silver = Database("Silver\n(Normalized)")
                gold = Storage("Gold\n(KPIs)")
                
                bronze >> Edge(label="ETL Transform") >> silver
                silver >> Edge(label="Aggregate") >> gold
        
        # GitHub Actions (ETL Engine)
        with Cluster("⚙️ Processamento Automatizado"):
            github_actions = Actions("GitHub Actions\n(Daily ETL)")
            python_scripts = Python("Python Scripts\n(Bronze→Silver→Gold)")
            
            github_actions >> python_scripts
        
        # Fontes de dados
        with Cluster("📊 Fontes de Dados"):
            org_repos = Repository("Repositórios\nda Organização")
            issues_source = Issue("Issues/PRs")
            commits_source = PullRequest("Commits/\nEvents")
            
            data_sources = [org_repos, issues_source, commits_source]
        
        # Fluxo principal de dados
        for source in data_sources:
            source >> Edge(label="GitHub API") >> github_actions
        
        python_scripts >> Edge(label="Store") >> bronze
        python_scripts >> Edge(label="Process") >> silver  
        python_scripts >> Edge(label="Generate") >> gold
        
        # Acesso aos dados
        react_app >> Edge(label="GitHub API\n(Read Bronze/Silver/Gold)", style="dashed") >> main_repo
        
        # Interação dos usuários
        for user in users:
            user >> Edge(label="HTTPS") >> firebase
        
        # Acesso direto para pesquisadores avançados
        pesquisadores >> Edge(label="API Access\n(Bronze/Silver)", 
                            style="dotted", 
                            color="orange") >> main_repo

if __name__ == "__main__":
    create_topology_diagram()
    print("Diagrama de topologia criado: topologia-dashboard.png")
