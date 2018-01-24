# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'busca_cliente.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DialogBuscarCliente(object):
    def setBuscarCliente(self, DialogBuscarCliente):
        DialogBuscarCliente.setObjectName(_fromUtf8("DialogBuscarCliente"))
        DialogBuscarCliente.resize(400, 350)
        self.frame = QtGui.QFrame(DialogBuscarCliente)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 350))
        self.frame.setStyleSheet(_fromUtf8("background: #0CA3D2"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 380, 330))
        self.frame_2.setStyleSheet(_fromUtf8("background: #FFF;\n"
"border: 5px solid #fFf;\n"
"border-radius: 20px;\n"
""))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.lb_titulo_modal = QtGui.QLabel(self.frame_2)
        self.lb_titulo_modal.setGeometry(QtCore.QRect(90, 20, 200, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        self.lb_titulo_modal.setFont(font)
        self.lb_titulo_modal.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_titulo_modal.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_titulo_modal.setObjectName(_fromUtf8("lb_titulo_modal"))
        self.lb_info = QtGui.QLabel(self.frame_2)
        self.lb_info.setGeometry(QtCore.QRect(20, 70, 80, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.lb_info.setFont(font)
        self.lb_info.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_info.setObjectName(_fromUtf8("lb_info"))
        self.lineEdit = QtGui.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(110, 70, 250, 25))
        self.lineEdit.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.tableWidget = QtGui.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(20, 110, 340, 192))
        self.tableWidget.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solide #FFF;\n"
"background: #FFF;\n"
"color: #000"))
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.verticalHeader().setVisible(False)

        self.tradBuscaCliente(DialogBuscarCliente)
        QtCore.QMetaObject.connectSlotsByName(DialogBuscarCliente)

    def tradBuscaCliente(self, DialogBuscarCliente):
        DialogBuscarCliente.setWindowTitle(_translate("DialogBuscarCliente", "Buscar Cliente", None))
        self.lb_titulo_modal.setText(_translate("DialogBuscarCliente", "Alterar Senha", None))
        self.lb_info.setText(_translate("DialogBuscarCliente", "Nome", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("DialogBuscarCliente", "Cod.", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("DialogBuscarCliente", "Nome:", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("DialogBuscarCliente", "Telefone", None))

