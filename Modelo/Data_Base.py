from sqlalchemy import (Column, ForeignKey, Integer, String, create_engine, Double, Date)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

#--------------------------------# Configuration #------------------------------------#

db = "sqlite:///Base_De_Datos.db"

engine = create_engine(db)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


#--------------------------------# Inheritance #------------------------------------#

#------------------------# Names Inheritance #------------------------#
class BaseModel_Names(Base):
    __abstract__ = True
    __allow_unmapped_ = True

    RFC = Column(String, primary_key=True)
    Nombre = Column(String)
    Apellido_Paterno = Column(String)
    Apellido_Materno = Column(String)
    Telefono = Column(Integer)

#--------------------------------# Classes #------------------------------------

#------------------------# Maintenance Class #------------------------#
class Mantenimiento(Base):
    __tablename__ = "mantenimiento"


    Orden = Column(Integer, primary_key=True)
    Estatus = Column(Integer)
    Factura = Column(Integer)

    # ------# FK's de Vehiculo, Empleado y Servicio #------#
    VIN = Column(ForeignKey("vehiculo.VIN"))
    ID_servicio = Column(ForeignKey("servicio.ID_servicio"))
    RFC_empleado = Column(ForeignKey("empleado.RFC"))


    def __repr__(self):
        return f"<Mantenimiento \n Orden = {self.Orden} \n Factura = {self.Factura} \n VIN = {self.VIN} \n ID de servicio = {self.ID_servicio} \n RFC del empleado = {self.RFC_empleado} \n>\n\n"


#------------------------# Vehicle Class #------------------------#
class Vehiculo(Base):
    __tablename__ = "vehiculo"


    VIN = Column(Integer, primary_key=True)
    Placa = Column(String)
    Marca = Column(String)
    Modelo = Column(String)
    Anio = Column(Integer)
    Motor = Column(String)
    Kilometraje = Column(Double)

    #------# FK de Clientes #------#
    RFC_Cliente = Column(ForeignKey("clientes.RFC"))

    # ------# Relacion con Mantenimiento #------#
    Maintenance = relationship(Mantenimiento)

    def __repr__(self):
        return f"<Vehiculo \n VIN = {self.VIN} \n Placa = {self.Placa} \n Marca = {self.Marca} \n Modelo = {self.Modelo} \n Año = {self.Año} \n Motor= {self.Motor} \n Kilometraje = {self.Kilometraje} \n RFC del cliente = {self.RFC_Cliente} \n>\n\n"


#------------------------# Client Class #------------------------#
class Cliente(BaseModel_Names):
    __tablename__ = "clientes"


    Calle = Column(String)
    Colonia = Column(String)
    no_exterior = Column(String)
    no_interior = Column(String)
    Ciudad = Column(String)
    Estado = Column(String)
    Codigo_Postal = Column(Integer)

    #------# Relacion con Vehiculo #------#
    vehicle = relationship(Vehiculo)


    def __repr__(self):
        return f"<Cliente\n RFC = {self.RFC} \n Nombre = '{self.Nombre}' \n Apellido Paterno = '{self.Apellido_Paterno}' \n Apellido Materno = '{self.Apellido_Materno}' \n Telefono = '{self.Telefono}' \n Calle = {self.Calle} \n Colonia = '{self.Colonia}' \n No. Exterior = {self.no_exterior} \n No. Interior = {self.no_interior} \n Ciudad = '{self.Ciudad}' \n Estado = {self.Estado} \n Codigo Postal = {self.Codigo_Postal} \n> \n\n"


#------------------------# Employee Class #------------------------#
class Empleado(BaseModel_Names):
    __tablename__ = "empleado"

    Contrasenia = Column(String)
    Puesto = Column(String)

    # ------# Relacion con Mantenimiento #------#
    Maintenance = relationship(Mantenimiento)

    def __repr__(self):
        return f"<Empleado\n RFC = {self.RFC} \n Nombre = '{self.Nombre}' \n Apellido Paterno = '{self.Apellido_Paterno}' \n Apellido Materno = '{self.Apellido_Materno}' \n Telefono = '{self.Telefono}' \n Puesto = {self.Puesto} \n> \n\n"


#------------------------# Spare parts / Refaction Bond (Class) #------------------------#
class Contenido(Base):
    __tablename__ = "servicios y refacciones"

    ID = Column(Integer, primary_key=True)

    #------# FK's de Servicios y Refacciones #------#
    ID_Servicios = Column(ForeignKey("servicio.ID_servicio"))
    ID_Refacciones = Column(ForeignKey("refacciones.ID_refacciones"))

    def __repr__(self):
        return f"<Servicios y Refacciones \n ID de Servicios = {self.ID_Servicios} \n ID de Refacciones = {self.ID_Refacciones} \n>\n\n"


#------------------------# Services Class #------------------------#
class Servicios(Base):
    __tablename__ = "servicio"


    ID_servicio = Column(Integer, primary_key=True)
    Fecha_inicio = Column(Date)
    Fecha_salida = Column(Date)
    Observaciones = Column(String)

    #------# Relacion con Servicios y Refacciones #------#
    contenido = relationship(Contenido)

    # ------# Relacion con Mantenimiento #------#
    Maintenance = relationship(Mantenimiento)


    def __repr__(self):
        return f"<Servicios \n ID = {self.ID_servicio} \n Fecha de inicio = {self.Fecha_inicio} \n Fecha de salida = {self.Fecha_salida} \n Observaciones = {self.Observaciones} \n>\n\n"


#------------------------# Spare Parts Class #------------------------#
class Refacciones(Base):
    __tablename__ = "refacciones"

    ID_refacciones = Column(Integer, primary_key=True)
    NombreRefacciones = Column(String)
    Modelo = Column(String)
    Cantidad = Column(Integer)
    Costo = Column(Double)

    #------# Relacion con Servicios y Refacciones #------#
    contenido = relationship(Contenido)


    def __repr__(self):
        return f"<Refacciones \n ID = {self.ID_refacciones} \n Nombre = {self.NombreRefacciones}\n Modelo = {self.Modelo} \n Cantidad = {self.Cantidad} \n Costo = {self.Costo} \n>\n\n"



#--------------------------------# METADATA #------------------------------------#
Base.metadata.create_all(engine)

def obtener_refacciones():
    return session.query(
        Refacciones.ID_refacciones,
        Refacciones.NombreRefacciones,
        Refacciones.Modelo,
        Refacciones.Cantidad,
        Refacciones.Costo
    ).all()