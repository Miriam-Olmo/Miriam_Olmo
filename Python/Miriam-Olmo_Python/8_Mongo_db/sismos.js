conn = new Mongo();
db = conn.getDB('sismosdb');

// result = db.sismos.find();


// actualizaciones (updates)
// actualizar uno
// result = db.sismos.updateOne(
// filtro
//     { lugar: 'Granada, Spain' },
//     // modificacion 
//     {
//         $set: { magnitud: 6.0 }
//     }
// );

// actualizar varios
// result = db.sismos.updateMany(
//     { lugar: 'Granada, Spain' },
//     // modificacion 
//     {
//         $set: { magnitud: 6.0 }
//     }
// );

// deletes
//  eliminar uno
// result = db.sismos.deleteOne(
//     {
//         codigo: "ak600000002"
//     }
// );


//  find

// result = db.sismos.countDocuments();

//  recuperar todos los elementos 
// result = db.sismos.find();

// recuperar solo los 5 primeros elementos
// result = db.sismos.find().limit(5);

// filtros con and
// result = db.sismos.find(
//     {
//         tipoMagnitud: 'mw',
//         tsunami: true
//     }
// ).count();

// limit
// result = db.sismos.find(
//     {
//         tipoMagnitud: 'mw',
//         tsunami: true
//     }
// ).limit(2);


// filtros mayor o igual que...
// result = db.sismos.find(
//     {
//         magnitud: {
//             $gte: 6
//         }
//     }
// ).count();

//  filtros mayor o igual que... y menor o igual que...
// result = db.sismos.find(
//     {
//         magnitud: {
//             $gte: 6, $lte: 7
//         }
//     }
// ).count();


// recuperar todos los sismos cuya red no sea us
// result = db.sismos.find(
//     {
//         red: {
//             $ne: 'us'
//         }
//     }
// ).count();


// 
// result = db.sismos.find(
//     {
//         magnitud: {
//             $gte: 7
//         },
//         profundidadKm: {
//             $lte: 60
//         }
//     }
// ).count();



// recuperar sismos que esten en una de las redes: us, ci o nc

// result = db.sismos.find(
//     {
//         red: {
//             $in: ['us', 'ci', 'nc']
//         }
//     }
// ).count();


// expresiones regulares
//  buscar sismos sucedidos en japon
// result = db.sismos.find(
//     {
//         lugar: {
//             $regex: 'japan', $options: 'i'
//         }
//     }
// ).count();


// Terremotos de las redes us o ak resultado 294
// result = db.sismos.find(
//     {
//         red: {
//             $in: ['us', 'ak']
//         }
//     }
// ).count();


// Terremotos de Chile resultado 114
// result = db.sismos.find(
//     {
//         lugar: {
//             $regex: 'chile', $options: 'i'
//         }
//     }
// ).count();

// Terremotos que NO sean de la red us respuesta 860
// result = db.sismos.find(
//     {
//         red: {
//             $ne: ['us']
//         }
//     }
// ).count();



printjson(result)