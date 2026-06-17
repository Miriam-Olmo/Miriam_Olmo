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


result = db.sismos.find(

);

printjson(result)