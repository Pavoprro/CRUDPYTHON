#1.- Importar librerias
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets, uic  
from modelo.clientedao import ClienteDAO

#2.- Cargar archivo .ui
class Load_ui_clientes(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargar archivo .ui
        uic.loadUi("ui/ui_clientes.ui", self)
        self.show()

        self.clientedao = ClienteDAO()

#3.- Configurar contenedores
        #eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        #Cerrar ventana
        self.boton_salir.clicked.connect(self.regresar_menu)
        # mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana
        #menu lateral
        self.boton_menu.clicked.connect(self.mover_menu)
        #Fijar ancho columnas
        self.tabla_clientes.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

#4.- Conectar botones a funciones
        #Botones para cambiar de página
        self.boton_agregar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_agregar))
        self.boton_buscar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_buscar))
        self.boton_actualizar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))
        self.boton_eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_eliminar))
        self.boton_consultar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_consultar))

        #Botones para guardar, buscar, actualizar, eliminar y salir
        self.boton_accion_agregar.clicked.connect(self.guardar_cliente)
        self.boton_accion_actualizar.clicked.connect(self.actualizar_cliente)
        self.boton_accion_eliminar.clicked.connect(self.eliminar_cliente)
        self.boton_accion_limpiar.clicked.connect(self.limpiar_formulario)
        self.boton_accion_refrescar.clicked.connect(self.llenar_tabla)

        self.boton_buscar_actualizar.clicked.connect(self.buscar_actualizar)
        self.boton_buscar_eliminar.clicked.connect(self.buscar_eliminar)
        self.boton_buscar_buscar.clicked.connect(self.buscar_buscar)

#5.- Operaciones con el modelo de datos 
    def guardar_cliente(self):
        self.clientedao.cliente.clave = self.clave_agregar.text()
        self.clientedao.cliente.nombre = self.nombre_agregar.text()
        self.clientedao.cliente.rfc = self.rfc_agregar.text()
        self.clientedao.cliente.telefono = self.telefono_agregar.text()
        self.clientedao.cliente.email = self.email_agregar.text()
        self.clientedao.cliente.direccion = self.direccion_agregar.text()

        self.clientedao.guardarCliente()
        self.mensaje.setText("El cliente ha sido registrado!")
        # Limpiar campos después de guardar
        self.clave_agregar.setText("")
        self.nombre_agregar.setText("")
        self.rfc_agregar.setText("")
        self.telefono_agregar.setText("")
        self.email_agregar.setText("")
        self.direccion_agregar.setText("")

    def limpiar_formulario(self):
        # Limpiar página BUSCAR
        self.clave_buscar.setText("")
        self.nombre_buscar.setText("")
        self.rfc_buscar.setText("")
        self.telefono_buscar.setText("")
        self.email_buscar.setText("")
        self.direccion_buscar.setText("")
        self.mensaje.setText("")

    def actualizar_cliente(self):
        self.clientedao.cliente.clave = self.clave_actualizar.text()
        self.clientedao.cliente.nombre = self.nombre_actualizar.text()
        self.clientedao.cliente.rfc = self.rfc_actualizar.text()
        self.clientedao.cliente.telefono = self.telefono_actualizar.text()
        self.clientedao.cliente.email = self.email_actualizar.text()
        self.clientedao.cliente.direccion = self.direccion_actualizar.text()

        self.clientedao.actualizarCliente()
        self.mensaje.setText("Cliente actualizado correctamente!")
        self.llenar_tabla()

    def eliminar_cliente(self):
        self.clientedao.cliente.clave = self.clave_eliminar.text()
        
        self.clientedao.eliminarCliente()
        self.mensaje.setText("Cliente eliminado correctamente!")
        self.llenar_tabla()
        
        # Limpiar campos después de eliminar
        self.clave_eliminar.setText("")
        self.nombre_eliminar.setText("")
        self.rfc_eliminar.setText("")
        self.telefono_eliminar.setText("")
        self.email_eliminar.setText("")
        self.direccion_eliminar.setText("")

    def llenar_tabla(self):
        datos = self.clientedao.listarClientes()
        self.tabla_clientes.setRowCount(len(datos))
        fila = 0
        for item in datos:
            self.tabla_clientes.setItem(fila, 0, QtWidgets.QTableWidgetItem(item[1]))  # Clave
            self.tabla_clientes.setItem(fila, 1, QtWidgets.QTableWidgetItem(item[2]))  # Nombre
            self.tabla_clientes.setItem(fila, 2, QtWidgets.QTableWidgetItem(item[3]))  # RFC
            self.tabla_clientes.setItem(fila, 3, QtWidgets.QTableWidgetItem(item[4]))  # Teléfono
            self.tabla_clientes.setItem(fila, 4, QtWidgets.QTableWidgetItem(item[5]))  # Email
            self.tabla_clientes.setItem(fila, 5, QtWidgets.QTableWidgetItem(item[6]))  # Dirección
            fila += 1

    def buscar_actualizar(self):
        self.clientedao.cliente.clave = self.clave_actualizar.text()
        datos = self.clientedao.buscarCliente()
        
        if len(datos) == 0:
            self.mensaje.setText('Clave no existe')
        else:
            # Llenar campos de actualizar con los datos encontrados
            self.clave_actualizar.setText(datos[0][1])  # Clave
            self.nombre_actualizar.setText(datos[0][2])  # Nombre
            self.rfc_actualizar.setText(datos[0][3])  # RFC
            self.telefono_actualizar.setText(datos[0][4])  # Teléfono
            self.email_actualizar.setText(datos[0][5])  # Email
            self.direccion_actualizar.setText(datos[0][6])  # Dirección
            self.mensaje.setText('Cliente listo para actualizar')

    def buscar_eliminar(self):
        self.clientedao.cliente.clave = self.clave_eliminar.text()
        datos = self.clientedao.buscarCliente()
        
        if len(datos) == 0:
            self.mensaje.setText('Clave no existe')
        else:
            # Llenar campos de eliminar con los datos encontrados
            self.clave_eliminar.setText(datos[0][1])  # Clave
            self.nombre_eliminar.setText(datos[0][2])  # Nombre
            self.rfc_eliminar.setText(datos[0][3])  # RFC
            self.telefono_eliminar.setText(datos[0][4])  # Teléfono
            self.email_eliminar.setText(datos[0][5])  # Email
            self.direccion_eliminar.setText(datos[0][6])  # Dirección
            self.mensaje.setText('Cliente listo para eliminar')

    def buscar_buscar(self):
        self.clientedao.cliente.clave = self.clave_buscar.text()
        datos = self.clientedao.buscarCliente()
        if len(datos) == 0:
            self.mensaje.setText('Clave no existe')
        else:
            self.nombre_buscar.setText(datos[0][2])  # Nombre
            self.rfc_buscar.setText(datos[0][3])  # RFC
            self.telefono_buscar.setText(datos[0][4])  # Teléfono
            self.email_buscar.setText(datos[0][5])  # Email
            self.direccion_buscar.setText(datos[0][6])  # Dirección
            self.mensaje.setText('Cliente encontrado')

# 6.- mover ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()

        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

#7.- Mover menú
    def mover_menu(self):
        if True:			
            width = self.frame_lateral.width()
            widthb = self.boton_menu.width()
            normal = 0
            if width==0:
                extender = 200
                self.boton_menu.setText("Menú")
            else:
                extender = normal
                self.boton_menu.setText("")
                
            self.animacion = QPropertyAnimation(self.frame_lateral, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
            
            self.animacionb = QPropertyAnimation(self.boton_menu, b'minimumWidth')
            self.animacionb.setStartValue(width)
            self.animacionb.setEndValue(extender)
            self.animacionb.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacionb.start()
        
    def regresar_menu(self):
        from load.load_ui_menu import Load_ui_menu  # ← IMPORTAR DENTRO de la función
        self.ventana_menu = Load_ui_menu()
        self.ventana_menu.show()
        self.close()