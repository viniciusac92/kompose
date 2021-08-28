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
