from modelo.conexionbd import ConexionBD
from modelo.producto import Producto

class ProductoDAO:
    def __init__(self):
        self.bd = ConexionBD()
        self.producto = Producto()

    def listarProducto(self):
        self.bd.establecerConexionDB()

        cursor = self.bd.conexion.cursor()
        sp = "exec [dbo].[sp_listar_productos]"
        cursor.execute(sp)
        filas = cursor.fetchall()
        for fila in filas:
            print(fila)

        self.bd.cerrarConexionBD()