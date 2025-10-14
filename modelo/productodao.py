from modelo.conexionbd import ConexionBD
from modelo.producto import Producto

class ProductoDAO:
    def __init__(self):
        self.bd = ConexionBD()
        self.producto = Producto()

    def listarProductos(self):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = "exec [dbo].[sp_listar_productos]"
        cursor.execute(sp)
        filas = cursor.fetchall()
        for fila in filas:
            print(fila)
        self.bd.cerrarConexionBD()

    def guardarProducto(self):
        self.bd.establecerConexionBD()
        sp = "exec [dbo].[sp_insertar_producto] @clave=?, @descripcion=?, @existencia=?, @precio=?"
        param = (self.producto.clave, self.producto.descripcion, self.producto.existencia, self.producto.precio)
        cursor = self.bd.conexion.cursor()
        cursor.execute(sp, param)
        self.bd.conexion.commit()  # Cambiado: commit en la conexión
        print("✅ Producto guardado correctamente en la BD")
        self.bd.cerrarConexionBD()

    def actualizarProducto(self):
        self.bd.establecerConexionBD()
        sp = "exec [dbo].[sp_actualizar_producto] @id_producto=?, @clave=?, @descripcion=?, @existencia=?, @precio=?"
        param = (self.producto.id_producto, self.producto.clave, self.producto.descripcion, self.producto.existencia, self.producto.precio)
        cursor = self.bd.conexion.cursor()
        cursor.execute(sp, param)
        cursor.commit()
        print("✅ Producto actualizado correctamente en la BD")
        self.bd.cerrarConexionBD()

    def eliminarProducto(self):
        self.bd.establecerConexionBD()
        sp = "exec [dbo].[sp_eliminar_producto] @id_producto=?"
        param = (self.producto.id_producto)
        cursor = self.bd.conexion.cursor()
        cursor.execute(sp, param)
        cursor.commit()
        print("✅ Producto eliminado correctamente en la BD")
        self.bd.cerrarConexionBD()
    
    def contarProductos(self):
        self.bd.establecerConexionBD()
        funcion = "SELECT [dbo].[fn_contar_productos] ()"
        cursor = self.bd.conexion.cursor()
        cursor.execute(funcion)
        cantidad = cursor.fetchone()
        print(cantidad[0])
        cursor.commit()
        self.bd.cerrarConexionBD()