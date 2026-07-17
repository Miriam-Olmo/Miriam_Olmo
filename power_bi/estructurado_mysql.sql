-- ============================================================
--  EJEMPLO: DATOS ESTRUCTURADOS
--  Base de datos relacional (MySQL)
--  Tienda online — clientes y pedidos
-- ============================================================
--
--  Los datos ESTRUCTURADOS tienen:
--    ✔ Esquema fijo (columnas definidas de antemano)
--    ✔ Tipos de dato por columna (INT, VARCHAR, DATE, DECIMAL...)
--    ✔ Relaciones entre tablas mediante claves
--    ✔ Se pueden consultar con SQL
-- ============================================================

-- Crear base de datos
CREATE DATABASE tienda_online;
USE tienda_online;

-- ----------------------------------------------------------
-- TABLA 1: clientes
--   Cada fila = un cliente
--   Cada columna tiene un nombre y un tipo de dato fijos
-- ----------------------------------------------------------
CREATE TABLE clientes (
    id_cliente  INT          NOT NULL AUTO_INCREMENT,  -- clave primaria
    nombre      VARCHAR(100) NOT NULL,
    email       VARCHAR(150) NOT NULL UNIQUE,
    ciudad      VARCHAR(80),
    fecha_alta  DATE         NOT NULL,
    PRIMARY KEY (id_cliente)
);

-- Insertar datos de ejemplo
INSERT INTO clientes (nombre, email, ciudad, fecha_alta) VALUES
('Ana García',     'ana.garcia@email.com',    'Madrid',    '2023-01-15'),
('Luis Martínez',  'luis.martinez@email.com', 'Barcelona', '2023-03-22'),
('Sara López',     'sara.lopez@email.com',    'Valencia',  '2023-06-10'),
('Pedro Sánchez',  'pedro.sanchez@email.com', 'Sevilla',   '2024-01-05');


-- ----------------------------------------------------------
-- TABLA 2: pedidos
--   Cada fila = un pedido realizado por un cliente
--   La columna id_cliente es CLAVE FORÁNEA → enlaza con clientes
-- ----------------------------------------------------------
CREATE TABLE pedidos (
    id_pedido    INT            NOT NULL AUTO_INCREMENT,
    id_cliente   INT            NOT NULL,              -- FK → clientes
    producto     VARCHAR(150)   NOT NULL,
    cantidad     INT            NOT NULL DEFAULT 1,
    precio_total DECIMAL(10,2)  NOT NULL,
    fecha_pedido DATE           NOT NULL,
    estado       ENUM('pendiente','enviado','entregado','cancelado') NOT NULL DEFAULT 'pendiente',
    PRIMARY KEY (id_pedido),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- Insertar datos de ejemplo
INSERT INTO pedidos (id_cliente, producto, cantidad, precio_total, fecha_pedido, estado) VALUES
(1, 'Monitor 27" 4K',         1,  349.99, '2024-02-10', 'entregado'),
(1, 'Teclado mecánico',        1,   89.50, '2024-03-05', 'enviado'),
(2, 'Silla ergonómica',        1,  220.00, '2024-02-28', 'entregado'),
(3, 'Auriculares Bluetooth',   2,   59.90, '2024-03-15', 'pendiente'),
(4, 'Webcam HD',               1,   45.00, '2024-03-20', 'pendiente');


-- ----------------------------------------------------------
-- CONSULTA: unir las dos tablas con JOIN
--   Esto es posible porque los datos son ESTRUCTURADOS
--   y tienen una relación definida por las claves
-- ----------------------------------------------------------
SELECT
    c.nombre          AS cliente,
    c.ciudad,
    p.producto,
    p.cantidad,
    p.precio_total,
    p.fecha_pedido,
    p.estado
FROM pedidos p
JOIN clientes c ON p.id_cliente = c.id_cliente
ORDER BY p.fecha_pedido;

-- ----------------------------------------------------------
-- RESULTADO ESPERADO (tabla perfectamente organizada):
--
-- cliente          ciudad      producto                cantidad  precio_total  fecha_pedido  estado
-- ---------------  ----------  ----------------------  --------  ------------  ------------  ----------
-- Ana García       Madrid      Monitor 27" 4K          1         349.99        2024-02-10    entregado
-- Luis Martínez    Barcelona   Silla ergonómica        1         220.00        2024-02-28    entregado
-- Ana García       Madrid      Teclado mecánico        1          89.50        2024-03-05    enviado
-- Sara López       Valencia    Auriculares Bluetooth   2          59.90        2024-03-15    pendiente
-- Pedro Sánchez    Sevilla     Webcam HD               1          45.00        2024-03-20    pendiente
-- ----------------------------------------------------------
