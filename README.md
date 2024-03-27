# Portafolio basado en Reflex para programadores, dinamico con archivo json


[![Reflex](https://img.shields.io/badge/Reflex-0.4.5+-5646ED?style=for-the-badge&logo=reflex&logoColor=white&labelColor=101010)](https://reflex.dev)

[![HTML](https://img.shields.io/badge/HTML-orange?style=for-the-badge&logo=html5&logoColor=white&labelColor=101010)](https://developer.mozilla.org/es/docs/Web/HTML)
[![CSS](https://img.shields.io/badge/CSS-blue?style=for-the-badge&logo=css3&logoColor=white&labelColor=101010)](https://developer.mozilla.org/es/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-yellow?style=for-the-badge&logo=javascript&logoColor=white&labelColor=101010)](https://developer.mozilla.org/es/docs/Web/JavaScript)

## Plantilla de portafolio web minimalista configurable a nivel gráfico y de contenido.

Desarrollado utilizando [Python](https://python.org) y [Reflex](https://reflex.dev), disponible para desplegar de forma estática (HTML, CSS, JS).

#### Proyecto basado en el proyecto realizado durante emisiones en directo desde [Twitch](https://twitch.tv/mouredev)

## Proyecto

Plantilla web para programadores desarrollada con la premisa de crear el "portafolio perfecto", con todas las secciones e información fundamental.

<a href="./demo.png"><img src="./demo.png" style="height: 50%; width:50%;"/></a>

* Avatar y datos principales
* Información de contacto, CV y redes
* Sobre mí
* Tecnologías
* Experiencia
* Proyectos
* Formación
* Extra

## Instalación

Puedes seguir la [guía oficial](https://reflex.dev/docs/getting-started/installation/) de Reflex.

`python3 -m venv .venv`

`source .venv/bin/activate`

`pip install reflex`

`reflex init`

`reflex run`

## Configuración

Principalmente puedes configurar el contenido y el aspecto gráfico del sitio web.

* Contenido: Edita el archivo [data.json](./assets/data/data.json) con la información de tu portafolio.
	* Campos opcionales dentro de `experience`, `projects` y `training`: *technologies, date, certificate, image, url y github*.
	* Los iconos generales se corresponden con los identificadores de [Lucide icons](https://lucide.dev/icons/).
	* Los iconos de las tecnologías se corresponden con los identificadores de [Devicon](https://devicon.dev/).
* Tema: Edita el tema gráfico de la web.
	* Descomenta la línea `rx.theme_panel()` en `portafolio.py`. 
	* Inicia el proyecto, selecciona la configuración que quieras y pulsa `Copy Theme`.
	* Añade esa información dentro de `theme=rx.theme()` en `portafolio.py`.


