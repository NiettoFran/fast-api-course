from fastapi import FastAPI

app = FastAPI(title="Fist App")

ANIMES_LIST = [
    {
        "id": 1,
        "title": "Black Clover",
        "description": "Asta, a boy born without magic in a world where magic is everything, fights to become the Wizard King alongside his rival Yuno.",
    },
    {
        "id": 2,
        "title": "One Piece",
        "description": "Monkey D. Luffy and his pirate crew sail the Grand Line in search of the legendary treasure known as One Piece.",
    },
    {
        "id": 3,
        "title": "DanDaDan",
        "description": "A skeptic and a believer in the paranormal team up after encountering both ghosts and aliens, gaining strange powers along the way.",
    },
    {
        "id": 4,
        "title": "Solo Leveling",
        "description": "Sung Jin-Woo, the weakest hunter in a world invaded by monsters, gains the unique ability to level up without limits.",
    },
    {
        "id": 5,
        "title": "Blue Lock",
        "description": "Japan's top young strikers are gathered in the Blue Lock program to develop the most egotistical striker who can lead the national team to win the World Cup.",
    },
]


@app.get("/")
def home():
    return {
        "message": "Welcome to my first app developed with FastAPI. Author: Francisco Nietto"
    }


@app.get("/animes")
def get_animes():
    return {"data": ANIMES_LIST}
