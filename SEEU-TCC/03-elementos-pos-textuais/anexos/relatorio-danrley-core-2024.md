**Visão Geral do Projeto ao Longo do Ano de 2024**

Durante o ano de 2024, o projeto de reserva de salas (e demais funcionalidades relacionadas, como integração com sistemas de eventos e alocação de professores) progrediu de forma não-linear, atravessando diversas fases de desenvolvimento e iterações técnicas. Partimos de um contexto inicial onde a equipe estava sendo formada e ajustada, definindo a visão do produto, e avançamos para um estágio em que algumas partes-chave da solução foram implementadas e integradas.  

O projeto teve início com um kickoff esclarecendo o objetivo do LabTech, a natureza de ambiente de aprendizagem e a motivação para engajar os participantes no desenvolvimento do sistema. Não foram atribuídos papéis rígidos — a ideia era que todos pudessem aprender e contribuir, porém essa abordagem flexível acabou gerando níveis variáveis de comprometimento e envolvimento, dependendo do perfil individual de cada participante.

**Processo de Trabalho e Soft Skills**

O processo de desenvolvimento seguiu iterativamente, com reuniões presenciais e online, uso de ferramentas de colaboração (Figma, Discord, GitHub) e tentativas de adotar boas práticas ágeis. Por outro lado, notou-se que muitos membros precisavam de orientação intensa, especialmente nos aspectos técnicos (conhecimentos de front-end, back-end, testes, integração, conceitos de arquitetura e padrões de projeto).

As soft skills tiveram um papel crítico:  
- **Comunicação:** Houve problemas com falta de transparência e atraso em reportar dificuldades. Alguns membros demoraram a pedir ajuda ou não se comunicaram eficazmente, o que gerou lentidão no processo. Por outro lado, aqueles que buscaram contato e orientação com o mentor (Danrley) evoluíram mais rapidamente.  
- **Trabalho em Equipe:** A equipe se mostrou disposta a ajudar-se mutuamente quando instigada, mas muitos não tomavam a iniciativa de se comunicar ou colaborar espontaneamente. Entretanto, integrantes como Guilherme e Nicole souberam buscar ajuda e seguir instruções, resultando em boas entregas.  
- **Dedicação e Autonomia:** Houve participantes que honraram seus compromissos, pesquisaram e resolveram problemas por conta própria, demonstrando capacidade de autoaprendizagem. Outros, porém, necessitaram de reforço contínuo, indicações de materiais de estudo e tiveram dificuldade em se organizar e entregar resultados.

**Evolução Técnica da Solução**

No decorrer do ano, algumas metas técnicas foram alcançadas:  
- **Back-end:** Implementação do backend com Python (Flask), persistência em MongoDB (Atlas), testes unitários e introdução a padrões de arquitetura (3 camadas, factory, singleton). A autenticação foi desacoplada para um serviço independente, permitindo escalabilidade.  
- **Front-end:** Foi desenvolvido em React, integrando fluxos de login, formulários para eventos e a criação de rotas privadas. Houve aprendizado de React Hook Forms, uso de Context API e tentativa de integração com APIs REST. Apesar das dificuldades de debugging e de lidar com requisições, alguns membros avançaram.  
- **Integrações e Arquitetura Geral:** Foram discutidas topologias de solução, criação e consumo de endpoints REST, GraphQL, autenticação via token e api-key, assim como interação com outros projetos e serviços relacionados a eventos, reservas e alocação de recursos.

**Perfis Identificados na Equipe**

1. **Guilherme**:  
   - **Habilidades Técnicas:** Evoluiu bastante no backend, compreendendo camadas de arquitetura, testes, padrões e boas práticas.  
   - **Soft Skills:** Comunicação transparente, dedicação, segue recomendações e aprende rápido. Perfil de um desenvolvedor Júnior robusto, próximo de Pleno.  
   - **Comportamento:** Ajuda na criação de cultura da equipe (PRs, documentação), sabe pedir ajuda e também auxiliar outros.

2. **Nicole**:  
   - **Habilidades Técnicas:** Conhecimentos básicos de frontend evoluíram. Aprendeu React, Hooks, formulários e conseguiu resolver problemas sem muita dependência do mentor. Ainda precisa refinar a integração com APIs e conceitos mais avançados.  
   - **Soft Skills:** Honra compromissos, comunicação razoável, autodidata e sabe pesquisar antes de pedir ajuda. Tem interesse genuíno em aprender.  
   - **Comportamento:** Mantém organização, busca ajuda quando necessário, não cria bloqueios desnecessários.

3. **Gustavo Saud**:  
   - **Habilidades Técnicas:** Conhecimentos básicos e dificuldades com ambiente de desenvolvimento. Não se aprofundou significativamente.  
   - **Soft Skills:** Teve problemas pessoais (perda de um ente querido) que impactaram engajamento. Comunicação pouco transparente e pouca iniciativa na resolução de problemas.  
   - **Comportamento:** Mostrou interesse, porém não manteve consistência no longo prazo. Poderia exercer papel mais administrativo ou analítico, focando em modelagem de processos em BPMN, pela dificuldade técnica.

4. **Emerson** (mencionado no início do projeto):  
   - **Habilidades Técnicas:** Tinha conhecimento de Spring Boot e experiência moderada, mas não conseguiu entregar nem o fluxo inicial.  
   - **Soft Skills:** Falhou na comunicação, não foi transparente quanto à indisponibilidade. “Ghosting” da equipe.  
   - **Comportamento:** Abandono do projeto sem aviso efetivo, prejudicando o andamento no início.

5. **Lucas Skywalker e Josué Castro**:  
   - **Habilidades Técnicas:** Dificuldade com conceitos básicos de frontend (requisições HTTP, axios, async/await, fluxo lógico de if/else), pouco familiarizados com debugging.  
   - **Soft Skills:** Comunicação tardia, dificuldade em pedir ajuda em tempo hábil. Estão aprendendo, mas falta base de lógica de programação e prática em problemas de programação.  
   - **Comportamento:** Demoram a entregar tasks, fazem commits diretos na branch principal ignorando recomendações. Precisam desenvolver maior disciplina e organização no fluxo de trabalho.

6. **Gabriel**:  
   - **Habilidades Técnicas:** Tem certa facilidade com Python, aprendeu sobre desacoplamento de serviços, adicionou logs, tentou seguir boas práticas. Precisa melhorar conceitos avançados de OOP e SOLID.  
   - **Soft Skills:** Bom comprometimento, aceita feedback, busca entender melhor a arquitetura e processos.  
   - **Comportamento:** Demonstra esforço e disposição. Receptivo a novas tarefas e a aprender.

**Feedback Pessoal para Cada Membro**

- **Guilherme:**  
  Continue assim. Você demonstrou um crescimento notável em pouco tempo. Mantenha sua postura transparente e colaborativa. Aprimore ainda mais suas habilidades de arquitetura e testes automatizados, pois tem tudo para alcançar nível Pleno em breve.

- **Nicole:**  
  Você mostrou determinação e capacidade de aprendizado. Continue estudando mais sobre integração com APIs, testes automatizados e boas práticas de React. Sua proatividade em buscar soluções sozinha é um ponto forte.

- **Gustavo Saud:**  
  Entendemos as dificuldades pessoais que enfrentou. Avalie seu interesse real no desenvolvimento de software ou considere um papel de análise de negócios/BPMN se desenvolvimento técnico não for sua principal vocação. Caso queira continuar no desenvolvimento, será fundamental melhorar comunicação, pedir ajuda quando travar e estabelecer um ritmo consistente de estudo.

- **Emerson:**  
  A falta de comunicação foi o principal ponto negativo. Em projetos futuros, seja transparente sobre sua disponibilidade. Não há problema em se afastar, desde que todos saibam e possam se replanejar.

- **Lucas Skywalker e Josué Castro:**  
  Vocês precisam fortalecer suas bases. Estudem lógica de programação, requisições HTTP, verbos, e pratiquem a construção de pequenos projetos. Aprendam a usar o Git de forma correta, seguindo o fluxo de PRs e evitando commits diretos na branch principal. Melhorar a comunicação, pedir ajuda logo que necessário e respeitar práticas de engenharia de software será essencial para o crescimento de vocês.

- **Gabriel:**  
  Você está indo bem. Continue aprendendo conceitos de OOP, SOLID, testes, debug e logging. Sua postura receptiva e interesse em aprender vão lhe permitir evoluir continuamente. Busque também ajudar outros membros, consolidando seu aprendizado por meio do ensino.

**Conclusão**

O ano de 2024 foi um período de aprendizado intenso, com progressos significativos no backend, na arquitetura da solução e na integração entre sistemas. Porém, houve desafios no front-end e na comunicação, além da necessidade de amadurecimento da equipe em termos de disciplina, organização e domínio técnico. As recomendações e feedbacks apontam caminhos claros para crescimento de cada um, permitindo que a equipe, como um todo, atinja um nível mais profissional e produtivo no próximo ciclo de desenvolvimento.


## Diário de bordo cru
Danrley Pereira — 4/13/2024 1:31 PM
kickoff 11h 13/04/2024
Kerlla começou explicando o que é o LabTech e qual é o objetivo. Tentou inspirar os participantes para motivá-los ao engajamento, falando sobre equity se o produto dê certo.
Ela e o Danrley deixaram claro que o ambiente é um ambiente de aprendizagem controlado, que não vamos engessar o processo nomeando papeis. O objetivo é claro, solucionar o problema de reserva de sala.
Emerson tem boa experiência com Spring Boot, certa experiência com Flutter e React, aprendendo Angular.
Nicole trabalha com help desk. html css básico. Preciso verificar lógica de programação
Gustavo atualmente está somente na faculdade. html css básico. Preciso verificar lógica de programação
Guilherme já está sendo mentorado pelo Danrley há uma ou duas semanas, desde a Campus Party Brasília 2024. Com auxilio conseguir criar endpoints para retornar as salas, buildings, schemas/tipos via restapi conectando no MongoDB.

Depois de uma explicação rápida do que temos, foram adicionados ao Figma e ao Discord. 
Reunião marcada para dia 16/04/2024 as 18:30 no laboratório de hardware da UDF
Danrley Pereira — 4/17/2024 2:00 AM
16/04/2024 18:30 Reunião com equipe, gustavo, nicole, emerson e guilherme
Chegaram na hora, eu me atrasei 15 minutos.
Fizemos o começo de um BPMN no quadro para entedermos o processo. 
Vamos implementar o caminho feliz por hora. Emerson ficou de passar o desenho no quadro pro bpmn.io
Nicole + Gustavo ficaram de mexer no Figma design e começar a mexer no React.
Guilherme vai continuar com a parte do backend.
Danrley Pereira — 5/1/2024 1:17 PM
20/04 a 30/04 Nicole rodou a interface e começou a desenvolver algumas telas, entrou em contato comigo algumas vezes. 
No mesmo período o Gustavo Saud perdeu um ente querido e não pode participar das atividades ainda.
Conversei com o Emerson e ele parece ter muitos compromissos e não sabe que não vai conseguir auxiliar o projeto, ele ainda não veio falar comigo para pedir a saída formal, vou esperar para ver quanto tempo ele leva para comunicar sua indisponibilidade para continuar participando do projeto.
3 pessoas pediram para entrar no projeto via email, FrancianeFerreira98@gmail.com e dev.ocgustavo@gmail.com, retornei pedindo que entrassem no canal do discord e tentando marca uma reunião com eles no laboratório de hardware, infelizmente não tive retorno.
Outra pessoa que entrou em contato foi a Luiza (luisa.machado.botelho.pereira@gmail.com) que colocou entraves para o encontro presencial, porém aceitou. No dia do encontro disse que não poderia ir pois tinha aula o que não condiz com o horário do encontro (18:30 as 19h). Parece não quere se encontrar presencial.
23/04/2024 18:30 reunião com duas estudantes de CC, Luiza e Victoria. Elas irão participar do projeto de transparência/Auditoria de gastos. Entradas e Saídas de qualquer orgão, osc, empresa, mandato. Pedi para elas fazerem um tutorial em Angular e preparar o ambiente.
01/05/2024 
Gustavo Saud começou a preparar o ambiente e rodar o frontend, Nicole passou algumas telas para ele.
Danrley Pereira — 9/2/2024 7:16 PM
No fim do mês de Abril o Emerson demonstrou não saber organizar seu tempo e que estava com muitos compromissos e não conseguiria agregar valor ao projeto. Não conseguindo entregar nem o fluxo que colocamos no quadro. Infelizmente ele não conseguiu ser transparente na comunicação e ser sincero sobre sua situação e que não conseguiria de fato honrar seu compromisso. O termo técnico é ghost.
Danrley Pereira — 9/2/2024 7:29 PM
Durante o mês de Maio, Guilherme foi presencialmente na sede da DW Corp (empresa que Danrley trabalha) para juntos conseguirem avançar no desenvolvimento da API. Danrley mostrou pra ele como usar o Poetry, como organizar o projeto em camadas, usar singleton e factory patterns, além de conversarem sobre a three tiers architecture. Todos esses conceitos foram introduzido enquanto Guilherme e Danrley desenvolviam as Estórias de Usuário do backend. Implementaram o registro de eventos em um banco MongoDB em nuvem (Atlas), gerenciamento de salas e reservas de sala. Guilhereme dedicou uma boa porção de tempo no desenvolvimento das atividades, ouvia o mentor (Danrley) e seguia suas instruções, esse comportamento favoreceu o seu aprendizado e evolução no entendimento de desenvolvimento de produtos de software.
Além disso, como o auxilio do do mentor, Guilherme adicionou cobertura no código que escreveu (testes unitários). 
Durante o mês de maio Danrley subiu um cloud function no Google Drive para poder enviar emails e adicionou à API o respectivo endpoint para enviar o email com o token de autenticação.
Entre 26/06/2024 e 10/07/2024
Danrley entrou em contato e buscou a participação do Gustavo. Após ele demonstrar interesse, acompanhou o progresso do mentorando, oferecendo suporte contínuo e sugerindo uma call para resolver problemas técnicos. O mentorando, apesar de tentar resolver os problemas por conta própria, se sentiu desmotivado por não conseguir avançar. Danrley ressaltou a importância da tentativa e ofereceu ajuda, incentivando uma comunicação mais transparente para evitar atrasos e desmotivação.
02/09/2024
Nicole, Guilherme e Danrley conversaram sobre o que conseguiram implementar. Nicole e Guilherme foram contratos nesse meio tempo, por isso o intervalo entre as atividades, para que eles pudessem se familiarizar com o trabalho e pudessem encontrar tempo para realização das atividades da fábrica de software.
Nicole conseguiu se familiarizar com o React e conseguiu implementar o fluxo de login com a verificações, e começou a desenvolver os formulários para pegar as informações dos eventos. Ela não implementou a integração com a Rest API que foi criada no Python. Se comprometeu em terminar os formulários de pegar dados de evento. Danrley mostrou pra ela a biblioteca React Hook Forms e falou sobre o Context hooks do React.
Guilhereme rodou a projeto na máquina e chegamos na conclusão de que está pronto a api, faltando somente alguns testes.
Nicole informou que o Gustavo Saud não procurou interação com ela, mesmo que ela tenha se disponibilizado a ajudar.
Danrley Pereira — 9/2/2024 7:42 PM
Até o momento nota-se que:
Guilherme honrou com seu compromisso e conseguiu entregar o backend, soube se comunicar e desenvolver o produto sem maiores problemas, Guilherme tem um perfil Júnior robusto e em pouco tempo se tornará um desenvolvedor Pleno.
Gustavo Saud teve dificuldades com configuração de ambiente e nem chegou a se aprofundar em desenvolvimento de sofftware. Demonstrou interesse e tentou na medida do possível entregar valor. Mesmo que tenha buscado agregar valor, e que Danrley e Nicole estavam dispostos a auxiliá-lo na resolução dos problemas, não conseguiu manter uma boa comunicação com a equipe e demonstrar compromisso profissional.  Foi identificado necessidade de motivação externa e por algumas questões da vida, como a perda de um familiar por exemplo, acabou não conseguindo agregar valor ao projeto.
Nicole demonstra interesse, porém tem menos experiência no desenvolvimento de produtos. Honra com seu compromisso e busca aprender. Consegue se auto gerenciar, pesquisar e resolver seus problemas sozinha, exigindo do mentor (Danrley) mais direcionamento (bibliotecas, conceitos mais abstratos e questões de regra de negócio)  e menos detalhes de implementação (como resolver bugs e usar o javascript, html e css).
Danrley Pereira — 9/21/2024 2:31 PM
12/09/2024
Gustavo Saud entregou o processo em bpmn que pedi para ele na semana passada. Ele demonstra interesse em aprender e continuar participando, estou pensando em integrá-lo em papel mais de analista de negócio.
Guilherme e Danrley se juntaram para poder integrar a autenticação, criada no backend (flask api), com o frontend (react app). Autenticação tá funcionando e a rota enviada por email está direcionando para o webapp e a verificação se o token é válido está funcionando.
21/09/2024
Danrley conversou o Lelton, gerente do time de Eventos, e decidiu que as ODSs serão disponilizadas através de um endpoint do backend core (flask api), a autenticação de funcionários da udf será usada centralmente também. Lelton ficou de ver analisar o uso do sympla (api e webapp) para não precisarmos construir uma solução completa de eventos.
Rodamos o angular-app e o spring-boot-api e não conseguimos autenticar usando as rotas do spring. O angular parece não estar integrado corretamente com a api.
a decisão do fim do dia foi que o Grupo de Eventos irá consumir os eventos do serviço de Reserva de sala e irão fazer o comportamento de inscrição no evento.
Depois eles irão fazer a autenticação dos organizadores usando a autenticação por email e irão mostrar os eventos do organizador somente.
 
Danrley Pereira — 9/21/2024 10:36 PM
21/09/2024
reunião do grupo do CORE/Reservas:
SKYWALKER - Lucas - RGM: 29418101 - BackEnd (Python e C)
Josué - RGM: 29786932 - BackEnd (C e Python)
Gabriel - RGM: 29615267 - Python, PSQL. Data Engineering

atividade da primeira semana:
Rodar projeto backend
Rodar projeto frontend
 
21/09/2024
Danrley conversou com Polyana (líder do Grupo de Alocação) e ficou de processar os dados da planilha e disponibilizar um servidor RestFul e um servidor graphql com client embutido. 
Danrley concluiu a atividade no mesmo dia. 
Danrley Pereira — 9/26/2024 3:51 PM
25/09/2024
Gabriel, Guilherme e Danrley se encontraram no LabTech 4R para criar as decorators de autenticação da api. Vamos fazer a autenticação por token para o usuário e por api-key para os serviços.
Danrley implementou e mostrou como faz as decorators por função/método, Guilherme entendeu um pouco melhor por dominar a solução e ter mais experiência com Python e o Gabriel teve um pouquinho mais de dificuldade, mas no fim das contas conseguir entender mais ou menos.
Gabriel conseguiu associar os professores ao curso (adicionar o código de curso na coleção de professores) no projeto de processar a planilha e dispobilizar via REST e GraphQL.
Gabriel demonstrou comprometimento indo presencial e resolvendo a Issue de associar professores ao curso.
Guilherme, como sempre, faz um bom trabalho; demonstra comprometimento e entendimento do que está sendo feito. Agora está melhorando o seu entendimento do fluxo de trabalho (criar os PRs e documentá-los) e me ajudando a criar uma cultura para nossa equipe
Danrley direcionou em como fazer a decorator por classe (grupo de rotas) e deixou para o Guilherme terminar a implementação. 
Danrley Pereira — 10/3/2024 7:31 PM
26/09/2024
Danrley definiu a topologia / arquitetura da solução completa (eventos, reservas, alocação de professores), incluindo autenticação, dados compartilhados através de uma api.
Danrley Pereira — 10/5/2024 1:45 AM
05/10/2024
Lucas Skywalker, Josué, Gabriel, Guilherme se reunirão para configurar ambiente.
Gabriel começou a extrair a autenticação da nossa API para ser um serviço separado.
Concordaram em fazer encontros presenciais. Josué atualizou nosso bpmn para adicionar a atividade de postar no tópico do Kafka o evento.
Danrley explicou a arquitetura/topologia da solução como um todo e deu um overview do diagrama bpm.
Danrley Pereira — 10/12/2024 11:54 AM
12/10/2024
Lucas Skywalker e Josué Castro se reuniram com o Danrley presencialmente.
Rodaram a solução de reservas, frontend React (interfaces-usuario) e o backend (python-services).
Encontraram um problema com a requisição de verificação do token, oq conseguiram resolver.
Foram levantados um bugfix para colocar a criação da hash na camada certa (está na SLL, mas deveria estar na BLL) e uma task para fazer a autenticação das rotas do frontend que deveriam ser protegidas. 
Danrley Pereira — 10/20/2024 12:30 PM
semana do dia 14 ao dia 18/10/2024
Lucas Skywalker e Josué Castro foram indicados para resolver a primeira atividade/issue deles. Eles irão resolver juntos, como Danrley recomendou. (Foram levantados um bugfix para colocar a criação da hash na camada certa (está na SLL, mas deveria estar na BLL) e uma task para fazer a autenticação das rotas do frontend que deveriam ser protegidas.)
Lucas não conseguiu rodar o frontend, mas o Danrley conseguiu auxiliá-lo a roda o backend. Ele ficou de configurar o ambiente dele.
Josué pediu para se reunir com o Danrley.
Danrley Pereira — 11/11/2024 1:30 AM
última semana de outubro e primeira semana de Novembro:
Frontend
Josué Castro e Lucas Skywalker avançaram na criação das rotas privadas, fizeram um componente de wrap para as rotas da biblioteca "react-router" e conseguiram direcionar o usuário para a tela de login; tiveram um erro com a autenticação feita pela api que estava rodando local e pediram ajuda pro Danrley.
O erro estava na requisição feita pelo cliente http no frontend que não estava passando os parâmetros (query params) corretamente. Lucas e Josué não conseguiram debugar a aplicação e entender o problema, eles não têm conhecimentos de verbos http, de como funciona uma requisição e resposta, Danrley mostrou como debugar a aplicação e como identificar onde está os problemas. Os conceitos necessários para conseguir resolver o problema encontrado, além de saber passar os parâmetros corretamente para o método get do "axios", era os conceitos de promises, async e await e falsy/truthy no javascript.
Danrley fez o commit resolvendo a requisição para a api, os desbloqueando (Lucas e Josué). 
A recomendação é que ambos estudem conceitos redes como requisição/resposta, além disso foi identificado falta de conforto com a construção de algoritmos, como não sabendo a syntax de if elses e construíndo escopos com chaves, organização do código etc, eles parecem possuir um perfil de iniciante. A recomendação é que eles resolvam desafios de programação para iniciantes para melhorarem suas habilidades de resolver problemas e escrever algoritmos, recomendo resolver os exercícios do beecrowd, antigo URI, com linguagens de programação de mais baixo nível, como C, Java ou C#. 
Danrley Pereira — 11/11/2024 1:42 AM
última semana de outubro e primeira semana de Novembro:
Gabriel
Conseguiu desacoplar a autenticação das reservas em outro serviço (api), ou seja, outros serviços podem usar a mesma lógica de autenticação do reservas. Precisou de ajuda, mas conseguiu fazer as coisas de maneira relativamente rápida. Pedi para ele adicionar logs na aplicação e ele não reclamou e tentou fazer, começou colocando logs em vários lugares, mas depois que pedi para criar uma classe estática responsável por isso, Gabriel seguiu em frente com a ajuda do Guilherme e fizeram a entrega. Danrley pediu para o Guilherme fazer a revisão do PR. Eles tiveram certa dificuldade de fazer a classe de maneira mais genérica, no entanto, sem grandes alarmes.
Danrley recomendou ao Gabriel fazer exercícios de programação do beecrowd. Gabriel parece se sentir confortável programando em python, mas precisa aprender conceitos como SOLID e orientação a objetos como um todo. Conceitos como herança, poliformismo, coesão, acoplamento etc.
Danrley Pereira — 11/11/2024 1:58 AM
02 e 03 de Novembro:
Lucas e Josué conseguiram terminar a privatização das rotas. Ou seja, agora o usuário só pode acessar as rotas (exceto login e acesso negado) se tiver devidamente autenticado. 
Ele criaram a página de acesso negado e colocaram um loading em formato texto.
Danrley pediu para colocarem um loading animado da internet e identificou um falso positivo para a autenticação, onde eles só verificaram se tinha um token presente no localStorage, não fazendo a requisição para a api com foco de validar o token.
No geral eles demoraram demasiadamente para entregar a task, para comunicar os passos que estavam tomando e para pedir ajuda.
Todos os integrantes do grupo têm dificuldade com uso do git cli e não sabem de gitflow. Danrley recomendou usarem o conventional commits e também seguir o fluxo de criar um PR no github e colocá-lo como reviewer, fazendo com que o processo possa ser um pouco mais assíncrono e remoto. O foco é poderem trabalhar de maneira mais independente. As requisições de mudanças são feitas pelo próprio github, no pull request. 
Outra estratégia adotada por Danrley foi não terem nenhum trello ou jira, usando um canal no discord chamado labtech-backlog, onde para issue criada no github é criado uma thread nesse canal para tratar de todas as comunicações relativas.
Dessa maneira centralizamos tudo no discord e github, facilitando a comunicação e a rastreabilidade do que foi e está sendo feito.
Danrley Pereira — 12/9/2024 3:00 PM
fim de novembro e primeira semana de Dezembro:
Lucas salvou os dados do formulário em um contexto do React e começou a pegar os dados da api (salas, ods, tipos de evento etc). Fez um PR e fez um commit direto na branch principal. Commitar na branch principal é uma alerta que precisa estar no relatório, depois de vários warnings, de mostrar como faz diversas vezes, ainda assim o Lucas e o Josué fizeram commits direto na branch principal. Isso pode demonstrar a vontade de só finalizar as obrigações com o LabTech, falta de atenção e/ou falta de vontade.
Josué como mencionado fez o commit da mudança de lógica da geração do hash para a camada de negócio, no entanto fez o merge sem esperar o Danrley. Josué não se comunicou bem durante o processo, sendo que nas últimas semanas teve que entregar algumas tasks para conseguir o certificado de estágio, mas não se comunicou efetivamente, nem pelo discord nem pelo grupo do whatsapp. Josué deixou um comentário na issue do github, mas não avisou ninguém da equipe sobre isso. Ele precisa melhorar a comunicação com urgência.
Gabriel fez a revisão de um PR que eu abri em relação a autenticação que estava com o endpoint no .env de maneira equivocada, não funcionando quando o python services tentava requisitar o serviço de autenticação. 
Gabriel é esforçado e se dispõe a aprender, ele vai precisar de mais desafios e treinamento na parte de testar e debuggar aplicações, criar e testar funcionalidade do frontend. 