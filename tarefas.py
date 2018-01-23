# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from Views.tarefas import Ui_frame_tarefa
from Views.confirmacao import Ui_Dialog

class MainTarefa(Ui_frame_tarefa):
    def main_tarefa(self, frame):
        super(MainTarefa, self).setTarefas(frame)
        self.ct_frame_tarefa.show()

        # Estilo dos Botões
        self.bt_cadastrar_tarefa.setStyleSheet("color: #FFF; border: 2px solid #0CA3D2; border-radius:10px;"
                                               "background: #FFF; color: #000")

        self.bt_cadastrar_tarefa.setText("Cadastrar")
        self.bt_cadastrar_tarefa.clicked.connect(self.confirmar_tarefa)

        self.bt_cancelar_cadastro.setStyleSheet("color: #FFF; border: 2px solid red; border-radius:10px;"
                                              "background: #FFF; color: #000")
        self.bt_cancelar_cadastro.setText("Cancelar")


        # self.filtro = QtGui.QSortFilterProxyModel()
        # self.filtro.setSourceModel(QtGui.QStandardItemModel(self.tabela_taregas_agendadas))
        # self.filtro.setFilterKeyColumn(1)
        # Tamanho, acao  e conteudo da tabela produtos
        self.tabela_taregas_agendadas.setColumnWidth(0, 75)
        self.tabela_taregas_agendadas.setColumnWidth(1, 120)
        self.tabela_taregas_agendadas.setColumnWidth(2, 80)
        self.tabela_taregas_agendadas.horizontalHeader().setResizeMode(QtGui.QHeaderView.Fixed)
        self.tabela_taregas_agendadas.verticalHeader().setVisible(False)

    def confirmar_tarefa(self):
        Janela = Ui_Dialog()
        Dialog = QtGui.QDialog()
        Janela.setConfirmacao(Dialog)
        Dialog.exec_()




