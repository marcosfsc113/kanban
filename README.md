Desafio Técnico: Kanban CarePlanner
Descrição do Projeto
O Kanban CarePlanner é uma aplicação web desenvolvida como solução para o Desafio Técnico para a Vaga 2. O objetivo é fornecer uma ferramenta visual, no estilo de um quadro Kanban, para que enfermeiros possam organizar e planejar o trabalho relacionado aos pacientes internados em sua ala. 

A aplicação utiliza uma API REST construída com Django e um frontend interativo que permite visualizar e gerenciar o fluxo de pacientes através das etapas de cuidado: Pendente, Triagem, Plano de Cuidado e Alta. 


Funcionalidades Principais

Visualização em Kanban: Exibe todos os pacientes como cards organizados em colunas que representam as etapas do cuidado. 



Detalhes do Paciente: Ao clicar em um card, uma tela modal exibe os dados completos do paciente (nome, estado civil, idade, sexo e data de admissão). 



Movimentação Drag-and-Drop: Permite que o enfermeiro arraste e solte os cards de uma coluna para outra, atualizando o status do paciente em tempo real. 


Persistência de Dados: Todas as informações são armazenadas em um banco de dados relacional PostgreSQL. 

Tecnologias Utilizadas
Backend: Django, Django REST Framework


Banco de Dados: PostgreSQL 

Frontend: HTML5, CSS3, JavaScript (vanilla)


Versionamento: Git e GitHub 

Pré-requisitos
Antes de começar, garanta que você tem os seguintes softwares instalados na sua máquina:

Python (versão 3.8 ou superior)

Pip (gerenciador de pacotes do Python)

Git

PostgreSQL (servidor de banco de dados)

Instalação e Configuração
Siga os passos abaixo para configurar e rodar o projeto localmente.

1. Clonar o Repositório

Bash

git clone [SEU_LINK_DO_REPOSITORIO_AQUI]
cd nome-do-repositorio
2. Criar e Ativar o Ambiente Virtual
É uma boa prática criar um ambiente virtual para isolar as dependências do projeto.

Bash

# Criar o ambiente
python -m venv venv

# Ativar no Windows
venv\Scripts\activate

# Ativar no macOS/Linux
source venv/bin/activate
3. Instalar as Dependências
Instale todas as bibliotecas Python necessárias com um único comando.

Bash

pip install -r requirements.txt
(Nota: Para criar o arquivo requirements.txt no seu projeto, rode pip freeze > requirements.txt)

4. Configurar o Banco de Dados PostgreSQL

Abra o seu cliente PostgreSQL (como o psql ou DBeaver).

Crie um novo banco de dados e um novo usuário para a aplicação.

SQL

CREATE DATABASE kanban_db;
CREATE USER kanban_user WITH PASSWORD 'sua_senha_segura';
GRANT ALL PRIVILEGES ON DATABASE kanban_db TO kanban_user;
5. Configurar as Variáveis de Ambiente

No diretório raiz do projeto, renomeie o arquivo .env.example para .env.

Abra o arquivo .env e preencha com as suas credenciais do banco de dados e uma nova SECRET_KEY.

SECRET_KEY='django-insecure-sua-chave-secreta-aqui'
DEBUG=True
DB_NAME='kanban_db'
DB_USER='kanban_user'
DB_PASSWORD='sua_senha_segura'
DB_HOST='localhost'
DB_PORT='5432'
6. Aplicar as Migrações
Este comando irá criar todas as tabelas necessárias no seu banco de dados, baseado nos modelos Django. 


Bash

python manage.py migrate
7. Criar um Superusuário
Crie um usuário administrador para acessar o Django Admin.

Bash

python manage.py createsuperuser
Siga as instruções para definir nome de usuário, e-mail e senha.

8. (Opcional) Popular Dados Iniciais
Para popular o quadro com as colunas padrão, você pode rodar o seguinte comando (se um script de seed for criado):

Bash

python manage.py seed_buckets
Ou adicionar as colunas manualmente através do Django Admin (/admin).

9. Rodar o Servidor de Desenvolvimento
Tudo pronto! Inicie o servidor.

Bash

python manage.py runserver
A aplicação estará disponível em http://127.0.0.1:8000/.

Documentação da API
(Copie e cole aqui a s