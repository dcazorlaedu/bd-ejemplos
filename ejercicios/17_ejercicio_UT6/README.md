# 17_ejercicio_UT6 · Procedimiento de reposición con reglas

**UT6 · RA5 · Nivel 2**
Programación de bases de datos

**Resultado de aprendizaje:** Desarrolla procedimientos almacenados evaluando y utilizando las sentencias del lenguaje incorporado en el sistema gestor de bases de datos.
**Criterios trabajados:** d), e), f), g), j)

## Situación

TiendaTech necesita una rutina que reciba una categoría y un umbral, calcule cuántos productos necesitan reposición y devuelva una etiqueta según el resultado.

## Enunciado

1. Crea una función determinista que clasifique un importe o una cantidad según varios intervalos y comprueba sus límites.
2. Crea un procedimiento con parámetros IN y OUT que calcule el número de productos bajo el umbral recibido.
3. Incluye IF/ELSEIF y un bucle acotado para generar un resumen por categoría; evita bucles infinitos.
4. Valida parámetros inválidos y documenta cómo notificar o gestionar el error sin dejar cambios parciales.
5. Ejecuta la rutina desde un guion SQL y muestra casos normal, límite y parámetro inválido.

## Entrega

Script con función y procedimiento, llamadas de prueba y explicación de parámetros, control de flujo y tratamiento de errores.

## Material

Esquema y datos ficticios: [`../material/tiendatech_mysql.sql`](../material/tiendatech_mysql.sql). Usa una base de datos de pruebas MySQL 8.4.

[Ver en el sitio web](https://dcazorlaedu.github.io/bd-ejemplos/ejercicios/17_ejercicio_UT6/)
