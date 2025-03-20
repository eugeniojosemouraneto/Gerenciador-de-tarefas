# MVP - Sistema Gerenciador de Tarefas e Compromissos

## Objetivo

O objetivo do MVP é validar as principais funcionalidades do sistema de gerenciamento de tarefas e compromissos, fornecendo uma solução utilizável com os recursos essenciais.

---

## Funcionalidades Essenciais

### 1. Cadastro e Autenticação de Usuários
- Cadastro com e-mail e senha.
- Login e logout com tokens JWT.
- Recuperação de senha via e-mail.

### 2. Gerenciamento de Tarefas
- Criar, editar e excluir tarefas.
- Adicionar descrição e data de vencimento.
- Marcar tarefas como concluídas.
- Visualização de tarefas pendentes e concluídas.

### 3. Notificações Simples
- Notificação por e-mail para tarefas próximas do vencimento.

### 4. Calendário Básico
- Visualização das tarefas em um calendário semanal.

### 5. Dashboard Simplificado
- Visualização rápida das tarefas pendentes e concluídas.

---

## Requisitos Técnicos

### Backend
- **Django REST Framework** para construção da API.
- Banco de dados **PostgreSQL**.
- Autenticação com **JWT**.
- Envio de e-mails com **SMTP**.

### Frontend
- **React com TypeScript**.
- Estilização com **CSS Modules**.
- Gerenciamento de estado com **Context API**.

### Deploy
- Backend hospedado no **Heroku**.
- Frontend hospedado no **Vercel**.

---

## Exclusões do MVP
- Login social com OAuth2.
- Autenticação de duas etapas (2FA).
- Compartilhamento de tarefas.
- Integração com Google Calendar.
- Modo Pomodoro e funcionalidades avançadas.

---

## Conclusão

Este MVP fornecerá uma base funcional para que os usuários possam gerenciar suas tarefas e validar a proposta de valor do sistema. A partir dos feedbacks obtidos, futuras iterações poderão expandir as funcionalidades conforme necessário.

