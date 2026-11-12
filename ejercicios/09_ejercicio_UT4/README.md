# 09_ejercicio_UT4 · Consultas básicas de catálogo

**UT4 · RA3 · Nivel 1**
Realización de consultas

**Resultado de aprendizaje:** Consulta la información almacenada en una base de datos empleando asistentes, herramientas gráficas y el lenguaje de manipulación de datos.
**Criterios trabajados:** a), b)

## Situación

El equipo comercial necesita consultar el catálogo de TiendaTech para preparar una campaña. Usa la base de datos ficticia del laboratorio SQL o el esquema MySQL de Material.

## Enunciado

1. Indica qué herramienta utilizarías para explorar las tablas y qué sentencia permite consultar datos.
2. Obtén nombre, precio y stock de productos activos; filtra los que tengan existencias y ordénalos por precio.
3. Muestra los productos dentro de un intervalo de precios, con alias claros y un límite de filas.
4. Escribe una consulta que encuentre nombres que contengan una palabra o patrón indicado por el usuario.

## Entrega

Archivo SQL con cuatro consultas comentadas y una captura o salida tabular que permita comprobarlas.

## Ampliación (opcional, no evaluable)

- Usa funciones de cadena y fecha (`CONCAT_WS`, `SUBSTRING_INDEX`, `DATE_FORMAT`, `TIMESTAMPDIFF`) para presentar los clientes y valida con `REGEXP` el formato de un correo. Explica por qué una función aplicada a una columna indexada puede impedir el uso del índice.

## Material

Esquema y datos ficticios: [`../material/tiendatech_mysql.sql`](../material/tiendatech_mysql.sql). Usa una base de datos de pruebas MySQL 8.4.

[Ver en el sitio web](https://dcazorlaedu.github.io/bd-ejemplos/ejercicios/09_ejercicio_UT4/)
