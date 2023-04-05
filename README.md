### Freight-quote-app

Este é um projeto em que o usuário pode cadastrar um pacote e pela própria página do django admin o usuário é capaz de selecionar o produto desejado e fazer a cotação do frete do mesmo.

Abaixo segue como executar o projeto:

## 1. Configuração inicial

Após clonar o projeto, crie um ambiente virtual 


### Ambiente virtual:

Para criar um ambiente virtual execute:

```shell
python -m venv venv
```
Em seguida ative o ambiente virtual:

(Linux) 

```shell
source venv/bin/activate
```

(Windows)

```shell
.\venv\Scripts\activate.ps1
```

### Migrations:

Primeiramente crie as migrations executando:

```shell
python manage.py makemigrations
```

em seguida execute as migrações:
```shell
python manage.py migrate
```

Crie um usuário admin para poder gerenciar os pacotes:
```
python manage.py createsuperuser
```

Por fim, inicie a API

```shell
python manage.py runserver
```
