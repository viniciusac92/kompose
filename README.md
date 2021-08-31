# Kompose

### Adicione aqui os erros e correções aplicadas

### EXEMPLO

---

**Código com erro:**

```sh
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

**Erro:** O app "songs" não está declarado em INSTALLED_APPS  
**O que ele causa:** O Django não consegue identificar as informações desse app para executá-lo.  
**Como corrigir:** Incluir a linha com o nome do app "songs" dentro de INSTALLED_APPS, fazendo com que ele seja reconhecido pelo Django.  
**Código corrigido:**

```sh
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "songs"
]
```

---

**Código com erro:**

```sh
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "songs"
]
```

**Erro:** O package "rest_framework" não está declarado em INSTALLED_APPS  
**O que ele causa:** O Django não consegue executar as funcionalidades extraídas de Django Rest Framework.  
**Como corrigir:** Incluir a linha com o nome do pacote "rest_framework" dentro de INSTALLED_APPS.  
**Código corrigido:**

```sh
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "songs"
]
```

---

**Código com erro:**

```sh
❯ docker-compose build
ERROR: The Compose file is invalid because:
Service web has neither an image nor a build context specified. At least one must be provided
```

**Erro:** A imagem do django app não foi localizada.  
**O que ele causa:** O comando "docker-compose build" não faz a criação dos serviços determinados no arquivo yaml.
**Como corrigir:** Incluir "build: ." no serviço "web".  
**Código corrigido:**

---

```sh
Error: Database is uninitialized and superuser password is not specified.
db_1 You must specify POSTGRES_PASSWORD to a non-empty value for the
db_1 superuser. For example, "-e POSTGRES_PASSWORD=password" on "docker run".
```

**Erro:** Senha do usuário não localizada.  
**O que ele causa:** O comando "docker-compose up" não faz a criação dos serviços determinados no arquivo yaml.
**Como corrigir:** Incluir "POSTGRES\_" no arquivo "dev.env" e no arquivo "settings.py".  
**Código corrigido:**

---

**Código com erro:**

```sh
FROM python:2.7
```

**Erro:** DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. A future version of pip will drop support for Python 2.7. More details about Python 2 support in pip, can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support...
**O que ele causa:** Falha na instalação do requirements.txt .  
**Como corrigir:** Alterar para a versão 3.9 .  
**Código corrigido:**

---

**Código com erro:**

```sh
settings.py

DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgre",
            "NAME": os.getenv("POSTGRES_DB"),
            "USER": os.getenv("POSTGRES_USER"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
            "HOST": "database",
            "PORT": 5432,
        }
    }

```

**Erro:** "ENGINE": "django.db.backends.postgre"
"HOST": "database"
**O que ele causa:**  
**Como corrigir:** Alterar para a descrição do "ENGINE" para "postgresql" e
colocar o "HOST" apontando para o serviço indicado no arquivo docker-compose, que seria o "db".
**Código corrigido:**
