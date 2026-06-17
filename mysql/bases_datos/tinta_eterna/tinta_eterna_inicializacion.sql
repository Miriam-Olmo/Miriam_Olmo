-- ============================================================
-- TINTA ETERNA — Librería digital
-- Script de inicialización para las 4 sesiones de SQL
-- ============================================================
--   mysql -u root -p < tinta_eterna_inicial.sql
-- ============================================================

DROP DATABASE IF EXISTS tinta_eterna;
CREATE DATABASE tinta_eterna CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE tinta_eterna;

-- ============================================================
-- TABLAS
-- ============================================================

CREATE TABLE editoriales (
    id INT UNSIGNED AUTO_INCREMENT,
    nombre VARCHAR(120) NOT NULL,
    pais VARCHAR(60),
    anyo_fundacion YEAR,
    PRIMARY KEY (id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE autores (
    id INT UNSIGNED AUTO_INCREMENT,
    nombre VARCHAR(80) NOT NULL,
    apellidos VARCHAR(120) NOT NULL,
    nacionalidad VARCHAR(60),
    fecha_nacimiento DATE,
    PRIMARY KEY (id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE libros (
    id INT UNSIGNED AUTO_INCREMENT,
    titulo VARCHAR(200) NOT NULL,
    anyo_publicacion YEAR,
    isbn VARCHAR(20) UNIQUE,
    genero VARCHAR(50),
    idioma VARCHAR(40),
    paginas SMALLINT UNSIGNED,
    precio DECIMAL(6,2),
    editorial_id INT UNSIGNED,
    PRIMARY KEY (id),
    FOREIGN KEY (editorial_id) REFERENCES editoriales(id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE libro_autor (
    id INT UNSIGNED AUTO_INCREMENT,
    libro_id INT UNSIGNED NOT NULL,
    autor_id INT UNSIGNED NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (libro_id) REFERENCES libros(id),
    FOREIGN KEY (autor_id) REFERENCES autores(id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE lectores (
    id INT UNSIGNED AUTO_INCREMENT,
    nombre VARCHAR(80) NOT NULL,
    apellidos VARCHAR(120) NOT NULL,
    email VARCHAR(254) UNIQUE,
    fecha_registro DATE,
    pais VARCHAR(60),
    PRIMARY KEY (id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE compras (
    id INT UNSIGNED AUTO_INCREMENT,
    lector_id INT UNSIGNED NOT NULL,
    libro_id INT UNSIGNED NOT NULL,
    fecha_compra DATE NOT NULL,
    precio_pagado DECIMAL(6,2),
    formato ENUM('epub','pdf','mobi') NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (lector_id) REFERENCES lectores(id),
    FOREIGN KEY (libro_id) REFERENCES libros(id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE resenas (
    id INT UNSIGNED AUTO_INCREMENT,
    lector_id INT UNSIGNED NOT NULL,
    libro_id INT UNSIGNED NOT NULL,
    estrellas TINYINT UNSIGNED,
    texto TEXT,
    fecha DATE,
    PRIMARY KEY (id),
    FOREIGN KEY (lector_id) REFERENCES lectores(id),
    FOREIGN KEY (libro_id) REFERENCES libros(id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- ============================================================
-- EDITORIALES (6)
-- ============================================================

INSERT INTO editoriales (nombre, pais, anyo_fundacion) VALUES
('Alfaguara',        'España',      1964),
('Anagrama',         'España',      1969),
('Planeta',          'España',      1949),
('Tusquets',         'España',      1969),
('Salamandra',       'España',      1989),
('Penguin Random',   'Reino Unido', 2013);

-- ============================================================
-- AUTORES (15)
-- ============================================================

INSERT INTO autores (nombre, apellidos, nacionalidad, fecha_nacimiento) VALUES
('Gabriel',   'García Márquez',  'Colombia',   '1927-03-06'),
('Isabel',    'Allende',         'Chile',      '1942-08-02'),
('Mario',     'Vargas Llosa',    'Perú',       '1936-03-28'),
('Carlos',    'Ruiz Zafón',      'España',     '1964-09-25'),
('Almudena',  'Grandes',         'España',     '1960-05-07'),
('Arturo',    'Pérez-Reverte',   'España',     '1951-11-25'),
('Julia',     'Navarro',         'España',     '1953-01-01'),
('Haruki',    'Murakami',        'Japón',      '1949-01-12'),
('Stephen',   'King',            'EEUU',       '1947-09-21'),
('Elena',     'Ferrante',        'Italia',     '1943-01-01'),
('Fernando',  'Aramburu',        'España',     '1959-01-01'),
('Delia',     'Owens',           'EEUU',       '1949-04-04'),
('Sally',     'Rooney',          'Irlanda',    '1991-02-20'),
('Ken',       'Follett',         'Reino Unido','1949-06-05'),
('Dolores',   'Redondo',         'España',     '1969-02-01');

-- ============================================================
-- LIBROS (40)
-- ============================================================

INSERT INTO libros (titulo, anyo_publicacion, isbn, genero, idioma, paginas, precio, editorial_id) VALUES
('Cien años de soledad',          1967, '978-8437604947', 'Realismo mágico', 'Español', 471, 12.90, 1),
('El amor en los tiempos del cólera', 1985, '978-8497592208', 'Romance',     'Español', 496, 11.50, 1),
('La casa de los espíritus',      1982, '978-8401242113', 'Realismo mágico', 'Español', 448, 10.90, 3),
('Paula',                         1994, '978-8401242120', 'Memorias',        'Español', 368, 9.90,  3),
('La ciudad y los perros',        1963, '978-8466337380', 'Drama',           'Español', 432, 11.90, 4),
('La fiesta del chivo',           2000, '978-8420471839', 'Histórica',       'Español', 528, 13.50, 1),
('La sombra del viento',          2001, '978-8408172178', 'Misterio',        'Español', 576, 14.90, 3),
('El juego del ángel',            2008, '978-8408163381', 'Misterio',        'Español', 672, 15.50, 3),
('El prisionero del cielo',       2011, '978-8408105672', 'Misterio',        'Español', 384, 12.90, 3),
('El corazón helado',             2007, '978-8483468081', 'Histórica',       'Español', 928, 16.90, 2),
('Los pacientes del doctor García', 2017, '978-8430618576', 'Histórica',     'Español', 768, 15.90, 1),
('El club Dumas',                 1993, '978-8420471846', 'Misterio',        'Español', 432, 11.90, 1),
('La tabla de Flandes',           1990, '978-8420471853', 'Misterio',        'Español', 368, 10.90, 1),
('La reina del sur',              2002, '978-8420471860', 'Thriller',        'Español', 544, 13.90, 1),
('Dispara, yo ya estoy muerto',   2013, '978-8401353857', 'Histórica',       'Español', 1008, 17.90, 3),
('Dime quién soy',                2010, '978-8401337178', 'Histórica',       'Español', 1104, 18.50, 3),
('Tokio blues',                   1987, '978-8483835043', 'Romance',         'Español', 384, 11.90, 5),
('Kafka en la orilla',            2002, '978-8483835050', 'Realismo mágico', 'Español', 600, 14.50, 5),
('1Q84',                          2009, '978-8483835067', 'Fantasía',        'Español', 744, 16.90, 5),
('Crónica del pájaro',            1994, '978-8483835074', 'Realismo mágico', 'Español', 928, 17.50, 5),
('It',                            1986, '978-8401021947', 'Terror',          'Español', 1504, 19.90, 6),
('El resplandor',                 1977, '978-8401021954', 'Terror',          'Español', 512, 12.90, 6),
('Misery',                        1987, '978-8401021961', 'Terror',          'Español', 384, 11.50, 6),
('Carrie',                        1974, '978-8401021978', 'Terror',          'Español', 304, 9.90,  6),
('La amiga estupenda',            2011, '978-8426402325', 'Drama',           'Español', 432, 12.50, 5),
('Un mal nombre',                 2012, '978-8426402332', 'Drama',           'Español', 544, 13.50, 5),
('Patria',                        2016, '978-8490663998', 'Drama',           'Español', 648, 14.90, 4),
('Los peces de la amargura',      2006, '978-8483832240', 'Relatos',         'Español', 224, 9.50,  4),
('La cría del cangrejo',          2018, '978-8420438061', 'Drama',           'Español', 416, 13.90, 1),
('Normal people',                 2018, '978-8417624217', 'Romance',         'Español', 288, 11.90, 2),
('Conversaciones entre amigos',   2017, '978-8417007638', 'Romance',         'Español', 336, 12.50, 2),
('Los pilares de la Tierra',      1989, '978-8401328466', 'Histórica',       'Español', 1296, 18.90, 6),
('Un mundo sin fin',              2007, '978-8401337307', 'Histórica',       'Español', 1280, 18.90, 6),
('La caída de los gigantes',      2010, '978-8401352485', 'Histórica',       'Español', 1024, 17.90, 6),
('El guardián invisible',         2013, '978-8423347940', 'Thriller',        'Español', 440, 12.90, 4),
('Legado en los huesos',          2013, '978-8423348169', 'Thriller',        'Español', 560, 13.90, 4),
('Ofrenda a la tormenta',         2014, '978-8423349296', 'Thriller',        'Español', 544, 13.90, 4),
('El maestro y Margarita',        1967, '978-8420674254', 'Fantasía',        'Español', 528, 13.50, 1),
('La templanza',                  2015, '978-8408148577', 'Romance',         'Español', 544, 14.50, 3),
('El tiempo entre costuras',      2009, '978-8499089377', 'Histórica',       'Español', 640, 14.90, 3);

-- ============================================================
-- LIBRO_AUTOR (N:M)
-- ============================================================

INSERT INTO libro_autor (libro_id, autor_id) VALUES
(1,1),(2,1),(3,2),(4,2),(5,3),(6,3),
(7,4),(8,4),(9,4),
(10,5),(11,5),
(12,6),(13,6),(14,6),
(15,7),(16,7),
(17,8),(18,8),(19,8),(20,8),
(21,9),(22,9),(23,9),(24,9),
(25,10),(26,10),
(27,11),(28,11),
(29,12),
(30,13),(31,13),
(32,14),(33,14),(34,14),
(35,15),(36,15),(37,15),
(38,6),
(39,5),
(40,7);

-- ============================================================
-- LECTORES (30)
-- ============================================================

INSERT INTO lectores (nombre, apellidos, email, fecha_registro, pais) VALUES
('Laura',    'Sánchez Gil',     'laura.sanchez@mail.com',  '2023-01-15', 'España'),
('Carlos',   'Moreno Ruiz',     'carlos.moreno@mail.com',  '2023-02-20', 'España'),
('Marta',    'Díaz Pérez',      'marta.diaz@mail.com',     '2023-03-10', 'México'),
('Javier',   'López Sanz',      'javier.lopez@mail.com',   '2023-04-05', 'España'),
('Ana',      'Romero Vega',     'ana.romero@mail.com',     '2023-05-12', 'Argentina'),
('Pablo',    'Gómez Torres',    'pablo.gomez@mail.com',    '2023-06-18', 'España'),
('Lucía',    'Fernández Cano',  'lucia.fernandez@mail.com','2023-07-22', 'Colombia'),
('Miguel',   'Álvarez Sol',     'miguel.alvarez@mail.com', '2023-08-30', 'España'),
('Sara',     'Jiménez Bravo',   'sara.jimenez@mail.com',   '2023-09-14', 'Chile'),
('Diego',    'Castro León',     'diego.castro@mail.com',   '2023-10-08', 'España'),
('Elena',    'Navarro Salas',   'elena.navarro@mail.com',  '2023-11-21', 'España'),
('Andrés',   'Vázquez Ríos',    'andres.vazquez@mail.com', '2023-12-03', 'México'),
('Rocío',    'Molina Pardo',    'rocio.molina@mail.com',   '2024-01-19', 'España'),
('Sergio',   'Ortiz Pascual',   'sergio.ortiz@mail.com',   '2024-02-14', 'España'),
('Beatriz',  'Iglesias Crespo', 'beatriz.iglesias@mail.com','2024-03-25', 'Argentina'),
('Tomás',    'Serrano Mora',    'tomas.serrano@mail.com',  '2024-04-11', 'España'),
('Cristina', 'Reyes Vidal',     'cristina.reyes@mail.com', '2024-05-09', 'España'),
('Daniel',   'Ramos Suárez',    'daniel.ramos@mail.com',   '2024-06-16', 'Perú'),
('Patricia', 'Cabrera Luna',    'patricia.cabrera@mail.com','2024-07-02', 'España'),
('Adrián',   'Méndez Vela',     'adrian.mendez@mail.com',  '2024-08-20', 'España'),
('Nuria',    'Vargas Solís',    'nuria.vargas@mail.com',   '2024-09-07', 'México'),
('Fernando', 'Marín Aguilar',   'fernando.marin@mail.com', '2024-10-13', 'España'),
('Silvia',   'Lorenzo Bravo',   'silvia.lorenzo@mail.com', '2024-11-28', 'España'),
('Raúl',     'Soler Herrero',   'raul.soler@mail.com',     '2024-12-05', 'Colombia'),
('Verónica', 'Esteban Calvo',   'veronica.esteban@mail.com','2025-01-17', 'España'),
('Iván',     'Reina Murillo',   'ivan.reina@mail.com',     '2025-02-22', 'España'),
('Alicia',   'Pereira Casas',   'alicia.pereira@mail.com', '2025-03-09', 'Argentina'),
('Óscar',    'Salgado Vega',    'oscar.salgado@mail.com',  '2025-04-14', 'España'),
('Mónica',   'Ríos Quintana',   'monica.rios@mail.com',    '2025-05-19', 'España'),
('Héctor',   'Lozano Velasco',  'hector.lozano@mail.com',  '2025-06-25', 'México');

-- ============================================================
-- COMPRAS (90)
-- ============================================================

INSERT INTO compras (lector_id, libro_id, fecha_compra, precio_pagado, formato) VALUES
(1, 1, '2023-02-01', 12.90, 'epub'), (1, 7, '2023-03-15', 14.90, 'epub'), (1, 21, '2023-06-20', 19.90, 'pdf'),
(1, 27, '2024-01-10', 14.90, 'epub'), (1, 17, '2024-05-05', 11.90, 'mobi'),
(2, 1, '2023-03-01', 12.90, 'pdf'), (2, 3, '2023-04-12', 10.90, 'pdf'), (2, 12, '2023-07-08', 11.90, 'epub'),
(2, 31, '2024-02-20', 18.90, 'epub'),
(3, 7, '2023-04-01', 14.90, 'epub'), (3, 8, '2023-05-15', 15.50, 'epub'), (3, 9, '2023-06-22', 12.90, 'epub'),
(3, 17, '2023-09-10', 11.90, 'mobi'), (3, 18, '2024-01-14', 14.50, 'mobi'),
(4, 5, '2023-05-01', 11.90, 'pdf'), (4, 6, '2023-06-18', 13.50, 'pdf'), (4, 14, '2023-10-05', 13.90, 'epub'),
(5, 21, '2023-06-01', 19.90, 'epub'), (5, 22, '2023-07-20', 12.90, 'epub'), (5, 23, '2023-09-15', 11.50, 'epub'),
(5, 24, '2023-11-08', 9.90, 'epub'),
(6, 1, '2023-07-01', 12.90, 'mobi'), (6, 25, '2023-08-12', 12.50, 'epub'), (6, 26, '2023-10-22', 13.50, 'epub'),
(6, 27, '2024-01-30', 14.90, 'pdf'),
(7, 3, '2023-08-01', 10.90, 'epub'), (7, 4, '2023-09-15', 9.90, 'epub'), (7, 38, '2024-03-10', 14.50, 'epub'),
(8, 7, '2023-09-01', 14.90, 'pdf'), (8, 8, '2023-10-18', 15.50, 'pdf'), (8, 9, '2023-12-05', 12.90, 'pdf'),
(8, 12, '2024-02-14', 11.90, 'epub'), (8, 13, '2024-04-20', 10.90, 'epub'),
(9, 17, '2023-10-01', 11.90, 'epub'), (9, 18, '2023-11-20', 14.50, 'epub'), (9, 19, '2024-01-15', 16.90, 'epub'),
(10, 31, '2023-11-01', 18.90, 'pdf'), (10, 32, '2023-12-18', 18.90, 'pdf'), (10, 33, '2024-02-25', 17.90, 'pdf'),
(11, 7, '2023-12-01', 14.90, 'epub'), (11, 35, '2024-01-20', 12.90, 'epub'), (11, 36, '2024-03-15', 13.90, 'epub'),
(11, 37, '2024-05-08', 13.90, 'epub'),
(12, 1, '2024-01-05', 12.90, 'mobi'), (12, 2, '2024-02-18', 11.50, 'mobi'),
(13, 21, '2024-01-25', 19.90, 'epub'), (13, 22, '2024-03-10', 12.90, 'epub'),
(14, 27, '2024-02-10', 14.90, 'pdf'), (14, 28, '2024-04-05', 9.50, 'pdf'),
(15, 7, '2024-03-01', 14.90, 'epub'), (15, 8, '2024-04-15', 15.50, 'epub'), (15, 10, '2024-06-20', 16.90, 'epub'),
(16, 29, '2024-04-01', 13.90, 'epub'), (16, 30, '2024-05-18', 11.90, 'epub'),
(17, 17, '2024-05-01', 11.90, 'mobi'), (17, 18, '2024-06-15', 14.50, 'mobi'), (17, 19, '2024-08-08', 16.90, 'mobi'),
(18, 5, '2024-06-01', 11.90, 'epub'), (18, 6, '2024-07-12', 13.50, 'epub'),
(19, 34, '2024-07-01', 12.90, 'epub'), (19, 35, '2024-08-20', 13.90, 'epub'), (19, 36, '2024-10-05', 13.90, 'epub'),
(20, 1, '2024-08-25', 12.90, 'pdf'), (20, 21, '2024-10-10', 19.90, 'pdf'),
(21, 25, '2024-09-15', 12.50, 'epub'), (21, 26, '2024-11-02', 13.50, 'epub'),
(22, 31, '2024-10-20', 18.90, 'epub'), (22, 32, '2024-12-08', 18.90, 'epub'),
(23, 7, '2024-12-01', 14.90, 'mobi'), (23, 11, '2025-01-15', 15.90, 'mobi'),
(24, 17, '2025-01-10', 11.90, 'epub'), (24, 19, '2025-02-22', 16.90, 'epub'),
(25, 27, '2025-02-05', 14.90, 'pdf'),
(26, 21, '2025-02-28', 19.90, 'epub'), (26, 22, '2025-04-12', 12.90, 'epub'),
(27, 29, '2025-03-15', 13.90, 'epub'), (27, 30, '2025-05-01', 11.90, 'epub'),
(28, 1, '2025-04-20', 12.90, 'epub'), (28, 7, '2025-05-15', 14.90, 'epub'),
(29, 34, '2025-05-10', 12.90, 'mobi'), (29, 35, '2025-06-18', 13.90, 'mobi'), (29, 36, '2025-07-22', 13.90, 'mobi'),
(30, 17, '2025-06-05', 11.90, 'epub'), (30, 18, '2025-07-12', 14.50, 'epub'),
(2, 7, '2024-06-10', 14.90, 'epub'), (4, 1, '2024-03-20', 12.90, 'pdf'), (6, 7, '2024-05-25', 14.90, 'mobi'),
(8, 21, '2024-08-30', 19.90, 'pdf'), (10, 1, '2024-04-15', 12.90, 'pdf'), (12, 31, '2024-09-20', 18.90, 'mobi');

-- ============================================================
-- RESEÑAS (63)
-- ============================================================

INSERT INTO resenas (lector_id, libro_id, estrellas, texto, fecha) VALUES
(1, 1, 5, 'Una obra maestra absoluta. Imprescindible.', '2023-02-20'),
(1, 7, 5, 'Engancha desde la primera página.', '2023-04-01'),
(1, 21, 4, 'Terrorífico y largo, pero merece la pena.', '2023-07-10'),
(2, 1, 5, 'Lo he releído tres veces.', '2023-03-15'),
(2, 3, 4, 'Allende en estado puro.', '2023-05-01'),
(2, 12, 3, 'Entretenido pero algo previsible.', '2023-08-01'),
(3, 7, 5, 'Zafón es un genio. Barcelona como personaje.', '2023-04-20'),
(3, 8, 4, 'No tan bueno como el primero pero muy bueno.', '2023-06-01'),
(3, 9, 4, 'Buen cierre de la saga.', '2023-07-15'),
(3, 17, 5, 'Murakami me ha conquistado.', '2023-10-01'),
(4, 5, 4, 'Vargas Llosa siempre cumple.', '2023-05-20'),
(4, 6, 5, 'La mejor novela sobre Trujillo.', '2023-07-01'),
(5, 21, 5, 'King en su mejor momento. Da miedo de verdad.', '2023-06-20'),
(5, 22, 4, 'El hotel más terrorífico de la literatura.', '2023-08-10'),
(5, 23, 4, 'Tensión psicológica brutal.', '2023-10-01'),
(6, 1, 5, 'Macondo es eterno.', '2023-07-20'),
(6, 25, 5, 'Ferrante retrata la amistad como nadie.', '2023-09-01'),
(6, 26, 5, 'Continúa la magia del primero.', '2023-11-05'),
(7, 3, 4, 'Una saga familiar preciosa.', '2023-08-20'),
(7, 4, 5, 'Desgarrador y honesto.', '2023-10-01'),
(8, 7, 5, 'Mi novela favorita de misterio.', '2023-09-20'),
(8, 8, 4, 'Buena continuación.', '2023-11-01'),
(8, 12, 4, 'Pérez-Reverte sabe enganchar.', '2024-03-01'),
(9, 17, 5, 'Melancólico y bellísimo.', '2023-10-20'),
(9, 18, 5, 'Surrealismo en su mejor forma.', '2023-12-01'),
(9, 19, 3, 'Demasiado largo para mi gusto.', '2024-02-01'),
(10, 31, 5, 'Follett construye mundos completos.', '2023-11-20'),
(10, 32, 5, 'La continuación perfecta.', '2024-01-05'),
(10, 33, 4, 'Algo más floja pero buena.', '2024-03-10'),
(11, 7, 5, 'Cada relectura descubre algo nuevo.', '2023-12-20'),
(11, 35, 4, 'Buen thriller del País Vasco.', '2024-02-10'),
(11, 36, 4, 'Redondo mantiene el nivel.', '2024-04-01'),
(12, 1, 5, 'Un clásico que nunca falla.', '2024-01-20'),
(13, 21, 5, 'Lo leí en tres noches sin dormir.', '2024-02-15'),
(14, 27, 5, 'Patria es necesaria. Te remueve.', '2024-03-01'),
(15, 7, 4, 'Muy buena ambientación.', '2024-04-01'),
(15, 10, 5, 'Almudena Grandes, qué pérdida.', '2024-07-01'),
(16, 29, 4, 'Naturaleza y misterio bien mezclados.', '2024-05-01'),
(17, 17, 5, 'Releído y sigue emocionando.', '2024-06-01'),
(17, 19, 4, 'Ambicioso y bien resuelto.', '2024-09-01'),
(18, 5, 3, 'Densa pero interesante.', '2024-07-01'),
(19, 34, 5, 'El guardián invisible me atrapó.', '2024-08-01'),
(19, 35, 4, 'Sigue la tensión.', '2024-09-15'),
(20, 1, 5, 'Obra cumbre del realismo mágico.', '2024-09-10'),
(21, 25, 4, 'Amistad femenina muy bien retratada.', '2024-10-01'),
(22, 31, 5, 'Mil páginas que se hacen cortas.', '2024-11-05'),
(23, 7, 5, 'El mejor Zafón.', '2024-12-15'),
(24, 17, 4, 'Murakami me cuesta pero me gusta.', '2025-01-20'),
(25, 27, 5, 'Imprescindible para entender el conflicto vasco.', '2025-02-10'),
(26, 21, 4, 'Terror clásico bien hecho.', '2025-03-05'),
(27, 29, 5, 'Una joya escondida.', '2025-03-25'),
(28, 1, 5, 'Siempre vuelvo a Macondo.', '2025-05-01'),
(28, 7, 4, 'Misterio adictivo.', '2025-06-01'),
(29, 34, 5, 'Trilogía completa imprescindible.', '2025-06-01'),
(30, 17, 4, 'Bonito y melancólico.', '2025-07-01'),
(3, 18, 5, 'Mi Murakami favorito.', '2024-02-01'),
(5, 24, 3, 'El primer King, se nota.', '2023-12-01'),
(8, 13, 4, 'Misterio bibliófilo delicioso.', '2024-05-01'),
(11, 37, 4, 'Cierre redondo de la trilogía.', '2024-06-01'),
(16, 30, 4, 'Romance millennial bien escrito.', '2024-06-10'),
(19, 36, 5, 'Redondo es la reina del thriller español.', '2024-11-01'),
(22, 32, 5, 'Otra obra maestra de Follett.', '2024-12-20'),
(29, 35, 4, 'Mantiene la tensión del primero.', '2025-07-01');

-- ============================================================
-- VERIFICACIÓN
-- ============================================================

SELECT 'Tinta Eterna inicializada correctamente.' AS estado;
SELECT
    (SELECT COUNT(*) FROM editoriales) AS editoriales,
    (SELECT COUNT(*) FROM autores)     AS autores,
    (SELECT COUNT(*) FROM libros)      AS libros,
    (SELECT COUNT(*) FROM libro_autor) AS libro_autor,
    (SELECT COUNT(*) FROM lectores)    AS lectores,
    (SELECT COUNT(*) FROM compras)     AS compras,
    (SELECT COUNT(*) FROM resenas)     AS resenas;
