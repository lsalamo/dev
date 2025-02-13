# GOOGLE

## BigQuery

### [Storage Princing](https://cloud.google.com/bigquery/pricing#storage)

En los primeros 90 días, las tablas se consideran «activas», y si no se utilizan durante >90 días, se consideran dentro del almacenamiento «a largo plazo». Existen diferentes formas de almacenar los datos: física y lógica. En la mayoría de los casos, el 'lógico' es más barato, mientras que no hay desventajas reales de lo que es posible hacer con los datos. Por lo tanto, recomendaría cambiar el almacenamiento a físico para todos ellos para ahorrar potencialmente un poco.

### [Compute Princing](https://cloud.google.com/bigquery/pricing#bigquery-pricing)

Esto cuesta 6,25 $ por TiB (~1100 GB), mientras que 1TiB al mes es gratuito. Al realizar consultas, siempre verás el tamaño de la consulta en la parte superior derecha cuando trabajes en la interfaz de usuario de BQ, por lo que cada consulta que se ejecute puede «validarse» antes en términos de costes. Por lo tanto, todos los que trabajan con BQ deben ser conscientes de los tamaños de consulta y su impacto en los costes. He comprobado los tamaños de las tablas para cada exportación GA4 (ver más abajo), y como puedes ver, la mayoría de las tablas no son tan grandes y por lo tanto, las consultas deberían ser regularmente bastante asequibles.

No tengo acceso a todos los informes de facturación de los proyectos, ya que no somos propietarios del contrato, pero permítanme tomar el proyecto infojobs-android-push como ejemplo (ver captura de pantalla y enlace): Como se puede ver, se puede ver un informe de costes y dividir las entradas por SKU (= storage & queries). La mayoría de los costes están siendo generados actualmente (mes actual) por el almacenamiento activo y a largo plazo (= 47,08 $ + 35,50 $), Análisis (= queries) = 1,64 $ y Streaming Export (= 9,33 $). La exportación de streaming sólo pareció estar activada durante 4 días y está desactivada de nuevo desde hoy temprano.

En teoría, existe la posibilidad de establecer cuotas de usuario para limitar la generación de costes por usuario o por proyecto. Por ejemplo, podría limitar las consultas a $X por día en el proyecto seleccionado y podría limitar los costes a una cantidad específica.


- cochesnet-c77b9
recomendación: cambiar el almacenamiento a físico
tamaño aproximado de la tabla para 1 día: 34 GB
es-motosnet: sin acceso
- milanuncios-618c8
recomendación: cambiar almacenamiento a físico
tamaño aproximado de la tabla para 1 día: 140 GB
- api-project-329785109876 (fotocasa):
recomendación: cambiar almacenamiento a físico
tamaño aproximado de la tabla para 1 día: 46 GB
- infojobs-android-push:
recomendación: cambiar almacenamiento a físico
tamaño aproximado de la tabla para 1 día: 90 GB




## CON CONSENTIMIENTO

### IMPLEMENTACION BASICA

Procesamiento: Los datos son utilizados para medir conversiones, analizar clics, sesiones, interacciones y comportamiento del usuario. 

#### VARIABLES

- Dirección IP: utilizada para fines de geolocalización y ajuste de región de privacidad. 

“Dirección IP y geolocalización inicial:
Cuando el consentimiento es rechazado (ad_storage='denied' o analytics_storage='denied'), las direcciones IP no se almacenan.
Sin embargo, se utilizan temporalmente para establecer la conexión y determinar la ubicación geográfica general del usuario (como país o ciudad).
La dirección IP se elimina inmediatamente después de que se complete este proceso, garantizando que no se almacene ni se registre.
Nivel de geolocalización en GA4:

GA4 utiliza la información derivada de la dirección IP para proporcionar datos de geolocalización a nivel de país y ciudad.
No se ofrece un nivel más granular (como barrio), y los datos no permiten identificar directamente a usuarios individuales.”

- Identificadores únicos: 
    - IDFA (Identifier for Advertisers en dispositivos Apple). 
    - GAID (Google Advertising ID en dispositivos Android).

- Tipo de dispositivos: movil, ordenador, etc

- Marca de tiempo de la visita

- Resolucion de la pantalla

- Informacion sobre el estado del consentimiento "denied"


**WEB**

- url
    - GCLID (Google Click Identifier)
    - DCLID (DoubleClick Identifier) 

- cookies: Las cookies y datos relacionados se almacenan en el navegador del usuario y cumplen con los períodos de retención del GDPR. 

    - Cookies analíticas (e.g., _ga, _gid). 
    - Cookies publicitarias (e.g., gac, IDE). 

- User Agent: Informacion sobre el navegador y sistema operativo

### IMPLEMENTACION AVANZADA

- Eventos clave adicionales: 
    - Duración de la sesión. 
    - Secuencias de clics. 
    - Conversiones específicas del anunciante (e.g., completación de formularios). 

- Procesamiento: Los datos son procesados completamente para análisis detallados, atribución avanzada y segmentación de usuarios. 
- Almacenamiento: Igual que en la implementación básica, pero puede incluir datos personalizados para objetivos específicos del anunciante. 

## SIN CONSENTIMIENTO

### IMPLEMENTACION BASICA

- Datos Recogidos: No se recopila información identificable ni cookies. 
- Procesamiento: No se realiza ningún procesamiento. 
- Almacenamiento: Ninguna información es almacenada. 

### IMPLEMENTACION AVANZADA

Información técnica básica:
- URL completa sin incluir cookies ni identificadores
- Parámetros de clic en anuncios (GCLID/DCLID). 
- Marca de tiempo de la visita. 
- User-agent (información sobre el navegador y sistema operativo). 
- Tipo de dispositivo (e.g., móvil, ordenador). 
- Resolución de pantalla. 
- Indicadores booleanos sobre el estado del consentimiento (e.g., "denied"). 
- Dirección IP: utilizada únicamente para geolocalización inicial y eliminada inmediatamente tras el proceso técnico. 

Procesamiento: 
- Los pings sin cookies se utilizan para modelizar métricas agregadas y anonimizadas, como tasas de conversión aproximadas. 

Almacenamiento: No se almacenan cookies ni identificadores personales. 


