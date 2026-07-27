
# Blog Project

A complete web system for a blog developed with Python and Django, running in Docker containers. The project supports rich-text posts with a WYSIWYG editor, image uploads with automatic resizing, categories, tags, static pages, search, and protection against brute-force login attempts.

## Features

* **Post Management:** Rich-text posts (via Summernote editor) with cover image, excerpt, slug, and publish/draft status.
* **Image Handling:** Automatic resizing/optimization of cover images and attachments after upload.
* **Categories & Tags:** Organize and filter posts by category or tag.
* **Static Pages:** Support for custom pages (e.g. About, Contact) independent of blog posts.
* **Search:** Search bar to find posts by keyword.
* **Author Filter:** List all posts created by a specific author.
* **Site Configuration:** Admin-managed site setup (title, description, menu links, favicon, and toggles for header/search/menu/pagination/footer visibility).
* **Login Protection:** Brute-force login attempt protection using `django-axes`.

## Technologies Used

* **Back-end:** Python 3, Django
* **Database:** PostgreSQL
* **Front-end:** HTML5, CSS3, Django Templates
* **Rich-text Editor:** django-summernote
* **Image Processing:** Pillow
* **Login Security:** django-axes
* **Environment Variables:** python-dotenv
* **Containerization:** Docker & Docker Compose

## How to run the project locally

This project is fully containerized, so the recommended way to run it is with Docker.

1. Clone this repository:

```
git clone https://github.com/LucasSekikawa/projeto-blog.git
```

2. Access the project folder:

```
cd projeto-blog
```

3. Create your environment variables file based on the example provided:

```
cp dotenv_files/.env-example dotenv_files/.env
```

Then open `dotenv_files/.env` and replace the `CHANGE-ME` placeholders with your own values (secret key, database name, user, and password).

4. Build and start the containers (Django app + PostgreSQL):

```
docker-compose up --build
```

5. The entrypoint script automatically waits for PostgreSQL to be ready, runs migrations, collects static files, and starts the server. Once the logs show the server running, access the project in your browser through the link: `http://127.0.0.1:8000/`

6. (Optional) To create an admin user to access the Django admin panel, open a new terminal and run:

```
docker exec -it djangoapp python manage.py createsuperuser
```

---

# Projeto Blog

Um sistema web completo para um blog desenvolvido com Python e Django, rodando em containers Docker. O projeto oferece posts em texto rico com editor WYSIWYG, upload de imagens com redimensionamento automático, categorias, tags, páginas estáticas, busca e proteção contra tentativas de login por força bruta.

## Funcionalidades

* **Gestão de Posts:** Posts em texto rico (via editor Summernote) com imagem de capa, resumo (excerpt), slug e status de publicado/rascunho.
* **Tratamento de Imagens:** Redimensionamento/otimização automática das imagens de capa e anexos após o upload.
* **Categorias e Tags:** Organização e filtragem dos posts por categoria ou tag.
* **Páginas Estáticas:** Suporte para páginas customizadas (ex.: Sobre, Contato) independentes dos posts do blog.
* **Busca:** Barra de pesquisa para encontrar posts por palavra-chave.
* **Filtro por Autor:** Listagem de todos os posts criados por um autor específico.
* **Configuração do Site:** Configurações gerenciadas pelo admin (título, descrição, links do menu, favicon e opções para exibir/ocultar cabeçalho, busca, menu, paginação e rodapé).
* **Proteção de Login:** Proteção contra tentativas de login por força bruta usando `django-axes`.

## Tecnologias Utilizadas

* **Back-end:** Python 3, Django
* **Banco de Dados:** PostgreSQL
* **Front-end:** HTML5, CSS3, Django Templates
* **Editor de Texto Rico:** django-summernote
* **Processamento de Imagens:** Pillow
* **Segurança de Login:** django-axes
* **Variáveis de Ambiente:** python-dotenv
* **Containerização:** Docker & Docker Compose

## Como executar o projeto localmente

Este projeto é totalmente containerizado, então a forma recomendada de executá-lo é com Docker.

1. Clone este repositório:

```
git clone https://github.com/LucasSekikawa/projeto-blog.git
```

2. Acesse a pasta do projeto:

```
cd projeto-blog
```

3. Crie o seu arquivo de variáveis de ambiente com base no exemplo fornecido:

```
cp dotenv_files/.env-example dotenv_files/.env
```

Em seguida, abra o arquivo `dotenv_files/.env` e substitua os valores `CHANGE-ME` pelas suas próprias informações (chave secreta, nome do banco, usuário e senha).

4. Construa e inicie os containers (aplicação Django + PostgreSQL):

```
docker-compose up --build
```

5. O script de entrypoint aguarda automaticamente o PostgreSQL ficar pronto, executa as migrações, coleta os arquivos estáticos e inicia o servidor. Quando o log mostrar o servidor rodando, acesse o projeto no seu navegador através do link: `http://127.0.0.1:8000/`

6. (Opcional) Para criar um usuário admin e acessar o painel administrativo do Django, abra um novo terminal e execute:

```
docker exec -it djangoapp python manage.py createsuperuser
```
