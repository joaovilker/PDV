# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from Views.home import Ui_frame_home

class MainHome( Ui_frame_home):
    def main_home(self, frame):
        super(MainHome, self).setHome(frame)
        self.ct_frame_inicio.show()

        # Tabela pedidos
        self.tabela_pedidos.setColumnWidth(0, 100)
        self.tabela_pedidos.setColumnWidth(1, 180)
        self.tabela_pedidos.setColumnWidth(2, 110)
        self.tabela_pedidos.setColumnWidth(3, 100)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(7)
        font.setBold(True)
        self.tabela_pedidos.setFont(font)
        self.tabela_pedidos.insertRow(0)
        self.tabela_pedidos.setItem(0, 0, QtGui.QTableWidgetItem(u"12-01-2018"))
        self.tabela_pedidos.setItem(0, 1, QtGui.QTableWidgetItem(u"AndrÉ França"))
        self.tabela_pedidos.setItem(0, 2, QtGui.QTableWidgetItem(u"(22) 99706-9161"))
        self.tabela_pedidos.setItem(0, 3, QtGui.QTableWidgetItem(u"Caneca Porcelana"))

        self.tabela_pedidos.insertRow(1)
        self.tabela_pedidos.setItem(1, 0, QtGui.QTableWidgetItem(u"30-12-1986"))
        self.tabela_pedidos.setItem(1, 1, QtGui.QTableWidgetItem(u"André Luis França"))
        self.tabela_pedidos.setItem(1, 2, QtGui.QTableWidgetItem(u"(22) 99706-9161"))
        self.tabela_pedidos.setItem(1, 3, QtGui.QTableWidgetItem(u"Caneca Porcelana"))

        self.tabela_pedidos.cellDoubleClicked.connect(self.ok)

        # Tabela tarefas
        self.tabela_tarefas.setColumnWidth(0, 100)
        self.tabela_tarefas.setColumnWidth(1, 190)
        # botao = QtGui.QPushButton()
        # botao.setText("Ver")
        # botao.clicked.connect(lambda: self.ok("Ola") )
        # botao.setStyleSheet("border-radius: 5px; background: #069")
        #
        # self.tabela_pedidos.setCellWidget(0, 0, botao)



    def ok(self, row, col):
        print "Click on " + str(row) + " " + str(col)
        print self.tabela_pedidos.item(row, 0 ).text()
