conn = new Mongo();
db = conn.getDB('sismosdb');

// $match
result = db.sismos.aggregate([
    {
        $match: {
            magnitud: { $gte: 6 }
        }
    }
]);

// printjson(result);

// $group
resultGroup = db.sismos.aggregate([
    {
        $match: {
            magnitud: { $gte: 6, $lte: 8 }
        }
    },
    {
        $group: {
            _id: '$red',
            total: { $sum: 1 },
            magnitudMedia: { $avg: '$magnitud' },
            magnitudMax: { $max: '$magnitud' }
        }
    },
    { $sort: { total: -1 } },
    { $limit: 5 }
]);

// printjson(resultGroup);

resultProject = db.sismos.aggregate([
    { $match: { magnitud: { $gte: 7 } } },
    { $project: { _id: 0, lugar: 1, magnitud: 1 } }
]);

// printjson(resultProject)

// Terremotos con tsunami
resultTsunami = db.sismos.aggregate([
    { $match: { tsunami: true } },
    { $count: "conTsunami" }
]);

// printjson(resultTsunami);

// $unwind
resultUnwind = db.sismos.aggregate([
    { $match: { _id: ObjectId('6a31265608d60da842eeb5c1') } },
    { $unwind: "$estaciones" }
]);

// printjson(resultUnwind);

// ¿Qué estación ha detectado más terremotos y qué magnitud local mide de media?
// $unwind, $group, $sort, $limit
resultEstacionTop = db.sismos.aggregate([
    { $unwind: '$estaciones' },
    {
        $group: {
            _id: '$estaciones.codigo',
            total: { $sum: 1 },
            magLocalMedia: { $avg: '$estaciones.magnitudLocal' }
        }
    },
    { $sort: { total: -1 } },
    { $limit: 1 }
]);

resultTablaLugares = db.sismos.aggregate([
    {
        $group: {
            _id: '$lugar',
            magMedia: { $avg: '$magnitud' }
        }
    },
    { $sort: { magMedia: -1 } }
]);

// printjson(resultTablaLugares);

// número de eventos por red, magnitud media, profundidad máxima registrada 
// (para luego) y la lista de ciudades distintas afectadas.
resultEventosRed = db.sismos.aggregate([
    {
        $group: {
            _id: '$red',
            eventos: { $sum: 1 },
            magMedia: { $avg: "$magnitud" },
            profMax: { $max: "$profundidadKm" },
            ciudades: { $addToSet: "$lugar" }
        }
    },
    {
        $project: {
            magMedia: { $round: ["$magMedia", 2] },
            eventos: 1,
            profMax: 1,
            ciudades: 1
        }
    }
]);

printjson(resultEventosRed);

// ¿En qué mes se concentraron más sismos de magnitud mayor que 6?
// $match
// $month -> aplicado sobre un campo fecha me devuelve el mes
// $group -> por mes

resultPorMes = db.sismos.aggregate([
    { $match: { magnitud: { $gte: 6 } } },
    {
        $group: {
            _id: { $month: "$fechaHora" },
            total: { $sum: 1 }
        }
    },
    { $sort: { total: -1 } },
    { $limit: 1 }
]);

printjson(resultPorMes)