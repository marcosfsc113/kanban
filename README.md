#  CarePlanner Kanban - Desafio Técnico

Este projeto é uma aplicação web baseada em Django e Django REST Framework que permite a visualização e o gerenciamento de pacientes internados por meio de um quadro Kanban. Foi desenvolvido como solução para o desafio técnico da **vaga 2 - CarePlanner e Painéis**.

---

##  Objetivo

Permitir que o enfermeiro organize os pacientes em diferentes etapas do cuidado hospitalar:

**Pendente → Triagem → Plano de Cuidado → Alta**

---

##  Tecnologias Utilizadas

- Python 3.11  
- Django 5.2  
- Django REST Framework  
- PostgreSQL  
- HTML5, CSS3, JavaScript (vanilla)  
- SortableJS (para arrastar os cards entre colunas)

---

##  Como Rodar o Projeto Localmente

### 1. Clone o repositório
```bash
git clone https://github.com/marcosfsc113/kanban
cd seu-repositorio

#  CarePlanner Kanban - Desafio Técnico

Este projeto é uma aplicação web baseada em Django e Django REST Framework que permite a visualização e o gerenciamento de pacientes internados por meio de um quadro Kanban. Foi desenvolvido como solução para o desafio técnico da **vaga 2 - CarePlanner e Painéis**.

---

##  Objetivo

Permitir que o enfermeiro organize os pacientes em diferentes etapas do cuidado hospitalar:

**Pendente → Triagem → Plano de Cuidado → Alta**

---

##  Tecnologias Utilizadas

- Python 3.11  
- Django 5.2  
- Django REST Framework  
- PostgreSQL  
- HTML5, CSS3, JavaScript (vanilla)  
- SortableJS (para arrastar os cards entre colunas)

---

##  Como Rodar o Projeto Localmente

### 1. Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

## 2. Crie e ative o ambiente virtual

python -m venv venv

Depois:

source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

## 3. Instale as dependências

pip install -r requirements.txt

## 4. Configure o banco de dados PostgreSQL

Antes de rodar as migrações, crie o banco e o usuário no PostgreSQL:

psql -U postgres

CREATE DATABASE kanban_db;
CREATE USER kanban_user WITH PASSWORD '12345';
GRANT ALL PRIVILEGES ON DATABASE kanban_db TO kanban_user;

Esses dados já estão configurados no settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kanban_db',
        'USER': 'kanban_user',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Para sair: exit

Lembre-se de se conectar ao banco:

psql -U kanban_user -d board

Dê permissão para o usuario kanban_user (para a criação de tabelas e etc)

ALTER DATABASE kanban_db OWNER TO kanban_user;

Para sair: exit

## 5. Aplique as migrações

python manage.py makemigrations
python manage.py migrate

## 6. (Opcional) Caso queira inserir dados teste

 psql -U kanban_user -d kanban_db

-- Inserir buckets (colunas do Kanban)
INSERT INTO bucket (nome) VALUES
('pendente'),
('triagem'),
('plano de cuidado'),
('alta');

-- Inserir cards (pacientes), um por etapa
INSERT INTO card (nome_paciente, data_admissao, estado_civil, idade, sexo, bucket_id) VALUES
('João da Silva',    '2025-06-01', 'Solteiro', 45, 'Masculino', 1),
('Maria Oliveira',   '2025-06-02', 'Casada',   38, 'Feminino',  2),
('Carlos Pereira',   '2025-06-03', 'Divorciado', 60, 'Masculino', 3),
('Ana Souza',        '2025-06-04', 'Viúva',    70, 'Feminino',  4);

Para sair: exit

## 7. (Opcional) Crie um superusuário

python manage.py createsuperuser

## 8. Inicie o servidor

python manage.py runserver

## 9. Acesse no navegador:

Quadro Kanban (interface): http://localhost:8000/

Admin do Django: http://localhost:8000/admin/

API RESTful: http://localhost:8000/api/


Documentação da API RESTful

A API segue o padrão RESTful e responde em JSON. Abaixo estão os principais endpoints disponíveis:

Buckets (Colunas do Kanban)
--------------------------------
Rotas geradas automaticamente pelo ModelViewSet:

- GET /api/buckets/
  → Lista todas as colunas (buckets)

- POST /api/buckets/
  → Cria uma nova coluna
  Body exemplo:
  {
    "nome": "nova coluna"
  }

- GET /api/buckets/{id}/
  → Detalha um bucket específico

- PUT /api/buckets/{id}/
  → Atualiza todos os dados de um bucket

- PATCH /api/buckets/{id}/
  → Atualiza parcialmente os dados de um bucket

- DELETE /api/buckets/{id}/
  → Deleta um bucket

Cards (Pacientes)
---------------------
Rotas geradas automaticamente pelo ModelViewSet:

- GET /api/cards/
  → Lista todos os pacientes

- POST /api/cards/
  → Cria um novo paciente
  Body exemplo:
  {
    "nome_paciente": "Pedro Gomes",
    "data_admissao": "2025-06-10",
    "estado_civil": "Casado",
    "idade": 52,
    "sexo": "Masculino",
    "bucket": 1
  }

- GET /api/cards/{id}/
  → Retorna os dados de um paciente específico

- PUT /api/cards/{id}/
  → Atualiza completamente os dados de um card

- PATCH /api/cards/{id}/
  → Atualiza parcialmente os dados de um card

- DELETE /api/cards/{id}/
  → Deleta um card

Atualização de Status (Mover card)
-------------------------------------
- PATCH /api/cards/{id}/update_status/
  → Atualiza o bucket (coluna) de um card
  Body exemplo:
  {
    "bucket_id": 3
  }
