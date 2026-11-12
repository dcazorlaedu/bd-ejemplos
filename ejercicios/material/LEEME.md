# Entorno de prácticas con Docker y DataGrip

1. Instala Docker (Docker Desktop o Docker Engine con el plugin *compose*).
2. En esta carpeta (`material/`) ejecuta: `docker compose up -d`.
3. Comprueba que MySQL está listo: `docker compose ps` debe mostrar `healthy`.
4. Conecta con **DataGrip**: *+ → Data Source → MySQL*; host `localhost`, puerto `3306`, usuario `alumno`, contraseña `alumno_dev`, base de datos `tiendatech_ejercicios`. Pulsa *Test Connection*.
5. MongoDB: `mongodb://localhost:27017` (DataGrip, Compass o `mongosh`). Carga los datos con `mongosh < tiendatech_mongo.js`.

Notas:
- El script SQL de `docker-entrypoint-initdb.d` solo se ejecuta cuando el volumen está **vacío**. Para volver a cargarlo: `docker compose down -v` (borra los datos) y `docker compose up -d`.
- Si el puerto 3306 está ocupado, cambia `"3306:3306"` por `"3307:3306"` y usa 3307 en DataGrip.
- Usuario y contraseñas son de ejemplo, solo para el aula. No uses datos reales.
