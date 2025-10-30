from PyQt5 import QtWidgets
import sys
from load.load_ui_login import Load_ui_login

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Load_ui_login()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()