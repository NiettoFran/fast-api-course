<div align="center">

# ⚡ fast-api-course

### Ejercicios y proyectos del curso _"FastAPI: Crea APIs eficientes con Python"_

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=python&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-Auth-black?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![Render](https://img.shields.io/badge/Deploy-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)

APIs REST con Pydantic, SQLAlchemy/SQLModel, JWT, arquitectura en capas, async, websockets y webhooks

</div>

---

## 📖 Índice

- [Sobre este repo](#-sobre-este-repo)
- [Stack](#️-stack)
- [Estructura](#-estructura)
- [Temario cubierto](#-temario-cubierto)
- [Progreso](#-progreso)
- [Cómo correrlo localmente](#-cómo-correrlo-localmente)
- [Autor](#-autor)

---

## 📚 Sobre este repo

Repo de práctica donde voy siguiendo el curso de FastAPI, sección por sección, con el objetivo de sumar un stack de Python al que ya vengo manejando con **PHP/Laravel** para construir APIs. La idea es que quede como referencia para repasar conceptos y como base para proyectos propios más adelante (varios orientados a ciberseguridad).

## 🛠️ Stack

|     | Tecnología                     | Uso                         |
| --- | ------------------------------ | --------------------------- |
| 🐍  | **Python 3.11+**               | Lenguaje base               |
| ⚡  | **FastAPI** + Uvicorn          | Framework y servidor ASGI   |
| 🧩  | **Pydantic**                   | Validaciones y schemas      |
| 🗄️  | **SQLAlchemy** / **SQLModel**  | ORM                         |
| 🐘  | **PostgreSQL**                 | Base de datos               |
| 🔀  | **Alembic**                    | Migraciones                 |
| 🔐  | **JWT** (OAuth2PasswordBearer) | Autenticación               |
| 🔌  | **WebSockets**                 | Comunicación en tiempo real |
| ☁️  | **Render**                     | Deploy                      |

## 🗂️ Estructura

```
fast-api-course/
├── 00-introduccion/
├── 01-tipado-validaciones/
├── 02-validacion-de-parametros-y-queries/
├── 03-bases-de-datos/
├── 04-arquitectura-y-modularizacion/
├── 05-dependencias-seguridad-y-jwt/
├── 06-funciones-sincronas-y-asincronas/
├── 07-manejo-de-archivos/
├── 8-proyecto-tags/
├── 9-proyecto-users/
├── 10-proyecto-categorias/
├── 11-proyecto-seeds/
├── 12-middlewares/
├── 13-sqlmodel-modelos-y-schemas/
├── 14-sqlmodel-servicios-y-rutas/
├── 15-migraciones/
├── 16-bonus-websockets/
├── 17-bonus-webhooks/
└── README.md
```

## 📋 Temario cubierto

<details>
<summary><b>00 · 🎬 Introducción</b></summary>
<br>

Presentación del curso, instalaciones recomendadas y setup del entorno.

</details>

<details>
<summary><b>01 · 🧩 Tipado y validaciones</b></summary>
<br>

Modelos con Pydantic, validaciones automáticas y personalizadas, campos opcionales.

</details>

<details>
<summary><b>02 · 🔍 Validación de parámetros y queries</b></summary>
<br>

Path/query params, paginación, orden y metadatos de endpoints.

</details>

<details>
<summary><b>03 · 🗄️ Bases de datos</b></summary>
<br>

Conexión con SQLAlchemy, modelos declarativos, relaciones uno-a-muchos y muchos-a-muchos, PostgreSQL.

</details>

<details>
<summary><b>04 · 🏗️ Arquitectura y modularización</b></summary>
<br>

Separación en capas: modelos, schemas, repositories y routers (repository pattern).

</details>

<details>
<summary><b>05 · 🔐 Dependencias, seguridad y JWT</b></summary>
<br>

Dependencias de FastAPI, JWT, hash de contraseñas, rutas protegidas.

</details>

<details>
<summary><b>06 · ⏱️ Funciones síncronas y asíncronas</b></summary>
<br>

Diferencias entre sync/async, errores comunes.

</details>

<details>
<summary><b>07 · 📁 Manejo de archivos</b></summary>
<br>

Subida de archivos, límites de tamaño, servido de estáticos.

</details>

<details>
<summary><b>8 · 🏷️ Proyecto: Tags</b></summary>
<br>

CRUD de etiquetas, listado paginado, tag más popular.

</details>

<details>
<summary><b>9 · 👤 Proyecto: Users</b></summary>
<br>

Modelo de usuario, registro y login, roles y permisos.

</details>

<details>
<summary><b>10 · 🗂️ Proyecto: Categorías</b></summary>
<br>

Relación de posts con categorías, CRUD completo.

</details>

<details>
<summary><b>11 · 🌱 Proyecto: Seeds</b></summary>
<br>

Datos de prueba, hash y contextmanager, slugs.

</details>

<details>
<summary><b>12 · 🧱 Middlewares</b></summary>
<br>

CORS, logging, request ID, bloqueo de IPs, cálculo de tiempos de proceso.

</details>

<details>
<summary><b>13 · 📝 SQLModel: modelos y schemas</b></summary>
<br>

Modelos de usuario, notas, etiquetas y compartidos con SQLModel.

</details>

<details>
<summary><b>14 · 🔧 SQLModel: servicios y rutas</b></summary>
<br>

Servicios, dependencias y rutas del proyecto Devinote.

</details>

<details>
<summary><b>15 · 🔀 Migraciones</b></summary>
<br>

Migraciones de base de datos con Alembic.

</details>

<details>
<summary><b>16 · 🔌 Bonus: WebSockets</b></summary>
<br>

Chat en tiempo real con WebSockets.

</details>

<details>
<summary><b>17 · 🪝 Bonus: Webhooks</b></summary>
<br>

Verificación de firma, integración con GitHub y Discord.

</details>

## ✅ Progreso

| Módulo                                  | Estado |
| --------------------------------------- | ------ |
| 00 · Introducción                       | ⬜     |
| 01 · Tipado y validaciones              | ⬜     |
| 02 · Validación de parámetros y queries | ⬜     |
| 03 · Bases de datos                     | ⬜     |
| 04 · Arquitectura y modularización      | ⬜     |
| 05 · Dependencias, seguridad y JWT      | ⬜     |
| 06 · Funciones síncronas y asíncronas   | ⬜     |
| 07 · Manejo de archivos                 | ⬜     |
| 8 · Proyecto Tags                       | ⬜     |
| 9 · Proyecto Users                      | ⬜     |
| 10 · Proyecto Categorías                | ⬜     |
| 11 · Proyecto Seeds                     | ⬜     |
| 12 · Middlewares                        | ⬜     |
| 13 · SQLModel: modelos y schemas        | ⬜     |
| 14 · SQLModel: servicios y rutas        | ⬜     |
| 15 · Migraciones                        | ⬜     |
| 16 · Bonus: WebSockets                  | ⬜     |
| 17 · Bonus: Webhooks                    | ⬜     |

> Actualizo ⬜ → ✅ a medida que voy terminando cada módulo.

---

## 👤 Autor

<div align="center">

**Valentín Francisco Nieto** (Fran)

[![Portfolio](https://img.shields.io/badge/Portfolio-N--Tech_Studio-red?style=flat-square)](https://ntech.studio)
[![GitHub](https://img.shields.io/badge/GitHub-NiettoFran-181717?style=flat-square&logo=github)](https://github.com/NiettoFran)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-niettovale-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/niettovale)

</div>
