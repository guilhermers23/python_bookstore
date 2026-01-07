# bookstore_python

BookStore APP - EBAC Módulo 13

# Guia de Configuração: Modelos e Admin (Django)

Este guia descreve o processo de refatoração do arquivo `models.py` para um pacote organizado e o registro dos apps no projeto.

---

## 1. Reestruturação das Models (Transformando em Pacote)

Quando o projeto cresce, organizar os modelos em arquivos separados facilita a manutenção.

1. **Criar o diretório**: Dentro da pasta do seu app (ex: `product/`), crie uma pasta chamada `models/`.
2. **Mover modelos**: Crie arquivos Python dentro dessa pasta para seus modelos (ex: `category.py`, `product.py`).
3. **Remover o antigo**: Delete o arquivo `models.py` da raiz do app, pois ele será substituído pela pasta.

---

## 2. Exportação no `__init__.py`

Para que o Django "enxergue" as classes dentro da pasta `models/`, elas precisam ser importadas no arquivo de inicialização do pacote.

- **Arquivo**: `product/models/__init__.py`
- **Código**:
  ```python
  from .product import Product
  from .category import Category
  ```

## 3. Registro dos Apps no Projeto

O Django só reconhecerá as tabelas do banco de dados e as configurações se os apps estiverem listados no arquivo mestre.

- **Arquivo**: `bookstore_python/settings.py`

- **Ação**: Adicione os apps na lista `INSTALLED_APPS`:

  ```python
  INSTALLED_APPS = [
  # ... apps nativos ...
  'product',
  'order',
  ]
  ```

## 4. Registro no Interface Admin

Para gerenciar os dados visualmente através do `/admin`.

- **Arquivo**: `product/admin.py`

Código:

```python
    from django.contrib import admin
    from .models import Product, Category # Busca automaticamente do __init__.py

    admin.site.register(Product)
    admin.site.register(Category)
```

Dica: Lembre-se de rodar python manage.py makemigrations e python manage.py migrate após reorganizar as pastas para garantir que o Django mapeou tudo corretamente.
