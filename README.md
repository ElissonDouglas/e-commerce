# &#x1F6D2; Fast Commerce

> Status: Desenvolvimento ⚠️

### Este projeto é uma aplicação de e-commerce iniciante desenvolvida com o framework Django. Ela inclui as funcionalidades básicas de um e-commerce, como a exibição de produtos, carrinho de compras e checkout.

***

## Techs Usadas

* Python: 3.10.6
* Django Framework: 4.1.5
* MySQL: 8.0.31
* HTML5
* CSS3
***

## Instalação

**Warning**
> Você precisar ter instalado em sua máquina: [Python](https://www.python.org/)

> Caso você prefira utilizar o MySQL você precisa configura-lo no arquivo ecommerce/settings.py e remover a configuração do SQLite3.
>


- Clone o repositório: <br>
>```sh
> git clone https://github.com/ElissonDouglas/e-commerce
>```

- Entre no diretório do projeto: <br>
>```sh
> cd e-commerce
>```

- Crie um ambiente virtual e ative-o:
>```sh
> python -m venv nome-do-ambiente
> source nome-do-ambiente/bin/activate
>```

- Instale as dependências:
>```sh
> pip install -r requirements.txt
>```

- Execute as migrations:
>```sh
> python manage.py makemigrations
> python manage.py migrate
>```

- Inicie o servidor:
>```sh
> python manage.py runserver
>```

### Agora você pode acessar a aplicação em http://localhost:8000/

## Uso

### Para adicionar produtos você pode usar o painel de administração do Django:

http://localhost:8000/admin/

> **Atenção**
> Para criar um super-usuário utilize o seguinte comando no terminal:
> ```sh
> python manage.py createsuperuser 
> ```

## Contribuição
Se você deseja contribuir para o projeto, siga estes passos:

1. Faça um fork deste repositório.
2. Crie uma branch com sua funcionalidade: git checkout -b minha-funcionalidade
3. Commit suas mudanças: git commit -m 'Adicionando minha funcionalidade'
4. Envie para o GitHub: git push origin minha-funcionalidade
5. Crie um Pull Request.

## Licença

Este projeto está sob a licença [MIT]. Veja o arquivo LICENSE.md para mais detalhes.
