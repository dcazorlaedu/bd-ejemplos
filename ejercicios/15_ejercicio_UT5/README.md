# 15_ejercicio_UT5 · Transacción de pedido y concurrencia

**UT5 · RA4 · Nivel 3**
Tratamiento de datos

**Resultado de aprendizaje:** Modifica la información almacenada en la base de datos utilizando asistentes, herramientas gráficas y el lenguaje de manipulación de datos.
**Criterios trabajados:** b), d), e), f), g), h)

## Situación

Al confirmar un pedido se deben insertar la cabecera y sus líneas, descontar stock y evitar que dos sesiones vendan las últimas unidades simultáneamente.

## Enunciado

1. Diseña el orden de operaciones dentro de una transacción InnoDB y define cómo comprobar que hay stock suficiente.
2. Demuestra COMMIT en un caso válido y ROLLBACK cuando falle una comprobación intermedia; incluye una anulación parcial mediante SAVEPOINT.
3. Simula dos sesiones que intentan actualizar el mismo producto. Registra qué observa cada sesión y cuándo queda bloqueada.
4. Compara brevemente el efecto de una lectura normal y una lectura con bloqueo (SELECT ... FOR UPDATE).
5. Explica cómo claves, restricciones y control de errores mantienen la consistencia incluso si la operación se cancela.

## Entrega

Guion de prueba para dos sesiones, secuencia de comandos y una tabla que describa bloqueo, resultado y estado final tras COMMIT/ROLLBACK.

## Material

Esquema y datos ficticios: [`../material/tiendatech_mysql.sql`](../material/tiendatech_mysql.sql). Usa una base de datos de pruebas MySQL 8.4.

[Ver en el sitio web](https://dcazorlaedu.github.io/bd-ejemplos/ejercicios/15_ejercicio_UT5/)
