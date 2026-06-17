-- operadores de comparacion (=,!=, <=, >=)


-- jugadores con nacionalidad distinta a española
select nombre, apellidos  
from jugadores
where nacionalidad <> 'España';

select distinct nacionalidad
from jugadores;

-- Lista los partidos donde el equipo local marcó 3 o más goles.
select id, fecha, equipo_local_id, goles_local 
from partidos
where goles_local >=3;

select p.id, goles_local 
from partidos p
where p.goles_local >=3;
-- Lista los delanteros del equipo 1
select nombre, apellidos, dorsal 
from jugadores
where equipo_id  = 1 and posicion = 'delantero';

select dorsal
from jugadores j 
where j.equipo_id  = 1 and posicion = 'delantero';

-- Lista los jugadores que son porteros O delanteros del equipo 2
select nombre, apellidos, dorsal, posicion 
from jugadores
where posicion='portero'
or (posicion='delantero' and equipo_id=2);

select dorsal, posicion
from jugadores j 
where j.equipo_id =2 and (posicion='portero' or posicion='delantero');


-- Partidos que terminaron en empate 
select id, estadio, fecha, goles_local, goles_visitante 
from partidos
where goles_local = goles_visitante;

select fecha, p.goles_local, p.goles_visitante 
from partidos p 
where p.goles_local = p.goles_visitante; 
-- Goles que NO son de jugada (penaltis, faltas, propias).
select jugador_id, minuto, tipo 
from goles
where tipo<>'jugada';

select minuto 
from goles
where tipo <>'jugada';
-- Jugadores del equipo 3 que sean centrocampistas o defensas.
select nombre, apellidos, dorsal, posicion 
from jugadores
where equipo_id =3 
and (posicion='centrocampista' or posicion='defensa');

select dorsal, posicion 
from jugadores
where equipo_id =3 and (posicion='centrocampista' or posicion='defensa');
-- Partidos con más de 4 goles totales
select goles_local, 
goles_visitante, 
goles_local +	goles_visitante as goles_totales,
estadio 
from partidos
where (goles_local + goles_visitante) >4;
-- Equipos de Madrid fundados antes de 2005
select id, nombre, ciudad, anyo_fundacion 
from equipos
where ciudad='Madrid' and anyo_fundacion<2005;

-- Jugadores con dorsal entre el 7 y el 11
select 
equipo_id,
nombre, 
apellidos,
dorsal
from jugadores
where dorsal >=7 and dorsal<=11
order by dorsal asc;

select 
equipo_id,
nombre,
dorsal 
from jugadores
where dorsal>=7 and dorsal <=11
order by dorsal asc;
-- Partidos donde ganó el local 
select 
id,
concat("Local ", goles_local, ' - ', goles_visitante, " Visitante") as resultado
from partidos
where goles_local > goles_visitante ;
-- Amarillas mostradas en la primera media hora 
select 
jugador_id,
minuto 
from sanciones
where tipo='amarilla' and minuto <=30;
-- Goles del jugador 53 marcados de penalti.
select 
jugador_id,
minuto,
tipo
from goles
where jugador_id=53 and tipo="penalti";
-- Jugadores de equipos 1, 2 o 3 que sean delanteros
select 
id,
nombre,
apellidos,
dorsal,
equipo_id 
from jugadores
where equipo_id >=1 and equipo_id<=3 and (posicion='delantero');
-- Partidos de la jornada 1 donde se marcaron más de 2 goles en total
select * 
from partidos
where jornada_id =1
and goles_local + goles_visitante <2
order by goles_visitante >2;
-- Goles marcados entre los minutos 40 y 50 que NO sean de penalti.

select *
from goles g where g.minuto >=40 and minuto <=50
and tipo <>'penalti'
order by minuto;

-- IN, BETWEEN, IS NULL
-- Jugadores de equipos 1, 2 o 3 que sean delanteros
select nombre, apellidos, equipo_id
from jugadores
where equipo_id in (1, 2, 3)
and posicion = 'delantero';

-- Jugadores con dorsal entre el 7 y el 11
select nombre, apellidos, dorsal
from jugadores
where dorsal BETWEEN 7 and 11;

-- Jugadores sin fecha de nacimiento
select nombre, apellidos, fecha_nacimiento
from jugadores
where fecha_nacimiento is NULL;

-- Lista los jugadores de los equipos 1, 4 y 7
select *
from jugadores
where equipo_id in (1, 4, 7);

-- Lista los goles que no son ni de penalti ni en propia puerta .
select id, minuto, tipo 
from goles
where tipo not in('penalti', 'propia');
-- Lista los goles marcados entre los minutos 30 y 60 
select jugador_id, minuto, tipo 
from goles
where minuto between 30 and 60;
-- Lista los jugadores que no tienen dorsal asignado.
select nombre, apellidos, dorsal 
from jugadores
where dorsal is null;

-- jugadores de los equipos 1 o 2, que sean centrocampista, nacidos entre 1996 y 1999
select *
from jugadores j 
where j.equipo_id in (1, 2)
and posicion = 'centrocampista'
and j.fecha_nacimiento between '1996-01-01' and '1999-12-31';

-- LIKE y comodines (%)
-- empieza por atletico
select *
from equipos e 
where nombre like 'Atletico%';

-- apellidos que acaben en ez
select nombre, apellidos
from jugadores j 
where apellidos like '%ez';

-- jugadores cuyo nombre tenga exactamente 4 letras
select nombre, j.apellidos 
from jugadores j 
where nombre like '____';

-- jugadores cuyo nombre tenga 4 letras y la segunda sea u
select nombre, j.apellidos 
from jugadores j 
where nombre like '_u__';

-- Jugadores no españoles ordenados por nacionalidad y luego por apellido.
select nombre, apellidos, nacionalidad
from jugadores
where nacionalidad <> 'España'
order by nacionalidad asc, apellidos asc;

-- Los 3 jugadores más veteranos de nacionalidad española que jueguen de delantero o centrocampista.
select nombre, apellidos, fecha_nacimiento, nacionalidad, posicion
from jugadores 
where nacionalidad  = "España"
and posicion in ('delantero', 'centrocampista')
order by fecha_nacimiento  asc 
limit 3;


-- Los 5 jugadores con dorsal más bajo que sean centrocampistas.
select nombre, apellidos, dorsal, posicion 
from jugadores
where posicion='centrocampista'
order by dorsal asc
limit 5;

-- Jugadores cuyo apellido empiece por 'M' o por 'S', ordenados alfabéticamente.
select nombre, apellidos, dorsal, posicion 
from jugadores
where apellidos like ('M%') or apellidos like ('S%')
order by apellidos asc ;

-- Goles de penalti marcados después del minuto 70.
select *
from goles
where tipo = 'penalti'
and minuto > 70;

