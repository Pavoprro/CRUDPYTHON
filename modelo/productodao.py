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
        self.bd.cerrarConexionBD()
        return filas

    def guardarProducto(self):
        self.bd.establecerConexionBD()
        sp = "exec [dbo].[sp_insertar_producto] @clave=?, @descripcion=?, @existencia=?, @precio=?"
        param = (self.producto.clave, self.producto.descripcion, self.producto.existencia, self.producto.precio)
        cursor = self.bd.conexion.cursor()
        cursor.execute(sp, param)
        self.bd.conexion.commit()  
        print("✅ Producto guardado correctamente en la BD")
        self.bd.cerrarConexionBD()

    def actualizarProducto(self):
        self.bd.establecerConexionBD()
        sp = "exec [dbo].[sp_actualizar_producto] @clave=?, @descripcion=?, @existencia=?, @precio=?"
        param = (self.producto.clave, self.producto.descripcion, self.producto.existencia, self.producto.precio)
        cursor = self.bd.conexion.cursor()
        cursor.execute(sp, param)
        cursor.commit()
        print("✅ Producto actualizado correctamente en la BD")
        self.bd.cerrarConexionBD()

    def eliminarProducto(self):
        self.bd.establecerConexionBD()
        sp = "exec [dbo].[sp_eliminar_producto] @clave=?"
        param = (self.producto.clave)
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
    
    def buscarProducto(self):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = "exec [dbo].[sp_buscar_producto] @clave = ?"
        param = [self.producto.clave]
        cursor.execute(sp,param)
        filas = cursor.fetchall()
        self.bd.cerrarConexionBD()
        return filas
    
