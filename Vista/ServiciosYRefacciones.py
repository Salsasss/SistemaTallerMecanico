import Data_Base
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=Data_Base.engine)
sesion = Session()

relacion = {
    1: [1, 2, 3, 4, 5],
    2: [6, 7, 8, 9, 10],
    3: [11, 12, 13, 4, 14],
    4: [15, 16, 5, 17, 18],
    5: [19, 20, 21, 22, 23],
    6: [24, 25, 26, 27, 28],
    7: [29, 30, 31, 32, 33],
    8: [34, 35, 36, 37, 38],
    9: [39, 40, 41, 42, 43],
    10: [44, 45, 46, 47],
    11: [1, 2, 48, 3, 5],
    12: [49, 50, 51, 52, 53],
    13: [54, 55, 28, 56, 57],
    14: [58, 59, 60, 61],
    15: [62, 63, 64, 65, 66],
    16: [6, 67, 68, 69, 70],
    17: [71, 72, 48, 73, 74],
    18: [75, 39, 41, 43, 42],
    19: [34, 76, 60, 61, 59],
    20: [77, 78, 79, 80, 81],
}

# Insertar registros en la tabla ServicioRefaccion
for id_servicio, id_refacciones in relacion.items():
    for id_refaccion in id_refacciones:
        servicio_refaccion = Data_Base.Contenido(ID_Servicios=id_servicio, ID_Refacciones=id_refaccion)
        sesion.add(servicio_refaccion)

# Confirmar los cambios
sesion.commit()