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
        for fila in filas:
            print(fila)
        print("✅ Clientes listados en BD")
        self.bd.cerrarConexionBD()

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
        sp = "exec [dbo].[sp_actualizar_cliente] @id_cliente=?, @clave=?, @nombre=?, @rfc=?, @telefono=?, @email=?, @direccion=?"
        param = (self.cliente.id_cliente, self.cliente.clave, self.cliente.nombre, self.cliente.rfc, self.cliente.telefono, self.cliente.email, self.cliente.direccion)
        cursor = self.bd.conexion.cursor()
        cursor.execute(sp, param)
        self.bd.conexion.commit()
        print("✅ Cliente actualizado correctamente en la BD")
        self.bd.cerrarConexionBD()

    def eliminarCliente(self):
        self.bd.establecerConexionBD()
        sp = "exec [dbo].[sp_eliminar_cliente] @id_cliente=?"
        param = (self.cliente.id_cliente,)
        cursor = self.bd.conexion.cursor()
        cursor.execute(sp, param)
        self.bd.conexion.commit()
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
    