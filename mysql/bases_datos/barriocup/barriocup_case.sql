-- CASE WHEN
-- Clasificar cada partido como "Victoria Local", "Victoria Visitante","Empate"

select id, goles_local, goles_Visitante,
case 
	when goles_local > goles_visitante then 'Victoria Local'
	when goles_local = goles_visitante then 'Empate'
	else 'Victoria Visitante'
end resultado
from partidos;

-- Etiqueta cada gol como 'Primera parte' (minuto <= 45) o 'Segunda parte'.
select partido_id, minuto, jugador_id,
case 
	when minuto<=45 then 'Primera Parte'
	else 'Segunda Parte'
end parte
from goles
order by minuto asc;

-- clasifica a los jugadores por edad: joven (<25), senior (25-31), veterano (>32)
select 
	nombre, 
	apellidos, 
	TIMESTAMPDIFF(YEAR, fecha_nacimiento, CURDATE()) as edad,
	case
		when TIMESTAMPDIFF(YEAR, fecha_nacimiento, CURDATE()) < 25 then 'Joven'
		when TIMESTAMPDIFF(YEAR, fecha_nacimiento, CURDATE()) <= 32 then 'Senior'
		else 'Veterano'
	end as edad
from jugadores;

-- FUNCIONES DE FECHA UTILES
	-- YEAR(fecha)
	-- MONTH(fecha)
	-- DAY(fecha)
	-- CURDATE()

-- Número de partidos jugados en cada mes (MONTH + GROUP BY)
select month(fecha) mes, count(*) partidos
from partidos
group by mes;

-- Media de goles del local redondeada hacia arriba (CEIL)
select ceil(AVG(goles_local )) goles_locales
from partidos;
-- Jugadores con dorsal par (MOD dorsal entre 2 = 0).
select dorsal 
from jugadores
where mod(dorsal, 2) = 0
order by dorsal desc;

