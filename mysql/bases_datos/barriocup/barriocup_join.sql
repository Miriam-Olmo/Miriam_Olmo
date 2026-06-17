
-- sin join
select 
g.id, 
g.partido_id, 
g.minuto, 
g.tipo, 
concat(j.nombre, ' ', j.apellidos) nombre_completo
from goles g, jugadores j
where g.jugador_id = j.id;

-- con JOIN
select 
g.id, 
g.partido_id, 
g.minuto, 
g.tipo, 
concat(j.nombre, ' ', j.apellidos) nombre_jugador
from goles g
join jugadores j on g.jugador_id = j.id;

-- INNER JOIN (mezcla ambas tablas y devuelve los resultados que no esten en blanco)
select 
g.id, 
g.partido_id, 
g.minuto, 
g.tipo, 
concat(j.nombre, ' ', j.apellidos) nombre_jugador
from goles g
inner join jugadores j on g.jugador_id = j.id;

-- Cada jugador con el nombre de su equipo.

select j.id,
concat(j.nombre, ' ', j.apellidos) nombre_completo,
e.nombre nombre_equipo
from jugadores j 
inner join equipos e on j.equipo_id = e.id;

-- El pichichi con NOMBRE: goleadores ordenados, mostrando nombre y número de goles
select
j.id,
concat(j.nombre, ' ', j.apellidos) nombre_completo_j,
count(g.id ) goles
from jugadores j
inner join goles g on j.id = g.jugador_id
group by  j.id
order by goles desc
limit 5;

-- Goleadores con su nombre y el de su CLUB
select j.nombre,
j.apellidos,
e.nombre nombre_equipo,
count(g.id) goles
from jugadores j
inner join goles g on j. id = g.jugador_id 
inner join equipos e on j.equipo_id = e.id
group by j.id;

-- Cada sanción con el nombre del jugador sancionado y el tipo de tarjeta.
select j.id,
concat(j.nombre, ' ', j.apellidos) nombre_completo,
s.tipo
from sanciones s
inner join jugadores j on s.jugador_id = j.id
order by j.id asc;
-- Lista de porteros con el nombre de su equipo.
select j.id,
j.equipo_id,
concat(j. nombre, ' ', j.apellidos) nombre_jugador,
j.posicion posicion,
e.nombre nombre_equipo
from jugadores j
inner join equipos e on j.equipo_id = e.id
where j.posicion = 'portero'
order by j.equipo_id ;


-- Número de jugadores por equipo, mostrando el NOMBRE del equipo
select 
e.nombre nombre_equipo,
count(j.id) jugadores_por_equipo
from equipos e
inner join jugadores j on e.id = j.equipo_id
group by e.id; 
-- Número de goles por equipo
select count(g.id) goles,
e.nombre
from goles g
inner join jugadores j on g.jugador_id = j.id
inner join equipos e on e.id = j.equipo_id 
group by e.id;
-- Goles del partido 17 con el nombre del goleador.
select
g.id,
g.partido_id,
g.minuto,
concat(j.nombre , ' ', j.apellidos) nombre_goleador
from goles g
inner join jugadores j on g.jugador_id = j.id
where g.partido_id = 17
order by g.minuto asc;

-- Goleadores con más de 3 goles, con su nombre y club
select 
j.nombre nombre_jugador,
e.nombre nombre_equipo,
count(g.id) goles
from jugadores j
inner join goles g on j.id = g.jugador_id
inner join equipos e on j.equipo_id = e.id
group by j.id 
having goles>3;

-- Goles por nacionalidad del goleador

select count(g.id) goles,
j.nacionalidad  nacionalidad
from goles g
inner join jugadores j on g.jugador_id = j.id 
group by j.nacionalidad
order by goles desc;


-- LEFT JOIN
-- jugadores que no han metido ningun gol
select *
from jugadores j
left join goles g on j.id = g.jugador_id
where g.id is null
and j.posicion <> 'portero';
-- todos los equipos y cuantos jugadores tienen
select e.nombre, count(j.id)
from equipos e
left join jugadores j on e.id = j.equipo_id
group by e.id;


insert into equipos (nombre, ciudad, entrenador, anyo_fundacion, estadio)
values ('Puerta Bonita', 'Madrid', 'Quique Sanchez Flores', 1923, 'Oporto');


-- Jugadores que nunca han sido sancionados
select j.nombre, j.apellidos
from jugadores j
left join sanciones s on j.id = s.jugador_id
where s.id is null;
-- Todos los jugadores con el número de goles que han marcado
select j.nombre,
j.apellidos,
count(g.id) goles
from jugadores j
left join goles g on j.id = g.jugador_id
group by j.id
order by goles asc;

-- cada partido mostrando el nombre del equipo local y del visitante
select p.id,
local.nombre,
visitante.nombre,
p.fecha,
concat(local.nombre, ' ', p.goles_local, ' - ', p.goles_visitante, ' ', visitante.nombre) resultado
from partidos p
inner join equipos local on p.equipo_local_id = local.id
inner join equipos visitante on p.equipo_visitante_id = visitante.id;

-- Todos los partidos del Atlético Tetuán (id 1), jueguen de local o de visitante, con el nombre del rival.
select p.id,
p.fecha,
local.nombre equipo_local,
visitante.nombre equipo_visitante
from partidos p
inner join equipos local on p.equipo_local_id = local.id 
inner join equipos visitante on p.equipo_visitante_id = visitante.id
where p.equipo_local_id = 1
or p.equipo_visitante_id = 1;
-- Partidos donde ganó el visitante, mostrando los nombres de ambos equipos.
select p.id,
local.nombre,
p.goles_local,
p.goles_visitante,
visitante.nombre 
from partidos p
inner join equipos local on p.equipo_local_id = local.id 
inner join equipos visitante on p.equipo_visitante_id = visitante.id
where p.goles_visitante > p.goles_local; 

select jugador_id
from goles g 
where partido_id = 1;

select nombre, apellidos
from jugadores j
where j.id in(
	select jugador_id
	from goles
	where partido_id = 1
);

-- jugadores que nunca han marcado

select distinct jugador_id
from goles g;

select nombre, apellidos
from jugadores j 
where id not in (
	select distinct jugador_id
	from goles g
);


-- El equipo con el año de fundación más antiguo
select min(anyo_fundacion )
from equipos e;

select nombre, anyo_fundacion
from equipos e 
where e.anyo_fundacion  = (
	select min(anyo_fundacion )
	from equipos e
);

-- Partidos con más goles que la media de goles totales por partido.
select round(avg(goles_local + goles_visitante), 2) media_goles
from partidos;

select id, goles_local + goles_visitante 
from partidos 
where goles_local + goles_visitante > (
	select round(avg(goles_local + goles_visitante), 2) media_goles
	from partidos
);
