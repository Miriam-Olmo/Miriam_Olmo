-- ============================================================
-- BARRIOCUP — Liga de fútbol amateur
-- Script de inicialización para las 4 sesiones de SQL
-- Módulo: Bases de Datos Relacionales - Curso Big Data Iniciación
-- ============================================================
--   mysql -u root -p < barriocup_inicial.sql
-- ============================================================

DROP DATABASE IF EXISTS barriocup;
CREATE DATABASE barriocup CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE barriocup;

-- ============================================================
-- TABLAS
-- ============================================================

CREATE TABLE equipos (
    id INT UNSIGNED AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    ciudad VARCHAR(80),
    anyo_fundacion YEAR,
    estadio VARCHAR(100),
    entrenador VARCHAR(120),
    PRIMARY KEY (id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE jugadores (
    id INT UNSIGNED AUTO_INCREMENT,
    nombre VARCHAR(80) NOT NULL,
    apellidos VARCHAR(120) NOT NULL,
    fecha_nacimiento DATE,
    nacionalidad VARCHAR(50),
    posicion ENUM('portero','defensa','centrocampista','delantero') NOT NULL,
    dorsal TINYINT UNSIGNED,
    equipo_id INT UNSIGNED,
    PRIMARY KEY (id),
    FOREIGN KEY (equipo_id) REFERENCES equipos(id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE jornadas (
    id INT UNSIGNED AUTO_INCREMENT,
    numero TINYINT UNSIGNED NOT NULL,
    fecha DATE,
    PRIMARY KEY (id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE partidos (
    id INT UNSIGNED AUTO_INCREMENT,
    jornada_id INT UNSIGNED,
    fecha DATE,
    equipo_local_id INT UNSIGNED NOT NULL,
    equipo_visitante_id INT UNSIGNED NOT NULL,
    goles_local TINYINT UNSIGNED,
    goles_visitante TINYINT UNSIGNED,
    estadio VARCHAR(100),
    PRIMARY KEY (id),
    FOREIGN KEY (jornada_id) REFERENCES jornadas(id),
    FOREIGN KEY (equipo_local_id) REFERENCES equipos(id),
    FOREIGN KEY (equipo_visitante_id) REFERENCES equipos(id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE goles (
    id INT UNSIGNED AUTO_INCREMENT,
    partido_id INT UNSIGNED NOT NULL,
    jugador_id INT UNSIGNED NOT NULL,
    minuto TINYINT UNSIGNED,
    tipo ENUM('jugada','penalti','falta','propia') DEFAULT 'jugada',
    PRIMARY KEY (id),
    FOREIGN KEY (partido_id) REFERENCES partidos(id),
    FOREIGN KEY (jugador_id) REFERENCES jugadores(id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE sanciones (
    id INT UNSIGNED AUTO_INCREMENT,
    partido_id INT UNSIGNED NOT NULL,
    jugador_id INT UNSIGNED NOT NULL,
    minuto TINYINT UNSIGNED,
    tipo ENUM('amarilla','roja') NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (partido_id) REFERENCES partidos(id),
    FOREIGN KEY (jugador_id) REFERENCES jugadores(id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- ============================================================
-- EQUIPOS (8)
-- ============================================================

INSERT INTO equipos (nombre, ciudad, anyo_fundacion, estadio, entrenador) VALUES
('Atlético Tetuán',   'Madrid',     1998, 'Campo de la Mina',       'Andrés Paredes'),
('Racing del Sur',    'Sevilla',    2002, 'La Bombonera Chica',     'Manuel Quirós'),
('CD Lavapiés',       'Madrid',     2005, 'Estadio del Mercado',    'Toni Berenguer'),
('Unión Vallekana',   'Madrid',     1995, 'Campo de Vallecas Bajo', 'Luis Mardones'),
('Sporting Triana',   'Sevilla',    2008, 'El Arenal',              'Rubén Castaño'),
('Real Carabanchel',  'Madrid',     2000, 'La Carolina',            'Iván Robledo'),
('Atlético Macarena', 'Sevilla',    2010, 'San Gil',                'Pedro Calderón'),
('CF Malasaña',       'Madrid',     2012, 'Campo 2 de Mayo',        'Sergio Valverde');

-- ============================================================
-- JUGADORES (~96, 12 por equipo)
-- ============================================================

INSERT INTO jugadores (nombre, apellidos, fecha_nacimiento, nacionalidad, posicion, dorsal, equipo_id) VALUES
-- Equipo 1: Atlético Tetuán
('Mario',   'Gil Ortega',       '1998-04-12', 'España',    'portero',        1,  1),
('David',   'Romero Paz',       '1996-07-23', 'España',    'defensa',        2,  1),
('Sergio',  'Luna Vega',        '1999-01-05', 'España',    'defensa',        4,  1),
('Hugo',    'Marín Soto',       '1997-11-18', 'España',    'centrocampista', 8,  1),
('Iker',    'Pardo León',       '2000-03-30', 'España',    'centrocampista', 10, 1),
('Adam',    'Benali',           '1998-09-14', 'Marruecos', 'delantero',      9,  1),
('Pablo',   'Sanz Ruiz',        '1995-06-08', 'España',    'delantero',      7,  1),
('Leo',     'Costa Silva',      '1999-12-22', 'Brasil',    'centrocampista', 6,  1),
('Jorge',   'Vidal Cano',       '1997-02-17', 'España',    'defensa',        3,  1),
('Marco',   'Rossi',            '1996-08-09', 'Italia',    'delantero',      11, 1),
('Unai',    'Etxeberria',       '2001-05-19', 'España',    'centrocampista', 14, 1),
('Diego',   'Mora Sáez',        '1998-10-03', 'España',    'portero',        13, 1),
-- Equipo 2: Racing del Sur
('Antonio', 'Ramírez Gil',      '1997-03-11', 'España',    'portero',        1,  2),
('Curro',   'Delgado Vázquez',  '1996-05-27', 'España',    'defensa',        2,  2),
('Joaquín', 'Herrera Luna',     '1998-08-14', 'España',    'defensa',        5,  2),
('Manu',    'Castro Pino',      '1999-04-02', 'España',    'centrocampista', 8,  2),
('Rafa',    'Ojeda Sol',        '1995-11-30', 'España',    'delantero',      9,  2),
('Brahim',  'El Amrani',        '2000-07-08', 'Marruecos', 'delantero',      7,  2),
('Pedro',   'Salas Romero',     '1997-09-21', 'España',    'centrocampista', 10, 2),
('Diego',   'Acosta Vela',      '1998-01-16', 'Argentina', 'centrocampista', 6,  2),
('Nacho',   'Reina Bravo',      '1999-06-25', 'España',    'defensa',        3,  2),
('Samu',    'Ndiaye',           '2001-02-13', 'Senegal',   'delantero',      11, 2),
('Álvaro',  'Cano Ferrer',      '1996-12-04', 'España',    'centrocampista', 14, 2),
('Lucas',   'Prieto Marín',     '2000-10-19', 'España',    'portero',        13, 2),
-- Equipo 3: CD Lavapiés
('Omar',    'Farah',            '1998-06-07', 'Somalia',   'portero',        1,  3),
('Raúl',    'Méndez Soto',      '1997-08-23', 'España',    'defensa',        4,  3),
('Yassine', 'Bouzid',           '1999-03-15', 'Marruecos', 'defensa',        2,  3),
('Cheng',   'Liu Wei',          '1996-09-29', 'China',     'centrocampista', 8,  3),
('Tomás',   'Iglesias Paz',     '2000-05-11', 'España',    'centrocampista', 10, 3),
('Dani',    'Ferreira Lima',    '1998-11-26', 'Portugal',  'delantero',      9,  3),
('Karim',   'Toure',            '1999-07-04', 'Costa de Marfil', 'delantero', 7, 3),
('Víctor',  'Núñez Salas',      '1997-01-19', 'España',    'centrocampista', 6,  3),
('Aarón',   'Crespo Vidal',     '2001-04-08', 'España',    'defensa',        3,  3),
('Saul',    'Ayala Ruiz',       '1996-10-13', 'España',    'delantero',      11, 3),
('Edu',     'Lozano Gil',       '2000-12-30', 'España',    'centrocampista', 14, 3),
('Marcos',  'Pena Vega',        '1998-02-22', 'España',    'portero',        13, 3),
-- Equipo 4: Unión Vallekana
('Fran',    'Quesada Mora',     '1997-05-09', 'España',    'portero',        1,  4),
('Álex',    'Tirado Sanz',      '1998-09-17', 'España',    'defensa',        2,  4),
('Borja',   'Calvo Ríos',       '1996-04-25', 'España',    'defensa',        4,  4),
('Mate',    'Kovač',            '1999-08-02', 'Croacia',   'centrocampista', 8,  4),
('Cristian','Bravo Lara',       '2000-02-14', 'España',    'centrocampista', 10, 4),
('Moussa',  'Diallo',           '1998-11-07', 'Mali',      'delantero',      9,  4),
('Javi',    'Olmo Sáez',        '1995-07-21', 'España',    'delantero',      7,  4),
('Nico',    'Domínguez Paz',    '1999-10-28', 'España',    'centrocampista', 6,  4),
('Rubén',   'Vega Castro',      '1997-03-06', 'España',    'defensa',        3,  4),
('Pol',     'Serra Mas',        '2001-06-12', 'España',    'delantero',      11, 4),
('Gorka',   'Aguirre Lizar',    '1996-12-19', 'España',    'centrocampista', 14, 4),
('Iván',    'Soler Ric',        '2000-09-23', 'España',    'portero',        13, 4),
-- Equipo 5: Sporting Triana
('Paco',    'Jiménez Roca',     '1997-07-15', 'España',    'portero',        1,  5),
('Salva',   'Moreno Gil',       '1998-03-28', 'España',    'defensa',        2,  5),
('Álvaro',  'Ruano Sol',        '1996-06-11', 'España',    'defensa',        5,  5),
('Lamine',  'Cissé',            '2000-01-24', 'Senegal',   'centrocampista', 8,  5),
('Jesús',   'Pavón Luna',       '1999-09-08', 'España',    'centrocampista', 10, 5),
('Bryan',   'Mosquera',         '1998-12-16', 'Colombia',  'delantero',      9,  5),
('Manu',    'Vela Cruz',        '1995-04-03', 'España',    'delantero',      7,  5),
('Adri',    'Cabello Mora',     '1999-11-21', 'España',    'centrocampista', 6,  5),
('Fer',     'Salgado Vega',     '1997-08-30', 'España',    'defensa',        3,  5),
('Iñaki',   'Beristain',        '2001-05-07', 'España',    'delantero',      11, 5),
('Quique',  'Ramos Pino',       '1996-02-18', 'España',    'centrocampista', 14, 5),
('Dani',    'Casas Bravo',      '2000-10-09', 'España',    'portero',        13, 5),
-- Equipo 6: Real Carabanchel
('Sergio',  'Lara Vidal',       '1997-04-19', 'España',    'portero',        1,  6),
('Juanmi',  'Pozo Sáez',        '1998-08-26', 'España',    'defensa',        2,  6),
('Ismael',  'Haddad',           '1999-02-13', 'Argelia',   'defensa',        4,  6),
('Marc',    'Vila Roig',        '1996-10-05', 'España',    'centrocampista', 8,  6),
('Aitor',   'Méndez Sol',       '2000-06-22', 'España',    'centrocampista', 10, 6),
('Cristo',  'Santana Pérez',    '1998-12-09', 'España',    'delantero',      9,  6),
('Luka',    'Petrović',         '1997-07-17', 'Serbia',    'delantero',      7,  6),
('Pau',     'Camps Ferrer',     '1999-05-30', 'España',    'centrocampista', 6,  6),
('Mohamed', 'Sylla',            '2001-01-11', 'Guinea',    'defensa',        3,  6),
('Joel',    'Ríos Marín',       '1996-09-24', 'España',    'delantero',      11, 6),
('Asier',   'Goikoetxea',       '2000-03-15', 'España',    'centrocampista', 14, 6),
('Toni',    'Bravo Luna',       '1997-11-02', 'España',    'portero',        13, 6),
-- Equipo 7: Atlético Macarena
('José',    'Carrasco Gil',     '1998-05-21', 'España',    'portero',        1,  7),
('Migue',   'Reyes Pino',       '1997-09-13', 'España',    'defensa',        2,  7),
('Alfonso', 'León Vázquez',     '1996-03-27', 'España',    'defensa',        5,  7),
('Wagner',  'Souza',            '1999-07-09', 'Brasil',    'centrocampista', 8,  7),
('Álex',    'Mota Sol',         '2000-11-16', 'España',    'centrocampista', 10, 7),
('Cheikh',  'Gueye',            '1998-02-04', 'Senegal',   'delantero',      9,  7),
('Rafa',    'Bermejo Ruiz',     '1995-08-28', 'España',    'delantero',      7,  7),
('Dani',    'Gálvez Mora',      '1999-04-15', 'España',    'centrocampista', 6,  7),
('Pepe',    'Lara Soto',        '1997-12-23', 'España',    'defensa',        3,  7),
('Tahar',   'Mansouri',         '2001-06-30', 'Túnez',     'delantero',      11, 7),
('Curro',   'Vega Pino',        '1996-10-12', 'España',    'centrocampista', 14, 7),
('Nando',   'Salas Gil',        '2000-08-19', 'España',    'portero',        13, 7),
-- Equipo 8: CF Malasaña
('Bruno',   'Castaño Vidal',    '1998-07-08', 'España',    'portero',        1,  8),
('Eric',    'Pons Mas',         '1997-11-25', 'España',    'defensa',        2,  8),
('Gabriel', 'Mendes',           '1999-05-13', 'Portugal',  'defensa',        4,  8),
('Teo',     'Navarro Sol',      '1996-01-29', 'España',    'centrocampista', 8,  8),
('Marcos',  'Gil Pardo',        '2000-09-06', 'España',    'centrocampista', 10, 8),
('Aymane',  'Tazi',             '1998-03-18', 'Marruecos', 'delantero',      9,  8),
('Guille',  'Ortiz Vega',       '1995-12-01', 'España',    'delantero',      7,  8),
('Nil',     'Roca Camps',       '1999-08-24', 'España',    'centrocampista', 6,  8),
('Hassan',  'Jallow',           '2001-04-11', 'Gambia',    'defensa',        3,  8),
('Iago',    'Vázquez Pena',     '1996-06-17', 'España',    'delantero',      11, 8),
('Pol',     'Estévez Ruiz',     '2000-02-28', 'España',    'centrocampista', 14, 8),
('Dani',    'Moreno Paz',       '1997-10-15', 'España',    'portero',        13, 8);

-- ============================================================
-- JORNADAS (7)
-- ============================================================

INSERT INTO jornadas (numero, fecha) VALUES
(1, '2024-09-15'),
(2, '2024-09-22'),
(3, '2024-09-29'),
(4, '2024-10-06'),
(5, '2024-10-20'),
(6, '2024-10-27'),
(7, '2024-11-03');

-- ============================================================
-- PARTIDOS (28: 4 por jornada x 7 jornadas)
-- ============================================================

INSERT INTO partidos (jornada_id, fecha, equipo_local_id, equipo_visitante_id, goles_local, goles_visitante, estadio) VALUES
-- Jornada 1
(1, '2024-09-15', 1, 2, 2, 1, 'Campo de la Mina'),
(1, '2024-09-15', 3, 4, 0, 0, 'Estadio del Mercado'),
(1, '2024-09-15', 5, 6, 3, 2, 'El Arenal'),
(1, '2024-09-15', 7, 8, 1, 1, 'San Gil'),
-- Jornada 2
(2, '2024-09-22', 2, 3, 2, 2, 'La Bombonera Chica'),
(2, '2024-09-22', 4, 5, 1, 3, 'Campo de Vallecas Bajo'),
(2, '2024-09-22', 6, 7, 0, 1, 'La Carolina'),
(2, '2024-09-22', 8, 1, 2, 4, 'Campo 2 de Mayo'),
-- Jornada 3
(3, '2024-09-29', 1, 3, 3, 0, 'Campo de la Mina'),
(3, '2024-09-29', 2, 4, 1, 1, 'La Bombonera Chica'),
(3, '2024-09-29', 5, 7, 2, 2, 'El Arenal'),
(3, '2024-09-29', 6, 8, 1, 0, 'La Carolina'),
-- Jornada 4
(4, '2024-10-06', 3, 5, 1, 2, 'Estadio del Mercado'),
(4, '2024-10-06', 4, 6, 2, 2, 'Campo de Vallecas Bajo'),
(4, '2024-10-06', 7, 1, 0, 2, 'San Gil'),
(4, '2024-10-06', 8, 2, 3, 3, 'Campo 2 de Mayo'),
-- Jornada 5
(5, '2024-10-20', 1, 4, 4, 1, 'Campo de la Mina'),
(5, '2024-10-20', 2, 5, 0, 1, 'La Bombonera Chica'),
(5, '2024-10-20', 3, 6, 2, 1, 'Estadio del Mercado'),
(5, '2024-10-20', 7, 8, 2, 0, 'San Gil'),
-- Jornada 6
(6, '2024-10-27', 4, 7, 1, 1, 'Campo de Vallecas Bajo'),
(6, '2024-10-27', 5, 8, 3, 1, 'El Arenal'),
(6, '2024-10-27', 6, 1, 0, 3, 'La Carolina'),
(6, '2024-10-27', 2, 3, 2, 0, 'La Bombonera Chica'),
-- Jornada 7
(7, '2024-11-03', 1, 5, 1, 1, 'Campo de la Mina'),
(7, '2024-11-03', 3, 7, 2, 3, 'Estadio del Mercado'),
(7, '2024-11-03', 4, 8, 2, 1, 'Campo de Vallecas Bajo'),
(7, '2024-11-03', 6, 2, 1, 2, 'La Carolina');

-- ============================================================
-- GOLES (~88) - jugador_id coherente con su equipo
-- ============================================================

INSERT INTO goles (partido_id, jugador_id, minuto, tipo) VALUES
-- P1 Tetuán 2-1 Racing (locales: 1-12, visit: 13-24)
(1, 6, 23, 'jugada'), (1, 7, 67, 'jugada'), (1, 17, 81, 'penalti'),
-- P3 Triana 3-2 Carabanchel (loc 49-60, vis 61-72)
(3, 53, 12, 'jugada'), (3, 53, 40, 'jugada'), (3, 55, 78, 'penalti'), (3, 66, 55, 'jugada'), (3, 67, 88, 'jugada'),
-- P4 Macarena 1-1 Malasaña (loc 73-84, vis 85-96)
(4, 78, 34, 'jugada'), (4, 90, 71, 'jugada'),
-- P5 Racing 2-2 Lavapiés (loc 13-24, vis 25-36)
(5, 17, 15, 'jugada'), (5, 18, 52, 'jugada'), (5, 30, 44, 'jugada'), (5, 31, 90, 'penalti'),
-- P6 Vallekana 1-3 Triana (loc 37-48, vis 49-60)
(6, 42, 28, 'jugada'), (6, 53, 33, 'jugada'), (6, 54, 60, 'jugada'), (6, 53, 85, 'penalti'),
-- P7 Carabanchel 0-1 Macarena
(7, 78, 73, 'jugada'),
-- P8 Malasaña 2-4 Tetuán
(8, 90, 20, 'jugada'), (8, 91, 65, 'jugada'), (8, 6, 30, 'jugada'), (8, 6, 50, 'jugada'), (8, 7, 70, 'jugada'), (8, 10, 88, 'penalti'),
-- P9 Tetuán 3-0 Lavapiés
(9, 6, 18, 'jugada'), (9, 7, 44, 'jugada'), (9, 10, 76, 'jugada'),
-- P10 Racing 1-1 Vallekana
(10, 18, 39, 'jugada'), (10, 42, 81, 'jugada'),
-- P11 Triana 2-2 Macarena
(11, 53, 22, 'jugada'), (11, 54, 67, 'jugada'), (11, 78, 11, 'jugada'), (11, 80, 90, 'penalti'),
-- P12 Carabanchel 1-0 Malasaña
(12, 66, 58, 'jugada'),
-- P13 Lavapiés 1-2 Triana
(13, 30, 25, 'jugada'), (13, 53, 49, 'jugada'), (13, 55, 83, 'jugada'),
-- P14 Vallekana 2-2 Carabanchel
(14, 42, 14, 'jugada'), (14, 43, 60, 'jugada'), (14, 66, 35, 'jugada'), (14, 67, 78, 'penalti'),
-- P15 Macarena 0-2 Tetuán
(15, 6, 40, 'jugada'), (15, 7, 75, 'jugada'),
-- P16 Malasaña 3-3 Racing
(16, 90, 12, 'jugada'), (16, 91, 48, 'jugada'), (16, 90, 70, 'penalti'), (16, 17, 30, 'jugada'), (16, 18, 55, 'jugada'), (16, 22, 89, 'jugada'),
-- P17 Tetuán 4-1 Vallekana
(17, 6, 10, 'jugada'), (17, 6, 33, 'jugada'), (17, 7, 55, 'jugada'), (17, 10, 80, 'penalti'), (17, 42, 66, 'jugada'),
-- P18 Racing 0-1 Triana
(18, 53, 72, 'jugada'),
-- P19 Lavapiés 2-1 Carabanchel
(19, 30, 28, 'jugada'), (19, 31, 64, 'jugada'), (19, 66, 88, 'penalti'),
-- P20 Macarena 2-0 Malasaña
(20, 78, 19, 'jugada'), (20, 80, 70, 'jugada'),
-- P21 Vallekana 1-1 Macarena
(21, 42, 44, 'jugada'), (21, 78, 81, 'jugada'),
-- P22 Triana 3-1 Malasaña
(22, 53, 15, 'jugada'), (22, 54, 50, 'jugada'), (22, 55, 77, 'penalti'), (22, 90, 62, 'jugada'),
-- P23 Carabanchel 0-3 Tetuán
(23, 6, 25, 'jugada'), (23, 7, 55, 'jugada'), (23, 10, 84, 'jugada'),
-- P24 Racing 2-0 Lavapiés
(24, 17, 33, 'jugada'), (24, 18, 71, 'jugada'),
-- P25 Tetuán 1-1 Triana
(25, 6, 48, 'jugada'), (25, 53, 79, 'penalti'),
-- P26 Lavapiés 2-3 Macarena
(26, 30, 20, 'jugada'), (26, 31, 60, 'jugada'), (26, 78, 35, 'jugada'), (26, 80, 70, 'jugada'), (26, 78, 88, 'penalti'),
-- P27 Vallekana 2-1 Malasaña
(27, 42, 30, 'jugada'), (27, 43, 65, 'jugada'), (27, 90, 82, 'jugada'),
-- P28 Carabanchel 1-2 Racing
(28, 66, 40, 'jugada'), (28, 17, 55, 'jugada'), (28, 18, 88, 'penalti');

-- ============================================================
-- SANCIONES (~46)
-- ============================================================

INSERT INTO sanciones (partido_id, jugador_id, minuto, tipo) VALUES
(1, 2, 35, 'amarilla'), (1, 14, 60, 'amarilla'), (1, 9, 88, 'roja'),
(3, 52, 40, 'amarilla'), (3, 62, 75, 'amarilla'),
(5, 19, 50, 'amarilla'), (5, 27, 82, 'amarilla'),
(8, 85, 25, 'amarilla'), (8, 3, 55, 'amarilla'),
(9, 26, 44, 'amarilla'), (9, 27, 70, 'roja'),
(11, 51, 33, 'amarilla'), (11, 75, 66, 'amarilla'),
(13, 25, 20, 'amarilla'), (13, 51, 80, 'amarilla'),
(14, 38, 55, 'amarilla'), (14, 62, 90, 'amarilla'),
(16, 86, 30, 'amarilla'), (16, 14, 60, 'amarilla'), (16, 14, 85, 'roja'),
(17, 38, 40, 'amarilla'),
(19, 26, 48, 'amarilla'), (19, 63, 77, 'amarilla'),
(20, 87, 35, 'amarilla'),
(22, 86, 50, 'amarilla'), (22, 49, 70, 'amarilla'),
(23, 62, 22, 'amarilla'), (23, 63, 66, 'roja'),
(26, 25, 40, 'amarilla'), (26, 73, 60, 'amarilla'), (26, 75, 88, 'amarilla'),
(28, 61, 33, 'amarilla'), (28, 13, 70, 'amarilla');

-- ============================================================
-- VERIFICACIÓN
-- ============================================================

SELECT 'BarrioCup inicializada correctamente.' AS estado;
SELECT
    (SELECT COUNT(*) FROM equipos)   AS equipos,
    (SELECT COUNT(*) FROM jugadores) AS jugadores,
    (SELECT COUNT(*) FROM jornadas)  AS jornadas,
    (SELECT COUNT(*) FROM partidos)  AS partidos,
    (SELECT COUNT(*) FROM goles)     AS goles,
    (SELECT COUNT(*) FROM sanciones) AS sanciones;
