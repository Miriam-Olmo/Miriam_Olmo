conn = new Mongo();
db = conn.getDB('sismosdb');

// result = db.sismos.find();

// UPDATE sismos SET lugar="", magnitud= 
// WHERE 

// updateOne, updateMany

// result = db.sismos.updateOne(
//     { lugar: 'Granada, Spain' },
//     {
//         $set: { magnitud: 4.34 }
//     }
// );

// result = db.sismos.updateOne(
//     { _id: ObjectId('6a31265608d60da842eeb5bf') },
//     {
//         $push: { fuentes: 'sp' },
//         $set: { magnitud: 3.4 }
//     }
// )

// result = db.sismos.deleteOne(
//     { codigo: 'ak600000002' }
// );

// select count(*) from tabla

// result = db.sismos.countDocuments();

// result = db.sismos.find().limit(5);

// result = db.sismos.find(
//     {
//         tipoMagnitud: 'mw',
//         tsunami: true
//     }
// ).limit(1);

// result = db.sismos.find({
//     magnitud: {
//         $gte: 6, $lte: 7
//     }
// }).count();

// Los sismos cuya red no sea 'us'
// result = db.sismos.find({
//     red: { $ne: 'us' }
// }).count();

/**
 * 
 * 
{ lugar: "...Tonga", magnitud: 8.1, profundidadKm: 61 }
{ lugar: "...Chile", magnitud: 7.4, profundidadKm: 25 }
...
 * 
 * 
 * 
 * 
 */

// result = db.sismos.find({
//     magnitud: { $gte: 7 }, // magnitud >= 7
//     profundidadKm: { $lte: 60 } // profundidadKm <= 60
// }).count();

// Los sismos que pertenezcan a la red 'us', 'ci' o 'nc'
// result = db.sismos.find({
//     red: { $in: ['us', 'ci', 'nc'] }
// }).count();

// Terremotos sucedidos en japan
// result = db.sismos.find({
//     lugar: { $regex: 'japan', $options: 'i' }
// }).count();

// Terremotos de las redes us o ak
result = db.sismos.find({
    red: { $in: ['us', 'ak'] }
}).count();

// Terremotos de Chile
result2 = db.sismos.find({
    lugar: { $regex: 'chile', $options: 'i' }
}).count();

// Terremotos que NO sean de la red us
result3 = db.sismos.find({
    red: { $ne: 'us' }
}).count();

result4 = db.sismos.find({
    red: { $nin: ['us'] }
}).count();

printjson(result3);
printjson(result4);