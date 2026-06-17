// comentario simple
/**comentario
 * multiple
 */


// establecer la conexion
conn = new Mongo();

// elegir base de datos
db = conn.getDB('prueba');

// recuperar todos los usuarios
// result = db.users.find();


// inserts

// insertar uno
// result = db.users.insertOne({
//     "nombre": "Manolo",
//     "email": "eldelbombo@gmail.com",
//     "direccion": "calle de la ilustracion 1"
// }
// );

// insertar muchos
result = db.users.insertMany(
    [
        { "nombre": "julieta", "email": "venegas@gmail.com", "direccion": "calle la solea 23" },
        { "nombre": "jose", "email": "eltorito@gmail.com", "direccion": "calle la soledad 23" }
    ]
);

// visualizarlo
printjson(result)