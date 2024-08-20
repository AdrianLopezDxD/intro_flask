import psycopg2

class Conexion:


    def __init__(self):
        self.con = psycopg2.connect("dbname=veterinaria-db user=postgre host=localhost password=lopezrojas19")
        
        """getConexion

            retorna la instancia de la base de datos

        """
        def getConexion(self):
            return self.con