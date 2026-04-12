# Accounts Auth System

Minissistema de autenticação desenvolvido com Django para estudo e prática de boas práticas de cadastro, login, ativação de conta por e-mail e redefinição de senha.

## Objetivo

Este projeto foi criado para demonstrar conhecimento prático em:

- customização do modelo de usuário no Django
- autenticação com e-mail como identificador principal
- envio de e-mail para confirmação de conta
- redefinição de senha por link seguro
- bloqueio de ações para usuários não ativados
- invalidação de links após uso e expiração por tempo
- organização do projeto com variáveis de ambiente
- estruturação de templates para autenticação

## Funcionalidades

- cadastro de usuário com e-mail único
- validação de senha com validadores do Django
- confirmação de conta por e-mail
- link de ativação com expiração e invalidação após uso
- login com e-mail e senha
- logout
- redefinição de senha por e-mail
- link de redefinição expirado e invalidado após uso
- dashboard protegido após autenticação
- bloqueio de reset de senha para usuários inativos

## Tecnologias utilizadas

- Python
- Django
- SQLite
- HTML
- django-environ

## Estrutura do projeto

```text
accounts/
├── accounts/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── core/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/
│   ├── registration/
│   │   ├── account_activation_email.html
│   │   ├── login.html
│   │   ├── password_reset_complete.html
│   │   ├── password_reset_confirm.html
│   │   ├── password_reset_done.html
│   │   ├── password_reset_form.html
│   │   └── signup.html
│   ├── base.html
│   └── dashboard.html
├── .env
├── .env.example
├── .gitignore
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/M2004GV/django-auth-system.git
cd django-auth-system
```

### 2. Crie e ative um ambiente virtual

Linux/macOS:

```bash
python -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto com base no `.env.example`.

**Em desenvolvimento**, o backend de console é o mais simples — os e-mails aparecem no terminal, sem necessidade de configurar SMTP:

```env
DEBUG=True
SECRET_KEY=change-me
ALLOWED_HOSTS=127.0.0.1,localhost

EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
DEFAULT_FROM_EMAIL=webmaster@localhost

TIME_ZONE=America/Fortaleza
LANGUAGE_CODE=pt-br
```

**Em produção**, substitua pelo backend SMTP com suas credenciais reais:

```env
DEBUG=False
SECRET_KEY=sua-chave-secreta-longa
ALLOWED_HOSTS=seudominio.com

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=seu_email@gmail.com
EMAIL_HOST_PASSWORD=sua_senha_de_app
DEFAULT_FROM_EMAIL=seu_email@gmail.com

TIME_ZONE=America/Fortaleza
LANGUAGE_CODE=pt-br
```

> Para Gmail, use uma [senha de app](https://support.google.com/accounts/answer/185833) — não a senha da conta.

### 5. Rode as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Execute o servidor

```bash
python manage.py runserver
```

Acesse:

- `http://127.0.0.1:8000/` — login
- `http://127.0.0.1:8000/signup/` — cadastro
- `http://127.0.0.1:8000/password_reset/` — redefinição de senha

## Fluxos implementados

### Cadastro

O usuário informa e-mail, senha e confirmação de senha. Após o envio, a conta é criada como inativa e um e-mail de ativação é enviado com um link contendo token seguro.

### Ativação

O usuário ativa a conta clicando no link recebido por e-mail. O link expira após o prazo configurado em `PASSWORD_RESET_TIMEOUT` e é invalidado imediatamente após o primeiro uso.

### Login

Após ativação, o usuário pode autenticar-se com e-mail e senha.

### Redefinição de senha

O sistema envia um link seguro para redefinição de senha. O link expira por tempo e é invalidado automaticamente após o uso, pois a alteração da senha torna o token anterior inválido. Apenas contas ativas podem iniciar esse fluxo.

## Boas práticas aplicadas

- uso de `AUTH_USER_MODEL` desde o início do projeto
- uso de `get_user_model()` em vez de importar o model diretamente
- uso de variáveis de ambiente para segredos e configuração
- separação de templates de autenticação
- uso das views built-in do Django para login e reset de senha
- bloqueio de redefinição para usuários inativos
- tokens gerados com `default_token_generator` do Django — com expiração e invalidação pós-uso
- links de ativação invalidados após o primeiro clique via atualização do `last_login`