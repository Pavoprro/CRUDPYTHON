from PyQt5 import QtWidgets, uic
from modelo.usuariodao import UsuarioDAO

class Load_ui_login(QtWidgets.QDialog):  # ← CAMBIAR A QDialog
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ui_login.ui", self)
        self.show()
        
        self.usuariodao = UsuarioDAO()
        self.boton_login.clicked.connect(self.validar_login)
        
        # Enter para login
        self.password_input.returnPressed.connect(self.validar_login)
    
    def validar_login(self):
        usuario = self.user_input.text()
        password = self.password_input.text()
        
        if not usuario or not password:
            print("❌ Usuario y contraseña requeridos")
            return
        
        if self.usuariodao.validar_login(usuario, password):
            print("✅ Login exitoso")
            self.abrir_menu()
        else:
            print("❌ Usuario o contraseña incorrectos")
    
    def abrir_menu(self):
        from load.load_ui_menu import Load_ui_menu  # ← IMPORTAR DENTRO
        self.ventana_menu = Load_ui_menu()
        self.ventana_menu.show()
        self.close()