# 📝 FastAPI Notes App

A sleek, lightweight, and efficient Notes Application built with **FastAPI**, **SQLAlchemy**, and **Jinja2 Templates**. This project demonstrates a full CRUD (Create, Read, Update, Delete) functionality with a clean SQLite backend.

---

## 🚀 Features

- **Create**: Quickly add new notes with a title and content.
- **Read**: View all your saved notes in a clean list format.
- **Update**: Edit existing notes to keep your information up to date.
- **Delete**: Remove notes with a single click.
- **Fast Performance**: Built on top of FastAPI for lightning-fast response times.
- **Simple UI**: Minimalist design using Jinja2 templates for a distraction-free experience.

---

## 🛠️ Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: [SQLAlchemy](https://www.sqlalchemy.org/) with SQLite
- **Templating**: [Jinja2](https://palletsprojects.com/p/jinja/)
- **Server**: [Uvicorn](https://www.uvicorn.org/)

---

## 📁 Project Structure

```text
fastapi-notes/
├── app/
│   ├── database.py    # Database configuration & session setup
│   ├── main.py        # FastAPI routes and application logic
│   └── models.py      # SQLAlchemy database models
├── static/
│   └── style.css      # Custom styling (CSS)
├── templates/
│   ├── base.html      # Base HTML layout
│   ├── index.html     # Homepage (List & Add Notes)
│   └── edit.html      # Edit Note page
├── main.py            # Entry point script
├── requirements.txt   # Project dependencies
└── notes.db           # SQLite database (generated at runtime)
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/fastapi-notes.git
cd fastapi-notes
```

### 2. Create a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install fastapi sqlalchemy jinja2 uvicorn python-multipart
```

---

## 🏃 Project Execution

To start the development server, run:

```bash
uvicorn app.main:app --reload
```

The application will be available at:
- **Web App**: `http://127.0.0.1:8000`
- **Interactive API Docs (Swagger)**: `http://127.0.0.1:8000/docs`

---

## 🧪 API Documentation

FastAPI automatically generates documentation for all your endpoints. You can explore and test the API directly from your browser:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have any improvements or new features in mind.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
