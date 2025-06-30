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
git clone https://github.com/seu-usuario/seu-repositorio.git
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
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

## 3. Instale as dependências

pip install -r requirements.txt

## 4. Configure o banco de dados PostgreSQL

Crie o banco de dados com as seguintes configurações (já definidas em settings.py):

Banco: kanban_db
Usuário: kanban_user
Senha: 12345
Host: localhost
Porta: 5432

## 5. Aplique as migrações

python manage.py makemigrations
python manage.py migrate

## 6. (Opcional) Crie um superusuário

python manage.py createsuperuser

## 7. Inicie o servidor

python manage.py runserver

## 8. Acesse no navegador:

Quadro Kanban (interface): http://localhost:8000/

Admin do Django: http://localhost:8000/admin/

API RESTful: http://localhost:8000/api/
