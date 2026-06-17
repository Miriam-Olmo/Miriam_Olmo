-- libros del genero Terror( columnas titulo)
select titulo
  from libros
where genero = 'Terror'

-- Libros con precio superior a 15 €. (Columnas esperadas: titulo, precio)
select titulo, precio 
from libros
where precio > 15

-- Libros de más de 500 páginas y precio menor de 15 €. (Columnas esperadas: titulo, paginas, precio)
select titulo, paginas, precio 
from libros
where paginas > 500 
  and precio < 15
  
-- Libros de 'Terror' o 'Fantasía' publicados después de 1985. (Columnas esperadas: titulo, genero, anyo_publicacion)
  select titulo, genero, anyo_publicacion
from libros
where (genero ='Terror' or genero = 'Fantasia')
and anyo_publicacion > 1985

-- Libros de las editoriales 1, 3 o 5. (Columnas esperadas: titulo, editorial_id)
select titulo, editorial_id
from libros
where editorial_id in (1,3,5)

-- Libros que no son ni de 'Romance' ni de 'Drama'. (Columnas esperadas: titulo, genero)
select titulo, genero
from libros
where genero not in ('Romance', 'Drama') 

-- Libros publicados entre 2000 y 2010.(Columnas esperadas: titulo, anyo_publicacion)
select titulo, anyo_publicacion
from libros
where anyo_publicacion between 2000 and 2010

-- Compras del primer semestre de 2024. (Columnas esperadas: id, lector_id, libro_id, fecha_compra)
select id, lector_id, libro_id, fecha_compra
from compras
where fecha_compra between '2024-01-01' and '2024-06-30'

-- Lectores sin país registrado.(Columnas esperadas: nombre, apellidos)
select nombre, apellidos
from lectores
where pais is null 

-- Libros cuyo título empieza por 'El '.(Columnas esperadas: titulo)
select titulo
from libros
where titulo like('El%')

-- Libros cuyo título contiene 'viento'.(Columnas esperadas: titulo)
select titulo
from libros
where titulo like ('%viento%')

-- Autores cuyos apellidos terminan en 'ez'.(Columnas esperadas: nombre, apellidos)
select nombre, apellidos
from autores
where apellidos like ('%ez')

-- Los 5 libros más caros.(Columnas esperadas: titulo, precio)
select titulo , precio 
from libros
order by precio DESC, titulo asc
limit 5

-- Libros de 'Histórica' ordenados del más antiguo al más nuevo.(Columnas esperadas: titulo, anyo_publicacion)
select titulo, anyo_publicacion
from libros
where genero = 'Historica'
order by anyo_publicacion asc 

-- Géneros distintos del catálogo.(Columnas esperadas: genero)
select DISTINCT genero
from libros

-- Número total de libros.(Columnas esperadas: total)
select count(*)total
from libros

-- Precio medio del catálogo (2 decimales).(Columnas esperadas: precio_medio)
select round(avg(precio),2) as precio_medio
from libros

-- Precio del libro más caro y del más barato.(Columnas esperadas: mas_caro, mas_barato)
select max(precio) mas_caro, min(precio) mas_barato
from libros

-- Ingresos totales (suma de todo lo pagado).(Columnas esperadas: ingresos)
select sum(precio_pagado) as ingresos
  from compras
  
  -- Número de lectores distintos que han comprado.(Columnas esperadas: lectores_compradores)
  select count(DISTINCT(lector_id)) as lectores_compradores 
from compras

-- Número de libros por género.(Columnas esperadas: genero, cantidad)
select genero, count(*) as cantidad
from libros
group by genero

-- Los 5 libros más vendidos (libro_id y número de ventas).(Columnas esperadas: libro_id, ventas)
select libro_id, count(*) as ventas
from compras
group by libro_id
order by ventas DESC, libro_id ASC
limit 5

-- Valoración media de cada libro (2 decimales).(Columnas esperadas: libro_id, media)
select libro_id, round(avg(estrellas),2) as media 
from resenas 
group by libro_id

-- Número de libros por editorial.(Columnas esperadas: editorial_id, libros)
SELECT editorial_id, count(*) as libros
from libros
group by editorial_id

-- Ingresos por mes.(Columnas esperadas: mes, ingresos)
select MONTH(fecha_compra) as mes, sum(precio_pagado) as ingresos
from compras
group by mes

-- Autores con más de 2 libros.(Columnas esperadas: autor_id, num_libros)
select autor_id, count(*) as num_libros
FROM libro_autor
group by autor_id
having num_libros > 2

-- Libros con valoración media superior a 4,5.(Columnas esperadas: libro_id, media)
SELECT libro_id, round(avg(estrellas),2) as media 
from resenas
GROUP BY libro_id
HAVING media > 4.5

-- Nombre completo de cada autor.(Columnas esperadas: autor)
SELECT concat(nombre,' ', apellidos) as autor
from autores

-- Número de compras por año.(Columnas esperadas: anyo, compras)
select year(fecha_compra) as anyo, count(*) AS comprass
from compras
group by anyo

-- Clasifica cada libro por precio: Barato (<12), Medio (12-15), Caro (>15).(Columnas esperadas: titulo, precio, rango)
select titulo, precio,
  Case 
    when precio < 12 then 'Barato'
    when precio <= 15 then 'Medio'
    else 'Caro'
  end as rango 
from libros

-- Cada libro con el nombre de su editorial.(Columnas esperadas: titulo, editorial)
select titulo, e.nombre as editorial 
from libros l 
inner join editoriales e on l.editorial_id = e.id

-- Cada compra con el título del libro y lo pagado.(Columnas esperadas: id, titulo, precio_pagado)
select c.id, titulo, precio_pagado
from compras c  
inner join libros l on c.libro_id = l.id

-- Los 5 libros más vendidos, con su título.(Columnas esperadas: titulo, ventas)
select l.titulo, count(c.libro_id) as ventas
from compras c
join libros l on c.libro_id = l.id
group by l.id, l.titulo
order by ventas desc 
limit 5





