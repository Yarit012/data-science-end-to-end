-- TODO: renombra a int_<tu_transformacion>.sql
-- Aplica aqui una transformacion o un join que combine mas de una tabla de staging,
-- usando ref() para referenciar los modelos de staging, nunca el nombre de la tabla cruda.
select
    TODO
from {{ ref('stg_TODO') }}
