# <img src='img/ga4/logo_ga4.png' style='height:40px;width:auto'> GA4

<!--TOC-->

- [Admin](#admin)
  - [1. Properties](#1-properties)
    - [1.1 Subproperties](#11-subproperties)
  - [2. Data Collection](#2-data-collection)
    - [2.1 Data Streams](#21-data-streams)
  - [3. Data display](#3-data-display)
    - [3.1 Events](#31-events)
    - [3.2 Custom Dimensions](#32-custom-dimensions)

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

### 3. Data display

#### 3.1 Events
---

> **\> Admin \> Property Settings \> Data Display \> Events**

Docs

- [Google Drive Luis > Parameters, Dimensions and Metrics](https://docs.google.com/spreadsheets/d/1QlV_FyvvziEg-LXUa_8-Y0_i9y9H7T-a5zc0SG3oaUo/edit?gid=0#gid=0)

Types

- [Automatically collected events](https://support.google.com/analytics/answer/9234069?hl=en&ref_topic=9756175)
- [Enhanced measurement events](https://support.google.com/analytics/answer/9216061?hl=en&ref_topic=9756175): Son eventos de medición mejorados sobre la interacción con su contenido, y no hay que programar nada. Para habilitar / desabilitar estos eventos ir a las sección de admin en Data Streams
    - page_view
    - scroll
    - click

- [Recommended events](https://support.google.com/analytics/answer/9267735?hl=en&ref_topic=13367566&sjid=2826369473343199309-EU): Son eventos para el e-commerce y recomendadores
    - ad_impression
    - purchase
    - add_to_cart
- [Custom events](https://support.google.com/analytics/answer/12229021?hl=en&ref_topic=13367566&sjid=2826369473343199309-EU)


#### 3.2 Custom Dimensions
---

> **\> Admin \> Property Settings \> Data Display \> Custom definitions \> Custom dimensions**










