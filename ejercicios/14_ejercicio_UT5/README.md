# 14_ejercicio_UT5 · Carga de una campaña promocional

**UT5 · RA4 · Nivel 2**
Tratamiento de datos

**Resultado de aprendizaje:** Modifica la información almacenada en la base de datos utilizando asistentes, herramientas gráficas y el lenguaje de manipulación de datos.
**Criterios trabajados:** a), b), c), d), h)

## Situación

La tienda quiere guardar en una tabla de trabajo los productos activos de una categoría cuyo stock está por debajo del mínimo, calcular una propuesta de reposición y registrar los cambios mediante un guion.

## Enunciado

1. Crea una tabla de trabajo con restricciones adecuadas para producto, stock actual, stock objetivo y fecha de revisión.
2. Rellénala con INSERT ... SELECT a partir del catálogo; documenta qué filas se seleccionan.
3. Actualiza el objetivo de reposición mediante una sentencia calculada y elimina de la tabla las filas que ya no cumplen la condición.
4. Agrupa las operaciones en un guion que pueda repetirse sin duplicar registros ni dejar datos incoherentes.

## Entrega

Guion completo con DDL, INSERT ... SELECT, UPDATE, DELETE y consultas de verificación antes y después.

## Material

Esquema y datos ficticios: [`../material/tiendatech_mysql.sql`](../material/tiendatech_mysql.sql). Usa una base de datos de pruebas MySQL 8.4.

[Ver en el sitio web](https://dcazorlaedu.github.io/bd-ejemplos/ejercicios/14_ejercicio_UT5/)
