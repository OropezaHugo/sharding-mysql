Sharding en MySQL - Laboratorio

**Introduccion**

El sharding es una técnica de escalabilidad horizontal en bases de datos que consiste en dividir los datos en múltiples instancias o fragmentos (shards) para distribuir la carga y mejorar el rendimiento. En este laboratorio, configuraremos un sistema de sharding en MySQL donde tendremos dos bases de datos (shard1 y shard2) y distribuiremos los usuarios entre ellas según un criterio específico.

**Requisitos previos**

Antes de ejecutar los comandos, asegúrate de tener instalado:

Docker y Docker Compose

Python 3 y pip

**Pasos para ejecutar el laboratorio**

Ejecuta los siguientes comandos en orden:

Levantar los servicios de MySQL con Docker Compose:

docker compose up -d

Esto iniciará un contenedor con MySQL y configurará las bases de datos necesarias.

Instalar el conector de MySQL para Python:

python3 -m pip install mysql-connector-python

Esto permitirá que Python se conecte a MySQL y ejecute las consultas necesarias.

Ejecutar el script de sharding:

python3 sharding.py

Esto insertará usuarios en diferentes shards según la lógica definida en el script.

**Explicación del sharding en este laboratorio**

Se crean dos bases de datos (shard1 y shard2).

Se crea una tabla users en cada shard con los mismos campos.

Se usa una función en Python para determinar en qué shard insertar cada usuario, basada en la longitud del correo electrónico.

Este enfoque es una introducción básica al sharding y cómo se puede implementar en MySQL con Python.

