from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import enlace

engine = create_engine(enlace)

from app import Matricula

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objetos de tipo Matricula
matricula1 = Matricula(nombre="Jorge", placa="LBA-1245", \
        anio=2018, costo=190)

matricula2 = Matricula(nombre="Freddy", placa="LBA-1425", \
        anio=2001, costo=184)

matricula3 = Matricula(nombre="Carlos", placa="ABC-5214", \
        anio=1990, costo=150)

matricula4 = Matricula(nombre="Luis", placa="DEF-9521", \
        anio=2021, costo=175)

# se agrega los objetos
# a la sesión
# a la espera de un commit
# para agregar un registro a la base de
# datos
session.add(matricula1)
session.add(matricula2)
session.add(matricula3)
session.add(matricula4)

# se confirma las transacciones
session.commit()
