# 07_ejercicio_UT3 · Vistas para cada perfil

**UT3 · RA2 · Nivel 2**
Creación de bases de datos relacionales

**Resultado de aprendizaje:** Crea bases de datos definiendo su estructura y las características de sus elementos según el modelo relacional.
**Criterios trabajados:** f), h)

## Situación

Sobre TiendaTech, el personal de almacén necesita consultar productos y existencias; dirección necesita un resumen de pedidos, pero no requiere los datos de contacto de clientes.

## Enunciado

1. Crea una vista de productos con categoría, proveedor, precio y stock, ocultando columnas que no necesita almacén.
2. Crea una vista de resumen de pedidos sin nombre, email ni otros datos personales del cliente.
3. Explica qué cambios en las tablas originales afectarían a las vistas y cuáles conviene documentar para que las consultas sean fiables.
4. Añade un índice a una tabla que mejore una consulta frecuente y utiliza EXPLAIN para comparar el plan antes y después.

## Entrega

Guion DDL de las vistas e índice, consultas de prueba y breve comparación de planes. Parte del esquema MySQL de TiendaTech facilitado en Material.

## Material

Esquema y datos ficticios: [`../material/tiendatech_mysql.sql`](../material/tiendatech_mysql.sql). Usa una base de datos de pruebas MySQL 8.4.

[Ver en el sitio web](https://dcazorlaedu.github.io/bd-ejemplos/ejercicios/07_ejercicio_UT3/)
