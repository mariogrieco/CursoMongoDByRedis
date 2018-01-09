# Mongo DB 
  ## Instalando...
     Paso 1: Importar la llave pública para el manejador de paquetes
        $ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
    Paso 2: Agregar el repositorio según la versión de Ubuntu
        Ubuntu 16.04 (Xenial)
          $ echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
    Paso 3: Actualizar los repositorios
        $ sudo apt-get update
    Paso 4: Instalar MongoDB
        $ sudo apt-get install -y mongodb-org

  ## Ejecutar MongoDB Community Edition en modo “daemon"

    $ sudo systemctl start mongod

## Detener MongoDB

    $ sudo service mongod stop

  o usando

    $ sudo systemctl stop mongod

## Verificar la ejecución de MongoDB

  Para verificar si MongoDB está ejecutando correctamente debes verificar los logs de Mongo en /var/logs/

    $ cat /var/log/mongodb/mongod.log

# Modelado de datos en MongoDB
  
  ## Relaciones uno a uno
  ## Relaciones uno a muchos
  ## Modelado de datos tipo árbol
  
    - Referencia al padre
    - Referencia a los hijos

# COMANDOS

  - show dbs
  - show collections
  - db.<collection>.insert({...})
  - use <dbName>
  - db.createCollection("<collectionName>")
  - load('name-file.js') Permite cargar un archivo JavaScript a MongoDB.

  # Acciones CRUD, insertar, modificar, eliminar y leer documentos de MongoDB

    - insert me permite insertar uno o varios documentos en la base de datos,
    - insertOne se usa para insertar unicamente un documentos. Vamos a insertar el documentos que ya teníamos. Es    - importante especificar que tipo de insert estas usando cuando estes trabajando en tus proyectos personales.
    - Si estas usando alguna versión de Mongo 2.x no vas a tener disponible la función insertOne porque se    implementó desde la versión 3.0.

   ## MongoDB proporciona los siguientes métodos para insertar documentos en una colección:

    - db.<collection>.insert({JSON-Document}) Permite agregar una o varias colecciones a una base de datos.
    - db.<collection>.insertOne({JSON-Document}) A diferencia del insert({JSON-Document}), este método solo inserta una colección.
    - db.<collection>.insertMany([{JSON-Document}, {Other-JSON-Document}, {...}]) Este método es similar a insert({JSON-Document}), sin embargo, este método fue incluido en la versión 3 de MongoDB por ende debe comenzar a usarse y evitar insert({JSON-Document}).

    ## Las operaciones de lectura, recuperan documentos de una colección. MongoDB proporciona los siguientes métodos para leer documentos de una colección:

    - db.<collection>.find() Imprime los primeros 20 documentos que encuentre. ( puedo usar function .pretty() o .limit())
    - db.<collection>.findOne() Imprime solo el primer documentos que encuentre.
      - > db.ticker.find({"last_updated": {$gt:"150646250"}})
      mod querys
        lt <
        lte <=
        gt >
        gte >=

    - limitar campos 
        - > db.ticker.find({"last_updated": {$gt:"150646250"}}, {<nombreField>: 0|1 (false|true),...})


   ## Modificación de documentos en la consola de MongoDB
   
    Las operaciones de actualización, modifican los documentos existentes en una colección. MongoDB proporciona los siguientes métodos para actualizar documentos de una colección:

   - db.<collection>.save({JSON-Document)} Modifica un campo si se encuentra en una colección, si no se agrega.
   - db.<collection>.update({JSON-Document)} Actualiza el documento por completo, es decir, elimina todos los campos y agrega los nuevos dejando así solo el _id.
   - db.<collection>.updateOne({filtro}, {"clave": "valor"}) Se actualizará el primer documento que coincida con el filtro.
   - db.<collection>.updateMany({filtro}, {"clave": "valor"}) Se actualizará todos los documentos que coincida con el filtro.
   - db.collection.update({NombreDelAtributo:“Valor”},{$set:{NombreDelAtributo:“Nuevo valor”}})

  
  ## Eliminar documentos en la consola de MongoDB

    Las operaciones de borrado, eliminan documentos de una colección. MongoDB proporciona los siguientes métodos para eliminar documentos de una colección:

   - db.<collection>.deleteOne({"filter")} Elimina el primer documento encontrado según el filtro.
   - db.<collection>.deleteMany({"filter")} Elimina todos los documentos encontrados según el filtro.
   - db.<collection>.remove({"filter")} Elimina un campo según el filtro, es decir, si coincide uno o muchos    documentos con el filtro serán eliminados de la base de datos.
   - db.<collection>.drop() Elimina todos los documentos de una colección.

  ## Indices en MongoDB
    

https://joaquinaraujo.github.io/mongodb-redis/
