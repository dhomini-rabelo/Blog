<h1>Blog Code Portal</h1>
<style>
    img {
        border: 0.5px solid #22272E !important;
        border-style: solid !important; 
        max-width: 100%; display: block; 
        margin: 0 auto; 
        margin-top: 30px;
    }
</style>
<img src="./readme/pc.PNG" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; display: block; margin: 0 auto; margin-top: 30px;">
<br>
<div style="display: flex; justify-content: space-evenly; align-items: center;">
    <img src="./readme/mobile.PNG" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
    <img src="./readme/main/base.PNG" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
</div>


<h2>🔗 Tópicos</h2>
<ul>
<li><a href="#about">Sobre</a></li>
<li><a href="#tools">Ferramentas</a></li>
<li><a href="#features">Features</a></li>
<li><a href="#db">Modelagem</a></li>
<li><a href="#project">Projeto</a></li>
<li><a href="#how_to_use">Como usar</a></li>
</ul>


<h2 id="about" style="margin-top: 30px;">📖 Sobre</h2>
<p>Blog compartilhado de tecnologia, basta criar uma conta e fazer seus posts sobre tecnologia</p>

<h2 id="tools" style="margin-top: 30px;">🛠️ Principais ferramentas</h2>

<ul>
<li>Fast</li>
<li>Django</li>
<li>Django Rest Framework</li>
<li>Django-summernote</li>
<li>Celery</li>
<li>Redis</li>
<li>Postgres</li>
<li>Celery beat</li>
<li>Flower</li>
<li>Docker</li>
<li>Docker-compose</li>
</ul>


<h2 id="features" style="margin-top: 30px;">🚀 Features</h2>

<ul>
<li>Django ORM</li>
<li>Autenticação do Django</li>
<li>Formulários com Fast</li>
<li>Tarefas usando Celery</li>
<li>Tarefas agendadas usando Celery beat</li>
<li>Dashboard de tarefas usando Flower</li>
<li>Sistema de mensagens com Fast</li>
<li>Campo de texto para posts usando Django-summernote</li>
<li>Javascript consumindo APIs</li>
<li>Site responsivo</li>
<li>Micro SPAs</li>
<li>Admin personalidzado</li>
<li>Envio de email</li>
<li>Cache</li>
</ul>


<h2 id="db" style="margin-top: 30px;">🏷️ Modelagem do banco de dados</h2>

<h3>User</h3>
<ul>
<li>Username ( gerenciada pelo AbstractUser do Django )</li>
<li>Senha ( gerenciada pelo AbstractUser do Django )</li>
<li>Nome</li>
<li>Email</li>
<li>Foto de perfil</li>
<li>My static pages JSON</li>
</ul>

<h3>Categorias</h3>
<ul>
<li>Nome</li>
<li>Slug</li>
<li>Imagem</li>
</ul>

<h3>Subcategorias</h3>
<ul>
<li>Nome</li>
<li>Slug</li>
<li>Imagem</li>
<li>Categoria FK</li>
</ul>

<h3>Sugestão de Categoria</h3>
<ul>
<li>Nome</li>
<li>Estado</li>
<li>User FK</li>
</ul>

<h3>Sugestão de Subcategoria</h3>
<ul>
<li>Nome</li>
<li>Estado</li>
<li>User FK</li>
</ul>

<h3>Post</h3>
<ul>
<li>Título</li>
<li>Descrição</li>
<li>Imagem</li>
<li>Autor (User) FK</li>
<li>Texto</li>
<li>Publicado BOOL</li>
<li>Código</li>
<li>Categoria FK</li>
<li>Subcategoria M2M</li>
<li>Data de criação</li>
<li>Data de última modificação</li>
</ul>


<h2 id="project"  style="margin-top: 30px;">🎥 Projeto</h2>
<ul>

<li style="margin-top: 30px;">
<h3>Sistema de administração</h3>
<img src="./readme/admin/login.PNG" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; display: block; max-width: 100%; margin-top: 20px;">
<img src="./readme/admin/dash.PNG" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; display: block; max-width: 100%; margin-top: 20px;">
</li>

<li style="margin-top: 30px;">
<h3>Flower</h3>
<img src="./readme/celery/index.PNG" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; display: block; max-width: 100%; margin-top: 20px;">
<img src="./readme/celery/many_tasks.PNG" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; display: block; max-width: 100%; margin-top: 20px;">
<img src="./readme/celery/tasks.PNG" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; display: block; max-width: 100%; margin-top: 20px;">
<img src="./readme/celery/oonly_task.PNG" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; display: block; max-width: 100%; margin-top: 20px;">
</li>

<li style="margin-top: 30px;">
<h3>Cadastro</h3>
<img src="./readme/login_group/register.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
<img src="./readme/login_group/email.png" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px; height: 766px; object-fit: cover;">
</li>

<li style="margin-top: 30px;">
<h3>Usuário salvo no sistema de administração</h3>
<img src="./readme/login_group/user_save.PNG" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
</li>

<li style="margin-top: 30px;">
<h3>Validação de formulário pelo backend</h3>
<p>Está feature está presente em todos os formulários do sistema</p>
<img src="./readme/login_group/backend_validation.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
</li>

<li style="margin-top: 30px;">
<h3>Validação de formulário pelo frontend</h3>
<p>Está feature está presente em todos os formulários do sistema</p>
<img src="./readme/login_group/frontend_validation.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
</li>

<li style="margin-top: 30px;">
<h3>Login no sistema</h3>
<img src="./readme/login_group/login.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
</li>

<li style="margin-top: 30px;">
<h3>Erros no login</h3>
<img src="./readme/login_group/login_errors.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
</li>

<li style="margin-top: 30px;">
<h3>Esqueci a senha</h3>
<img src="./readme/login_group/forgot_password.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
</li>

<li style="margin-top: 30px;">
<h3>Alterar dados básicos</h3>
<p>Ao criar seu perfil, o sistema sorteia uma foto de usuário, você pode editar essa foto do mesmo modo que edita uma foto de um post</p>
<img src="./readme/account/edit_profile.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
</li>

<li style="margin-top: 30px;">
<h3>Alterar senha</h3>
<img src="./readme/account/change_password.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
</li>

<li style="margin-top: 30px;">
<h3>Alterar email</h3>
<img src="./readme/account/change_email.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
</li>

<li style="margin-top: 30px;">
<h3>Enviando sugestões</h3>
<p>O usuário não pode criar categorias e subcategorias, mas ele pode enviar sugestões para os administradores</p>
<img src="./readme/account/send_suggestions.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
</li>

<li style="margin-top: 30px;">
<h3>Sugestões no sistema de administração</h3>
<img src="./readme/account/admin_suggestions.PNG" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; display: block; max-width: 100%; margin-top: 20px;">
<img src="./readme/account/admin_suggestions_change_state.PNG" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; display: block; max-width: 100%; margin-top: 20px;">
<img src="./readme/account/admin_suggestion_category_change_state.PNG" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; display: block; max-width: 100%; margin-top: 20px;">
</li>

<li style="margin-top: 30px;">
<h3>Respostas das sugestões</h3>
<p>As respostas são registradas após o administrador mudar o estado das sugestões no sistema de administração</p>
<img src="./readme/account/result_suggestions.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
</li>

<li style="margin-top: 30px;">
<h3>Criando um post</h3>
<img src="./readme/account/create_post.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
</li>

<li style="margin-top: 30px;">
<h3>Editando um post</h3>
<p>A seção EDITAR lista seus posts publicados e a seção RASCUNHOS lista seus posts não publicados</p>
<img src="./readme/account/edit_post.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
</li>

<li style="margin-top: 30px;">
<h3>Tela inicial - Lista de Posts</h3>
<img src="./readme/main/index.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
</li>

<li style="margin-top: 30px;">
<h3>Lista de categorias</h3>
<img src="./readme/main/categories_view.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
</li>

<li style="margin-top: 30px;">
<h3>Lista de Autores</h3>
<img src="./readme/main/authors.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
</li>

<li style="margin-top: 30px;">
<h3>Fazendo busca</h3>
<img src="./readme/main/search.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
</li>

<li style="margin-top: 30px;">
<h3>Navegação rápida</h3>
<p>Apenas com dados do backend e consumo de APIs, essas páginas ficam num formato de SPA</p>
<img src="./readme/main/fast_navigation.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
<p style="margin-top: 20px;">A url é dinâmica</p>
<img src="./readme/main/dinamic_url.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
<p style="margin-top: 20px;">Esta feature também está presente nas páginas de login e cadastro</p>
<img src="./readme/login_group/spa.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
</li>

<li style="margin-top: 30px;">
<h3>Telas no computador</h3>
<p>Esse projeto foi feito com o conceito de mobile first</p>
<img src="./readme/main/pc_views.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; max-width: 100%; margin-top: 20px;">
</li>

<li style="margin-top: 30px;">
<h3>Logout</h3>
<img src="./readme/login_group/logout_PC.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; display: block; max-width: 100%; margin-top: 20px;">
<img src="./readme/login_group/logout.gif" alt="project-image" style="border: 0.5px solid #22272E !important; border-style: solid !important; display: block; max-width: 100%; margin-top: 20px;">
</li>

</ul>

<h2 id="how_to_use" style="margin-top: 30px;">🛠️ Como usar</h2>

<p>Para usar você deve ter docker instalado na sua máquina, atualizar as dependências, configurar o arquivo .env.dev e renomeá-lo para .env, depois disso basta apenas rodar o comando abaixo:</p>

```
docker-compose up --build
```
