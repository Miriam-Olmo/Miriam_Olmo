-- INSERT

insert into equipos (nombre, ciudad, anyo_fundacion, estadio, entrenador)
values ('deportivo usera', "madrid", 2015, "la meseta", "quique hidalgo");

-- UPDATE

update jugadores
set dorsal=21
where id=5;

-- prueba de WHERE
select * from jugadores
where id=5

-- update cambiar el estadio de todos los partidos de un equipo: 
-- pon el estadio provisional a todos los partidos
-- donde el equipo 8 sea local

update partidos
set estadio='estadio provisional' 
where equipo_local_id=8;

select * from partidos
where equipo_local_id=8;

-- Cambiar a 'falta' el tipo de todos 
-- los goles que ahora son 'penalti' en el partido 17.

update goles
set tipo="falta"
where tipo='penalti' and partido_id=17;

select * from goles
where tipo='penalti' and partido_id=17;


 
-- DELETE

delete from equipos 
where id=9;

select * from equipos where id=9;


-- Borrar todos los goles anteriores 
-- al minuto 15 (goles tempranos).
delete from goles 
where minuto<15;

select * from goles where minuto<15;

-- Borrar todas las sanciones del jugador 27.
delete from sanciones 
where jugador_id=27;

select * from sanciones where jugador_id=27;

-- Borrar el jugador 96

delete from jugadores
where id=96;

select * from jugadores where id=96;


