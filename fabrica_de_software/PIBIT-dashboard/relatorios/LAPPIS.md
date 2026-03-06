# Relatório de Reunião – Conversa com representante do LAPPIS

**Participantes:** Danrley Pereira (IBICT) e Dra. Carla (Coordenadora LAPPIS)
**Data:** 22/08/2025
**Local:** FGA – UnB
**Tema central:** Discussão sobre fábricas de software acadêmicas, métricas de interação e experiências do LAPPIS

---

## 1. Contexto Institucional

* O LAPPIS está atualmente envolvido em **sistemas estruturantes para controle orçamentário no poder executivo**.
* Um dos maiores desafios enfrentados é a **fragmentação de sistemas que não se comunicam entre si**, dificultando a gestão integrada.

---

## 2. Reflexões sobre o Modelo de “Fábrica de Software”

* Houve uma **crítica ao conceito de fábrica de software**, considerando que ele não se mostra tão eficiente para **construção de software** em ambientes acadêmicos ou inovadores.
* A visão defendida é que o modelo precisa ser **repensado e adaptado** para contemplar práticas mais alinhadas à inovação e ao aprendizado dos alunos.

---

## 3. Arquitetura e Tratamento de Dados

* Foi **sugerido o uso da Arquitetura Medalhão (Medallion Architecture)** para organização e tratamento de dados.
* Estrutura proposta:

  * **Bronze (Raw):** extração de dados de múltiplas fontes (GitHub, GitLab, Notion).
  * **Silver:** transformação e homogeneização em modelos definidos, deixando dados organizados e prontos para análises.
  * **Gold:** camada final de conhecimento, disponibilizando insights consolidados para a comunidade.
* Conclusão: **atualização semanal dos dados é suficiente** para o dashboard proposto.

---

## 4. Métricas Quantitativas e Qualitativas

* Foi ressaltada a **necessidade de interpretar dados quantitativos por meio de análises qualitativas**.
* Apenas os números não revelam o contexto; a combinação dos dois métodos gera inferências mais robustas sobre os projetos e interações.

---

## 5. Formação Acadêmica e Experiência dos Alunos

* Desafios: disciplinas regulares têm em média **4 meses de duração**, dificultando a vivência em projetos complexos.
* Solução do LAPPIS:

  * Os alunos geralmente entram a partir do **4º semestre**.
  * Permanência média: **2 anos**.
  * Esse período permite **imersão mais próxima da realidade de mercado** e construção de experiências consistentes.

---

## 6. Métricas de Interações em Repositórios

* Foi destacado o **potencial de análise via gráficos de rede** entre alunos e repositórios:

  * **Aluno integrador:** interage com muitos membros/repositórios, possivelmente explorando várias áreas (dados, frontend, APIs, plataforma, etc.).
  * **Aluno especialista:** concentra interações em áreas específicas (ex.: plataforma → SRE/DevOps).
* O dashboard de métricas pode **mapear perfis de alunos**, ajudando a entender trajetórias e papéis dentro dos projetos.

---

## 7. Conclusões e Próximos Passos

* Há alinhamento de que um **dashboard com métricas de interação entre alunos é útil e viável**.
* O modelo de dados em camadas (Bronze → Silver → Gold) será a base do ETL.
* A análise deverá considerar não apenas métricas numéricas, mas também **contexto qualitativo** para gerar conhecimento válido.

---

👉 Esse relatório pode ser usado como **documento de registro** da reunião ou como **ementa de acompanhamento**, para alinhar próximos passos.

Quer que eu também formate essa versão em **ABNT NBR 10719 (Relatório Técnico)** — já que você está no contexto acadêmico e isso pode ser útil para documentação oficial?
