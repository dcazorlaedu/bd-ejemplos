# 08_ejercicio_UT3 · Usuarios y privilegios mínimos

**UT3 · RA2 · Nivel 3**
Creación de bases de datos relacionales

**Resultado de aprendizaje:** Crea bases de datos definiendo su estructura y las características de sus elementos según el modelo relacional.
**Criterios trabajados:** f), g), h)

## Situación

La base de datos de una tienda tendrá perfiles de consulta, almacén y administración. Cada perfil debe recibir solo los permisos imprescindibles.

## Enunciado

1. Crea usuarios de ejemplo con nombres no personales y configura la autenticación sin incluir contraseñas reales en la entrega.
2. Asigna permisos de solo lectura al perfil de consulta; permisos limitados de actualización al de almacén; reserva la administración del esquema para un perfil distinto.
3. Comprueba los privilegios concedidos y demuestra, con consultas de prueba, una operación permitida y otra denegada por perfil.
4. Revoca un permiso y verifica el cambio. Incluye el guion para crear las vistas que necesiten los perfiles.

## Entrega

Guion DCL de MySQL 8.4, matriz perfil-permiso y evidencias de las pruebas. No publiques credenciales ni uses cuentas reales.

## Ampliación (opcional, no evaluable)

- Haz una copia lógica con `mysqldump` (`--single-transaction --routines --triggers`), restáurala en otra base de datos y compara el número de filas de cada tabla. Automatiza la copia con un script y una línea de `cron` que conserve solo los 7 últimos días.

## Material

Esquema y datos ficticios: [`../material/tiendatech_mysql.sql`](../material/tiendatech_mysql.sql). Usa una base de datos de pruebas MySQL 8.4.

[Ver en el sitio web](https://dcazorlaedu.github.io/bd-ejemplos/ejercicios/08_ejercicio_UT3/)
