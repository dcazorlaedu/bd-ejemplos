// Datos totalmente ficticios para prácticas. Ejecutar solo en una base de pruebas.
db = db.getSiblingDB("tiendatech_ejercicios");

db.productos.drop();
db.productos.insertMany([
  {sku: "TEC-001", nombre: "Portátil Aero 14", categoria: "Portátiles", precio: 749, stock: 12, activo: true, etiquetas: ["oficina", "portatil"]},
  {sku: "TEC-002", nombre: "Móvil Zeta 5G", categoria: "Móviles", precio: 329, stock: 30, activo: true, etiquetas: ["movil", "5g"]},
  {sku: "TEC-003", nombre: "Teclado mecánico", categoria: "Periféricos", precio: 69.9, stock: 25, activo: true, etiquetas: ["periferico", "gaming"]},
  {sku: "TEC-004", nombre: "SSD 1TB", categoria: "Almacenamiento", precio: 79.9, stock: 40, activo: true, etiquetas: ["ssd", "almacenamiento"]},
  {sku: "TEC-005", nombre: "Router WiFi 6", categoria: "Redes", precio: 89, stock: 17, activo: true, etiquetas: ["redes", "wifi"]}
]);

db.pedidos.drop();
db.pedidos.insertMany([
  {id: 1001, fecha: ISODate("2026-10-04T10:00:00Z"), estado: "entregado", lineas: [
    {sku: "TEC-001", nombre: "Portátil Aero 14", cantidad: 1, precioUnitario: 749},
    {sku: "TEC-003", nombre: "Teclado mecánico", cantidad: 2, precioUnitario: 69.9}
  ]},
  {id: 1002, fecha: ISODate("2026-10-05T11:30:00Z"), estado: "enviado", lineas: [
    {sku: "TEC-002", nombre: "Móvil Zeta 5G", cantidad: 2, precioUnitario: 329},
    {sku: "TEC-005", nombre: "Router WiFi 6", cantidad: 1, precioUnitario: 89}
  ]},
  {id: 1003, fecha: ISODate("2026-10-06T09:15:00Z"), estado: "pendiente", lineas: [
    {sku: "TEC-004", nombre: "SSD 1TB", cantidad: 3, precioUnitario: 79.9}
  ]}
]);
