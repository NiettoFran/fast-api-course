from fastapi import Body, FastAPI, HTTPException, Query, status

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
def get_anime(
    anime_id: int,
    include_description: bool | None = Query(
        default=None,
        description="Flag to decide whether or not to include the anime description.",
    ),
):
    for anime in ANIMES_LIST:
        if anime["id"] == anime_id:
            if include_description:
                return {"data": anime}

            return {"data": {"id": anime["id"], "title": anime["title"]}}

    return {"error": "Anime Not Found"}


@app.post("/animes")
def create_anime(anime: dict = Body(...)):

    if "title" not in anime or "description" not in anime:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The title and description are mandatory",
        )

    if not str(anime["title"]).strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The title cannot be empty",
        )

    if not str(anime["description"]).strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The description cannot be empty",
        )

    new_id = (ANIMES_LIST[-1]["id"] + 1) if ANIMES_LIST else 1

    new_anime = {
        "id": new_id,
        "title": anime["title"],
        "description": anime["description"],
    }

    ANIMES_LIST.append(new_anime)

    return {"message": "Created anime"}


@app.put("/animes/{anime_id}")
def update_anime(anime_id: int, data: dict = Body(...)):

    if "title" not in data or "description" not in data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The title and description are mandatory",
        )

    if not str(data["title"]).strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The title cannot be empty.",
        )

    if not str(data["description"]).strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The description cannot be empty.",
        )

    for anime in ANIMES_LIST:
        if anime_id == anime["id"]:
            anime["title"] = data["title"]
            anime["description"] = data["description"]

            return {"message": "Updated anime successfully", "data": anime}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Anime Not Found")


@app.delete("/animes/{anime_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_anime(anime_id: int):

    for index, anime in enumerate(ANIMES_LIST):
        if anime["id"] == anime_id:
            ANIMES_LIST.pop(index)
            # return {"message": "Deleted anime successfuly"}
            return

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Anime Not Found")
