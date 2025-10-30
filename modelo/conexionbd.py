import pyodbc

class ConexionBD:
    def __init__(self):
        self.conexion = None

    def establecerConexionBD(self):
        try:
            self.conexion = pyodbc.connect(
                'DRIVER={SQL Server};'
                'SERVER=DESKTOP-9GNK739\\PROYE_DESARROLLO;'  # ← CORREGIDO
                'DATABASE=bdsistema;'
                'UID=sa;'
                'PWD=Password01;'
            )
            print('✅ Conexion exitosa!')
            return True

        except Exception as error:
            print('❌ Error en conexion: ' + str(error))
            return False

    def cerrarConexionBD(self):
        if self.conexion:
            self.conexion.close()
            print('🔌 Conexion cerrada')