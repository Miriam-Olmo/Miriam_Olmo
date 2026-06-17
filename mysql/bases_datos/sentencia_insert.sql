/* sintaxis del INSERT
 * 
 * INSERT INTO nombre_tabla (col1, col2, col3...)
 * VALUES (valor_col1, valor_col2, valor_col3...)
 */

insert into alumnos (nombre, email, telefono, contacto_emergencia, fecha_nacimiento)
values ("manolo", "eldelbombo@gmail.com", "620603569","666954625", "2001-05-29");
-- ver todos los registros de la tabla alumnos
select * from alumnos;

-- INSERT multiple sobre la tabla instructores
insert into instructores (nombre, email, año_certificacion)
values 
	("felipe", "felipon@gmail.com", "1998"),
	("mortadelo", "elbuti@gmail.com", "1995"),
	("filomena", "lafilo@gmail.com", "2000");

select * from instructores;
