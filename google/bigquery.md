# <img src='img/bigquery/logo.png' style='height:40px;width:auto'> BigQuery

<!--TOC-->

- [1. Storage Princing](#1-storage-princing)
- [2. Compute Princing](#2-compute-princing)

<!--TOC-->

## [1. Storage Princing](https://cloud.google.com/bigquery/pricing#storage)

Tipos de tablas
___

- **Activo:** incluye todas las particiones de tablas y tablas que se hayan modificado en los últimos 90 días.
- **A largo plazo:** incluye cualquier tabla o partición de tabla que no se haya modificado durante >90 días. El precio de almacenamiento de esa tabla se reduce automáticamente en alrededor de un 50 %. No hay ninguna diferencia en el rendimiento, la durabilidad o la disponibilidad entre el almacenamiento activo y a largo plazo.

Tipo de almacenamiento
___

La elección del modelo afecta los precios de almacenamiento, pero no el rendimiento de las consultas

- **Almacenamiento lógico:** Se refiere a los datos no comprimidos.

- **Almacenamiento físico:** Son los datos comprimidos tal como se almacenan en disco.

## [2. Compute Princing](https://cloud.google.com/bigquery/pricing#bigquery-pricing)

Esto cuesta 6,25 $ por TiB (~1100 GB), mientras que 1TiB al mes es gratuito. Al realizar consultas, siempre verás el tamaño de la consulta en la parte superior derecha cuando trabajes en la interfaz de usuario de BQ

En teoría, existe la posibilidad de establecer cuotas de usuario para limitar la generación de costes por usuario o por proyecto. Por ejemplo, podría limitar las consultas a $X por día en el proyecto seleccionado y podría limitar los costes a una cantidad específica.
