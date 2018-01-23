# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from Views.clientes import Ui_frame_clientes
from Class.Funcoes import Funcoes
from Views.confirmacao import Ui_Dialog
from Crud.clientes import CrudCliente
from Crud.lista_indices import ListasIndices

class MainClientes(Ui_frame_clientes):
    def main_clientes(self, frame):
        super(MainClientes, self).setClientes(frame)
        self.ct_frame_clientes.show()

        # Classes
        self.funcao = Funcoes()
        self.lista_indicies = ListasIndices()

        # Ajustes no Formulário
        self.tx_telefone_cliente.setInputMask("(00) 00000-0000#")


        # Estilo dos Botoes
        self.funcao.estilo_botao_acao(self.bt_cadastrar_clientes, self.bt_cancelar_cliente)

        # Tamanho, acao  e conteudo da tabela produtos
        self.tabela_clientes.setColumnWidth(0, 40)
        self.tabela_clientes.setColumnWidth(1, 250)
        self.tabela_clientes.horizontalHeader().setResizeMode(QtGui.QHeaderView.Fixed)
        self.tabela_clientes.verticalHeader().setVisible(False)
        # self.tabela_clientes.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        self.tabela_clientes.cellDoubleClicked.connect(self.selecionar_cliente)
        self.tx_buscar_clientes.returnPressed.connect(self.busca_na_tabela)

        self.tx_cod = QtGui.QLineEdit()
        self.tx_cod.setHidden(True)




        # Ação dos Botoes
        # Cadastro
        self.bt_cadastrar_clientes.clicked.connect(self.confirmar_cliente)
        self.bt_cancelar_cliente.clicked.connect(self.cancela_cliente)

        # Combobox Estados
        self.lista_indicies.todos_estados()
        self.tx_estado_cliente.addItems(self.lista_indicies.lista_estados)
        self.tx_estado_cliente.setEditable(True)
        self.tx_estado_cliente.setCurrentIndex(18)

        # add itens tabela
        self.listar_clientes()


    def listar_clientes(self):
        busca = CrudCliente()
        busca.crud_tabela_cliente()

        while self.tabela_clientes.rowCount() > 0:
            self.tabela_clientes.removeRow(0)

        x = 0
        while x < len(busca.nome_cliente):
            self.tabela_clientes.insertRow(x)
            self.tabela_clientes.setItem(x, 0, QtGui.QTableWidgetItem(str(busca.cod_cliente[x])))
            self.tabela_clientes.setItem(x, 1, QtGui.QTableWidgetItem(busca.nome_cliente[x]))
            x += 1



    # selecionar item na tabela
    def selecionar_cliente(self, row, col):

        busca = CrudCliente()
        busca.buscar_cliente_selecionado(str(self.tabela_clientes.item(row, 0).text()))
        self.tx_cod.setText(str(busca.cod_cliente))
        self.tx_nome_cliente.setText(busca.nome_cliente)
        self.tx_nome_cliente_2.setText(busca.sobremone)
        self.tx_cpf_cliente.setText(busca.cpf)
        self.tx_telefone_cliente.setText(busca.telefone)
        self.tx_endereco_cliente.setText(busca.endereco)
        self.tx_numero_cliente.setText(str(busca.num))
        self.tx_bairo_cliente.setText(busca.bairro)
        self.tx_complemento_cliente.setText(busca.comeplemento)
        self.tx_cep_cliente.setText(str(busca.cep))
        self.tx_referencia_cliente.setText(busca.referencia)
        self.tx_cidade_cliente.setText(busca.cidade)
        self.tx_estado_cliente.addItem(busca.estado)

    def busca_na_tabela(self):
        while self.tabela_clientes.rowCount() > 0:
            self.tabela_clientes.removeRow(0)
        busca = CrudCliente()

        busca.busca_tabela(unicode(self.tx_buscar_clientes.text()).encode("utf-8"))

        i = 0
        while i < len(busca.nome_cliente):
            self.tabela_clientes.insertRow(i)
            self.tabela_clientes.setItem(i, 0, QtGui.QTableWidgetItem(str(busca.cod_cliente[i])))
            self.tabela_clientes.setItem(i, 1, QtGui.QTableWidgetItem(busca.nome_cliente[i]))
            i += 1

        self.tx_buscar_clientes.clear()



    #Janela COnfirmação de Cadastro
    def confirmar_cliente(self):
        Janela = Ui_Dialog()
        Dialog = QtGui.QDialog()
        Janela.setConfirmacao(Dialog)
        Janela.lb_info.setText("Cliente:")
        Janela.lb_titulo_modal.setText("Cadastrar / Atualizar?")
        Janela.lb_descricao.setText(unicode(self.tx_nome_cliente.text()))
        Janela.buttonBox.width()
        Janela.buttonBox.setStyleSheet("color: #FFF; border: 2px solid #0CA3D2; border-radius:10px;"
                                       "background: #FFF; color: #000; width: 100px; height: 30px")
        QtCore.QObject.connect(Janela.buttonBox, QtCore.SIGNAL("accepted()"), self.cadastrar_cliente)
        Dialog.exec_()

    def cancela_cliente(self):
        for filho in self.ct_clientes.findChildren(QtGui.QLineEdit):
            filho.clear()
        self.tx_cod.clear()


    def cadastrar_cliente(self):
        Cadastro = CrudCliente()
        Cadastro.cod_cliente = str(self.tx_cod.text())
        Cadastro.nome_cliente = unicode(self.tx_nome_cliente.text()).encode("utf8")
        Cadastro.sobremone = unicode(self.tx_nome_cliente_2.text()).encode("utf8")
        Cadastro.telefone = unicode(self.tx_telefone_cliente.text()).encode("utf8")
        Cadastro.cpf = unicode(self.tx_cpf_cliente.text()).encode("utf8")
        Cadastro.endereco = unicode(self.tx_endereco_cliente.text()).encode("utf8")
        Cadastro.num = str(self.tx_numero_cliente.text())
        Cadastro.bairro = unicode(self.tx_bairo_cliente.text()).encode("utf8")
        Cadastro.comeplemento = unicode(self.tx_complemento_cliente.text()).encode("utf8")
        Cadastro.cep = unicode(self.tx_cep_cliente.text()).encode("utf8")
        Cadastro.referencia = unicode(self.tx_referencia_cliente.text()).encode("utf8")
        Cadastro.cidade = unicode(self.tx_cidade_cliente.text()).encode("utf8")
        Cadastro.estado = unicode(self.tx_estado_cliente.currentText())
        Cadastro.cadastro_cliente()

        for filho in self.ct_clientes.findChildren(QtGui.QLineEdit):
            filho.clear()
        self.tx_cod.clear()
        self.tx_buscar_clientes.clear()
        self.busca_na_tabela()









