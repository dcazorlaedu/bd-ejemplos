# 10_ejercicio_UT4 · Pedidos, clientes y productos

**UT4 · RA3 · Nivel 2**
Realización de consultas

**Resultado de aprendizaje:** Consulta la información almacenada en una base de datos empleando asistentes, herramientas gráficas y el lenguaje de manipulación de datos.
**Criterios trabajados:** c), d)

## Situación

Dirección quiere saber quién hizo cada pedido y qué productos se incluyeron. También necesita ver clientes sin pedidos y pedidos que todavía no tienen empleado asignado.

## Enunciado

1. Consulta cada pedido con la fecha y el nombre del cliente mediante una composición interna.
2. Incluye en otro resultado todos los clientes, aunque no hayan hecho pedidos, e identifica correctamente las columnas NULL.
3. Muestra pedidos con el nombre del empleado cuando exista, sin perder los pedidos que no tengan empleado.
4. Obtén el detalle de líneas incluyendo nombre de producto, cantidad y precio unitario; evita duplicar filas por una unión mal planteada.

## Entrega

Cuatro consultas SQL y una frase que explique por qué se eligió INNER JOIN o LEFT JOIN en cada caso.

## Material

Esquema y datos ficticios: [`../material/tiendatech_mysql.sql`](../material/tiendatech_mysql.sql). Usa una base de datos de pruebas MySQL 8.4.

[Ver en el sitio web](https://dcazorlaedu.github.io/bd-ejemplos/ejercicios/10_ejercicio_UT4/)
