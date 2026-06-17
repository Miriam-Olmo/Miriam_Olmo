/*
 * sintaxis 
 * UPDATE nombre_tabla
 * SET columna=valornuevo [,col2=valorn2, col3=valorn3...]
 * [WHERE condicion];
 *
 */

update alumnos 
set nombre="jacinta"
where id=2;

-- muestra todos los registros de la tabla que pongas, si pones where solo muestra el que eliges
select *from alumnos
where id=2;

-- insertar 5 cursos (nombre,precio, horas)

insert into cursos (nombre, precio, horas)
values
	("aquagym", 20.5, 30),
	("waterpolo", 90, 100),
	("natacion artistica", 600, 500),
	("buceo", 80, 50),
	("padelsurf", 500, 300);
select * from cursos;

-- actualizar todos los precios de los cursos que tengan mas de 50 horas
update cursos
set precio=900
where horas>=50;
select * from cursos;