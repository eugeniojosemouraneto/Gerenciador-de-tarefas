# Sistema Gerenciador de Tarefas e Compromissos

Um sistema completo para gerenciamento de tarefas e compromissos, desenvolvido com Django REST Framework (API) e React com TypeScript (frontend). Este projeto foi criado para servir como portfólio, demonstrando habilidades de nível pleno.

---

## Funcionalidades Essenciais

### 1. Cadastro e Autenticação de Usuários
- Cadastro com e-mail e senha.
- Autenticação de duas etapas (2FA) via aplicativos como Google Authenticator ou Authy.
- Tokens JWT com tempo de inatividade configurável (ex: 30 minutos) para deslogar automaticamente.
- Login com redes sociais **apenas via Google, Microsoft e Apple** (usando OAuth2).
- Recuperação de senha via e-mail com token expirável.

### 2. Gerenciamento de Tarefas
- Criar, editar e excluir tarefas.
- Adicionar descrição, data de vencimento, prioridade (baixa, média, alta) e tags.
- Marcar tarefas como concluídas.
- **Notificações de tarefas:**
  - Alertas para tarefas próximas do vencimento.
  - Lembretes personalizados (ex: 1 hora antes, 1 dia antes).
  - Envio de notificações por e-mail, Telegram ou WhatsApp (integrado com APIs de terceiros).
- Cadastro de lembretes para tarefas com data e hora específicas.
- Visualização de tarefas atrasadas ou pendentes.

### 3. Calendário e Compromissos
- Visualização de tarefas e compromissos em um calendário (semanal, mensal).
- Adicionar eventos recorrentes (ex: aulas, reuniões).
- **Integração com Google Calendar:**
  - Sincronização automática de tarefas e compromissos.
  - Opção para o usuário permitir ou negar a vinculação.
- Notificações de lembrete por e-mail ou push notification.

### 4. Colaboração
- Compartilhar tarefas ou listas com outros usuários.
- **Controle de permissões:**
  - O criador da tarefa tem permissão máxima (editar, excluir, compartilhar).
  - Usuários convidados podem receber permissões personalizadas (ex: apenas visualizar, editar parcialmente).
- Comentários em tarefas compartilhadas para discussão.
- Notificações para usuários convidados sobre atualizações na tarefa.

---

## Funcionalidades Avançadas

### 1. Dashboard Personalizado
- Gráficos de produtividade (tarefas concluídas ao longo do tempo).
- Visão geral das tarefas pendentes, concluídas e atrasadas.
- Métricas de desempenho (ex: tempo médio para concluir tarefas).

### 2. Integração com Ferramentas Externas
- Integração com Google Calendar, Outlook, etc.
- Sincronização de tarefas entre dispositivos.
- Importar/exportar tarefas em formato CSV ou JSON.

### 3. Modo Foco (Pomodoro)
- Temporizador Pomodoro integrado ao sistema.
- Bloqueio de distrações durante o modo foco.
- Relatório de tempo gasto em tarefas.

### 4. Planejamento de Metas
- Definir metas de longo prazo (ex: passar no concurso X em 6 meses).
- Dividir metas em tarefas menores.
- Acompanhamento de progresso.

### 5. Notas e Anotações
- Criar notas rápidas vinculadas a tarefas ou independentes.
- Formatação básica de texto (negrito, itálico, listas).
- Anexar arquivos ou links às notas.

### 6. Temas e Personalização
- Temas claros e escuros.
- Personalização de cores e layout.

### 7. Acessibilidade
- Suporte a leitores de tela.
- Teclas de atalho para navegação rápida.

---

## Recursos Técnicos

### 1. API RESTful
- Endpoints bem documentados (usando Swagger ou Redoc).
- Paginação e filtros avançados nas listagens.
- Validação de dados robusta no backend.

### 2. Frontend Moderno
- Componentes reutilizáveis no React.
- Gerenciamento de estado com Redux ou Context API.
- Uso de hooks e boas práticas do React.
- Design responsivo (funciona bem em mobile e desktop).

### 3. Testes
- Testes unitários e de integração no backend (Django pytest).
- Testes de componentes no frontend (React Testing Library ou Jest).
- Testes E2E com Cypress ou Selenium.

### 4. Deploy e CI/CD
- Deploy da API em plataformas como Heroku, AWS ou DigitalOcean.
- Deploy do frontend em Vercel ou Netlify.
- Pipeline de CI/CD com GitHub Actions ou GitLab CI.

### 5. Segurança
- Proteção contra SQL Injection e XSS.
- Rate limiting para evitar abuso da API.
- Criptografia de senhas e dados sensíveis.

---

## Diferenciais para o Portfólio

### 1. Documentação Completa
- Documentação da API (Swagger/Redoc).
- README detalhado no GitHub com instruções de instalação e uso.
- Explicação das decisões técnicas no código (comentários ou um arquivo `DECISIONS.md`).

### 2. Uso de Boas Práticas
- Clean Code no backend e frontend.
- Padrões de commit semânticos.
- Versionamento da API (ex: `/api/v1/`).

### 3. Demonstração de Habilidades Pleno
- Escalabilidade: uso de caching (Redis) e otimização de queries.
- Internacionalização (i18n) para suportar múltiplos idiomas.
- Microserviços (opcional): separar funcionalidades como autenticação e notificações em serviços independentes.

### 4. Projeto Publicado
- Link para o projeto online (frontend e backend).
- Vídeo demonstrativo no YouTube ou LinkedIn mostrando o sistema em funcionamento.

---

## Ideias Extras

### 1. Gamificação
- Sistema de recompensas por tarefas concluídas (ex: pontos, badges).
- Ranking de produtividade entre usuários.

### 2. Inteligência Artificial
- Sugestões automáticas de tarefas baseadas em hábitos.
- Análise de sentimentos em notas ou descrições de tarefas.

### 3. Mobile-First
- Desenvolver um PWA (Progressive Web App) para uso offline.
- Aplicativo mobile nativo (usando React Native).

### 4. Integração com IA Generativa
- Sugestões de tarefas ou planejamento usando GPT (ex: OpenAI API).
- Geração automática de resumos ou anotações.

---

## Roadmap Sugerido

### 1. Fase 1: MVP (Produto Mínimo Viável)
- Cadastro e autenticação de usuários (com 2FA e login social).
- CRUD de tarefas com notificações e lembretes.
- Calendário básico com integração ao Google Calendar.
- Frontend simples com React.

### 2. Fase 2: Funcionalidades Intermediárias
- Colaboração com controle de permissões.
- Dashboard e métricas.
- Modo foco (Pomodoro).

### 3. Fase 3: Diferenciais e Polimento
- Gamificação ou IA.
- Testes e documentação.
- Deploy e publicação.

---

## Como Contribuir
1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adicionando nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

---

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Feito com ❤️ por [Seu Nome](https://github.com/eugeniojosemouraneto).