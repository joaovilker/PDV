# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
import sys
from Class.Funcoes import Funcoes
from Views.main import Ui_MainWindow
from home import MainHome
from estoque import MainEstoque
from clientes import MainClientes
from pedidos import MainPedidos
from tarefas import MainTarefa
from usuarios import MainUsuarios


class Main(QtGui.QMainWindow, Ui_MainWindow, Funcoes, MainHome, MainEstoque, MainClientes ,MainPedidos, MainTarefa,
           MainUsuarios):
    def __init__(self, parent=None ):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.janela_home()
        self.setFixedSize(900, 621)

        # parametros Inicias
        # Titulo e Logo
        self.setWindowTitle("Azul e Rosa Personalizados - Home")
        self.lb_logo.setPixmap(QtGui.QPixmap('Images/logo.png'))


        # Estilo dos botões
        for filho in self.ct_topo.findChildren(QtGui.QPushButton):
            efeito = QtGui.QGraphicsDropShadowEffect()
            efeito.setColor(QtGui.QColor("#ff00ff"))
            efeito.setOffset(0, 0)
            efeito.setBlurRadius(15)
            filho.setGraphicsEffect(efeito)
            filho.setStyleSheet(" QPushButton{border-radius: 10px; background: #00ffff;}"
                                "QPushButton:disabled {background: #FFF}"
                                "QPushButton:hover{color: #FFF}")



        """ Atalhoes de Teclado """
        # Atalho Home
        self.atalho_inicio = QtGui.QAction("Atalho Home", self)
        self.atalho_inicio.setShortcut(QtGui.QKeySequence("Alt+H"))
        self.addAction(self.atalho_inicio)
        self.atalho_inicio.triggered.connect(self.janela_home)

        # Estoque
        self.atalho_estoque = QtGui.QAction("Atalho Estoque", self)
        self.atalho_estoque.setShortcut(QtGui.QKeySequence("F3"))
        self.addAction(self.atalho_estoque)
        self.atalho_estoque.triggered.connect(self.janela_estoque)

        # Clientes
        self.atalho_clientes = QtGui.QAction("Atalho Clientes", self)
        self.atalho_clientes.setShortcut(QtGui.QKeySequence("F4"))
        self.addAction(self.atalho_clientes)
        self.atalho_clientes.triggered.connect(self.janela_clientes)

        # Pedidos
        self.atalho_pedidos = QtGui.QAction(('Atalho tedidos'), self)
        self.atalho_pedidos.setShortcut(QtGui.QKeySequence("F7"))
        self.addAction(self.atalho_pedidos)
        self.atalho_pedidos.triggered.connect(self.janela_pedidos)

        # Tarefas
        self.atalho_tarefa = QtGui.QAction("Atalho Tarefa", self)
        self.atalho_tarefa.setShortcut((QtGui.QKeySequence("F6")))
        self.addAction(self.atalho_tarefa)
        self.atalho_tarefa.triggered.connect(self.janela_tarefa)

        # Usuarios
        self.atalho_usuarios = QtGui.QAction("Atalho Usuários", self)
        self.atalho_usuarios.setShortcut("F5")
        self.addAction(self.atalho_usuarios)
        self.atalho_usuarios.triggered.connect(self.janela_usuarios)


        # Ações dos Botões
        # Home
        self.bt_inicio.clicked.connect(self.janela_home)
        # Estoque
        self.bt_estoque.clicked.connect(self.janela_estoque)
        # Clientes
        self.bt_clientes.clicked.connect(self.janela_clientes)
        # Pedidos
        self.bt_pedidos.clicked.connect(self.janela_pedidos)
        # Tarefa
        self.bt_tarefas.clicked.connect(self.janela_tarefa)
        # Usuarios
        self.bt_usuarios.clicked.connect(self.janela_usuarios)







    # Abrindo Janelas

    def janela_home(self):
        self.limpa_frame(self.ct_conteudo)
        self.desativa_botao(self.ct_topo, self.bt_inicio)
        self.main_home(self.ct_conteudo)
        self.setWindowTitle("Azul e Rosa Personalizados - Home")

    def janela_estoque(self):
        self.limpa_frame(self.ct_conteudo)
        self.desativa_botao(self.ct_topo, self.bt_estoque)
        self.main_estoque(self.ct_conteudo)
        self.setWindowTitle("Azul e Rosa Personalizados - Estoque")

    def janela_clientes(self):
        self.limpa_frame(self.ct_conteudo)
        self.desativa_botao(self.ct_topo, self.bt_clientes)
        self.main_clientes(self.ct_conteudo)
        self.setWindowTitle("Azul e Rosa Personalizados - Clientes")


    def janela_pedidos(self):
        self.limpa_frame(self.ct_conteudo)
        self.main_pedidos(self.ct_conteudo)
        self.desativa_botao(self.ct_topo, self.bt_pedidos)
        self.setWindowTitle("Azul e Rosa Personalizados - Pedidos")

    def janela_usuarios(self):
        self.limpa_frame(self.ct_conteudo)
        self.main_usuarios(self.ct_conteudo)
        self.desativa_botao(self.ct_topo, self.bt_usuarios)
        self.setWindowTitle("Azul e Rosa Personalizados - Usuarios")


    def janela_tarefa(self):
        self.limpa_frame(self.ct_conteudo)
        self.main_tarefa(self.ct_conteudo)
        self.desativa_botao(self.ct_topo, self.bt_tarefas)
        self.setWindowTitle("Azul e Rosa Personalizados - Tarefas")







if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    app.exec_()
