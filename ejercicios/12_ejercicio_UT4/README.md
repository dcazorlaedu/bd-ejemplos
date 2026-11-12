# 12_ejercicio_UT4 · Subconsultas y optimización del informe

**UT4 · RA3 · Nivel 4**
Realización de consultas

**Resultado de aprendizaje:** Consulta la información almacenada en una base de datos empleando asistentes, herramientas gráficas y el lenguaje de manipulación de datos.
**Criterios trabajados:** f), h)

## Situación

TiendaTech quiere localizar productos cuyo precio supera la media de su categoría, clientes con actividad por encima de la media y pedidos sin líneas. Las consultas se ejecutarán sobre MySQL.

## Enunciado

1. Resuelve la selección de productos mediante una subconsulta correlacionada y ofrece una alternativa con JOIN o tabla derivada.
2. Localiza clientes con al menos un pedido mediante EXISTS y explica por qué NOT IN puede dar resultados inesperados cuando aparece NULL.
3. Encuentra pedidos sin líneas y valores desconocidos usando IS NULL, no comparaciones de igualdad con NULL.
4. Utiliza EXPLAIN para analizar una consulta con filtros y JOIN; propone un índice, vuelve a medir y documenta si el plan mejora.
5. Compara las dos versiones de la consulta en legibilidad, resultados y plan de ejecución.

## Entrega

Consultas MySQL, salidas de EXPLAIN antes/después y una justificación de la estrategia de optimización. Usa el esquema de Material.

## Material

Esquema y datos ficticios: [`../material/tiendatech_mysql.sql`](../material/tiendatech_mysql.sql). Usa una base de datos de pruebas MySQL 8.4.

[Ver en el sitio web](https://dcazorlaedu.github.io/bd-ejemplos/ejercicios/12_ejercicio_UT4/)
