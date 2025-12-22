from sqlmodel import create_engine

#Conexion a database

DB_URL = "mysql+pymysql://root:@localhost:3307/bd_contando"

engine = create_engine(DB_URL, echo=True)
