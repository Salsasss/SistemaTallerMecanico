import Data_Base
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=Data_Base.engine)
sesion = Session()

servicios = [
    ("Mantenimiento Preventivo", 1000),
    ("Reparación del Motor", 3000),
    ("Sistema de Frenos", 3500),
    ("Transmisión", 2500),
    ("Sistema de Suspensión y Dirección", 2000),
    ("Aire Acondicionado y Climatización", 1750),
    ("Neumáticos y Alineación", 2200),
    ("Sistema Eléctrico y Electrónico", 1800),
    ("Escape y Emisiones", 2000),
    ("Inspección y Diagnóstico", 1500),
    ("Cambio de Fluidos y Filtros", 2500),
    ("Reparación de Carrocería y Pintura", 5000),
    ("Reparación del Sistema de Enfriamiento", 2000),
    ("Reemplazo de Batería", 1000),
    ("Limpieza y Detallado", 1000),
    ("Sistema de Encendido", 1300),
    ("Sistema de Combustible", 2000),
    ("Sistema de Escape", 2000),
    ("Sistema de Carga", 2300),
    ("Sistema de Ventilación y Calefacción", 1700)
]

for servicio, costo in servicios:
    x = Data_Base.Servicios(servicio, costo)
    sesion.add(x)

sesion.commit()