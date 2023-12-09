

class Futbolista:
    def __init__(self,nombre,apellidos,edad,demarcacion,internacional):
        self.nombre=nombre
        self.apellidos=apellidos
        self.edad=edad
        self.demarcacion=demarcacion
        self.internacional=internacional


    def to_db_collection(self):
        return {
            "nombre":self.nombre,
            "apellidos":self.apellidos,
            "edad":self.edad,
            "demarcacion":self.demarcacion,
            "internacional":self.internacional
        }

    def __str__(self):
        return (f'Nombre:{self.nombre},Apellidos:{self.apellidos},Edad:{self.edad},Demarcacion:{self.demarcacion},Internacional:{self.internacional}')