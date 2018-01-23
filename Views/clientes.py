# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clientes.ui'
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

class Ui_frame_clientes(object):
    def setClientes(self, frame_clientes):
        frame_clientes.setObjectName(_fromUtf8("frame_clientes"))
        frame_clientes.resize(900, 493)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        frame_clientes.setFont(font)
        frame_clientes.setStyleSheet(_fromUtf8(""))
        frame_clientes.setFrameShape(QtGui.QFrame.StyledPanel)
        frame_clientes.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_frame_clientes = QtGui.QFrame(frame_clientes)
        self.ct_frame_clientes.setGeometry(QtCore.QRect(0, 0, 900, 493))
        self.ct_frame_clientes.setStyleSheet(_fromUtf8("background: #0CA3D2"))
        self.ct_frame_clientes.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ct_frame_clientes.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_frame_clientes.setObjectName(_fromUtf8("ct_frame_clientes"))
        self.ct_clientes = QtGui.QFrame(self.ct_frame_clientes)
        self.ct_clientes.setGeometry(QtCore.QRect(30, 20, 500, 423))
        self.ct_clientes.setStyleSheet(_fromUtf8("background: #FFF;\n"
"border: 5px solid #fFf;\n"
"border-radius: 20px;\n"
""))
        self.ct_clientes.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ct_clientes.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_clientes.setObjectName(_fromUtf8("ct_clientes"))
        self.lb_pedidos_agendados_2 = QtGui.QLabel(self.ct_clientes)
        self.lb_pedidos_agendados_2.setGeometry(QtCore.QRect(25, 10, 450, 30))
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
        self.label_clientes = QtGui.QLabel(self.ct_clientes)
        self.label_clientes.setGeometry(QtCore.QRect(25, 60, 75, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_clientes.setFont(font)
        self.label_clientes.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.label_clientes.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clientes.setObjectName(_fromUtf8("label_clientes"))
        self.tx_nome_cliente = QtGui.QLineEdit(self.ct_clientes)
        self.tx_nome_cliente.setGeometry(QtCore.QRect(105, 60, 120, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_nome_cliente.setFont(font)
        self.tx_nome_cliente.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_nome_cliente.setObjectName(_fromUtf8("tx_nome_cliente"))
        self.label_clientes_2 = QtGui.QLabel(self.ct_clientes)
        self.label_clientes_2.setGeometry(QtCore.QRect(25, 95, 75, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_clientes_2.setFont(font)
        self.label_clientes_2.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.label_clientes_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clientes_2.setObjectName(_fromUtf8("label_clientes_2"))
        self.tx_telefone_cliente = QtGui.QLineEdit(self.ct_clientes)
        self.tx_telefone_cliente.setGeometry(QtCore.QRect(105, 95, 120, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_telefone_cliente.setFont(font)
        self.tx_telefone_cliente.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_telefone_cliente.setText(_fromUtf8(""))
        self.tx_telefone_cliente.setObjectName(_fromUtf8("tx_telefone_cliente"))
        self.label_clientes_3 = QtGui.QLabel(self.ct_clientes)
        self.label_clientes_3.setGeometry(QtCore.QRect(230, 60, 75, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_clientes_3.setFont(font)
        self.label_clientes_3.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.label_clientes_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clientes_3.setObjectName(_fromUtf8("label_clientes_3"))
        self.tx_nome_cliente_2 = QtGui.QLineEdit(self.ct_clientes)
        self.tx_nome_cliente_2.setGeometry(QtCore.QRect(315, 60, 160, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_nome_cliente_2.setFont(font)
        self.tx_nome_cliente_2.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_nome_cliente_2.setText(_fromUtf8(""))
        self.tx_nome_cliente_2.setObjectName(_fromUtf8("tx_nome_cliente_2"))
        self.label_clientes_4 = QtGui.QLabel(self.ct_clientes)
        self.label_clientes_4.setGeometry(QtCore.QRect(230, 95, 75, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_clientes_4.setFont(font)
        self.label_clientes_4.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.label_clientes_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clientes_4.setObjectName(_fromUtf8("label_clientes_4"))
        self.tx_cpf_cliente = QtGui.QLineEdit(self.ct_clientes)
        self.tx_cpf_cliente.setGeometry(QtCore.QRect(315, 95, 160, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_cpf_cliente.setFont(font)
        self.tx_cpf_cliente.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_cpf_cliente.setObjectName(_fromUtf8("tx_cpf_cliente"))
        self.label_clientes_5 = QtGui.QLabel(self.ct_clientes)
        self.label_clientes_5.setGeometry(QtCore.QRect(25, 130, 75, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_clientes_5.setFont(font)
        self.label_clientes_5.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.label_clientes_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clientes_5.setObjectName(_fromUtf8("label_clientes_5"))
        self.tx_endereco_cliente = QtGui.QLineEdit(self.ct_clientes)
        self.tx_endereco_cliente.setGeometry(QtCore.QRect(105, 130, 225, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_endereco_cliente.setFont(font)
        self.tx_endereco_cliente.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_endereco_cliente.setText(_fromUtf8(""))
        self.tx_endereco_cliente.setObjectName(_fromUtf8("tx_endereco_cliente"))
        self.label_clientes_6 = QtGui.QLabel(self.ct_clientes)
        self.label_clientes_6.setGeometry(QtCore.QRect(340, 130, 55, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_clientes_6.setFont(font)
        self.label_clientes_6.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.label_clientes_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clientes_6.setObjectName(_fromUtf8("label_clientes_6"))
        self.tx_numero_cliente = QtGui.QLineEdit(self.ct_clientes)
        self.tx_numero_cliente.setGeometry(QtCore.QRect(405, 130, 70, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_numero_cliente.setFont(font)
        self.tx_numero_cliente.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_numero_cliente.setText(_fromUtf8(""))
        self.tx_numero_cliente.setObjectName(_fromUtf8("tx_numero_cliente"))
        self.label_clientes_7 = QtGui.QLabel(self.ct_clientes)
        self.label_clientes_7.setGeometry(QtCore.QRect(25, 165, 75, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_clientes_7.setFont(font)
        self.label_clientes_7.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.label_clientes_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clientes_7.setObjectName(_fromUtf8("label_clientes_7"))
        self.tx_bairo_cliente = QtGui.QLineEdit(self.ct_clientes)
        self.tx_bairo_cliente.setGeometry(QtCore.QRect(105, 165, 120, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_bairo_cliente.setFont(font)
        self.tx_bairo_cliente.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_bairo_cliente.setText(_fromUtf8(""))
        self.tx_bairo_cliente.setObjectName(_fromUtf8("tx_bairo_cliente"))
        self.label_clientes_8 = QtGui.QLabel(self.ct_clientes)
        self.label_clientes_8.setGeometry(QtCore.QRect(230, 165, 75, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_clientes_8.setFont(font)
        self.label_clientes_8.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.label_clientes_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clientes_8.setObjectName(_fromUtf8("label_clientes_8"))
        self.tx_complemento_cliente = QtGui.QLineEdit(self.ct_clientes)
        self.tx_complemento_cliente.setGeometry(QtCore.QRect(315, 165, 160, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_complemento_cliente.setFont(font)
        self.tx_complemento_cliente.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_complemento_cliente.setText(_fromUtf8(""))
        self.tx_complemento_cliente.setObjectName(_fromUtf8("tx_complemento_cliente"))
        self.label_clientes_9 = QtGui.QLabel(self.ct_clientes)
        self.label_clientes_9.setGeometry(QtCore.QRect(25, 235, 75, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_clientes_9.setFont(font)
        self.label_clientes_9.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.label_clientes_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clientes_9.setObjectName(_fromUtf8("label_clientes_9"))
        self.tx_cidade_cliente = QtGui.QLineEdit(self.ct_clientes)
        self.tx_cidade_cliente.setGeometry(QtCore.QRect(105, 235, 225, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_cidade_cliente.setFont(font)
        self.tx_cidade_cliente.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_cidade_cliente.setText(_fromUtf8(""))
        self.tx_cidade_cliente.setObjectName(_fromUtf8("tx_cidade_cliente"))
        self.label_clientes_10 = QtGui.QLabel(self.ct_clientes)
        self.label_clientes_10.setGeometry(QtCore.QRect(340, 235, 55, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_clientes_10.setFont(font)
        self.label_clientes_10.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.label_clientes_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clientes_10.setObjectName(_fromUtf8("label_clientes_10"))
        self.tx_estado_cliente = QtGui.QComboBox(self.ct_clientes)
        self.tx_estado_cliente.setGeometry(QtCore.QRect(405, 235, 70, 25))
        self.tx_estado_cliente.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_estado_cliente.setEditable(True)
        self.tx_estado_cliente.setObjectName(_fromUtf8("tx_estado_cliente"))
        self.label_clientes_11 = QtGui.QLabel(self.ct_clientes)
        self.label_clientes_11.setGeometry(QtCore.QRect(25, 200, 75, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_clientes_11.setFont(font)
        self.label_clientes_11.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.label_clientes_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clientes_11.setObjectName(_fromUtf8("label_clientes_11"))
        self.tx_cep_cliente = QtGui.QLineEdit(self.ct_clientes)
        self.tx_cep_cliente.setGeometry(QtCore.QRect(105, 200, 120, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_cep_cliente.setFont(font)
        self.tx_cep_cliente.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_cep_cliente.setText(_fromUtf8(""))
        self.tx_cep_cliente.setObjectName(_fromUtf8("tx_cep_cliente"))
        self.label_clientes_12 = QtGui.QLabel(self.ct_clientes)
        self.label_clientes_12.setGeometry(QtCore.QRect(230, 200, 75, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_clientes_12.setFont(font)
        self.label_clientes_12.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.label_clientes_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clientes_12.setObjectName(_fromUtf8("label_clientes_12"))
        self.tx_referencia_cliente = QtGui.QLineEdit(self.ct_clientes)
        self.tx_referencia_cliente.setGeometry(QtCore.QRect(315, 200, 160, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_referencia_cliente.setFont(font)
        self.tx_referencia_cliente.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_referencia_cliente.setText(_fromUtf8(""))
        self.tx_referencia_cliente.setObjectName(_fromUtf8("tx_referencia_cliente"))
        self.bt_cadastrar_clientes = QtGui.QPushButton(self.ct_clientes)
        self.bt_cadastrar_clientes.setGeometry(QtCore.QRect(25, 370, 90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.bt_cadastrar_clientes.setFont(font)
        self.bt_cadastrar_clientes.setObjectName(_fromUtf8("bt_cadastrar_clientes"))
        self.bt_cancelar_cliente = QtGui.QPushButton(self.ct_clientes)
        self.bt_cancelar_cliente.setGeometry(QtCore.QRect(125, 370, 90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.bt_cancelar_cliente.setFont(font)
        self.bt_cancelar_cliente.setObjectName(_fromUtf8("bt_cancelar_cliente"))
        self.ct_clientes2 = QtGui.QFrame(self.ct_frame_clientes)
        self.ct_clientes2.setGeometry(QtCore.QRect(570, 20, 300, 423))
        self.ct_clientes2.setStyleSheet(_fromUtf8("background: #FFF;\n"
"border: 2px solid #fff;\n"
"border-radius: 20px;"))
        self.ct_clientes2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ct_clientes2.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_clientes2.setObjectName(_fromUtf8("ct_clientes2"))
        self.lb_tarefas_agendadas_2 = QtGui.QLabel(self.ct_clientes2)
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
        self.tx_buscar_clientes = QtGui.QLineEdit(self.ct_clientes2)
        self.tx_buscar_clientes.setGeometry(QtCore.QRect(50, 370, 200, 30))
        self.tx_buscar_clientes.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_buscar_clientes.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_buscar_clientes.setObjectName(_fromUtf8("tx_buscar_clientes"))
        self.label_clientes_13 = QtGui.QLabel(self.ct_clientes2)
        self.label_clientes_13.setGeometry(QtCore.QRect(100, 340, 100, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_clientes_13.setFont(font)
        self.label_clientes_13.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF url(\'/Files/Python/AeR/Images/buscar.png\') no-repeat  right ;\n"
"color: #000;\n"
""))
        self.label_clientes_13.setTextFormat(QtCore.Qt.AutoText)
        self.label_clientes_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clientes_13.setObjectName(_fromUtf8("label_clientes_13"))
        self.tabela_clientes = QtGui.QTableWidget(self.ct_clientes2)
        self.tabela_clientes.setGeometry(QtCore.QRect(5, 60, 290, 250))
        self.tabela_clientes.setStyleSheet(_fromUtf8("background: #FFF; border: none; border-radius: 0"))
        self.tabela_clientes.setAutoScroll(True)
        self.tabela_clientes.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabela_clientes.setTextElideMode(QtCore.Qt.ElideRight)
        self.tabela_clientes.setObjectName(_fromUtf8("tabela_clientes"))
        self.tabela_clientes.setColumnCount(3)
        self.tabela_clientes.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tabela_clientes.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabela_clientes.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabela_clientes.setHorizontalHeaderItem(2, item)
        self.tabela_clientes.verticalHeader().setVisible(False)

        self.trad_clientes(frame_clientes)
        QtCore.QMetaObject.connectSlotsByName(frame_clientes)

    def trad_clientes(self, frame_clientes):
        frame_clientes.setWindowTitle(_translate("frame_clientes", "Frame", None))
        self.lb_pedidos_agendados_2.setText(_translate("frame_clientes", "Cadastrar / Editar Clientes", None))
        self.label_clientes.setText(_translate("frame_clientes", "Nome", None))
        self.label_clientes_2.setText(_translate("frame_clientes", "Telefone", None))
        self.label_clientes_3.setText(_translate("frame_clientes", "Sobrenome", None))
        self.label_clientes_4.setText(_translate("frame_clientes", "CPF", None))
        self.tx_cpf_cliente.setInputMask(_translate("frame_clientes", "###.###.###-##; ", None))
        self.tx_cpf_cliente.setText(_translate("frame_clientes", "..----", None))
        self.label_clientes_5.setText(_translate("frame_clientes", "Endereço", None))
        self.label_clientes_6.setText(_translate("frame_clientes", "Num.", None))
        self.label_clientes_7.setText(_translate("frame_clientes", "Bairro", None))
        self.label_clientes_8.setText(_translate("frame_clientes", "Compl.", None))
        self.label_clientes_9.setText(_translate("frame_clientes", "Cidade", None))
        self.label_clientes_10.setText(_translate("frame_clientes", "Estado", None))
        self.label_clientes_11.setText(_translate("frame_clientes", "Cep", None))
        self.label_clientes_12.setText(_translate("frame_clientes", "Referência", None))
        self.bt_cadastrar_clientes.setText(_translate("frame_clientes", "Cadastrar", None))
        self.bt_cancelar_cliente.setText(_translate("frame_clientes", "Cancelar", None))
        self.lb_tarefas_agendadas_2.setText(_translate("frame_clientes", "Todos Clientes", None))
        self.tx_buscar_clientes.setPlaceholderText(_translate("frame_clientes", "Buscar", None))
        self.label_clientes_13.setText(_translate("frame_clientes", "Pesquisar", None))
        item = self.tabela_clientes.horizontalHeaderItem(0)
        item.setText(_translate("frame_clientes", "Cod:", None))
        item = self.tabela_clientes.horizontalHeaderItem(1)
        item.setText(_translate("frame_clientes", "Descrição", None))
        item = self.tabela_clientes.horizontalHeaderItem(2)
        item.setText(_translate("frame_clientes", "QTDE", None))

