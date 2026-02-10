from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from .database import Base, engine, SessionLocal
from .models import Note

Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_notes(request: Request, db: Session = Depends(get_db)):
    notes = db.query(Note).all()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "notes": notes}
    )

@app.post("/add")
def add_note(
    title: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db)
):
    note = Note(title=title, content=content)
    db.add(note)
    db.commit()
    return RedirectResponse("/", status_code=303)

@app.get("/edit/{note_id}")
def edit_page(note_id: int, request: Request, db: Session = Depends(get_db)):
    note = db.query(Note).get(note_id)
    return templates.TemplateResponse(
        "edit.html",
        {"request": request, "note": note}
    )

@app.post("/edit/{note_id}")
def edit_note(
    note_id: int,
    title: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db)
):
    note = db.query(Note).get(note_id)
    note.title = title
    note.content = content
    db.commit()
    return RedirectResponse("/", status_code=303)

@app.get("/delete/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).get(note_id)
    db.delete(note)
    db.commit()
    return RedirectResponse("/", status_code=303)
