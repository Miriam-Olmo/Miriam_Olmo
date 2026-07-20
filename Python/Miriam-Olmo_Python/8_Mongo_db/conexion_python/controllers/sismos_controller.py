from db.config import get_collection
from bson import ObjectId


def get_all(n):
    col = get_collection()
    return list(col.find().limit(n))
    #return list(col.find({},{'lugar':1,'_id':0, 'magnitud':1}).limit(n))
    
    
def get_by_city(city):
    col = get_collection()
    return list( col.find({'lugar': { "$regex": city , "$options": 'i'}}) )


def insert_sismo(sismo):
    col = get_collection()
    resultado = col.insert_one(sismo)
    return f"El sismo se ha insertado con exito y tiene id {resultado.inserted_id}"


def delete_sismo(id):
    # convertir el id str en un id ObjectId
    oid = ObjectId(id)
    col = get_collection()
    result = col.delete_one({"_id": oid})
    return f"Se han borrado {result.deleted_count} sismos"


def filter_by_magnitude(magnitude):
    col = get_collection()
    result = list(col.find({"magnitud": {"$gte": magnitude}}).sort("magnitud", -1))
    return result

def get_by_id(id_sismo):
    oid = ObjectId(id_sismo)
    col = get_collection()
    sismo = col.find_one({'_id': oid })
    return sismo

def update_sismo(id, data):
    oid = ObjectId(id)
    col = get_collection()
    result = col.update_one({'_id': oid}, {'$set': data})
    return f' se han actualizado {result.matched_count} sismos'