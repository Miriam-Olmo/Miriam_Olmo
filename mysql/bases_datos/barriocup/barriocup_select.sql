-- extraer todos los campos
select * from equipos;

-- extraer campos concretos
select nombre, apellidos, posicion
from jugadores;

-- sacar nombre completo y posicion
select concat (nombre," ", apellidos) as nombre_completo, posicion
from jugadores;

-- listar todos los equipos(nombre, anyo_fundacion)

select nombre, anyo_fundacion
from equipos
order by anyo_fundacion asc;

-- mostrar los goles mas tempraneros del campeonato
-- solo quiero ver el partido, jugador y minuto
select partido_id, jugador_id, minuto
from goles
order by minuto asc;

-- limitar el numero de registros que quiero
select partido_id, jugador_id, minuto
from goles
order by minuto asc
limit 3;


-- Listar los 10 jugadores más jóvenes
select nombre,apellidos,fecha_nacimiento 
from jugadores
order by fecha_nacimiento desc 
limit 10;
-- Listar los nombres de los jugadores que son porteros.
select id, nombre, apellidos
from jugadores
where posicion='portero';
-- Mostrar los 15 goles más tardíos (mayor minuto), 
-- con partido, jugador y minuto.
select partido_id, jugador_id, minuto
from goles
order by minuto desc
limit 15;

-- Mostrar cada partido como texto: 'Local X - Y Visitante'. No incluir los nombres de los equipos
select concat("Local"," ", goles_local, " ", "-"," ", goles_visitante," ", "Visitante") as marcadores
from partidos;

-- Listar los jugadores con alias 'Ficha' que concatene apellidos en mayúsculas + ', ' + nombre
select concat (UPPER(apellidos), ", ", nombre) as ficha
from jugadores;

-- Mostrar los partidos con más goles totales: ordena por (goles_local + goles_visitante) descendente, top 5.
select goles_local, goles_visitante, goles_local + goles_visitante as goles_totales
from partidos
order by goles_totales desc
limit 5;


-- DISTINCT (no muestra las nacionalidades que esten repetidas)
select distinct nacionalidad 
from jugadores;
-- cuando metes mas campos no funciona el DISTINCT 
select distinct nacionalidad, nombre
from jugadores;

-- listar las ciudades que tienen equipos
select distinct ciudad 
from equipos;

-- OFFSET ( define desde que registro empieza a visualizar)
select id, nombre, apellidos
from jugadores
limit 10
offset 12;

-- pagina: 1 offset: 0
select id, nombre, apellidos
from jugadores
limit 10
offset 0;
-- pagina: 2 offset: 10
select id, nombre, apellidos
from jugadores
limit 10
offset 10;
-- pagina: 3 offset: 20
select id, nombre, apellidos
from jugadores
limit 10
offset 20;

-- limit (10), pagina (1, 2, 3...)
-- (calculo del offset) ofset: (pagina-1) * limit


-- Mostrar los 3 partidos más recientes (por fecha) con su estadio.
select id, fecha, estadio
from partidos
order by fecha desc  
limit 3;


-- Convertir en rojas todas las amarillas del jugador 14 (acumulación).
update sanciones
set tipo='roja'
where tipo='amarilla' and jugador_id=14;

select * from sanciones
where jugador_id=14;

-- Subir el dorsal en 1 a todos los jugadores del equipo 7.
update jugadores
set dorsal=dorsal+1
where equipo_id=7;

select * from jugadores 
where equipo_id=7;

-- Calcular la edad de cada jugador (alias 'edad') y ordenar de mayor a menor.(NO HACER)

select 
nombre,
apellidos,
timestampdiff(year, fecha_nacimiento, CURDATE() ) as edad
from jugadores
order by edad desc;



