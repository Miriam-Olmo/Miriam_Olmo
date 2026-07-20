// Comentario
/**
 * Comentario
 * en varias líneas
 */
conn = new Mongo();
db = conn.getDB('prueba');

// select * from users;
// result = db.users.find();

// INSERTS
// result = db.users.insertOne({
//     nombre: 'Valentina',
//     email: 'valen123@gmail.com',
//     direccion: 'Calle Manuela Malasaña 34'
// });

result = db.users.insertMany([
    {
        nombre: 'Inés',
        email: 'ines@yahoo.es',
        direccion: 'Calle Barco 27'
    },
    {
        nombre: 'Roberto',
        email: 'robertinchi@hotmail.es',
        direccion: 'Calle Mérida 23'
    },
    {
        nombre: 'Mariola',
        email: 'mariadelao@gmail.com',
        direccion: 'Calle Ballesta 26'
    }
]);

printjson(result);