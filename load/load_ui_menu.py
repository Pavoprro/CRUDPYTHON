from PyQt5 import QtWidgets, uic
from load.load_ui_productos import Load_ui_productos
from load.load_ui_clientes import Load_ui_clientes

class Load_ui_menu(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ui_menu.ui", self)
        self.show()
        
        # Conectar botones
        self.boton_productos.clicked.connect(self.abrir_productos)
        self.boton_clientes.clicked.connect(self.abrir_clientes)
        self.boton_salir.clicked.connect(self.cerrar_sesion)  # ← CAMBIADO
    
    def abrir_productos(self):
        self.ventana_productos = Load_ui_productos()
        self.ventana_productos.show()
        self.close()
    
    def abrir_clientes(self):
        self.ventana_clientes = Load_ui_clientes()
        self.ventana_clientes.show()
        self.close()
    
    def abrir_productos(self):
        from load.load_ui_productos import Load_ui_productos  # ← IMPORTAR DENTRO
        self.ventana_productos = Load_ui_productos()
        self.ventana_productos.show()
        self.close()

    def abrir_clientes(self):
        from load.load_ui_clientes import Load_ui_clientes  # ← IMPORTAR DENTRO
        self.ventana_clientes = Load_ui_clientes()
        self.ventana_clientes.show()
        self.close()

    def cerrar_sesion(self):
        from load.load_ui_login import Load_ui_login  # ← IMPORTAR DENTRO
        self.ventana_login = Load_ui_login()
        self.ventana_login.show()
        self.close()