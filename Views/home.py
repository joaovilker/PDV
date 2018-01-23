# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
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

class Ui_frame_home(object):
    def setHome(self, frame_home):
        frame_home.setObjectName(_fromUtf8("frame_home"))
        frame_home.resize(900, 493)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        frame_home.setFont(font)
        frame_home.setStyleSheet(_fromUtf8(""))
        frame_home.setFrameShape(QtGui.QFrame.StyledPanel)
        frame_home.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_frame_inicio = QtGui.QFrame(frame_home)
        self.ct_frame_inicio.setGeometry(QtCore.QRect(0, 0, 900, 493))
        self.ct_frame_inicio.setStyleSheet(_fromUtf8("background: #0CA3D2"))
        self.ct_frame_inicio.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ct_frame_inicio.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_frame_inicio.setObjectName(_fromUtf8("ct_frame_inicio"))
        self.ct_pedidos = QtGui.QFrame(self.ct_frame_inicio)
        self.ct_pedidos.setGeometry(QtCore.QRect(30, 20, 500, 423))
        self.ct_pedidos.setStyleSheet(_fromUtf8("background: #FFF;\n"
"border: 5px solid #fFf;\n"
"border-radius: 20px;\n"
""))
        self.ct_pedidos.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ct_pedidos.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_pedidos.setObjectName(_fromUtf8("ct_pedidos"))
        self.lb_pedidos_agendados_2 = QtGui.QLabel(self.ct_pedidos)
        self.lb_pedidos_agendados_2.setGeometry(QtCore.QRect(120, 10, 260, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.lb_pedidos_agendados_2.setFont(font)
        self.lb_pedidos_agendados_2.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_pedidos_agendados_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_pedidos_agendados_2.setObjectName(_fromUtf8("lb_pedidos_agendados_2"))
        self.tabela_pedidos = QtGui.QTableWidget(self.ct_pedidos)
        self.tabela_pedidos.setGeometry(QtCore.QRect(5, 45, 490, 350))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tabela_pedidos.setFont(font)
        self.tabela_pedidos.setStyleSheet(_fromUtf8("background: #FFF; border: none; border-radius: 0"))
        self.tabela_pedidos.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabela_pedidos.setObjectName(_fromUtf8("tabela_pedidos"))
        self.tabela_pedidos.setColumnCount(4)
        self.tabela_pedidos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        item.setFont(font)
        self.tabela_pedidos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        item.setFont(font)
        self.tabela_pedidos.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        item.setFont(font)
        self.tabela_pedidos.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        item.setFont(font)
        self.tabela_pedidos.setHorizontalHeaderItem(3, item)
        self.tabela_pedidos.horizontalHeader().setVisible(True)
        self.tabela_pedidos.verticalHeader().setVisible(False)
        self.tabela_pedidos.verticalHeader().setHighlightSections(True)
        self.ct_pedidos_2 = QtGui.QFrame(self.ct_frame_inicio)
        self.ct_pedidos_2.setGeometry(QtCore.QRect(570, 20, 300, 423))
        self.ct_pedidos_2.setStyleSheet(_fromUtf8("background: #FFF;\n"
"border: 2px solid #fff;\n"
"border-radius: 20px;"))
        self.ct_pedidos_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ct_pedidos_2.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_pedidos_2.setObjectName(_fromUtf8("ct_pedidos_2"))
        self.lb_tarefas_agendadas_2 = QtGui.QLabel(self.ct_pedidos_2)
        self.lb_tarefas_agendadas_2.setGeometry(QtCore.QRect(75, 10, 150, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.lb_tarefas_agendadas_2.setFont(font)
        self.lb_tarefas_agendadas_2.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_tarefas_agendadas_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_tarefas_agendadas_2.setObjectName(_fromUtf8("lb_tarefas_agendadas_2"))
        self.tabela_tarefas = QtGui.QTableWidget(self.ct_pedidos_2)
        self.tabela_tarefas.setGeometry(QtCore.QRect(5, 45, 290, 192))
        self.tabela_tarefas.setStyleSheet(_fromUtf8("background: #FFF; border: none; border-radius: 0"))
        self.tabela_tarefas.setObjectName(_fromUtf8("tabela_tarefas"))
        self.tabela_tarefas.setColumnCount(2)
        self.tabela_tarefas.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        item.setFont(font)
        self.tabela_tarefas.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabela_tarefas.setHorizontalHeaderItem(1, item)

        self.tradHome(frame_home)
        QtCore.QMetaObject.connectSlotsByName(frame_home)

    def tradHome(self, frame_home):
        frame_home.setWindowTitle(_translate("frame_home", "Frame", None))
        self.lb_pedidos_agendados_2.setText(_translate("frame_home", "Pedidos agendados", None))
        item = self.tabela_pedidos.horizontalHeaderItem(0)
        item.setText(_translate("frame_home", "Data", None))
        item = self.tabela_pedidos.horizontalHeaderItem(1)
        item.setText(_translate("frame_home", "Cliente", None))
        item = self.tabela_pedidos.horizontalHeaderItem(2)
        item.setText(_translate("frame_home", "Telefone", None))
        item = self.tabela_pedidos.horizontalHeaderItem(3)
        item.setText(_translate("frame_home", "Detalhes", None))
        self.lb_tarefas_agendadas_2.setText(_translate("frame_home", "Tarefas do Dia", None))
        item = self.tabela_tarefas.horizontalHeaderItem(0)
        item.setText(_translate("frame_home", "Data", None))
        item = self.tabela_tarefas.horizontalHeaderItem(1)
        item.setText(_translate("frame_home", "Tarefa", None))

