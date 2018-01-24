# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usuarios.ui'
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

class Ui_FrameUsuarios(object):
    def setUsuarios(self, FrameUsuarios):
        FrameUsuarios.setObjectName(_fromUtf8("FrameUsuarios"))
        FrameUsuarios.resize(900, 493)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        FrameUsuarios.setFont(font)
        FrameUsuarios.setStyleSheet(_fromUtf8(""))
        FrameUsuarios.setFrameShape(QtGui.QFrame.StyledPanel)
        FrameUsuarios.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_frame_usuarios = QtGui.QFrame(FrameUsuarios)
        self.ct_frame_usuarios.setGeometry(QtCore.QRect(0, 0, 900, 493))
        self.ct_frame_usuarios.setStyleSheet(_fromUtf8("background: #0CA3D2"))
        self.ct_frame_usuarios.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ct_frame_usuarios.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_frame_usuarios.setObjectName(_fromUtf8("ct_frame_usuarios"))
        self.ct_usuarios = QtGui.QFrame(self.ct_frame_usuarios)
        self.ct_usuarios.setGeometry(QtCore.QRect(30, 20, 500, 423))
        self.ct_usuarios.setStyleSheet(_fromUtf8("background: #FFF;\n"
"border: 5px solid #fFf;\n"
"border-radius: 20px;\n"
""))
        self.ct_usuarios.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ct_usuarios.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_usuarios.setObjectName(_fromUtf8("ct_usuarios"))
        self.lb_pedidos_agendados_2 = QtGui.QLabel(self.ct_usuarios)
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
        self.label_clientes = QtGui.QLabel(self.ct_usuarios)
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
        self.tx_nome_usuario = QtGui.QLineEdit(self.ct_usuarios)
        self.tx_nome_usuario.setGeometry(QtCore.QRect(105, 60, 120, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_nome_usuario.setFont(font)
        self.tx_nome_usuario.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_nome_usuario.setObjectName(_fromUtf8("tx_nome_usuario"))
        self.label_clientes_2 = QtGui.QLabel(self.ct_usuarios)
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
        self.tx_telefone_usuario = QtGui.QLineEdit(self.ct_usuarios)
        self.tx_telefone_usuario.setGeometry(QtCore.QRect(105, 95, 120, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_telefone_usuario.setFont(font)
        self.tx_telefone_usuario.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_telefone_usuario.setObjectName(_fromUtf8("tx_telefone_usuario"))
        self.label_clientes_3 = QtGui.QLabel(self.ct_usuarios)
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
        self.tx_sobrenome_usuario = QtGui.QLineEdit(self.ct_usuarios)
        self.tx_sobrenome_usuario.setGeometry(QtCore.QRect(315, 60, 160, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_sobrenome_usuario.setFont(font)
        self.tx_sobrenome_usuario.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_sobrenome_usuario.setText(_fromUtf8(""))
        self.tx_sobrenome_usuario.setObjectName(_fromUtf8("tx_sobrenome_usuario"))
        self.label_clientes_4 = QtGui.QLabel(self.ct_usuarios)
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
        self.tx_cpf_usuario = QtGui.QLineEdit(self.ct_usuarios)
        self.tx_cpf_usuario.setGeometry(QtCore.QRect(315, 95, 160, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_cpf_usuario.setFont(font)
        self.tx_cpf_usuario.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_cpf_usuario.setObjectName(_fromUtf8("tx_cpf_usuario"))
        self.label_clientes_5 = QtGui.QLabel(self.ct_usuarios)
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
        self.tx_endereco_usuario = QtGui.QLineEdit(self.ct_usuarios)
        self.tx_endereco_usuario.setGeometry(QtCore.QRect(105, 130, 225, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_endereco_usuario.setFont(font)
        self.tx_endereco_usuario.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_endereco_usuario.setText(_fromUtf8(""))
        self.tx_endereco_usuario.setObjectName(_fromUtf8("tx_endereco_usuario"))
        self.label_clientes_6 = QtGui.QLabel(self.ct_usuarios)
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
        self.tx_numero_endereco_usuario = QtGui.QLineEdit(self.ct_usuarios)
        self.tx_numero_endereco_usuario.setGeometry(QtCore.QRect(405, 130, 70, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_numero_endereco_usuario.setFont(font)
        self.tx_numero_endereco_usuario.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_numero_endereco_usuario.setText(_fromUtf8(""))
        self.tx_numero_endereco_usuario.setObjectName(_fromUtf8("tx_numero_endereco_usuario"))
        self.label_clientes_7 = QtGui.QLabel(self.ct_usuarios)
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
        self.tx_bairo_usuario = QtGui.QLineEdit(self.ct_usuarios)
        self.tx_bairo_usuario.setGeometry(QtCore.QRect(105, 165, 120, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_bairo_usuario.setFont(font)
        self.tx_bairo_usuario.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_bairo_usuario.setText(_fromUtf8(""))
        self.tx_bairo_usuario.setObjectName(_fromUtf8("tx_bairo_usuario"))
        self.label_clientes_8 = QtGui.QLabel(self.ct_usuarios)
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
        self.tx_complemento_usuario = QtGui.QLineEdit(self.ct_usuarios)
        self.tx_complemento_usuario.setGeometry(QtCore.QRect(315, 165, 160, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_complemento_usuario.setFont(font)
        self.tx_complemento_usuario.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_complemento_usuario.setText(_fromUtf8(""))
        self.tx_complemento_usuario.setObjectName(_fromUtf8("tx_complemento_usuario"))
        self.label_clientes_9 = QtGui.QLabel(self.ct_usuarios)
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
        self.tx_cidade_usuario = QtGui.QLineEdit(self.ct_usuarios)
        self.tx_cidade_usuario.setGeometry(QtCore.QRect(105, 235, 225, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_cidade_usuario.setFont(font)
        self.tx_cidade_usuario.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_cidade_usuario.setText(_fromUtf8(""))
        self.tx_cidade_usuario.setObjectName(_fromUtf8("tx_cidade_usuario"))
        self.label_clientes_10 = QtGui.QLabel(self.ct_usuarios)
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
        self.tx_estado_usuario = QtGui.QComboBox(self.ct_usuarios)
        self.tx_estado_usuario.setGeometry(QtCore.QRect(405, 235, 70, 25))
        self.tx_estado_usuario.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_estado_usuario.setObjectName(_fromUtf8("tx_estado_usuario"))
        self.label_clientes_11 = QtGui.QLabel(self.ct_usuarios)
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
        self.tx_cep_usuario = QtGui.QLineEdit(self.ct_usuarios)
        self.tx_cep_usuario.setGeometry(QtCore.QRect(105, 200, 120, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_cep_usuario.setFont(font)
        self.tx_cep_usuario.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_cep_usuario.setObjectName(_fromUtf8("tx_cep_usuario"))
        self.label_clientes_12 = QtGui.QLabel(self.ct_usuarios)
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
        self.tx_referencia_usuario = QtGui.QLineEdit(self.ct_usuarios)
        self.tx_referencia_usuario.setGeometry(QtCore.QRect(315, 200, 160, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_referencia_usuario.setFont(font)
        self.tx_referencia_usuario.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_referencia_usuario.setText(_fromUtf8(""))
        self.tx_referencia_usuario.setObjectName(_fromUtf8("tx_referencia_usuario"))
        self.bt_cadastrar_usuario = QtGui.QPushButton(self.ct_usuarios)
        self.bt_cadastrar_usuario.setGeometry(QtCore.QRect(25, 370, 90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.bt_cadastrar_usuario.setFont(font)
        self.bt_cadastrar_usuario.setObjectName(_fromUtf8("bt_cadastrar_usuario"))
        self.bt_cancelar_ = QtGui.QPushButton(self.ct_usuarios)
        self.bt_cancelar_.setGeometry(QtCore.QRect(125, 370, 90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.bt_cancelar_.setFont(font)
        self.bt_cancelar_.setObjectName(_fromUtf8("bt_cancelar_"))
        self.label_clientes_13 = QtGui.QLabel(self.ct_usuarios)
        self.label_clientes_13.setGeometry(QtCore.QRect(25, 305, 75, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_clientes_13.setFont(font)
        self.label_clientes_13.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.label_clientes_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clientes_13.setObjectName(_fromUtf8("label_clientes_13"))
        self.line = QtGui.QFrame(self.ct_usuarios)
        self.line.setGeometry(QtCore.QRect(205, 285, 270, 5))
        self.line.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.line.setFrameShadow(QtGui.QFrame.Raised)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_clientes_14 = QtGui.QLabel(self.ct_usuarios)
        self.label_clientes_14.setGeometry(QtCore.QRect(25, 270, 175, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_clientes_14.setFont(font)
        self.label_clientes_14.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.label_clientes_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clientes_14.setObjectName(_fromUtf8("label_clientes_14"))
        self.tx_login = QtGui.QLineEdit(self.ct_usuarios)
        self.tx_login.setGeometry(QtCore.QRect(105, 305, 140, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tx_login.setFont(font)
        self.tx_login.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_login.setText(_fromUtf8(""))
        self.tx_login.setObjectName(_fromUtf8("tx_login"))
        self.tx_nivel_acesso = QtGui.QComboBox(self.ct_usuarios)
        self.tx_nivel_acesso.setGeometry(QtCore.QRect(105, 340, 140, 25))
        self.tx_nivel_acesso.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_nivel_acesso.setObjectName(_fromUtf8("tx_nivel_acesso"))
        self.label_clientes_16 = QtGui.QLabel(self.ct_usuarios)
        self.label_clientes_16.setGeometry(QtCore.QRect(25, 340, 75, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_clientes_16.setFont(font)
        self.label_clientes_16.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.label_clientes_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clientes_16.setObjectName(_fromUtf8("label_clientes_16"))
        self.label_clientes_17 = QtGui.QLabel(self.ct_usuarios)
        self.label_clientes_17.setGeometry(QtCore.QRect(250, 340, 75, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_clientes_17.setFont(font)
        self.label_clientes_17.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.label_clientes_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clientes_17.setObjectName(_fromUtf8("label_clientes_17"))
        self.tx_status = QtGui.QComboBox(self.ct_usuarios)
        self.tx_status.setGeometry(QtCore.QRect(335, 340, 140, 25))
        self.tx_status.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_status.setObjectName(_fromUtf8("tx_status"))
        self.bt_aterar_senha = QtGui.QPushButton(self.ct_usuarios)
        self.bt_aterar_senha.setGeometry(QtCore.QRect(270, 305, 100, 25))
        self.bt_aterar_senha.setObjectName(_fromUtf8("bt_aterar_senha"))
        self.ct_usuarios2 = QtGui.QFrame(self.ct_frame_usuarios)
        self.ct_usuarios2.setGeometry(QtCore.QRect(570, 20, 300, 423))
        self.ct_usuarios2.setStyleSheet(_fromUtf8("background: #FFF;\n"
"border: 2px solid #fff;\n"
"border-radius: 20px;"))
        self.ct_usuarios2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ct_usuarios2.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_usuarios2.setObjectName(_fromUtf8("ct_usuarios2"))
        self.lb_tarefas_agendadas_2 = QtGui.QLabel(self.ct_usuarios2)
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
        self.tabela_usuarios = QtGui.QTableWidget(self.ct_usuarios2)
        self.tabela_usuarios.setGeometry(QtCore.QRect(5, 60, 290, 250))
        self.tabela_usuarios.setStyleSheet(_fromUtf8("background: #FFF; border: none; border-radius: 0"))
        self.tabela_usuarios.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabela_usuarios.setTextElideMode(QtCore.Qt.ElideRight)
        self.tabela_usuarios.setObjectName(_fromUtf8("tabela_usuarios"))
        self.tabela_usuarios.setColumnCount(2)
        self.tabela_usuarios.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tabela_usuarios.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabela_usuarios.setHorizontalHeaderItem(1, item)
        self.tx_buscar_usuarios = QtGui.QLineEdit(self.ct_usuarios2)
        self.tx_buscar_usuarios.setGeometry(QtCore.QRect(50, 370, 200, 30))
        self.tx_buscar_usuarios.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_buscar_usuarios.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_buscar_usuarios.setObjectName(_fromUtf8("tx_buscar_usuarios"))
        self.label_clientes_18 = QtGui.QLabel(self.ct_usuarios2)
        self.label_clientes_18.setGeometry(QtCore.QRect(100, 340, 100, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_clientes_18.setFont(font)
        self.label_clientes_18.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF url(\'/Files/Python/AeR/Images/buscar.png\') no-repeat  right ;\n"
"color: #000;\n"
""))
        self.label_clientes_18.setTextFormat(QtCore.Qt.AutoText)
        self.label_clientes_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clientes_18.setObjectName(_fromUtf8("label_clientes_18"))

        self.tradUsuarios(FrameUsuarios)
        self.tx_estado_usuario.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(FrameUsuarios)
        FrameUsuarios.setTabOrder(self.tx_nome_usuario, self.tx_sobrenome_usuario)
        FrameUsuarios.setTabOrder(self.tx_sobrenome_usuario, self.tx_telefone_usuario)
        FrameUsuarios.setTabOrder(self.tx_telefone_usuario, self.tx_cpf_usuario)
        FrameUsuarios.setTabOrder(self.tx_cpf_usuario, self.tx_endereco_usuario)
        FrameUsuarios.setTabOrder(self.tx_endereco_usuario, self.tx_numero_endereco_usuario)
        FrameUsuarios.setTabOrder(self.tx_numero_endereco_usuario, self.tx_bairo_usuario)
        FrameUsuarios.setTabOrder(self.tx_bairo_usuario, self.tx_complemento_usuario)
        FrameUsuarios.setTabOrder(self.tx_complemento_usuario, self.tx_cep_usuario)
        FrameUsuarios.setTabOrder(self.tx_cep_usuario, self.tx_referencia_usuario)
        FrameUsuarios.setTabOrder(self.tx_referencia_usuario, self.tx_cidade_usuario)
        FrameUsuarios.setTabOrder(self.tx_cidade_usuario, self.tx_estado_usuario)
        FrameUsuarios.setTabOrder(self.tx_estado_usuario, self.tx_login)
        FrameUsuarios.setTabOrder(self.tx_login, self.bt_aterar_senha)
        FrameUsuarios.setTabOrder(self.bt_aterar_senha, self.tx_nivel_acesso)
        FrameUsuarios.setTabOrder(self.tx_nivel_acesso, self.tx_status)
        FrameUsuarios.setTabOrder(self.tx_status, self.bt_cadastrar_usuario)
        FrameUsuarios.setTabOrder(self.bt_cadastrar_usuario, self.bt_cancelar_)
        FrameUsuarios.setTabOrder(self.bt_cancelar_, self.tabela_usuarios)
        FrameUsuarios.setTabOrder(self.tabela_usuarios, self.tx_buscar_usuarios)

    def tradUsuarios(self, FrameUsuarios):
        FrameUsuarios.setWindowTitle(_translate("FrameUsuarios", "Frame", None))
        self.lb_pedidos_agendados_2.setText(_translate("FrameUsuarios", "Cadastrar / Editar Usuário", None))
        self.label_clientes.setText(_translate("FrameUsuarios", "Nome", None))
        self.label_clientes_2.setText(_translate("FrameUsuarios", "Telefone", None))
        self.tx_telefone_usuario.setInputMask(_translate("FrameUsuarios", "(00) 00000-0000; ", None))
        self.tx_telefone_usuario.setText(_translate("FrameUsuarios", "() -", None))
        self.label_clientes_3.setText(_translate("FrameUsuarios", "Sobrenome", None))
        self.label_clientes_4.setText(_translate("FrameUsuarios", "CPF", None))
        self.tx_cpf_usuario.setInputMask(_translate("FrameUsuarios", "000.000.000-00; ", None))
        self.tx_cpf_usuario.setText(_translate("FrameUsuarios", "..-", None))
        self.label_clientes_5.setText(_translate("FrameUsuarios", "Endereço", None))
        self.label_clientes_6.setText(_translate("FrameUsuarios", "Num.", None))
        self.label_clientes_7.setText(_translate("FrameUsuarios", "Bairro", None))
        self.label_clientes_8.setText(_translate("FrameUsuarios", "Compl.", None))
        self.label_clientes_9.setText(_translate("FrameUsuarios", "Cidade", None))
        self.label_clientes_10.setText(_translate("FrameUsuarios", "Estado", None))
        self.label_clientes_11.setText(_translate("FrameUsuarios", "Cep", None))
        self.tx_cep_usuario.setInputMask(_translate("FrameUsuarios", "0000-000; ", None))
        self.tx_cep_usuario.setText(_translate("FrameUsuarios", "-", None))
        self.label_clientes_12.setText(_translate("FrameUsuarios", "Referência", None))
        self.bt_cadastrar_usuario.setText(_translate("FrameUsuarios", "Cadastrar", None))
        self.bt_cancelar_.setText(_translate("FrameUsuarios", "Cancelar", None))
        self.label_clientes_13.setText(_translate("FrameUsuarios", "Usuario", None))
        self.label_clientes_14.setText(_translate("FrameUsuarios", "Dados Acesso", None))
        self.label_clientes_16.setText(_translate("FrameUsuarios", "Nível", None))
        self.label_clientes_17.setText(_translate("FrameUsuarios", "Status", None))
        self.bt_aterar_senha.setText(_translate("FrameUsuarios", "Alterar Senha", None))
        self.lb_tarefas_agendadas_2.setText(_translate("FrameUsuarios", "Todos os Usuários", None))
        item = self.tabela_usuarios.horizontalHeaderItem(0)
        item.setText(_translate("FrameUsuarios", "Cod", None))
        item = self.tabela_usuarios.horizontalHeaderItem(1)
        item.setText(_translate("FrameUsuarios", "Nome Usuário", None))
        self.tx_buscar_usuarios.setPlaceholderText(_translate("FrameUsuarios", "Buscar", None))
        self.label_clientes_18.setText(_translate("FrameUsuarios", "Pesquisar", None))

