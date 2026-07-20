conn = new Mongo();
db = conn.getDB('sismosdb');

// result = db.sismos.find({
//     magnitud: { $gte: 6 },
//     profundidadKm: { $lt: 30 }
// });

// result = db.sismos.find({
//     $or: [
//         { magnitud: { $gte: 6 } },
//         { profundidadKm: { $lt: 30 } }
//     ]
// }).count();

// magnitud mayor 6 Y tsunami TRUE
result1 = db.sismos.find({
    magnitud: { $gt: 6 },
    tsunami: true
}).count();

// magnitud mayor 6 O tsunami TRUE
result2 = db.sismos.find({
    $or: [
        { magnitud: { $gt: 6 } },
        { tsunami: true }
    ]
}).count();

printjson(result1);
printjson(result2);

// ORDENAR
// Los 10 terremotos más fuertes
// result = db.sismos.find()
//     .sort({
//         magnitud: -1
//     })
//     .limit(10);

// Recuperar 20 terremotos, paginados, página 2, ordenados por fechaHora DESC
page = 5;
limit = 10;
skip = (page - 1) * limit;

result = db.sismos.find(
    {}, // Filtro
    { _id: 0, codigo: 1, magnitud: 1, lugar: 1 } // Proyección
)
    .sort({ fechaHora: -1 })
    .skip(skip)
    .limit(limit)

printjson(result);

// Top 5 por magnitud y fecha recuperando únicamente lugar, magnitud y fecha
resultFinal = db.sismos.find(
    {}, { _id: 0, lugar: 1, magnitud: 1, fechaHora: 1 }
)
    .sort({ magnitud: -1, fechaHora: -1 })
    .limit(5);

printjson(resultFinal);