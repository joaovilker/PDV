# coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from Views.usuarios import Ui_FrameUsuarios
from Class.Funcoes import Funcoes
from Views.confirmacao import Ui_Dialog
from Views.janela_senha import Ui_Dialog_senha
from Crud.usuarios import CrudUsuarios
from Crud.lista_indices import ListasIndices

class MainUsuarios(Ui_FrameUsuarios):
    def main_usuarios(self, frame):
        super(MainUsuarios, self).setUsuarios(frame)


        # Classe
        self.funcao = Funcoes()
        self.combobox_status = ListasIndices()
        self.combobox_status.lista_status()
        self.combobox_status.todos_estados()
        self.combobox_status.combobox_nivel()

        # Tamanho, acao  e conteudo da tabela produtos
        self.tabela_usuarios.setColumnWidth(0, 40)
        self.tabela_usuarios.setColumnWidth(1, 250)
        self.tabela_usuarios.horizontalHeader().setResizeMode(QtGui.QHeaderView.Fixed)
        self.tabela_usuarios.verticalHeader().setVisible(False)
        # Ação de 2 clickes na tabela
        self.tabela_usuarios.cellDoubleClicked.connect(self.selecionar_usuarios)
        # Campo Busca
        self.tx_buscar_usuarios.returnPressed.connect(self.busca_usuarios)
        # Preechendo tabela
        self.add_tabela_usuarios()

        # Campo Oculdo ID usuarios
        self.tx_cod_usuario = QtGui.QLineEdit()
        self.tx_cod_usuario.setHidden(True)

        # Ajustes, Campos e Ações Formulario
        # Combobox Status
        self.tx_status.addItems(self.combobox_status.lst_status)
        self.tx_status.setCurrentIndex(0)
        self.tx_status.setEditable(False)
        # Combobox Estados
        self.tx_estado_usuario.addItems(self.combobox_status.lista_estados)
        self.tx_estado_usuario.setEditable(True)
        self.tx_estado_usuario.setCurrentIndex(18)
        # Combobox Nível
        self.tx_nivel_acesso.addItems(self.combobox_status.lst_nivel)
        # Desabilitando botão cadastro
        self.bt_cadastrar_usuario.setEnabled(False)
        # Funcao Habilitar botão incluir
        self.tx_login.textChanged.connect(self.habilitar)
        self.tx_nome_usuario.textChanged.connect(self.habilitar)

        # Botao cadastrar
        self.bt_cadastrar_usuario.clicked.connect(self.confirmar_usuario)
        # Botao Cancelar
        self.bt_cancelar_.clicked.connect(self.cancelar_cadastro_usuarios)
        # Estilo dos botões
        self.funcao.estilo_botao_acao(self.bt_cadastrar_usuario, self.bt_cancelar_)
        # Botao Alterar Senha
        self.bt_aterar_senha.setEnabled(False)
        efeito = QtGui.QGraphicsDropShadowEffect()
        efeito.setColor(QtGui.QColor("#ff00ff"))
        efeito.setOffset(0, 0)
        efeito.setBlurRadius(15)
        self.bt_aterar_senha.setGraphicsEffect(efeito)
        self.bt_aterar_senha.setStyleSheet(" QPushButton{border-radius: 10px; border: none; background: #00ffff;}"
                            "QPushButton:disabled {background: #FFF}"
                                           "QPushButton:hover {color: #fff}")
        # Acão Botão Alterar Senha
        self.bt_aterar_senha.clicked.connect(self.alterar_senha)


        """ Exbibe o Flame """
        self.ct_frame_usuarios.show()
        """ Fim """

    def add_tabela_usuarios(self):
        busca = CrudUsuarios()
        busca.crud_tabela_usuarios()
        i = 0
        while i < len(busca.usuario):
            self.tabela_usuarios.insertRow(i)
            self.tabela_usuarios.setItem(i, 0, QtGui.QTableWidgetItem(str(busca.id_usuario[i])))
            self.tabela_usuarios.setItem(i, 1, QtGui.QTableWidgetItem(busca.usuario[i]))
            i += 1


    def confirmar_usuario(self):
        Janela = Ui_Dialog()
        Dialog = QtGui.QDialog()
        Janela.setConfirmacao(Dialog)
        Janela.lb_info.setText(QtCore.QString.fromUtf8("Usuário"))
        Janela.lb_titulo_modal.setText("Cadastrar / Atualizar?")
        Janela.lb_descricao.setText(unicode(self.tx_nome_usuario.text()))
        Janela.buttonBox.setStyleSheet("color: #FFF; border: 2px solid #0CA3D2; border-radius:10px;"
                                       "background: #FFF; color: #000; width: 100px; height: 30px")
        QtCore.QObject.connect(Janela.buttonBox, QtCore.SIGNAL("accepted()"), self.cadastrar_usuario)
        Dialog.exec_()

    # Selecionando da tabela
    def selecionar_usuarios(self, row):
        busca = CrudUsuarios()

        busca.buscar_usuarios_selecionado(str(self.tabela_usuarios.item(row, 0).text()))
        self.tx_cod_usuario.setText(str(busca.id_usuario))
        self.tx_nome_usuario.setText(busca.nome_usuario)
        self.tx_sobrenome_usuario.setText(busca.sobremone)
        self.tx_cpf_usuario.setText(busca.cpf)
        self.tx_telefone_usuario.setText(busca.telefone)
        self.tx_endereco_usuario.setText(busca.endereco)
        self.tx_numero_endereco_usuario.setText(str(busca.num))
        self.tx_bairo_usuario.setText(busca.bairro)
        self.tx_complemento_usuario.setText(busca.comeplemento)
        self.tx_cep_usuario.setText(str(busca.cep))
        self.tx_referencia_usuario.setText(busca.referencia)
        self.tx_cidade_usuario.setText(busca.cidade)
        self.tx_estado_usuario.setCurrentIndex(int(busca.estado))
        self.tx_login.setText(busca.usuario)
        self.tx_status.setCurrentIndex(busca.status)
        self.tx_nivel_acesso.setCurrentIndex(busca.nivel)

        # Ativando Botão Alterar Senha
        self.bt_aterar_senha.setEnabled(True)



    # Busca Campo pesquisa
    def busca_usuarios(self):
        # self.campo =  self.tx_buscar_produto.text()
        #
        # if len(self.campo) > 3:
        #     print self.tx_buscar_produto.text()
        while self.tabela_usuarios.rowCount() > 0:
            self.tabela_usuarios.removeRow(0)
        busca = CrudUsuarios()
        busca.busca_usuario_tabela(unicode(self.tx_buscar_usuarios.text()).encode("utf-8"))

        i = 0
        while i < len(busca.usuario):
            self.tabela_usuarios.insertRow(i)
            self.tabela_usuarios.setItem(i, 0, QtGui.QTableWidgetItem(str(busca.id_usuario[i])))
            self.tabela_usuarios.setItem(i, 1, QtGui.QTableWidgetItem(busca.usuario[i]))

            i += 1
        self.tx_buscar_usuarios.clear()

    # Habilitar Botao Cadastro
    def habilitar(self, event):
        if len(self.tx_login.text()) > 1 and len(self.tx_nome_usuario.text()) > 1:
            self.bt_cadastrar_usuario.setEnabled(True)
        else:
            self.bt_cadastrar_usuario.setEnabled(False)

    # Cadastro de usuário
    def cadastrar_usuario(self):
        cadastro = CrudUsuarios()
        cadastro.id_usuario = unicode(self.tx_cod_usuario.text()).encode("utf8")
        cadastro.nome_usuario = unicode(self.tx_nome_usuario.text()).encode("utf8")
        cadastro.sobremone = unicode(self.tx_sobrenome_usuario.text()).encode("utf8")
        cadastro.telefone = unicode(self.tx_telefone_usuario.text()).encode("utf8")
        cadastro.cpf = unicode(self.tx_cpf_usuario.text()).encode("utf8")
        cadastro.endereco = unicode(self.tx_endereco_usuario.text()).encode("utf8")
        cadastro.num = self.tx_numero_endereco_usuario.text()
        cadastro.bairro = unicode(self.tx_bairo_usuario.text()).encode("utf8")
        cadastro.comeplemento = unicode(self.tx_complemento_usuario.text()).encode("utf8")
        cadastro.cep = unicode(self.tx_cep_usuario.text()).encode("utf8")
        cadastro.referencia = unicode(self.tx_referencia_usuario.text()).encode("utf8")
        cadastro.cidade = unicode(self.tx_cidade_usuario.text()).encode("utf8")
        cadastro.estado = self.tx_estado_usuario.currentIndex()
        cadastro.usuario = unicode(self.tx_login.text()).encode("utf8")

        cadastro.nivel = self.tx_nivel_acesso.currentIndex()
        cadastro.status = self.tx_status.currentIndex()
        cadastro.cadastro_usuarios()

        # Limpando e atualizando a tabela
        self.busca_usuarios()
        # Limpando todos os campos
        for filho in self.ct_usuarios.findChildren(QtGui.QLineEdit):
            filho.clear()

        self.tx_estado_usuario.setCurrentIndex(0)
        self.tx_nivel_acesso.setCurrentIndex(0)
        self.tx_status.setCurrentIndex(0)

    # Janela Alterar Senha
    def alterar_senha(self):
        Dialog = QtGui.QDialog()
        PopUp = Ui_Dialog_senha()
        PopUp.setAlterarSenha(Dialog)
        # Desabilitando Botão Ok
        PopUp.bt_dialog_alterar_senha.setEnabled(False)

        # Dasabilitando campos de novas senha até que a senha seja cheacada
        PopUp.tx_senha_antiga_2.setEnabled(False)
        PopUp.tx_senha_antiga_3.setEnabled(False)
        # Estilo do PushButton
        PopUp.pushButton.setStyleSheet("QPushButton {color: #FFF; border: 2px solid #0CA3D2; border-radius:10px;"
                                       "background: #00ffff; color: #000; width: 100px; height: 30px}"
                                       "QPushButton:hover{color: #fff; border:2px solid #000 }")

        self.funcao.estilo_botao_acao(PopUp.bt_dialog_alterar_senha, PopUp.bt_dialog_cancelar)
        # Checando senha antiga
        def checar_senha(senha):
            buscar = CrudUsuarios()
            buscar.verifica_senha(str(self.tx_cod_usuario.text()))
            # Checar Senha Antiga

            if buscar.senha == unicode(PopUp.tx_senha_antiga.text()):

                PopUp.tx_senha_antiga.setStyleSheet("background-image: url('Images/ok.png'); "
                                                    "background-position: right; background-repeat: no-repeat; "
                                                    "color: #000; border: 2px solid #0CA3D2; border-radius:10px;")
                PopUp.tx_senha_antiga_2.setEnabled(True)
                PopUp.tx_senha_antiga_3.setEnabled(True)
                PopUp.bt_dialog_alterar_senha.setEnabled(True)

            else:
                PopUp.tx_senha_antiga.setStyleSheet("background-image: url('Images/no.png'); "
                                                    "background-position: right; background-repeat: no-repeat; "
                                                    "color: #000; border: 2px solid #0CA3D2; border-radius:10px;")
                PopUp.tx_senha_antiga_2.setEnabled(False)
                PopUp.tx_senha_antiga_3.setEnabled(False)
                PopUp.bt_dialog_alterar_senha.setEnabled(False)

        # Comparando senhas novas digitadas
        def compara_nova_senha(event):
            if PopUp.tx_senha_antiga_3.text() == PopUp.tx_senha_antiga_2.text():
                PopUp.tx_senha_antiga_2.setStyleSheet("background-image: url('Images/ok.png'); "
                                                    "background-position: right; background-repeat: no-repeat; "
                                                    "color: #000; border: 2px solid #0CA3D2; border-radius:10px;")
                PopUp.tx_senha_antiga_3.setStyleSheet("background-image: url('Images/ok.png'); "
                                                    "background-position: right; background-repeat: no-repeat; "
                                                    "color: #000; border: 2px solid #0CA3D2; border-radius:10px;")
            else:
                PopUp.tx_senha_antiga_2.setStyleSheet("background-image: url('Images/no.png'); "
                                                      "background-position: right; background-repeat: no-repeat; "
                                                      "color: #000; border: 2px solid #0CA3D2; border-radius:10px;")
                PopUp.tx_senha_antiga_3.setStyleSheet("background-image: url('Images/no.png'); "
                                                      "background-position: right; background-repeat: no-repeat; "
                                                      "color: #000; border: 2px solid #0CA3D2; border-radius:10px;")

        # Chamando funcao checa senha on click e return pressed
        PopUp.tx_senha_antiga.returnPressed.connect(lambda : checar_senha(PopUp.tx_senha_antiga.text()))
        PopUp.pushButton.clicked.connect(lambda : checar_senha(PopUp.tx_senha_antiga.text()))
        # Cancelar e Fechar janela
        def fechar_janela():
            Dialog.close()
        PopUp.bt_dialog_cancelar.clicked.connect(fechar_janela)

        # Alterando a senha no DB
        def altera_senha():
            # Crud
            update = CrudUsuarios()
            update.id_usuario = self.tx_cod_usuario.text()
            update.senha = unicode(PopUp.tx_senha_antiga_2.text()).encode("utf8")
            update.alterar_senha()

            #popup Mensagem
            DConfirm = QtGui.QDialog()
            Confirm = Ui_Dialog()
            Confirm.setConfirmacao(DConfirm)
            Confirm.lb_info.setText(QtCore.QString.fromUtf8("Usuário"))
            Confirm.lb_titulo_modal.setText(QtCore.QString.fromUtf8("Senha Alterada !"))
            Confirm.lb_descricao.setText(unicode(self.tx_nome_usuario.text()))
            Confirm.buttonBox.setStyleSheet("color: #FFF; border: 2px solid #0CA3D2; border-radius:10px;"
                                           "background: #FFF; color: #000; width: 100px; height: 30px")
            QtCore.QObject.connect(Confirm.buttonBox, QtCore.SIGNAL("accepted()"), fechar_janela)
            DConfirm.exec_()


        # Acao botao Alterar senha
        PopUp.bt_dialog_alterar_senha.clicked.connect(altera_senha)
        # Chamando comparador de senha
        PopUp.tx_senha_antiga_3.textChanged.connect(compara_nova_senha)
        # Titulo do Poput
        Dialog.setWindowTitle("Alterar senha")
        # Executando o PoPup
        Dialog.exec_()
    # Fim Janela Altarar senha


    def alteracao_senha(self, senha):
        print senha

    def cancelar_cadastro_usuarios(self):
        for filho in self.ct_usuarios.findChildren(QtGui.QLineEdit):
            filho.clear()
        self.tx_cod_usuario.clear()
        self.tx_estado_usuario.setCurrentIndex(19)
        self.tx_nivel_acesso.setCurrentIndex(1)
        self.tx_status.setCurrentIndex(1)
        self.busca_usuarios()
        self.bt_aterar_senha.setEnabled(False)
