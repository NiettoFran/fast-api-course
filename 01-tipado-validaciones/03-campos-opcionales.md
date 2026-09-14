# Campos opcionales y valores por defecto

Hasta ahora, en los modelos de este proyecto (`PostCreate`, `PostUpdate`) todos los campos son obligatorios: si `title` o `content` no vienen en el body, Pydantic rechaza la petición con un 422. Pero no todos los campos de una API tienen que ser obligatorios. Es común querer que un campo pueda omitirse y, si no se envía, se le asigne un valor por defecto (por ejemplo `published: bool = True`), o que directamente pueda no tener ningún valor y eso sea válido (por ejemplo un `tags` que puede ser `None` si el post todavía no tiene etiquetas).

## Dos conceptos distintos que se suelen confundir

Es importante separar dos ideas que a menudo se mezclan:

- **Campo opcional para enviar** (no es obligatorio incluirlo en el JSON): se logra dándole un **valor por defecto** al campo. Si el cliente no lo manda, Pydantic usa ese valor.
- **Campo que puede ser `None`**: se logra declarando el tipo como una unión con `None` (`str | None`). Esto no lo hace opcional de enviar por sí solo; solo dice que, si se envía, `None` es un valor válido además del tipo declarado.

En la práctica, casi siempre se combinan las dos cosas: un campo que acepta `None` **y además** tiene `None` como valor por defecto, para que también se pueda omitir del todo.

```python
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str
    published: bool = True        # opcional de enviar, valor por defecto True
    summary: str | None = None    # opcional de enviar y además puede ser None
```

Si se declarara `summary: str | None` sin el `= None`, el campo seguiría siendo **obligatorio**: habría que enviarlo explícitamente, aunque su valor fuera `null`. La única forma de hacerlo opcional de enviar es agregarle un valor por defecto.

## `Optional[X]` vs `X | None`

Antes de Python 3.10, la única forma de expresar "este valor puede ser de tipo X o puede ser `None`" era usando `Optional` del módulo `typing`:

```python
from typing import Optional

class Post(BaseModel):
    summary: Optional[str] = None
```

`Optional[str]` es, en realidad, solo un alias de `Union[str, None]`. Nunca significó "opcional" en el sentido de "no obligatorio"; el nombre es un poco engañoso porque mucha gente lo asocia con "puedo omitir este campo", cuando lo único que declara es que `None` es un valor aceptado además de `str`. Que el campo sea opcional de enviar depende, como se explicó arriba, de si tiene un valor por defecto (`= None`) o no.

A partir de Python 3.10 (PEP 604), el lenguaje incorporó una sintaxis nativa para expresar uniones de tipos usando el operador `|`, directamente sobre los tipos, sin necesidad de importar nada de `typing`:

```python
class Post(BaseModel):
    summary: str | None = None
```

Esta forma es equivalente en significado a `Optional[str] = None`: ambas dicen "este campo acepta un `str` o `None`, y si no se envía, vale `None`". La diferencia entre una y otra no es de comportamiento, sino de **sintaxis y de versión de Python soportada**:

| | `Optional[str]` | `str \| None` |
|---|---|---|
| Requiere importar | `from typing import Optional` | Nada (sintaxis del lenguaje) |
| Versión mínima de Python | Cualquiera (con `typing`) | 3.10 en adelante |
| Significado | `Union[str, None]` | `Union[str, None]` |
| Estado actual | Sigue funcionando, pero es la forma "antigua" | Forma recomendada hoy en día |

Pydantic (a partir de la versión 2, que es la que usa FastAPI actualmente) entiende ambas sintaxis exactamente igual, porque en tiempo de ejecución `str | None` produce el mismo objeto de tipo (`types.UnionType`) que representa una unión, y Pydantic sabe interpretar esa unión sin importar cómo se haya escrito. Por eso, en proyectos nuevos con Python 3.10+ (como el de este curso) se prefiere `str | None` por ser más corta, más legible y no requerir un import adicional. `Optional` sigue existiendo y se sigue viendo en código más antiguo o en proyectos que deben soportar versiones de Python anteriores a 3.10, pero para código nuevo la recomendación general es usar `|`.

## Ejemplo aplicado a este proyecto

Si quisiéramos que `PostUpdate` permitiera actualizar solo algunos campos (patrón habitual en un `PUT`/`PATCH` parcial), se vería así con la sintaxis moderna:

```python
class PostUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
```

Con este modelo, un cliente podría enviar `{"title": "Nuevo título"}` sin incluir `content`, y Pydantic construiría el objeto con `content=None`, en vez de rechazar la petición por faltar ese campo. Del lado del código de la ruta, hay que recordar entonces comprobar si cada campo llegó o no (por ejemplo, actualizando solo los campos que no sean `None`), porque ahora `None` puede significar tanto "el cliente quiere borrar el valor" como "el cliente no envió el campo", según cómo se diseñe la lógica de negocio.

## Resumen

- Un valor por defecto (`= algo`) es lo que hace que un campo sea opcional **de enviar**.
- `X | None` (o su equivalente antiguo `Optional[X]`) es lo que hace que un campo pueda **valer `None`**.
- `Optional[X]` y `X | None` significan exactamente lo mismo para Pydantic; la diferencia es solo de sintaxis y de la versión mínima de Python requerida (3.10+ para `|`).
- En código nuevo se prefiere `X | None` por ser más simple y no requerir importar `Optional` de `typing`.
