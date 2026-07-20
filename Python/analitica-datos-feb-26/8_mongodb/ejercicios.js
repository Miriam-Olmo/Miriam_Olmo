conn = new Mongo();
db = conn.getDB('sismosdb');

// 1. Terremotos con magnitud entre 5 y 6.5, que no hayan generado tsunami y que su estado sea revisado
result = db.sismos.find(
    { magnitud: { $gt: 5, $lt: 6.5 } },
    { tsunami: false },
    { estado: 'reviewed' },
);

// 2. Terremotos con magnitud entre 4 y 5, que además sean, o muy superficiales (profundidadKm < 10) o muy profundos (profundidadKm > 500)
ejercicio2 = db.sismos.find({
    magnitud: { $gt: 4, $lt: 5 },
    $or: [
        { profundidadKm: { $lt: 10 } },
        { profundidadKm: { $gt: 500 } },
    ]
}, { _id: 0, magnitud: 1, profundidadKm: 1 });

printjson(ejercicio2);

// Los terremotos que no sean de la red 'us', ni de la red 'ci', ni tengan alerta 'red' 
ejercicio3 = db.sismos.find({
    $nor: [
        { red: 'ci' },
        { red: 'us' },
        { alerta: 'red' }
    ]
}, { _id: 0, lugar: 1, red: 1, alerta: 1 });

printjson(ejercicio3);

// Sismos medidos con escala mw o mww, y de magnitud 7 o más.
ejercicio4 = db.sismos.find({
    tipoMagnitud: { $in: ['mw', 'mww'] },
    magnitud: { $gte: 7 }
}, { _id: 0, lugar: 1, tipoMagnitud: 1, magnitud: 1 });

printjson(ejercicio4);

// Sismos ocurridos en el segundo semestre de 2026 (del 1 de julio al 31 de diciembre, ambos incluidos).
ejercicio5 = db.sismos.find({
    fechaHora: {
        $gte: ISODate('2026-07-01'),
        $lte: ISODate('2026-12-31')
    }
}, { _id: 0, lugar: 1, fechaHora: 1 });

printjson(ejercicio5);

// Queremos buscar terremotos en los que las estaciones cumplan con ciertos filtros
// distanciaKM < 50 y magnitudLocal >= 6

ejercicio6 = db.sismos.find({
    estaciones: {
        $elemMatch: {
            distanciaKm: { $lt: 50 },
            magnitudLocal: { $gte: 6 }
        }
    }
}, { _id: 0, lugar: 1, estaciones: 1 })

printjson(ejercicio6)

// Recuperar todos los sismos cuyo type de la ubicación sea Point
ejercicio7 = db.sismos.find({
    'ubicacion.type': 'Point'
}).count();

printjson(ejercicio7)