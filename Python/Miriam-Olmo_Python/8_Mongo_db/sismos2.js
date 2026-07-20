conn = new Mongo();
db = conn.getDB('sismosdb');

// OR
// result = db.sismos.find({
//     $or:
//         [{ magnitud: { $gte: 6 } },
//         { profundidadKm: { $lte: 30 } }]
// }).count();


//  magnitud mayor que 6 y tsunami true  resultado 336

// result = db.sismos.find(
//     [{
//         magnitud: {
//             $gte: 6
//         }
//     },
//     { tsunami: true }]
// ).count();

//  magnitud mayor quqe 6 o tsunami true resultado 349
// result = db.sismos.find(
//     {
//         $or: [{ magnitud: { $gte: 6 } },
//         { tsunami: true }
//         ]
//     }
// ).count();

// ordenar
//  los 10 terremotos mas fuertes
// result = db.sismos.find(
// ).sort({
//     magnitud: -1
// }).limit(10);


//  recuperar 20 terremotos paginados, pagina 2 y ordenados por fechaHora desc
// page = 1;
// limit = 25;
// skip = (page - 1) * limit;

// result = db.sismos.find({}, { _id: 0, codigo: 1, magnitud: 1, lugar: 1 })
//     .sort(
//         { fechaHora: -1 })
//     .skip(skip)
//     .limit(limit)
//     ;

// Top 5 por magnitud y fecha recuperando únicamente lugar, magnitud y fecha
// result = db.sismos.find({}, { _id: 0, lugar: 1, magnitud: 1, fechaHora: 1 }).sort({ magnitud: -1 },
//     { fechaHora: -1 }
// ).limit(5);





printjson(result)