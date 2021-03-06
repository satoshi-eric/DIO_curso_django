# Desenvolvimento para internet e banco de dados com Python e Django

## Introdução aos conceitos e ambiente Django

### Sistemas web
* São software/aplicações hospedados na internet e podem ser acessados por requisições http
* Permitem ser usados ser nessecidade de download e instalação
* Outra definição que pode ser dada é tudo que é processado em um servidor

### Vantagens do sistema web
* São seguros pois estão em um servidor
* Não necessitam de dependências
* São mais rápidas e menos trabalhosas para a disponibilização de novas atualizações

### Python para web
* Python é usado para muitos seguimentos:
  * Ciência de dados
  * Administração de sistemas
  * Desenvolvimento de software para desktops (GUI)
  * Jogos
  * Sistemas Web
* Python tem crescido muito nos sistemas web muito por causa dos framework
* Existem outros frameworks: Flask, Pyramid, Tornado, web2py, Bottle
  
### Framework Django

* Incentiva o desenvolvimento limpo
* Abstrai muito do trabalho do desenvolvedor
* Django é gratuito e open-source
* É o framework mais popular do mercado
  
### Estrutura Django
![Estrutura do projeto](images/estrutura_django.png)

## Primeiro projeto

Criando ambiente virtual

```
python -m venv dev_django
.\dev_django\Scripts\activate
pip install django
django-admin startproject <nome do projeto>
```

Com isso, uma estrutura de diretórios será criada. Para executar o projeto, basta usar o comando 
``` 
python manage.py runserver 
```
no diretório onde o `manage.py` está e o servidor django será criado. A porta padrão do django é a porta 8000.

Agora, vamos criar uma aplicação com o comando:
```
django-admin startproject core
```

Basta mover a pasta criada para o diretório raíz do projeto. Como criamos um novo app, precisamos entrar no arquivo settings.py e adicionar "core" à lista INSTALLED_APPS para o django interpretar o app como um app do projeto. 

### Exercício 

No projeto criado, acrecentar uma rota que realize operações matemáticas entre 2 números.

## Estrutura básica do django

### Django-admin

* Todos os comandos utilizados (startproject, startapp) são realizados pelo django-admin.py. 
* É utilizado para realizar tarefas administrativas.Para verificar os comandos disponíveis, basta usar o comando
```
django-admin --help
```
O django-admin fica no ambiente virtual. 

### Manage

* Envolve o django-admin como se fosse uma interface entre o projeto e o django-admin
* Delega tarefas para o django-admin
* Responsável por colocar o pacote do projeto no sys.path
* Define a variável de ambiente DJANGO_SETTINGS_MODULE que aponta para o arquivo settings.py

### WSGI

* Web Server Gateway Interface (Interface de porta de entrada do servidor web)
* Plataforma padrão para aplicações web em python
* Serve de interface do Servidor e a Aplicação Web
* O startproject inicia uma configuração padrão do WSGI
* Com o runserver, é iniciado um servidor de aplicação leve. Esse servidor é espesificado pela configuração WSGI_APPLICATION. Esse servidor é para desenvolvimento. Para produção, é necessário de um servidor mais robusto.
  
### Settings

* Responsável pelas configurações do Django
* Nele, é possível configurar: apps, conexão com BD, templates, time zone, cache, segurança, arquivos estáticos, etc.

### URLs

* É um schema de URL
* Responsável por gerenciar as rotas das URLs, onde é possível configurar para onde cada rota será executada

### Views

* Responsável por processar e retornar resposta para o cliente que fez a requisição.

### Models

* Define modelo de dados inteiramente em python
* Faz a abstração do banco de dados. Transforma todas as tabelas do banco de dados em classes e os acessos são feitos em linguagem python onde o Django realiza a transformação para o SQL.

### Admin

* Interface administrativa gerada automaticamente pelo Django
* Ele lê metadados que estão nas models e fornece uma interface poderosa e pronta para manipulação de dados.
* Acessa a tela de administração de dados

### Static

* Responsável por armazenar arquivos estáticos
* CSS, Javascript, imagens

### Templates

* Responsável por armazenar arquivos HTML
* Diretório padrão para armazenar todo o conteúdo HTML da nossa aplicação.

## Projeto

* Aplicação totalmente do zero que simula uma agenda
* A plaicação terá persistência de banco de dados
* A aplicação será multiusuário
* Cada usuário irá vizualizar sua própria agenda e não a dos demais
* A aplicação irá contar com autenticação

### Tabelas padrões do Django

* O Django possui tabelas padrões que são utilizadas principalmente para segurança e autenticação.
* É possível criar essas tabelas usando o comando `migrate`
* Ao criar essas tabelas, é necessário criar o primeiro usuário para acessar o painel do Django admin
* Para criar esse usuário, é necessário usar o comando `creaatesuperuser`
* Essas tabelas existem para auxiliar e agilizar a parte dee autenticação e perfis de acesso
* Entre as tabelas padrão, estão Usuário, Grupo e Perfil
* Com as tabelas padrões, é possível criar usuários e definir perfis de qual usuário pode acessar determinado conteúdo

### Começando projeto

Para criar as atbelas, usamos o comando
```
python manage.py migrate
```

Para criar um superusuário, usaremos o comando
```
python manage.py createsuperuser --username admin
```

email: admin@agenda.com.br
password: admin123

senhas de todos os outros usuários: Hello123!

## Criando tabaelas com models

### Migração de dados no Django

* Para migração de dados no django, é necessário que hajam classes criadas
* Com essas classes, é necessário usar o comando `migrate` para a migração.
* Também pode-se usar o comando migrations para a criação do arquivo de migração, para não migrar às cegas. 
* Também pode-se usar o comando sqlmigrate para visualizar os comandos do banco de dados

### Criando tabelas

Para criar uma tabela, é necessário criar uma model, uma classe que será representada dentro do aplicativo. Depois disso, usar o comando 
```
python .\manage.py makemigrations core
```
```
python manage.py sqlmigrate core 0001 
```
```
python .\manage.py migrate core 0001
```
O `makemigrations` cria um arquivo de migração. O `sqlmigrate` mostra os comandos SQL que serão utilizados depois pelo `migrate` que atualiza as tabelas do banco de dados.

## Criando página de listagem

* O django oferece no seu modelo de templates a capacidade de utilizar comandos python dentro do HTML
* Com isso, é possível usar comandos if e for

Para isso, precisamos criar páginas HTML que irão mostrar os eventos para os usuários. Antes de criar essas paginas, precisamos criar um diretório chamado **templates** onde essas páginas estarão. 

Agora, precisamos avisar ao django que esse diretório existe. Em settings, existe uma constante chamada `TEMPLATES` onde dentro dela há uma lista chamada `DIRS`   onde será colocado o diretório dos templates. Adicionamos o seguinte item à lista:

```python
os.path.join(BASE_DIR, 'templates)
```

Agora, o django reconhece o diretório templates e podemos criar as páginas HTML. 

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Agenda</title>
  <h1>Agenda</h1>
</head>
<body>
    <h1>Agendamentos</h1>
    
    <p>Desenvolvido por Eric</p>
</body>
</html>
```

Agora, precisamos configurar as views para renderizar essa página. No arquivo views.py, adicionamos a seguinte função:

```python
def lista_eventos(request):
    evento = Evento.objects.all() 
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
```

Ela irá fazer a requisição ao banco de dados e irá mostrar a página para o usuário. Com o django, é possível enviar dados do back-end para o front-end usando o render como mostrado acima. Com isso, é possível renderizar os dados na página. Para isso, na página, usaremos uma sintaxe que permite acessar esses dados:

```html
  <ul style="font-size: 18px;">
      {% for evento in eventos %}
          <li>{{evento.titulo}} - {{evento.get_data_evento}}</li>
      {% endfor %}
  </ul>
```

Agora, os dados do servidor serão mostrados para o usuário.

## Autenticação

### Pacote de autenticação do django

* O django já possui um pacot de autnticação em `django.contrib.auth` 
* Cria tabelas de usuários e permissões
* É necessário que ele esteja no `INSTALLED_APPS` do  `settings.py`

### authenticate

* É a função responsável por autenticar usuário
```python
user = authenticate(username=username, password=password)
```

### login 
* Responsável por criar uma sessão para o usuário autenticado
```python
login(requesst, user)
```

### logout
* Apaga os dados da sessão do usuário
```python
user = logout(request)
```

### login_required
* Responsável por validar a autenticação do usuário
* É um decorador utilizado em todas as funções/views que necessitam de um usuário logado
```python
@login_required(login_url='/login/')
def lista_eventos(request):
```

### Decoradores
* São funções usadas sobre outras funções
* São usados para adicionar funcionalidade às funções

