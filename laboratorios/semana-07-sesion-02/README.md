# Semana 7, Sesión 2: Repaso Medio Semestre

> Objetivo de la sesión: consolidar los conceptos de formulación de problemas e infraestructura de datos mediante preguntas dirigidas por ustedes mismos, y relacionar el concepto de contrato de datos con el pipeline de su propio proyecto.

**Lectura previa de esta sesión:** ["What Is a Data Contract?"](https://www.ibm.com/think/topics/data-contract), IBM Think.

**Referencia:** ["From Monolith to Contract-Driven Data Mesh"](https://towardsdatascience.com/from-monolith-to-contract-driven-data-mesh/), Towards Data Science.

Esta sesión no tiene un ejercicio de código nuevo. Es una guía de repaso: la llenas antes de la sesión, con tus propias preguntas sin resolver, y la usas durante la sesión para seguir el turno de preguntas y la discusión del cierre.

## Antes de la sesión: tu pregunta por categoría

Para cada categoría, escribe la pregunta concreta que todavía no puedes responder con seguridad, no una duda general. "No entendí bien Kestra" no se puede resolver en dos minutos; "no sé por qué mi flow no espera a que Postgres esté listo" sí.

Si una categoría ya te quedó completamente clara, escribe "sin pregunta" y seguimos a la siguiente en clase.

**Formulación de problemas (Semanas 1-2):**

_(tu pregunta, o "sin pregunta")_

**Contenedores e infraestructura como código (Semana 3):**

_(tu pregunta, o "sin pregunta")_

**Orquestación y calidad de datos (Semana 4):**

_(tu pregunta, o "sin pregunta")_

**Warehouse y modelado analítico (Semana 5):**

_(tu pregunta, o "sin pregunta")_

**Procesamiento batch y streaming (Semana 6):**

_(tu pregunta, o "sin pregunta")_

**Integración de principio a fin (Semana 7, Sesión 1):**

_(tu pregunta, o "sin pregunta")_

## Durante el turno de preguntas

Espacio para anotar, de las preguntas de tus compañeros, la que más te sirvió a ti también (la que resolvió algo que no habías anotado como tu propia pregunta):

_(tu respuesta)_

## Discusión complementaria, contrato de datos

**Antes de la discusión, a partir de la lectura:** según el artículo de IBM, ¿qué distingue a un contrato de datos de la documentación tradicional de un esquema?

_(tu respuesta)_

**Pregunta de la discusión:** ¿qué garantiza un contrato de datos entre el equipo que produce y el equipo que consume un pipeline, que una prueba de dbt corriendo en silencio no garantiza por sí sola?

_(tu respuesta, antes de la discusión en clase)_

**Después de la discusión, ¿qué agregarías o cambiarías de tu respuesta?**

_(tu respuesta)_

**Aplicado a tu propio proyecto:** de las pruebas `unique`/`not_null` que ya escribiste en el `schema.yml` de dbt (Semana 5, Sesión 2), elige una columna de tu warehouse cuyo significado exacto no queda claro solo con el nombre de la columna (¿una fecha en qué huso horario? ¿un monto con o sin impuesto?). Escribe, en una frase, la aclaración que le harías a alguien que fuera a consumir esa tabla sin haber visto tu código.

_(tu respuesta)_

## Antes de la próxima sesión

La próxima sesión es la Evaluación Medio Semestre. Repasa las seis categorías del mapa de repaso de esta sesión, con especial atención a las preguntas que anotaste arriba.
