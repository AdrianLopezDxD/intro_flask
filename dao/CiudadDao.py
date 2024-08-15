from conexión.Conexión import Conexion


class CiudadDao:

    def getCiudades(self):

        ciudadSQL = """
        SELECT id, descripcion
        FROM ciudades
        """
        conexion = Conexion()
        con = conexion.getConexion()