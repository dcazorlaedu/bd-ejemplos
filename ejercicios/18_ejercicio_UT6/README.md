# 18_ejercicio_UT6 · Auditoría de cambios y tarea programada

**UT6 · RA5 · Nivel 3**
Programación de bases de datos

**Resultado de aprendizaje:** Desarrolla procedimientos almacenados evaluando y utilizando las sentencias del lenguaje incorporado en el sistema gestor de bases de datos.
**Criterios trabajados:** a), b), c), d), f), g), h), i), j)

## Situación

La empresa quiere auditar las variaciones de precio, conservar el valor anterior y nuevo, y generar cada noche un resumen de cambios.

## Enunciado

1. Diseña una tabla de auditoría que almacene producto, usuario de base de datos, instante y valores anterior/nuevo, sin copiar datos personales innecesarios.
2. Crea un trigger que registre solo los cambios reales de precio; prueba actualización de una y varias filas.
3. Crea un procedimiento que recorra un conjunto de productos con cursor, cierre el cursor correctamente y use un manejador NOT FOUND.
4. Define un evento diario que ejecute el resumen; comprueba la configuración de Event Scheduler y explica cómo deshabilitarlo.
5. Fuerza un error controlado y demuestra que la rutina cierra recursos y comunica el problema.

## Entrega

Guion MySQL con tabla, trigger, procedimiento, cursor, manejadores y evento; añade pruebas y explica el orden de ejecución.

## Ampliación (opcional, no evaluable)

- Inspecciona las rutinas creadas con `information_schema.routines` y `SHOW CREATE`; concede a un usuario `EXECUTE` solo sobre un procedimiento y compara `SQL SECURITY DEFINER` con `INVOKER`.

## Material

Esquema y datos ficticios: [`../material/tiendatech_mysql.sql`](../material/tiendatech_mysql.sql). Usa una base de datos de pruebas MySQL 8.4.

[Ver en el sitio web](https://dcazorlaedu.github.io/bd-ejemplos/ejercicios/18_ejercicio_UT6/)
