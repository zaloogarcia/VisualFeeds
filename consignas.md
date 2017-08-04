# Paradigmas de Programación: Laboratorio 4

## Web APIs y Lenguajes Interpretados de Alto Nivel

En este laboratorio verán Web APIs y lenguajes interpretados de alto nivel,
particularmente verán el uso de [Python](https://www.python.org/) con el micro
web framework llamado [Flask](http://flask.pocoo.org/). 

## Lector de RSS/Atom Feeds

Deberán hacer una aplicación web para leer actualizaciones de información
(noticias, posts, etc.) de diferentes medios, usualmente conocidas como feeds.
Estos medios tienen que proveer actualizaciones mediante los protocolos
[RSS](https://en.wikipedia.org/wiki/RSS) y/o
[Atom](https://en.wikipedia.org/wiki/Atom_(standard)). La aplicación deberá
proveer un método para suscribirse y desuscribirse a feeds. 

La aplicación deberá mostrar únicamente los feeds a los que el usuario se haya
suscripto. Para eso, cada usuario deberá identificarse. La aplicación deberá
proveer un método para que el usuario se registre por primera vez y para que se
autentique cada vez que quiera entrar de vuelta. El registro y logeo deberán
ser llevados a cabo de las APIs OAuth de
[Google](https://developers.google.com/identity/protocols/OpenIDConnect#setredirecturi) y
[GitHub](https://developer.github.com/v3/oauth/).

El backend de la aplicación estará escrito en Python mediante el framework
Flask, con ayuda de algunas librerías extra para el trabajo de OAuth y la
lectura del XML de los feeds.

Se les brindará código inicial para facilitarles el trabajo, sobre todo en
términos de UI.

### Librerías y Frameworks

Para realizar el trabajo es necesaria la instalación de algunas librerías. En
primer lugar, se recomienda el uso de
[virtualenv](https://virtualenv.pypa.io/en/latest/) para aislar el entorno de
desarrollo.

Una vez instalado virtualenv, se crea y carga el entorno virtual:

    virtualenv venv
    source venv/bin/activate

Las librerías necesarias para el desarrollo de la aplicación, para instalar con
virtualenv son las siguientes:

* [Flask](http://flask.pocoo.org/): El framework web.
* [feedparser](https://pythonhosted.org/feedparser/): Para leer feeds RSS/Atom.
* [Flask-OAuthlib](https://flask-oauthlib.readthedocs.io/en/latest/): Para
  poder manejar APIs OAuth para el sign-up de la página web.
* [peewee](http://docs.peewee-orm.com/en/latest/): Un ORM, para crear los
  modelos de manera más simple.
* [Flask-Login](https://flask-login.readthedocs.org/en/latest/): Un manejador
  de sesiones de usuario para Flask, para facilitar el login/logout de los
  usuarios. Está integrado al modelo de usuario.

También hay un par de librerías que no son obligatorias, pero son altamente
recomendables para hacer más sencillo el trabajo:

* [iPython](https://ipython.org/): Un shell interactivo para trabajar con Python.
* [ipdb](https://pypi.python.org/pypi/ipdb): Un debugger interactivo e
  intuitivo muy sencillo de usar.

### Requerimientos Funcionales

Se especifica a continuación el detalle de los requerimientos que deberá
cumplir el laboratorio:

1. El laboratorio debe seguir una arquitectura básica de
   [Model-view-controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
   (MVC). 
    * Se les entregará el código con los modelos de los usuarios y los feeds de
      cada usuario.
2. La aplicación debe pedir que los usuarios se registren mediante una cuenta
   en los servicios de Google y Github. 
3. Una vez hecho el sign-up, el servicio de OAuth debe servir para el
   login/logout. 
    * Se debe poder hacer logout en la misma página principal una vez iniciada
      la sesión. 
    * Se debe requerir inicio de sesión para poder acceder a la lista de feeds.
4. Cada sesión iniciada con un usuario distinto deberá mostrar la lista de
feeds de dicho usuario, con la posibilidad de agregar nuevos feeds y eliminar
feeds existentes.
5. Al acceder a un feed se deberán mostrar los items del mismo correctamente
formateados en el HTML.

## Consignas

1. Implementar el sistema buscando desacoplar todo en varios módulos, y no todo
   en un mismo archivo (se entrega la estructura inicial). En el caso de
   necesitar de variables globales, hacerlo mediante _settings_ de la
   aplicación.
2. Respetar el uso de sesiones para los permisos. No se debe poder acceder a
   una página de feeds de un usuario sin haber iniciado correctamente la
   sesión.
3. Se entregará código inicial con la siguiente estructura, se recomienda
   seguirla para facilitar el trabajo.

        static/
        templates/
        README.md
        app.py
        auth.py
        models.py
        runserver.py
        settings.py
    * Los archivos de código tienen la siguiente función:
        - `app.py`: Crea la aplicación Flask que se usará en los demás módulos.
        - `auth.py`: Maneja todo lo referente a trabajo con sesiones y APIs.
        - `models.py`: Tiene los modelos que se usarán en la aplicación (el
          código se entrega).
        - `runserver.py`: Es el módulo que manejará los controladores (también
          conocidos como vistas), y es el archivo que se corre para ejecutar la
          aplicación.
        - `settings.py`: Contiene las settings que se utilizarán a lo largo de la
          aplicación. Se entregarán algunas settings, pero puede que deban
          utilizar más.
    * El subdirectorio `templates/` contiene los templates (views) que se
      escriben en formato [Jinja2](http://jinja.pocoo.org/docs/dev/). El html
      se entregará para que no deban escribirlo, pero aún así deberán leerlo
      para poder conectarlo con la aplicación.
    * El subdirectorio `static/` contiene los archivos estáticos, como pueden
      ser archivos javascript y/o css. No se recomienda tocar este directorio
      porque puede desconfigurarse la UI.

4. Se deberá contar con una base de datos en formato sqlite (archivo .db) para
   facilitar la implementación. Dicha base de datos **NO DEBE** ser subida con
   el resto de los archivos fuente. De igual manera, el entorno virtual, de ser
   creado, **NO DEBE** subirse al repositorio.
    * Se les proporcionarán los settings básicos para alcanzar dicho sistema.
5. Se deberá crear un archivo README, donde se explicará: las decisiones de
   diseño que tomaron, las dependencias que se tienen (si no son las listadas
   arriba), de donde instalarlas (en caso de que no pueda instalarse via
   `pip`), etc. 
6. El código debe respetar el coding-style definido por el standard
   [PEP8](https://www.python.org/dev/peps/pep-0008/), esto se puede chequear
   mediante la [herramienta pep8](https://pypi.python.org/pypi/pep8).

### Puntos Extras

Los siguientes puntos suman a la nota final, sin restar, no obstante _solo se
tendrán en cuenta si los requerimientos del laboratorio ya han sido cumplidos_:

* Utilizar APIs de Facebook, Twitter o alguna otra opción.
* Utilizar alguna librería javascript (como [jQuery](https://jquery.com/)) para
  que agregar y eliminar feeds sea mediante
  [AJAX](https://en.wikipedia.org/wiki/Ajax_(programming)).
* Aplicar protección de ataques
  [CSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery) a
  formularios vulnerables.

## Características de la Presentación

* Fecha de entrega: hasta el 20/05/2016 a las 23:59:59.999
* Deberán crear un tag indicando el release para corregir.

        git tag -a 4.0 -m 'Laboratorio 4'

* Si no está el tag se considerará como entregado hasta el último commit antes
  del deadline. No se consideran commits posteriores al tag.

## Recomendaciones y Extras

### Recomendaciones Generales

* El laboratorio es sencillo de implementar una vez que se tenga en claro lo
  que se debe hacer. Para esto __deben leer documentación__, en la documentación
  de las APIs y librerías está la mayoría de la información necesaria, y
  existen miles de posts en blogs explicando cosas.
* Diseñen teniendo en cuenta la posibilidad de reutilizar código. Si deben
  escribir lo mismo o cosas similares más de una vez replanteen como pueden
  hacerlo.
* Documenten las porciones de código no intuitivas.

### Recursos de Utilidad

* Les recomiendo utilizar [PyCharm](https://www.jetbrains.com/pycharm/), la
  versión Community Edition tiene muchas utilidades, como completado de código,
  corrección PEP8 en tiempo real, etc.
* Leer algunos (preferentemente todos) los siguientes links, son de mucha
  ayuda:
    * [Documentación de OAuth de Google](https://developers.google.com/identity/protocols/OpenIDConnect#setredirecturi)
    * [Documentación de OAuth de Github](https://developer.github.com/v3/oauth/)
    * [Flask](http://flask.pocoo.org/docs/0.10/tutorial/), tutorial básico de
      Flask.
    * [OAuth Authentication with
      Flask](http://blog.miguelgrinberg.com/post/oauth-authentication-with-flask),
      utiliza una librería distinta de OAuthlib, pero sirve para darse una idea
      general de que trata OAuth.
    * [How to make a Flask blog in one hour or
      less](http://charlesleifer.com/blog/how-to-make-a-flask-blog-in-one-hour-or-less/),
      tutorial bastante sencillo de como hacer un blog en Flask, idea de la que
      partí para hacer este proyecto.
    * [Ejemplos de OAuthlib para distintas
      APIs](https://github.com/lepture/flask-oauthlib/tree/master/example)
    * [Flask Snippet for CSRF Protection](http://flask.pocoo.org/snippets/3/),
      un snippet que sirve para garantizar protección CSRF en Flask.
    * [Larger
      Applications](http://flask.pocoo.org/docs/0.10/patterns/packages/),
      explica como modularizar las aplicaciones de Flask.
    * [Structuring flask apps, a how-to for those coming from
      Django](http://charlesleifer.com/blog/structuring-flask-apps-a-how-to-for-those-coming-from-django/),
      similar al link anterior, sirve para estructurar aplicaciones flask.
