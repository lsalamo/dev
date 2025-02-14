# <img src='img/ga4/logo_ga4.png' style='height:40px;width:auto'> GA4

<!--TOC-->

- [Admin](#admin)
  - [1. Properties](#1-properties)
    - [1.1 Subproperties](#11-subproperties)
  - [2. Data Collection](#2-data-collection)
    - [2.1 Data Streams](#21-data-streams)
    - [2.2 Google Signals](#22-google-signals)
    - [2.3 Sessions](#23-sessions)
  - [3. Data display](#3-data-display)
    - [3.1 Events](#31-events)
    - [3.2 Custom Dimensions and Events](#32-custom-dimensions-and-events)
    - [3.3 User ID](#33-user-id)

<!--TOC-->

## Admin

### 1. Properties

#### 1.1 Subproperties
---

> **\> Admin \> Property Settings \> Property \> Subproperty management**

Una subpropiedad es una propiedad que recibe datos filtrados de una propiedad fuente.

> **IMPORTANTE:** Hay que crear los data streams antes validar los identificadores de web y apps.

Docs

- [List of dimensions you can use to configure filter conditions](https://support.google.com/analytics/answer/11526072?hl=en#dimensions&zippy=%2Clist-of-dimensions-you-can-use-to-configure-filter-conditions)

![alt text](img/ga4/subproperty-min.jpg)

Filters

- Measurement ID: Unique WebSite  ID of your web. 
> **Example:** G-6NE7MBSF9K
- GMP app ID: Unique Firebase application ID of your application
> **Example:** 1:200592347366:android:27f39a56993c94fd

![alt text](img/ga4/subproperty_web-min.jpg)
![alt text](img/ga4/subproperty_and-min.jpg)
![alt text](img/ga4/subproperty_ios-min.jpg)

### 2. Data Collection

#### 2.1 Data Streams
---

> **\> Admin \> Property Settings \> Data collection and modification \> Data streams**

- Cada propiedad de Google Analytics 4 puede tener hasta 50 data streams, que se pueden combinar entre data streams webs y apps.
- Genera un fragmento de código que agregas a tu aplicación o sitio para recopilar esos datos.
- Si elimina un flujo de datos, Analytics conserva los datos históricos, pero no se realiza ningún otro procesamiento de esos datos ni se pueden utilizar en filtros de informes.

> **IMPORTANTE:** Hay que consultar los "Firebase App ID" en la [consola de Firebase](https://console.firebase.google.com/).

![alt text](img/ga4/data_stream_web.jpg)
![alt text](img/ga4/data_steram_and.jpg)
![alt text](img/ga4/data_stream_ios.jpg)

#### 2.2 Google Signals
---

> **\> Admin \> Property Settings \> Data collection and modification \> Data colection \> Google signals data collection**

Completa los datos de los usuarios que acceden a un sitio web o una aplicación a través de dispositivos en los que han iniciado sesión en sus cuentas de Google y tienen habilitada la personalización de anuncios. Estos datos son demográficos, intereses, etc.

#### [2.3 Sessions](https://support.google.com/analytics/answer/9191807)
---

Google recopila automáticamente un evento "**session_start**" y genera un ID de sesión (**ga_session_id** - timestamp de cuando inicia la sesión) y un número de sesión (**ga_session_number** - número de sesiones que un usuario ha iniciado hasta la sesión actual) 


- **Session Timeout:** 30 minutos 
- **Engaged Session Timeout:** 10 segundos

Web

> **\> Admin \> Property Settings \> Data collection and modification \> Data streams \> Configure tag settings \> Adjust session timeout**

[Android](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setSessionTimeoutDuration(long))

```js
// El valor predeterminado es 1800000 (30 minutos).
FirebaseAnalytics.getInstance(this).setSessionTimeoutDuration(1800000); 
```
[iOS](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Classes/Analytics#setsessiontimeoutinterval_:)

```js
// El valor predeterminado es 1800 segundos (30 minutos).
Analytics.setSessionTimeoutInterval(1800) 
```

### 3. Data display

#### 3.1 Events
---

> **\> Admin \> Property Settings \> Data Display \> Events**

- Collect: Desde aquí se muestran todos los eventos que llegan a través de todos los "Data Streams"
- Analyse: Si se quiere usar estos eventos para analizarlos debemos crear "Custom Events"

Docs

- [Google Drive Luis > Parameters, Dimensions and Metrics](https://docs.google.com/spreadsheets/d/1QlV_FyvvziEg-LXUa_8-Y0_i9y9H7T-a5zc0SG3oaUo/edit?gid=0#gid=0)

Types

- [Automatically collected events:](https://support.google.com/analytics/answer/9234069?hl=en&ref_topic=9756175) Son eventos que GA4 se recopilan automáticamente sin ninguna configuración adicional.
    - page_view: Triggered when a user views a page
    - first_visit: Recorded on a user's first visit to the site
    - session_start: Marks the beginning of a user session
- [Enhanced measurement events:](https://support.google.com/analytics/answer/9216061?hl=en&ref_topic=9756175) Son eventos que GA4 se recopilan automáticamente cuando se habilita la medición mejorada en la sección de configuación "Data Streams"
    - file_download
    - scroll
    - click

- [Recommended events:](https://support.google.com/analytics/answer/9267735?hl=en&ref_topic=13367566&sjid=2826369473343199309-EU) Son eventos que implementas, pero que tienen nombres y parámetros predefinidos por GA4 en función de tu industria o negocio. Estos eventos desbloquean capacidades de generación de informes existentes y futuras.
    - ad_impression
    - purchase
    - add_to_cart
- [Custom events:](https://support.google.com/analytics/answer/12229021?hl=en&ref_topic=13367566&sjid=2826369473343199309-EU) Son eventos que usted define. Asegúrese de crear eventos personalizados únicamente cuando ningún otro evento funcione para su caso de uso.
    - Ad Replied Email
    - Ad Phone Called
    - Ad Deleted

#### [3.2 Custom Dimensions and Events](https://support.google.com/analytics/answer/14240153)
---

> **\> Admin \> Property Settings \> Data Display \> Custom definitions \> Custom dimensions / Custom metrics**

Steps

1. **Code:** Añades un evento con sus parametros o propiedades de usuario a tu código web o app.

2. **Collect:** Usuario visita tu web o app y la data es enviada a GA4

3. **Configuration:** Creamos "custom dimensions or metrics" para analizar la data. 

4. **Analyze:** Después de 24-48 horas tienes la data disponible para analizar. 

Custom Dimensions Types

- User-scoped custom dimensions: para informar de "user properties"

- Event-scoped custom dimensions: para informar de "event parameters"

- Item-scoped custom dimensions: para informat de "ecommerce parameters"

> **IMPORTANTE:** La creación de una dimensión personalizada con una gran cantidad de valores únicos puede afectar negativamente a sus informes. 

Custom Metrics Types

- Custom metrics: Le permite analizar valores numéricos de los parámetros del evento

- Calculated metrics: Le permite combinar una o más métricas existentes y/o métricas personalizadas para producir una métrica nueva y potencialmente más valiosa.

Limits

| Types of custom dimension   |      Standard property      |  360 property |
|----------|:-------------:|------:|
| User-scoped custom dimensions | 25 | 100 |
| Event-scoped custom dimensions | 50 | 125 |
| Item-scoped custom dimensions | 10 | 25 |
| Custom metrics | 50 | 125 |
| Calculated metrics | 5 | 50 |

#### [3.3 User ID](https://support.google.com/analytics/answer/10976610)
---

> **\> Admin \> Property Settings \> Data Display \> Reporting Identity**

Google Analytics mide a los usuarios en distintos dispositivos y plataformas

- **User-ID:** Identificaciones persistentes para usuarios que iniciaron sesión. Es el más preciso, porque utiliza datos que usted recopila para identificar a sus usuarios.
> **Example:** sdrn:coches.net:user:12151777

- **Device ID:** Analytics también puede utilizar el ID del dispositivo como espacio de identidad. En los sitios web, el ID del dispositivo obtiene su valor del "**client ID (first party cookie "_ga")**". En las aplicaciones, el ID del dispositivo es el "**app-instance-ID**".

- **Modeling:** GA4 se basa en el aprendizaje automático para modelar los datos del usuario para aquellos usuarios que se niegan a dar su consentimiento para compartir sus datos.

Types

- **Blended:** User-ID > device ID > modeling.
- **Observed:** User-ID > device ID. 
- **Device based:** device ID e ignora los otros

![alt text](img/ga4/reporting_identity.jpg)



CONSENT MODE

analytics_storage='denied'
analytics_storage='granted'


BIGQUERY -> RAW DATA --> EVENTOS SIN PROCESAR
- Cuando desee obtener resultados más precisos de sus datos sin procesar, vea los resultados en BigQuery.
- Cuando desee resultados más eficientes, visualice los resultados en sus informes estándar y personalizados y en Explorations y Looker Studio.






