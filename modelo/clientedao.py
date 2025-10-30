from modelo.conexionbd import ConexionBD
from modelo.cliente import Cliente

class ClienteDAO:
    def __init__(self):
        self.bd = ConexionBD()
        self.cliente = Cliente()

    def listarClientes(self):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = "exec [dbo].[sp_listar_clientes]"
        cursor.execute(sp)
        filas = cursor.fetchall()
        self.bd.cerrarConexionBD()
        return filas  # ✅ AGREGADO: retornar filas en lugar de solo imprimir

    def guardarCliente(self):
        self.bd.establecerConexionBD()
        sp = "exec [dbo].[sp_insertar_cliente] @clave=?, @nombre=?, @rfc=?, @telefono=?, @email=?, @direccion=?"
        param = (self.cliente.clave, self.cliente.nombre, self.cliente.rfc, self.cliente.telefono, self.cliente.email, self.cliente.direccion)
        cursor = self.bd.conexion.cursor()
        cursor.execute(sp, param)
        self.bd.conexion.commit()
        print("✅ Cliente guardado correctamente en la BD")
        self.bd.cerrarConexionBD()

    def actualizarCliente(self):
        self.bd.establecerConexionBD()
        sp = "exec [dbo].[sp_actualizar_cliente] @clave=?, @nombre=?, @rfc=?, @telefono=?, @email=?, @direccion=?"  # ✅ QUITAR id_cliente
        param = (self.cliente.clave, self.cliente.nombre, self.cliente.rfc, self.cliente.telefono, self.cliente.email, self.cliente.direccion)  # ✅ QUITAR id_cliente
        cursor = self.bd.conexion.cursor()
        cursor.execute(sp, param)
        self.bd.conexion.commit()  # ✅ CORREGIDO: cursor.commit() → self.bd.conexion.commit()
        print("✅ Cliente actualizado correctamente en la BD")
        self.bd.cerrarConexionBD()

    def eliminarCliente(self):
        self.bd.establecerConexionBD()
        sp = "exec [dbo].[sp_eliminar_cliente] @clave=?"  # ✅ CAMBIADO: id_cliente → clave
        param = (self.cliente.clave,)  # ✅ CORREGIDO: agregar coma para tupla
        cursor = self.bd.conexion.cursor()
        cursor.execute(sp, param)
        self.bd.conexion.commit()  # ✅ CORREGIDO: cursor.commit() → self.bd.conexion.commit()
        print("✅ Cliente eliminado correctamente en la BD")
        self.bd.cerrarConexionBD()
    
    def contarClientes(self):
        self.bd.establecerConexionBD()
        funcion = "SELECT [dbo].[fn_contar_clientes] ()"
        cursor = self.bd.conexion.cursor()
        cursor.execute(funcion)
        cantidad = cursor.fetchone()
        print(cantidad[0])
        self.bd.cerrarConexionBD()
        return cantidad[0]  # ✅ AGREGADO: retornar valor
    
    def buscarCliente(self):  # ✅ NUEVA FUNCIÓN: para los botones de buscar
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = "exec [dbo].[sp_buscar_clientes] @clave = ?"
        param = [self.cliente.clave]
        cursor.execute(sp, param)
        filas = cursor.fetchall()
        self.bd.cerrarConexionBD()
        return filas
