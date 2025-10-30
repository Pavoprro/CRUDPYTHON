from modelo.conexionbd import ConexionBD
from modelo.usuario import Usuario

class UsuarioDAO:
    def __init__(self):
        self.bd = ConexionBD()
        self.usuario = Usuario()

    def validar_login(self, usuario, password):
        try:
            if not self.bd.establecerConexionBD():
                return False
                
            cursor = self.bd.conexion.cursor()
            query = "SELECT id_usuario, usuario, password, nombre FROM usuarios WHERE usuario = ? AND password = ? AND activo = 1"
            param = (usuario, password)
            
            cursor.execute(query, param)
            usuario_encontrado = cursor.fetchone()
            
            if usuario_encontrado:
                self.usuario.id_usuario = usuario_encontrado[0]
                self.usuario.usuario = usuario_encontrado[1]
                self.usuario.password = usuario_encontrado[2]
                self.usuario.nombre = usuario_encontrado[3]
                return True
            return False
            
        except Exception as e:
            print(f"Error en login: {str(e)}")
            return False
        finally:
            self.bd.cerrarConexionBD()
    