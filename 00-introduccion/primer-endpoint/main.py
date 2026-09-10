from fastapi import FastAPI, Query

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
        "message": "Welcome to my first app developed with FastAPI.",
        "author": "Francisco Nieto",
    }


@app.get("/animes")
def list_animes(
    query: str | None = Query(default=None, description="Text to filter anime")
):
    if query:
        # Without list comprehension
        # results = []

        # for anime in ANIMES_LIST:
        #     if query.lower() == anime["title"].lower():
        #         results.append(anime)

        # With list comprehension
        results = [
            anime for anime in ANIMES_LIST if query.lower() in anime["title"].lower()
        ]

        return {"data": results, "query": query}
    return {"data": ANIMES_LIST}


@app.get("/animes/{anime_id}")
def get_anime(anime_id: int):
    data = [anime for anime in ANIMES_LIST if anime["id"] == anime_id]

    if len(data) == 0:
        return {"error": "Anime Not Found"}
    return {"data": data[0]}
