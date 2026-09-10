# Práctica: API de un arsenal de ciberseguridad

## Contexto

Eres parte del equipo de una plataforma de entrenamiento para hackers éticos (_red team_). El equipo necesita una pequeña API para gestionar el **arsenal de herramientas de ciberseguridad** que se recomienda a los estudiantes según la fase del pentesting en la que se encuentren: reconocimiento, escaneo, explotación, post-explotación o defensa.

Tu tarea es construir esta API utilizando **únicamente** lo visto hasta ahora en el curso: una lista en memoria como "base de datos", parámetros de ruta, parámetros de query, el cuerpo de la petición como diccionario, manejo de errores con `HTTPException` y códigos de estado adecuados. No se requiere (ni se debe usar todavía) una base de datos real, modelos de Pydantic, ni ningún paquete externo adicional.

## Modelo de datos

Cada herramienta del arsenal debe representarse como un diccionario con, al menos, los siguientes campos:

- `id`: identificador numérico único de la herramienta.
- `name`: nombre de la herramienta (por ejemplo, Nmap, Metasploit, Wireshark, Burp Suite, John the Ripper).
- `category`: fase del pentesting a la que pertenece (por ejemplo, "Reconnaissance", "Scanning", "Exploitation", "Post-Exploitation" o "Defense").
- `description`: una breve descripción de para qué sirve la herramienta.

Al iniciar la aplicación, la lista debe venir precargada con al menos 5 herramientas de ejemplo, cubriendo distintas categorías.

## Requisitos funcionales

La API debe exponer los siguientes endpoints:

1. **Endpoint de bienvenida:** una ruta raíz que devuelva un mensaje de bienvenida junto con información del autor de la API.

2. **Listar herramientas:** un endpoint que devuelva todas las herramientas del arsenal. Debe aceptar un parámetro de query opcional que permita filtrar las herramientas cuyo nombre contenga el texto buscado (sin distinguir mayúsculas de minúsculas), de forma similar a como se hizo con el listado de animes.

3. **Obtener una herramienta por id:** un endpoint que reciba el `id` como parámetro de ruta y devuelva la herramienta correspondiente. Debe aceptar un parámetro de query opcional (por ejemplo, `include_description`) que decida si la respuesta incluye o no la descripción completa. Si el `id` no existe, debe responderse con un código de error adecuado indicando que la herramienta no fue encontrada.

4. **Crear una herramienta:** un endpoint que reciba en el cuerpo de la petición los datos de una nueva herramienta (`name`, `category` y `description`) y la agregue al arsenal, calculando automáticamente su `id`. Debe validar que los tres campos estén presentes y que ninguno esté vacío, devolviendo un error de petición inválida en caso contrario.

5. **Actualizar una herramienta:** un endpoint que reciba el `id` como parámetro de ruta y los nuevos datos en el cuerpo de la petición, reemplazando por completo los datos de la herramienta existente. Debe aplicar las mismas validaciones que la creación, y devolver un error si el `id` no existe.

6. **Eliminar una herramienta:** un endpoint que reciba el `id` como parámetro de ruta y elimine la herramienta correspondiente del arsenal, respondiendo sin contenido si la eliminación fue exitosa, o con un error si el `id` no existe.

## Criterios de validación y códigos de estado

- Todas las respuestas de error deben usar el código de estado HTTP que mejor represente la situación (por ejemplo, datos inválidos, recurso no encontrado).
- La creación y la actualización deben rechazar cuerpos de petición donde falte algún campo obligatorio o donde algún campo venga vacío o compuesto solo de espacios en blanco.
- La eliminación exitosa no debe devolver contenido en el cuerpo de la respuesta.

## Bonus (opcional)

- Agrega un parámetro de query adicional en el listado para filtrar las herramientas por `category`.
- Agrega un campo `difficulty` (por ejemplo, "Beginner", "Intermediate", "Advanced") a cada herramienta y permite filtrar por él también.
- Prueba todos los endpoints desde la documentación interactiva generada automáticamente por FastAPI, antes de dar la práctica por finalizada.
