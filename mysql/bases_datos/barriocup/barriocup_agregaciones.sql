-- contar cuantos jugadores hay en la liga
select count(*) as total_jugadores
from jugadores; 

-- cuantos goles hay
select count(*) as goles_totales
from goles;

-- MAX MIN
select max(minuto) as gol_tardio, 
min(minuto) as gol_tempranero,
count(*) as num_goles 
from goles; 

-- AVG (AVERAGE)
select round(AVG(p.goles_local), 2) media_goles_local
from partidos p; 

-- ¿Cuál es la media del minuto en el que se marcan los goles?
select avg(minuto) media_minuto_gol
from goles;

-- ¿Cuántos jugadores distintos han marcado al menos un gol?
select count(distinct(jugador_id)) jugadores_goleadores
from goles;
-- ¿Cuántos goles de penalti se han marcado?
select count(*) as penaltis_marcados
from goles
where tipo='penalti';

-- todos los goles marcados
select sum(goles_local + goles_visitante ) as goles_totales
from partidos

-- COUNT, SUM, AVG, MAX, MIN


-- GROUP BY

-- cuantos jugadores tiene cada equipo?
select equipo_id, count(*) as num_jugadores
from jugadores
group by equipo_id; 

-- ¿ cuantos jugadores hay por cada posicion
select posicion, count(*) as numero_jugadores
from jugadores
group by posicion;

-- ¿que jugador es el pichichi?
select jugador_id, 
count(*) as goles,
max(minuto) as mas_tardio,
min(minuto) as mas_tempranero
from goles
group by jugador_id
order by goles desc;


-- Número de goles por tipo (jugada, penalti, falta, propia).
select tipo, count(*) as tipo_goles
from goles
group by tipo;
-- Número de goles en cada partido
select partido_id, count(*) as goles_partido
from goles
group by partido_id
order by goles.partido_id asc;
-- Media de minuto de los goles agrupada por tipo de gol.
select tipo, round(avg(minuto), 2) as media_minuto
from goles
group by tipo
order by media_minuto asc;


-- numero de jugadores por equipo y posicion
select equipo_id, posicion, count(*) cantidad_por_posicion
from jugadores j 
group by equipo_id, posicion;

-- numero de porteros y delantero por equipo
select equipo_id, posicion, count(*) cantidad_por_posicion
from jugadores j 
where posicion in ('portero', 'delantero')
group by equipo_id, posicion;

-- HAVING (filtrar despues de haber agrupado con group by)

-- numero de goles por jugador pero solo si ga metido mas de 3 goles
select jugador_id, count(*) as num_goles
from goles
group by jugador_id
having num_goles > 3;

-- nacionalidad con mas de 5 jugadores
select distinct nacionalidad, count(*) as nacionalidad_jug
from jugadores
group by nacionalidad
having  nacionalidad_jug >5;

-- Jugadores con 2 o más tarjetas
select jugador_id, count(*) as sanciones_jugador
from sanciones
group by jugador_id
having sanciones_jugador > 2;
-- Tipos de gol que se han dado más de 10 veces.
select tipo, count(*) as goles_tipo
from goles
group by tipo
having goles_tipo > 10;
-- Jornadas cuya suma de goles del local supera los 6.
select jornada_id, sum(goles_local) as goles_jornada
from partidos
group by jornada_id
having goles_jornada >6;
-- Posiciones con menos de 25 jugadores
select posicion, count(*) as posicion_m
from jugadores
group by posicion
having posicion_m < 25
order by posicion_m asc ;

-- Entre los goles que NO son de penalti, jugadores con más de 2 goles
select jugador_id, count(*) as gol_jugador
from goles
where tipo <> 'penalti'
group by jugador_id
having gol_jugador > 2;

-- Considerando solo las amarillas, jugadores con 2 o más amarillas.
select jugador_id, count(*) as amarillas
from sanciones
where tipo = 'amarilla'
group by jugador_id
having amarillas >= 2;

-- consulta usando como subconsulta una anterior
select nombre, apellidos
from jugadores
where id in (
	select jugador_id
	from sanciones
	where tipo = 'amarilla'
	group by jugador_id
	having count(*) >= 2
);

-- GROUP CONCAT
select tipo, count(*) as goles_tipo, group_concat(minuto)
from goles
group by tipo
having goles_tipo > 10;


