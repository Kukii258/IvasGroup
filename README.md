# IvasGroup 🎤🎥🏟️

**IvasGroup** is a sleek, modern website for a professional event production company. The platform showcases the firm’s broad range of services, past work, and contact information. From concerts to TV broadcasting, the site offers a visual and informative experience for potential clients.

## 🌟 Features

### 🔹 Home Page
- Full-width **image slider** with 8 curated images, each representing a service segment:
  - Concerts
  - Conferences
  - TV Production
  - Sports Events
  - Corporate Events
  - Exhibitions
  - Fashion Shows
  - Touring

- **Who We Are**: Introduction to the IvasGroup story and company values  
- **Our Services**: Summary of key offerings across industries  
- **Our Equipment**: Overview of professional-grade gear used in event production  

### 🖼️ Gallery
A filterable image gallery featuring real project snapshots.
- Filters include:
  - All
  - Corporate Events
  - Concert and Touring
  - Sporting Events
  - Fashion Events
  - Exhibitions
  - TV Broadcasting

### 🧑‍💼 About Us
- Company background and mission  
- Profiles of team members and leadership  

### 📬 Contact Page
- Contact form that auto-sends email to the team  
- Company info and address  
- Embedded interactive map  

---

## ⚙️ Tech Stack

- **Python / Django**
- **PostgreSQL**
- **HTML + Tailwind CSS / Sass**
- **JavaScript**
- **Celery** (for async tasks)
- **Docker** and **Heroku** support via Cookiecutter Django

---

## 🚀 Getting Started

To run the app locally:

```bash
git clone https://gitlab.com/your-user/ivasgroup.git
cd ivasgroup
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Create a superuser:

```bash
python manage.py createsuperuser
```

---

## 🔄 Development & Tools

### Type Checks

```bash
mypy ivasgroup
```

### Running Tests

```bash
pytest
coverage run -m pytest
coverage html
open htmlcov/index.html
```

### Celery Workers

```bash
celery -A config.celery_app worker -l info
```

### Periodic Tasks

```bash
celery -A config.celery_app beat
```

---

## 📦 Deployment

### Docker

Full [Docker setup guide here](https://cookiecutter-django.readthedocs.io/en/latest/3-deployment/deployment-with-docker.html)

### Heroku

See [Heroku deployment guide](https://cookiecutter-django.readthedocs.io/en/latest/3-deployment/deployment-on-heroku.html)

---

## 📄 License

MIT

---

## 👥 Author

**Luka Kukelj**  
[GitLab Profile](https://gitlab.com/kukelj.luka)
