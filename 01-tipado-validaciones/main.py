# BaseModel es la clase de Pydantic de la que heredan todos nuestros modelos
# de datos. Cada clase que hereda de BaseModel describe la forma de un JSON:
# qué campos tiene y de qué tipo debe ser cada uno.

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Posts API", version="1.0.0")

POSTS = [
    {
        "id": 1,
        "title": "Getting started with FastAPI",
        "content": "FastAPI uses Python type hints to validate, serialize and document your API automatically.",
    },
    {
        "id": 2,
        "title": "Why Pydantic matters",
        "content": "Pydantic turns plain type annotations into real runtime validation for request and response data.",
    },
    {
        "id": 3,
        "title": "Draft: async in Python",
        "content": "Notes about async/await and how ASGI servers handle concurrent requests.",
    },
]


# Modelo base: define los campos comunes a "crear" y "actualizar" un post.
# title y content son obligatorios porque no tienen valor por defecto;
# si faltan o no son str, Pydantic rechaza la petición antes de que
# el código de la función llegue a ejecutarse.
class PostBase(BaseModel):
    title: str
    content: str = "Valor por defecto"


# PostCreate hereda todos los campos de PostBase sin agregar nada nuevo.
# Se define como una clase aparte (en vez de usar PostBase directamente)
# para poder diferenciarla semánticamente y poder añadirle campos propios
# de "creación" en el futuro sin tocar PostBase ni PostUpdate.
class PostCreate(PostBase):
    pass


# Modelo independiente para actualizar. Aunque hoy tiene los mismos campos
# que PostBase, se define aparte para poder evolucionar el "update" (por
# ejemplo, hacer los campos opcionales) sin afectar la validación de "create".
class PostUpdate(BaseModel):
    title: str
    content: str | None = None


@app.get("/")
def home():
    return {"message": "Welcome to the Posts API", "author": "Francisco Nieto"}


@app.get("/posts")
def list_posts():
    return {"data": POSTS}


# Al declarar el parámetro "post" con el tipo PostCreate, le decimos a
# FastAPI que ese objeto debe venir del body de la petición (no de la URL
# ni de query params). FastAPI usa Pydantic para: leer el JSON del body,
# validar que tenga "title" y "content" como strings, y si algo falla,
# responder automáticamente con un 422 y el detalle del error, sin que
# esta función llegue siquiera a ejecutarse.
@app.post("/posts")
def create_post(post: PostCreate):

    new_id = (POSTS[-1]["id"] + 1) if POSTS else 1

    # post.title y post.content son atributos ya validados y tipados como
    # str (no simples claves de dict), gracias a que post es una instancia
    # de PostCreate.
    new_post = {
        "id": new_id,
        "title": post.title,
        "content": post.content,
    }

    POSTS.append(new_post)
    return {"message": "Created post successfully", "data": new_post}


@app.get("/posts/{post_id}")
def get_post(post_id: int):
    for post in POSTS:
        if post["id"] == post_id:
            return {"data": post}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


# Aquí conviven dos formas distintas de validación de FastAPI: post_id
# viene de la ruta (path param) y se valida solo con el type hint "int"
# (sin Pydantic, es una validación simple de FastAPI); data viene del
# body y se valida con el modelo PostUpdate, igual que en create_post.
@app.put("/posts/{post_id}")
def update_post(post_id: int, data: PostUpdate):

    for post in POSTS:
        if post["id"] == post_id:
            update_data = data.model_dump(exclude_unset=True)
            post.update(update_data)

            return {"message": "Updated post successfully", "data": post}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int):

    for index, post in enumerate(POSTS):
        if post["id"] == post_id:
            POSTS.pop(index)
            return

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
