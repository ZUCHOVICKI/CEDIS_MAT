# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(588, 407)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 591, 361))
        self.tabWidget.setObjectName("tabWidget")
        self.AgregarElemento = QtWidgets.QWidget()
        self.AgregarElemento.setObjectName("AgregarElemento")
        self.Elementos = QtWidgets.QComboBox(self.AgregarElemento)
        self.Elementos.setGeometry(QtCore.QRect(40, 90, 171, 22))
        self.Elementos.setObjectName("Elementos")
        self.Elementos.addItem("")
        self.Cantidad = QtWidgets.QSpinBox(self.AgregarElemento)
        self.Cantidad.setGeometry(QtCore.QRect(250, 90, 42, 22))
        self.Cantidad.setObjectName("Cantidad")
        self.AgregarElementoButton = QtWidgets.QPushButton(self.AgregarElemento)
        self.AgregarElementoButton.setGeometry(QtCore.QRect(350, 90, 75, 23))
        self.AgregarElementoButton.setObjectName("AgregarElementoButton")
        self.FechaElemento = QtWidgets.QDateEdit(self.AgregarElemento)
        self.FechaElemento.setGeometry(QtCore.QRect(70, 40, 110, 22))
        self.FechaElemento.setObjectName("FechaElemento")
        self.ElementosCompletos = QtWidgets.QTextBrowser(self.AgregarElemento)
        self.ElementosCompletos.setGeometry(QtCore.QRect(130, 140, 256, 192))
        self.ElementosCompletos.setObjectName("ElementosCompletos")
        self.tabWidget.addTab(self.AgregarElemento, "")
        self.AgregarIndividual = QtWidgets.QWidget()
        self.AgregarIndividual.setObjectName("AgregarIndividual")
        self.Fecha_individual = QtWidgets.QDateEdit(self.AgregarIndividual)
        self.Fecha_individual.setGeometry(QtCore.QRect(70, 30, 110, 22))
        self.Fecha_individual.setObjectName("Fecha_individual")
        self.AgregarComponenteButton = QtWidgets.QPushButton(self.AgregarIndividual)
        self.AgregarComponenteButton.setGeometry(QtCore.QRect(350, 80, 75, 23))
        self.AgregarComponenteButton.setObjectName("AgregarComponenteButton")
        self.CantidadIndividual = QtWidgets.QSpinBox(self.AgregarIndividual)
        self.CantidadIndividual.setGeometry(QtCore.QRect(250, 80, 42, 22))
        self.CantidadIndividual.setObjectName("CantidadIndividual")
        self.ElementosIndividuales = QtWidgets.QTextBrowser(self.AgregarIndividual)
        self.ElementosIndividuales.setGeometry(QtCore.QRect(230, 120, 256, 192))
        self.ElementosIndividuales.setObjectName("ElementosIndividuales")
        self.OptionElementos = QtWidgets.QComboBox(self.AgregarIndividual)
        self.OptionElementos.setGeometry(QtCore.QRect(240, 30, 181, 22))
        self.OptionElementos.setObjectName("OptionElementos")
        self.OptionComponente = QtWidgets.QComboBox(self.AgregarIndividual)
        self.OptionComponente.setGeometry(QtCore.QRect(60, 80, 141, 22))
        self.OptionComponente.setObjectName("OptionComponente")
        self.tabWidget.addTab(self.AgregarIndividual, "")
        self.EliminarIndividual = QtWidgets.QWidget()
        self.EliminarIndividual.setObjectName("EliminarIndividual")
        self.EliminarIndividualBoton = QtWidgets.QPushButton(self.EliminarIndividual)
        self.EliminarIndividualBoton.setGeometry(QtCore.QRect(290, 170, 75, 23))
        self.EliminarIndividualBoton.setObjectName("EliminarIndividualBoton")
        self.FechasEliminar = QtWidgets.QComboBox(self.EliminarIndividual)
        self.FechasEliminar.setGeometry(QtCore.QRect(130, 130, 161, 22))
        self.FechasEliminar.setObjectName("FechasEliminar")
        self.tabWidget.addTab(self.EliminarIndividual, "")
        self.Visualizar = QtWidgets.QWidget()
        self.Visualizar.setObjectName("Visualizar")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.Visualizar)
        self.textBrowser_3.setGeometry(QtCore.QRect(30, 10, 341, 271))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.GenerarOrden = QtWidgets.QPushButton(self.Visualizar)
        self.GenerarOrden.setGeometry(QtCore.QRect(414, 122, 111, 21))
        self.GenerarOrden.setObjectName("GenerarOrden")
        self.tabWidget.addTab(self.Visualizar, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 588, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Elementos.setItemText(0, _translate("MainWindow", "Elementos"))
        self.AgregarElementoButton.setText(_translate("MainWindow", "Agregar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AgregarElemento), _translate("MainWindow", "Agregar Elemento"))
        self.AgregarComponenteButton.setText(_translate("MainWindow", "Agregar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AgregarIndividual), _translate("MainWindow", "Agregar Componente"))
        self.EliminarIndividualBoton.setText(_translate("MainWindow", "Eliminar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EliminarIndividual), _translate("MainWindow", "Eliminar Individual"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.GenerarOrden.setText(_translate("MainWindow", "Generar Reporte"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Visualizar), _translate("MainWindow", "Visualizar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
