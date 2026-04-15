# Accounts Auth System

Minissistema de autenticação desenvolvido com Django para estudo e prática de boas práticas de cadastro, login, ativação de conta por e-mail e redefinição de senha.

## Objetivo

Este projeto foi criado para demonstrar conhecimento prático em:

- Customização do modelo de usuário no Django
- Autenticação com e-mail como identificador principal
- Envio de e-mail para confirmação de conta
- Redefinição de senha por link seguro
- Bloqueio de ações para usuários não ativados
- Invalidação de links após uso e expiração por tempo
- Organização do projeto com variáveis de ambiente
- Containerização com Docker
- Uso de PostgreSQL como banco de dados

---

## Funcionalidades

- Cadastro de usuário com e-mail único
- Validação de senha com validadores do Django
- Confirmação de conta por e-mail
- Link de ativação com expiração e invalidação após uso
- Login com e-mail e senha
- Logout
- Redefinição de senha por e-mail
- Link de redefinição expirado e invalidado após uso
- Dashboard protegido após autenticação
- Bloqueio de reset de senha para usuários inativos

---

## Tecnologias Utilizadas

- Python
- Django
- PostgreSQL
- Docker
- Docker Compose
- django-environ
- HTML

---

## Estrutura do Projeto

```text
accounts/
├── accounts/
├── core/
├── templates/
├── Dockerfile
├── docker-compose.yml
├── .env
├── .env.example
├── .gitignore
├── manage.py
└── requirements.txt
```

---

## Como Executar com Docker (Recomendado)

### 1. Clone o repositório

```bash
git clone https://github.com/M2004GV/django-auth-system.git
cd django-auth-system
```

### 2. Configure o `.env`

Crie o arquivo `.env` baseado no `.env.example`:

```env
DEBUG=True
SECRET_KEY=change-me
ALLOWED_HOSTS=127.0.0.1,localhost

DATABASE_URL=postgres://accounts_user:accounts_pass@db:5432/accounts_db

POSTGRES_DB=accounts_db
POSTGRES_USER=accounts_user
POSTGRES_PASSWORD=accounts_pass

EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
DEFAULT_FROM_EMAIL=webmaster@localhost

TIME_ZONE=America/Fortaleza
LANGUAGE_CODE=pt-br
```

### 3. Suba os containers

```bash
docker compose up --build
```

### 4. Acesse a aplicação

```text
http://localhost:8000
```

### O que acontece automaticamente:
* O PostgreSQL é iniciado.
* O Django espera o banco de dados ficar pronto.
* As migrations são aplicadas automaticamente.
* O servidor é iniciado.

---

## Testando E-mails (Modo Desenvolvimento)

Como a configuração atual utiliza:

```env
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

Os e-mails serão exibidos diretamente no terminal do container. Isso permite testar a **ativação de conta** e o **reset de senha** sem precisar configurar um servidor SMTP real.

---

## Fluxos Implementados

### Cadastro
* Usuário cria conta com e-mail.
* Conta inicia como inativa.
* Envio de link de ativação com token seguro.

### Ativação
* Link expira conforme a configuração `PASSWORD_RESET_TIMEOUT`.
* Link é invalidado imediatamente após o uso.

### Login
* Permitido apenas para usuários ativos.

### Redefinição de Senha
* Envio de link com token.
* Expiração automática do token.
* Invalidação após uso.
* Bloqueio do envio para usuários não ativados.

---

## Boas Práticas Aplicadas

* Configuração do `AUTH_USER_MODEL` desde o início do projeto.
* Uso da função `get_user_model()` para referenciar o usuário.
* Geração de tokens seguros com `default_token_generator`.
* Expiração e invalidação rigorosa de links sensíveis.
* Proteção contra enumeração de usuários no reset de senha.
* Separação de configurações sensíveis via arquivo `.env`.
* Containerização para garantir consistência entre ambientes.

