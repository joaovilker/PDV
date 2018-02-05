# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from Views.busca_pedido import Ui_BuscaPedido
from Crud.pedidos import CrudPedidos

class BuscaPedido(QtGui.QDialog, Ui_BuscaPedido):
    def buscaProduos(self, janela):
        super(BuscaPedido, self).setBuscaPedido(janela)

        self.todos_pedidos()


    def todos_pedidos(self):
        busca = unicode(self.lineEdit.text()).encode("utf8")
        busca = CrudPedidos()
        busca.busca_pedidos(busca)


        i = 0;
        while i < len(busca.cod_pedido):

            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i, 0, QtGui.QTableWidgetItem(str(busca.cod_pedido[i])))
            self.tableWidget.setItem(i, 1, QtGui.QTableWidgetItem(busca.cliente[i]))
            self.tableWidget.setItem(i, 2, QtGui.QTableWidgetItem(busca.status_pedido[i]))
            self.tableWidget.setItem(i, 3, QtGui.QTableWidgetItem(busca.data_entrega[i]))
            self.tableWidget.setItem(i, 4, QtGui.QTableWidgetItem("R$: "+format(busca.entrada[i], ".2f")))
            self.tableWidget.setItem(i, 5, QtGui.QTableWidgetItem("R$: " + format(busca.saldo_devedor[i], ".2f")))
            self.tableWidget.setItem(i, 6, QtGui.QTableWidgetItem("R$: " + format(busca.valor_total[i], ".2f")))


            i += 1

