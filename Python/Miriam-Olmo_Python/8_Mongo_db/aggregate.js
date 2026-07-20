conn = new Mongo();
db = conn.getDB('sismosdb');

//  $match ( se encarga de los filtrados)
result = db.sismos.aggregate([
    {
        $match:
            { magnitud: { $gte: 6 } }
    }
]);

// printjson(result)

// $group (agrupa los documentos por un campo concreto)
resultgroup = db.sismos.aggregate([
    {
        $group: { _id: '$red', total: { $sum: 1 } }
    }
]);

// printjson(resultgroup);

// magnitud media agrupada por id
resultgroupMedia = db.sismos.aggregate([
    {
        $group: {
            _id: '$red',
            total: { $sum: 1 },
            magnitudMedia: { $avg: '$magnitud' }
        }
    }
]);

// printjson(resultgroupMedia);

// magnitud maxima
resultgroupMax = db.sismos.aggregate([
    {
        $group: { _id: '$red', total: { $sum: 1 }, magnitudMedia: { $avg: '$magnitud' }, magnitudMax: { $max: '$magnitud' } }
    }
]);

// printjson(resultgroupMax);


// ordenar (.sort())
resultgrouporder = db.sismos.aggregate([
    {
        $group: { _id: '$red', total: { $sum: 1 }, magnitudMedia: { $avg: '$magnitud' }, magnitudMax: { $max: '$magnitud' } }
    }, { $sort: { total: -1 } }
]);

// printjson(resultgrouporder);


// limitar numero de registros limit()
resultgrouplimit = db.sismos.aggregate([
    {
        $group: { _id: '$red', total: { $sum: 1 }, magnitudMedia: { $avg: '$magnitud' }, magnitudMax: { $max: '$magnitud' } }
    }, { $sort: { total: -1 } }, { $limit: 5 }
]);

// printjson(resultgrouplimit);


//  match/group
resultMatchGroup = db.sismos.aggregate([
    { $match: { magnitud: { $gte: 6, $lte: 8 } } },
    {
        $group: { _id: '$red', total: { $sum: 1 }, magnitudMedia: { $avg: '$magnitud' }, magnitudMax: { $max: '$magnitud' } }
    }, { $sort: { total: -1 } }, { $limit: 5 }
]);

// printjson(resultMatchGroup);

// project
resultProject = db.sismos.aggregate([
    {
        $match: { magnitud: { $gte: 7 } }
    },
    {
        $project: { lugar: 1, magnitud: 1 }
    }
]);

// printjson(resultProject);


// terremotos con tsunami
result1 = db.sismos.aggregate([
    {
        $match: { tsunami: true }
    }
]);

// printjson(result1);

// contar $count()
resultcount = db.sismos.aggregate([
    {
        $match: { tsunami: true }
    },
    { $count: 'contarTsunami' }
]);

// printjson(resultcount);


// $unwind (genera los documentos diferentes por cada subdocumento(array))

resultUnwind = db.sismos.aggregate([
    { $match: { _id: ObjectId('6a31265b38698bd7f979def7') } },
    { $unwind: "$estaciones" }
]);

// printjson(resultUnwind);


// ¿qué estación  ha detectado más terremotos y qué magnitud local mide de media?
// $unwind, $group, $sort, $limit
result2 = db.sismos.aggregate([
    { $unwind: "$estaciones" },
    { $group: { _id: "$estaciones.codigo", total: { $sum: 1 }, magLocalMedia: { $avg: '$estaciones.magnitudLocal' } } },
    { $sort: { total: -1 } },
    { $limit: 1 }
]);

// printjson(result2);


// Tabla de lugares ordenadas por su magnitud media, de mayor a menor
result3 = db.sismos.aggregate([
    { $group: { _id: '$lugar', magnitudMedia: { $avg: '$magnitud' } } },
    { $sort: { magnitudMedia: -1 } }
]);

// printjson(result3);


// número de eventos por red, magnitud media (2 decimales), profundidad máxima registrada y la lista de ciudades distintas afectadas.

result4 = db.sismos.aggregate([
    { $group: { _id: '$red', eventos: { $sum: 1 }, magnitudMedia: { $avg: '$magnitud' }, profundidadMax: { $max: '$profundidadKm' }, ciudades: { $addToSet: '$lugar' } } },
    { $project: { magnitudMedia: { $round: ["$magnitudMedia", 2] }, eventos: 1, profundidadMax: 1, ciudades: 1 } }
]);

// printjson(result4);

// ¿En qué mes se concentraron más sismos de magnitud 6?
// $match
// $month -> aplicado sobre un campo fecha me devuelve el mes
// $group -> por mes

result5 = db.sismos.aggregate([
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

// printjson(result5);