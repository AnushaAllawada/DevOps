# DevConnects

**DevConnects** is a responsive full-stack social media platform built for developers to connect, collaborate, and share knowledge.
It supports user profiles, posts, interactions, and a follow system — with a modern frontend and robust backend integrated through RESTful APIs.

## 🚀 Tech Stack

- **Frontend**: React.js, Tailwind CSS
- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **DevOps Tools**:GitHub Actions

---

## 🧩 Features

- Developer profile creation
- Post creation, likes, and comments
- Follow/unfollow system
- Mobile-responsive design
- JWT-based authentication and authorization
- RESTful API integration
- CI/CD setup using GitHub Actions

---

## 🐳 Local Setup (Using Docker)

```bash
# Clone the repository
git clone https://github.com/yourusername/devconnects.git
cd devconnects

# Build and start the containers
docker-compose up --build

# The app will run on http://localhost:3000 (React) and http://localhost:8000 (Django API)
