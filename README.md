## ☑️ Task-Manager: A Modern Django Task Management Application

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.13.7-blue?logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Django-5.2.5-06402B?logo=django&logoColor=white" />
    <img src="https://img.shields.io/badge/Bootstrap-5.3.8-7952B3?logo=bootstrap&logoColor=white" />
    <img src="https://img.shields.io/badge/HTMX-2.0.7-7952B3?logo=htmx&logoColor=white" />
    <img src="https://img.shields.io/badge/Hyperscript-0.9.14-7952B3?logo=htmx&logoColor=white" />
    <img src="https://img.shields.io/badge/JavaScript-BA8E23?logo=javascript&logoColor=white" />
    <img src="https://img.shields.io/badge/SQLite-dev-cyan?logo=sqlite&logoColor=white" />
    <img src="https://img.shields.io/badge/PostgreSQL-18-blue?logo=postgresql&logoColor=white" />
    <img src="https://img.shields.io/badge/Docker-28.5.2-blue?logo=docker&logoColor=white" />
</p>

---

## 📖 Overview

**Task-Manager** is a full-stack Django web application designed as a modern task management system. It delivers a seamless, interactive user experience powered by **HTMX** for dynamic content loading. Users can create, update, and manage projects and tasks in a responsive, mobile-friendly interface.

---

## ⚡ Features

- **Projects**
  - Create, update, delete projects
  - Dynamic project counters and details with HTMX
- **Tasks**
  - Add, edit, delete, mark as complete
  - Set task priority (Low, Medium, High)
  - Optional due dates
  - Live updates of task lists and counters
- **Interactive UI**
  - HTMX-powered modals for creating/updating projects and tasks
  - Responsive design with Bootstrap 5
- **Database**
  - Supports SQLite (development) and PostgreSQL (production)
- **Dockerized**
  - Full Docker Compose setup for app + PostgreSQL
- **Testing & Linting**
  - Ruff linter configured
  - Automated Django unit tests for projects and tasks

---

## 🛠️ Tech Stack

- **Backend:** Django 5.2.5  
- **Frontend:** Bootstrap 5.3.8, HTMX 2.0.7, Hyperscript 0.9.14, Vanilla JS  
- **Database:** SQLite (dev), PostgreSQL 18 (prod)  
- **Containerization:** Docker & Docker Compose  
- **Code Quality:** Ruff linter, automated Django tests  

---

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/task-manager.git
cd task-manager
```

### 2. Environment Variables
```env
DEBUG=True
SECRET_KEY=your-secret-key
POSTGRES_DB=taskmanager_db
POSTGRES_USER=taskmanager_user
POSTGRES_PASSWORD=taskmanager_pass
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
```

### 3. Using Docker
```bash
docker compose up --build
```

### 4. Using Virtual Environment (Optional)

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
# in settings.py comment postgres config and uncomment sqlite config; optionally run single postgres docker service
python manage.py migrate
python manage.py runserver

```

### 🧪 Running Tests

```bash
# Django tests
python manage.py test

# Ruff linter
ruff check 
```

### 📂 Project Structure

```
.
├── apps/
│   ├── accounts/
│   └── tasks/
├── compose.yaml
├── core/
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── Dockerfile
├── manage.py
├── pyproject.toml
├── README.md
├── requirements.txt
├── static/
└── templates/
    ├── account/
    ├── _base.html
    └── includes/

```

### ⚙️ Usage

- Register or log in.
- Create projects and tasks.
- Set priorities and due dates for tasks.
- Tasks and projects update dynamically without page reloads.
- Use modals to quickly edit tasks/projects.