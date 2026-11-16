-- TODO: renombra a marts_<tu_pregunta_de_negocio>.sql
-- Agrega el resultado de tu modelo intermedio en la pregunta final que tu proyecto necesita responder.
select
    TODO_columna_de_agrupacion,
    count(*) as TODO_alias
from {{ ref('int_TODO') }}
group by TODO_columna_de_agrupacion
