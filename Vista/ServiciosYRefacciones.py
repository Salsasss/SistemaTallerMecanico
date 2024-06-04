import Data_Base
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=Data_Base.engine)
sesion = Session()

relacion = {
    1: [(1, 1), (2, 2), (3, 2), (4, 1), (5, 2)],
    2: [(6, 2), (7, 3), (8, 1), (9, 2), (10, 1)],
    3: [(11, 4), (12, 1), (13, 1), (4, 2), (14, 2)],
    4: [(15, 3), (16, 3), (5 , 2), (17, 1), (18, 3)],
    5: [(19, 1), (20, 2), (21, 2), (22, 5), (23, 1)],
    6: [(24, 3), (25, 4), (26, 7), (27, 3), (28, 5)],
    7: [(29, 3), (30, 4), (31, 4), (32, 3), (33, 3)],
    8: [(34, 6), (35, 4), (36, 3), (37, 2), (38, 2)],
    9: [(39, 3), (40, 3), (41, 2), (42, 2), (43, 2)],
    10:[(44, 2), (45, 2), (46, 1), (47, 3)],
    11:[(1, 1), (2, 1), (48, 1), (3, 2), (5, 3)],
    12:[(49, 5), (50, 2), (51, 2), (52, 1), (53, 1)],
    13:[(54, 4), (55, 4), (28, 1), (56, 2), (57, 1)],
    14:[(58, 3), (59, 5), (60, 3), (61, 1)],
    15:[(62, 2), (63, 6), (64, 4), (65, 1), (66, 1)],
    16:[(6, 1), (67, 3), (68, 4), (69, 2), (70, 2)],
    17:[(71, 6), (72, 1), (48, 5), (73, 2), (74, 1)],
    18:[(75, 5), (39, 3), (41, 6), (43, 3), (42, 1)],
    19:[(34, 3), (76, 1), (60, 3), (61, 5), (59, 1)],
    20:[(77, 2), (78, 2), (79, 2), (80, 2), (81, 2)],
}

# Insertar registros en la tabla ServicioRefaccion
for id_servicio, refacciones in relacion.items():
    for id_refaccion, cantidad_refaccion in refacciones:
        servicio_refaccion = Data_Base.Contenido(ID_Servicios=id_servicio, ID_Refacciones=id_refaccion, Cantidad_necesaria=cantidad_refaccion)
        sesion.add(servicio_refaccion)

# Confirmar los cambios
sesion.commit()