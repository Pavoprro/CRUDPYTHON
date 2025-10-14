import pyodbc

class ConexionBD:
    def __init__(self):
        self.conexion = ''

    def establecerConexionBD(self):
        try:
            self.conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=SALAF008-17\SQLEXPRESS;DATABASE=bdsistema;UID=sa;PWD=Password01')
            print('conexion exitosa!')
        
        except Exception as error:
            print('Error en conexión' + str(error))

    def cerrarConexionBD(self):
        self.conexion.close()
        