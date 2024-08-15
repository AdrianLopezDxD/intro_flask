import psycopg2

class Conexion:


    def __init__(self):
        self.con = psycopg2.connect("dbname=veterinaria-db user=postgre password=lopezrojas19")
        """getConexión

            retorna la instancia de la base de datos

        """
        def getConexión(self):
            return self.con