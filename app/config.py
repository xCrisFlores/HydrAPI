#Archivo de configuracion, verificar y validar la cadena de conexion para cada maquina local
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = (
        r"mssql+pyodbc://localhost\SQLEXPRESS/HydrAI_DB?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server"
    )
