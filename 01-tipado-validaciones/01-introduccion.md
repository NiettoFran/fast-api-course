# Pydantic

## ¿Qué es?

Pydantic es una librería de Python que permite definir la "forma" de tus datos usando clases normales de Python (con **type hints**), y a partir de esa definición:

- Valida que los datos recibidos cumplan esos tipos.
- Convierte tipos compatibles automáticamente (ej. un `"123"` a `int` si el campo es `int`).
- Lanza errores claros y detallados cuando algo no cumple lo esperado.
- Serializa/deserializa esos datos hacia y desde JSON, dicts, etc.

FastAPI usa Pydantic internamente para todo lo relacionado con el body de las peticiones, las respuestas y la generación automática de documentación (Swagger/OpenAPI).

## ¿Para qué se usa?

En una API, necesitas asegurarte de que los datos que llegan (body de un POST, PUT, etc.) tienen la forma correcta antes de trabajar con ellos. Por ejemplo, si esperas un `title: str` y un `content: str`, no quieres que el cliente te mande un número donde va el título, o que se le olvide mandar el campo.

Con Pydantic, defines un modelo (una clase que hereda de `BaseModel`) declarando los campos y sus tipos, y la validación ocurre sola cuando FastAPI recibe la petición y construye ese modelo.

```python
from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str
```

Cuando FastAPI recibe un POST con este modelo como parámetro, automáticamente:

1. Lee el JSON del body.
2. Verifica que existan `title` y `content`.
3. Verifica que ambos sean strings (o los convierte si es razonable).
4. Si algo falla, responde con un error 422 explicando exactamente qué campo falló y por qué.
5. Si todo está bien, te entrega un objeto `PostCreate` con atributos `post.title` y `post.content`, ya validados.

## Ventajas frente a validar "a mano"

Validar a mano normalmente se ve así:

```python
def create_post(data: dict):
    if "title" not in data or not isinstance(data["title"], str):
        raise HTTPException(status_code=422, detail="title inválido")
    if "content" not in data or not isinstance(data["content"], str):
        raise HTTPException(status_code=422, detail="content inválido")
    # ... y así con cada campo
```

Comparado con eso, Pydantic ofrece:

- **Menos código repetitivo**: declaras el tipo una vez y la validación se genera sola, en vez de escribir un `if` por cada campo y cada regla.
- **Mensajes de error consistentes**: todos los errores de validación tienen el mismo formato (código, campo, tipo esperado), en vez de mensajes distintos según quién escribió cada validación manual.
- **Documentación automática**: FastAPI usa el modelo para generar el esquema OpenAPI/Swagger, así que la documentación de la API nunca se desincroniza del código.
- **Autocompletado y chequeo de tipos**: como `post.title` es un atributo real con tipo `str`, tu editor te ayuda con autocompletado y herramientas como `mypy` pueden detectar errores antes de ejecutar el código.
- **Conversión de tipos**: convierte automáticamente tipos "razonables" (ej. `"5"` a `int`), algo que a mano habría que programar caso por caso.
- **Reutilización**: los modelos se pueden heredar y componer (como hace `PostCreate` heredando de `PostBase` en este proyecto), evitando duplicar definiciones.

## Desventajas / cosas a tener en cuenta

- **Curva de aprendizaje**: hay que entender cómo funcionan los modelos, la herencia entre ellos, y en proyectos más avanzados cosas como `Field`, validadores personalizados (`@field_validator`), etc.
- **Menos control fino "a simple vista"**: para validaciones muy específicas o lógicas de negocio complejas, a veces hay que combinar Pydantic con validadores personalizados, lo que añade una capa extra de conceptos.
- **Dependencia externa**: agregas una librería más al proyecto (aunque en el ecosistema FastAPI es prácticamente un estándar, no una opción externa rara).
- **Rendimiento**: la validación automática tiene un costo en tiempo de ejecución comparado con no validar nada, aunque normalmente es despreciable frente a los beneficios en seguridad y mantenibilidad.
- **Rigidez inicial**: si los datos de entrada son muy variables o poco estructurados, definir un modelo fijo puede sentirse más restrictivo que trabajar con un `dict` libre (aunque esa "libertad" es justo lo que causa bugs en producción).

## Ejemplo 1: validación básica de tipos

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

# Esto funciona: "30" se convierte automáticamente a int
user = User(name="Ana", age="30")
print(user.age)  # 30 (int, no str)

# Esto lanza un error de validación (ValidationError)
user_invalido = User(name="Ana", age="no soy un número")
```

## Ejemplo 2: campos opcionales con valores por defecto

```python
from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    title: str
    content: str
    published: bool = True          # valor por defecto
    tags: Optional[list[str]] = None  # opcional, puede no venir

post = Post(title="Hola", content="Mi primer post")
print(post.published)  # True (no hacía falta enviarlo)
print(post.tags)       # None
```
