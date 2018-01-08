# Mongo DB 

  ## Ejecutar MongoDb

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


    https://joaquinaraujo.github.io/mongodb-redis/
