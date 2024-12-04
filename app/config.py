class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    SQLALCHEMY_DATABASE_URI = (
        r"mssql+pyodbc:<servidor>/HydrAI_DB?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server"
    )
