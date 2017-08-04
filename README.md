#**Laboratorio 4**:
# Web APIs y Lenguajes Interpretados de Alto Nivel
![webapi.png](https://bitbucket.org/repo/LLGjg7/images/3271124487-webapi.png)
#### Bouer Daniel, Garcia Gonzalo.
---

##Introduccion

Una API es un conjunto de funciones y procedimientos que cumplen una o muchas funciones con el fin de ser utilizadas por otro software. Las siglas API vienen del inglés *Application Programming Interface*. En español sería Interfaz de Programación de Aplicaciones.

Una API nos permite implementar las funciones y procedimientos que engloba en nuestro proyecto sin la necesidad de programarlas de nuevo. En términos de programación, es una capa de abstracción.

![API.jpeg](https://bitbucket.org/repo/LLGjg7/images/820998029-API.jpeg)

En este caso desarrollamos una aplicación web para leer feeds en los que los usuarios son registrados por medio de [Google][G], [Github][GI] o [Facebook][F] gracias a las API's OAuth de los respectivos medios de registracion.

---

##Implementacion

El laboratorio  se desarrolla dentro de un entorno aislado para [Python][P] mediante **virtualenv**, en donde es posible instalar paquetes sin interferir con los paquetes de Python del sistema. 

Se utilizo el Flask, un micro framework escrito en  Python. Se llama micro framework porque no obliga al desarrollador usar una herramienta o libreria en particular. No tiene ninguna capa de abtraccion para la base de datos, validacion de formularios, manejo de carga, varias tecnologias abiertas de autenticacion ni otras herramientas comunes que tienen los frameworks. Es por eso que existen extensiones para este Framework que fueron utilizadas, por ejemplo **Flask-Login**,**Flask-OAuth**, y tambien se agregaron otras herramientas para complementar la implementacion como **peewee**, y **feedparser**.  

Se utilizo la API **OAuth** 
   
 [OAuth][AO] (*Open Authorization*) es un protocolo que permite flujos simples de autorización para sitios web o aplicaciones informáticas. Se trata de un protocolo que permite autorización segura de una API de modo estándar y simple para aplicaciones de escritorio, móviles y web.

OAuth permite a un usuario del sitio de Github, Facebook o Google compartir su información con nuestro sitio sin compartir toda su identidad. Para los consumidores, OAuth es un método de interactuar con datos protegidos y publicarlos. Para nosotros, OAuth proporciona a los usuarios un acceso a sus datos al mismo tiempo que protege las credenciales de su cuenta.

![OAUTH.png](https://bitbucket.org/repo/LLGjg7/images/2825592454-OAUTH.png)

La aplicacion corre en la direccion 'http://localhost:5000' donde esta funcionando el server implementado en el archivo *runserver.py*. La aplicacion se encarga del Login del usuario y el manejo de los feeds, pero no funciona sin las funciones implementadas en runserver. Una vez que el cliente ya esta loggeado, se muestran los feeds que estan almacenadas en la base de datos implementado con peewee como una tabla de triplas '([User, Feed], True)'.

En runserver estan implementadas todas las funciones , cubirendo todos los casos, el parseo , la carga de datos a la base de datos, el login, que llaman sus respectivos *templates* de html para ser visualizadas por el usuario.

En el caso de Login se corroboran unos campos, descriptos en el grafico anterior, dependiendo del provedor (Google , Github, etc) de la informacion del cliente y se almacenan en la base de datos. Esos campos de cada proveedor son definidos en *auth.py*.
Para esto se registra la aplicacion en las paginas de las API's de los provedores, donde se obtienen las Keys (*id* y *secret*) almacenadas en *settings.py*. Luego de Loggearse se redirecciona al usuario al url *index*.

Una vez autenticados los usuarios, se los agrega a la base de datos(usando **peewee**) con la informacion correspondiente. Para revisar si el usuario ya existe en nuestra base de datos revisamos el *social_id*, un campo que los sitios de autenticacion aseguran es unico. El usuario se registra y **peewee** le asigna automaticamente un id, con el cual se podrá cambiar el usuario en el futuro. Los metodos para conseguir la información varían de acuerdo al servidor usado, pero todas involucran el uso de oauth.remote_app.get() de flask_oauthlib.client. Esta función envía un pedido con el token de autenticación a un sitio (especificado por el website) para pedir cierta información. Si el usuario le ha dado permiso al app para acceder a esta información, se la envía.

A la hora de agregar *feeds*, se imprime la plantilla *newfeed.html*, luego se parsean los argumentos otorgados por el usuario y se crea un nuevo feed con los campos que componen un rss, como el titulo , descripcion , etc. Para hacer todo este trabajo, se utiliza **feedparser**. **feedparser** consigue la información necesaria de un feed. Tambien nos permite revisar si el feed tiene un formato de xml valido, y si el feed no esta vacio. Una vez revisado esto, se consigue la informacion relevante del feed y se la agrega a la base de datos, asociada al usuario actual (*current_user*). Este feed luego se utiliza para mostrar mas informacion, en el template *rss.html*. Para ello volvemos a parsear el feed y mostramos sus "entries".

Cada usuario tiene asociado a el una lista de feeds, y cada feed en la base de datos tiene asociado un usuario. Para esto se utiliza el *ForeignKeyField* de **peewee**. Esto permite crear relaciones entre elementos de tablas distintas en la base de datos, y nos permite acceder a traves de un usario a sus feeds, y a traves de un feed a su usuario. De esta forma solamente permitimos a un usuario acceso a sus propios feeds.

---

##Conclusion

Queremos agradecer a la catedra por atender nuestras dudas en todo momento y por darnos la oportunidad de aprender sobre el desarrollo de web API's, ya que son herramientas muy utiles y demandadas en el desarrollo web.

---

##Bibliografia

 * [Flask-OAuth](https://pythonhosted.org/Flask-OAuth/)
 * [Facebook][F]
 * [Google][G]
 * [AOuth 2.0][AO]
 * [Github][GI]
 * [Blog miguel grinberg](http://blog.miguelgrinberg.com/post/oauth-authentication-with-flask)
 * [Stackoverflow](http://stackoverflow.com/questions/8605703/how-to-verify-facebook-access-token)


[G]:<https://developers.google.com/>
[GI]:<https://developer.github.com>
[AO]:<http://oauth.net/2/>
[P]:<http://www.python.org>
[F]:<https://developers.facebook.com>