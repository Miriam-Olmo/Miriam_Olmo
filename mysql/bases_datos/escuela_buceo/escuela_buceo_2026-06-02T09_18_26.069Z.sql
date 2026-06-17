CREATE TABLE IF NOT EXISTS `alumnos` (
	`id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
	`nombre` VARCHAR(255),
	`email` VARCHAR(255) UNIQUE,
	`telefono` VARCHAR(255) NOT NULL,
	`contacto_emergencia` VARCHAR(255),
	`fecha_nacimiento` DATE,
	PRIMARY KEY(`id`)
);


CREATE TABLE IF NOT EXISTS `cursos` (
	`id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
	`nombre` VARCHAR(255),
	`precio` DECIMAL(6,2),
	`horas` SMALLINT,
	`curso_pre_id` INTEGER,
	PRIMARY KEY(`id`)
);


CREATE TABLE IF NOT EXISTS `instructores` (
	`id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
	`nombre` VARCHAR(255),
	`email` VARCHAR(255) NOT NULL UNIQUE,
	`año_certificacion` YEAR,
	PRIMARY KEY(`id`)
);


CREATE TABLE IF NOT EXISTS `instructores_cursos` (
	`id_instructor` INTEGER NOT NULL,
	`id_curso` INTEGER NOT NULL,
	PRIMARY KEY(`id_instructor`, `id_curso`)
);


CREATE TABLE IF NOT EXISTS `matricula` (
	`id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
	`id_alumno` INTEGER NOT NULL,
	`id_curso` INTEGER NOT NULL,
	`id_instructor` INTEGER NOT NULL,
	`fecha_inicio` DATETIME,
	`fecha_fin` DATETIME,
	`nota` DECIMAL,
	PRIMARY KEY(`id`)
);


ALTER TABLE `instructores`
ADD FOREIGN KEY(`id`) REFERENCES `instructores_cursos`(`id_instructor`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `cursos`
ADD FOREIGN KEY(`id`) REFERENCES `instructores_cursos`(`id_curso`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `alumnos`
ADD FOREIGN KEY(`id`) REFERENCES `matricula`(`id_alumno`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `cursos`
ADD FOREIGN KEY(`id`) REFERENCES `matricula`(`id_curso`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `instructores`
ADD FOREIGN KEY(`id`) REFERENCES `matricula`(`id_instructor`)
ON UPDATE NO ACTION ON DELETE NO ACTION;