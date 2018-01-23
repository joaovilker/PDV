# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'janela_senha.ui'
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

class Ui_Dialog_senha(object):
    def setAlterarSenha(self, Dialog_senha):
        Dialog_senha.setObjectName(_fromUtf8("Dialog_senha"))
        Dialog_senha.resize(400, 250)
        self.frame = QtGui.QFrame(Dialog_senha)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 250))
        self.frame.setStyleSheet(_fromUtf8("background: #0CA3D2"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 380, 230))
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
        self.lb_info.setGeometry(QtCore.QRect(20, 70, 110, 25))
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
        self.tx_senha_antiga = QtGui.QLineEdit(self.frame_2)
        self.tx_senha_antiga.setGeometry(QtCore.QRect(140, 70, 150, 25))
        self.tx_senha_antiga.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000;\n"
""))
        self.tx_senha_antiga.setEchoMode(QtGui.QLineEdit.Password)
        self.tx_senha_antiga.setObjectName(_fromUtf8("tx_senha_antiga"))
        self.lb_info_2 = QtGui.QLabel(self.frame_2)
        self.lb_info_2.setGeometry(QtCore.QRect(20, 105, 110, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.lb_info_2.setFont(font)
        self.lb_info_2.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_info_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_info_2.setObjectName(_fromUtf8("lb_info_2"))
        self.tx_senha_antiga_2 = QtGui.QLineEdit(self.frame_2)
        self.tx_senha_antiga_2.setEnabled(True)
        self.tx_senha_antiga_2.setGeometry(QtCore.QRect(140, 105, 150, 25))
        self.tx_senha_antiga_2.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_senha_antiga_2.setEchoMode(QtGui.QLineEdit.Password)
        self.tx_senha_antiga_2.setObjectName(_fromUtf8("tx_senha_antiga_2"))
        self.lb_info_3 = QtGui.QLabel(self.frame_2)
        self.lb_info_3.setEnabled(True)
        self.lb_info_3.setGeometry(QtCore.QRect(20, 140, 110, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.lb_info_3.setFont(font)
        self.lb_info_3.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.lb_info_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_info_3.setObjectName(_fromUtf8("lb_info_3"))
        self.tx_senha_antiga_3 = QtGui.QLineEdit(self.frame_2)
        self.tx_senha_antiga_3.setGeometry(QtCore.QRect(140, 140, 150, 25))
        self.tx_senha_antiga_3.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_senha_antiga_3.setEchoMode(QtGui.QLineEdit.Password)
        self.tx_senha_antiga_3.setObjectName(_fromUtf8("tx_senha_antiga_3"))
        self.pushButton = QtGui.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(295, 70, 70, 26))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.bt_dialog_alterar_senha = QtGui.QPushButton(self.frame_2)
        self.bt_dialog_alterar_senha.setGeometry(QtCore.QRect(10, 180, 100, 30))
        self.bt_dialog_alterar_senha.setObjectName(_fromUtf8("bt_dialog_alterar_senha"))
        self.bt_dialog_cancelar = QtGui.QPushButton(self.frame_2)
        self.bt_dialog_cancelar.setGeometry(QtCore.QRect(120, 180, 100, 30))
        self.bt_dialog_cancelar.setObjectName(_fromUtf8("bt_dialog_cancelar"))

        self.tradSenha(Dialog_senha)
        QtCore.QMetaObject.connectSlotsByName(Dialog_senha)

    def tradSenha(self, Dialog_senha):
        Dialog_senha.setWindowTitle(_translate("Dialog_senha", "Confirmação", None))
        self.lb_titulo_modal.setText(_translate("Dialog_senha", "Alterar Senha", None))
        self.lb_info.setText(_translate("Dialog_senha", "Senha Antiga", None))
        self.lb_info_2.setText(_translate("Dialog_senha", "Nova Senha", None))
        self.lb_info_3.setText(_translate("Dialog_senha", "Confimar Senha", None))
        self.pushButton.setText(_translate("Dialog_senha", "Verificar", None))
        self.bt_dialog_alterar_senha.setText(_translate("Dialog_senha", "Alterar", None))
        self.bt_dialog_cancelar.setText(_translate("Dialog_senha", "Cancelar", None))

