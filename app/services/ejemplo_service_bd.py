from app.database.modelo_ejemplo import Ejemplo

def get_all_ejemplos():
    ejemplos = Ejemplo.query.all()
    return [e.to_dict() for e in ejemplos] 