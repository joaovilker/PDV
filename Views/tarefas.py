# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tarefas.ui'
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

class Ui_frame_tarefa(object):
    def setTarefas(self, frame_tarefa):
        frame_tarefa.setObjectName(_fromUtf8("frame_tarefa"))
        frame_tarefa.resize(900, 493)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        frame_tarefa.setFont(font)
        frame_tarefa.setStyleSheet(_fromUtf8(""))
        frame_tarefa.setFrameShape(QtGui.QFrame.StyledPanel)
        frame_tarefa.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_frame_tarefa = QtGui.QFrame(frame_tarefa)
        self.ct_frame_tarefa.setGeometry(QtCore.QRect(0, 0, 900, 493))
        self.ct_frame_tarefa.setStyleSheet(_fromUtf8("background: #0CA3D2"))
        self.ct_frame_tarefa.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ct_frame_tarefa.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_frame_tarefa.setObjectName(_fromUtf8("ct_frame_tarefa"))
        self.ct_tarefas = QtGui.QFrame(self.ct_frame_tarefa)
        self.ct_tarefas.setGeometry(QtCore.QRect(30, 20, 500, 423))
        self.ct_tarefas.setStyleSheet(_fromUtf8("background: #FFF;\n"
"border: 5px solid #fFf;\n"
"border-radius: 20px;\n"
""))
        self.ct_tarefas.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ct_tarefas.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_tarefas.setObjectName(_fromUtf8("ct_tarefas"))
        self.lb_pedidos_agendados_2 = QtGui.QLabel(self.ct_tarefas)
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
        self.label_tarefa = QtGui.QLabel(self.ct_tarefas)
        self.label_tarefa.setGeometry(QtCore.QRect(25, 60, 75, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_tarefa.setFont(font)
        self.label_tarefa.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.label_tarefa.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tarefa.setObjectName(_fromUtf8("label_tarefa"))
        self.tx_tarefa_para = QtGui.QComboBox(self.ct_tarefas)
        self.tx_tarefa_para.setGeometry(QtCore.QRect(105, 60, 370, 25))
        self.tx_tarefa_para.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_tarefa_para.setObjectName(_fromUtf8("tx_tarefa_para"))
        self.label_tarefa_2 = QtGui.QLabel(self.ct_tarefas)
        self.label_tarefa_2.setGeometry(QtCore.QRect(25, 95, 75, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_tarefa_2.setFont(font)
        self.label_tarefa_2.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.label_tarefa_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tarefa_2.setObjectName(_fromUtf8("label_tarefa_2"))
        self.tx_tarefa_data = QtGui.QDateEdit(self.ct_tarefas)
        self.tx_tarefa_data.setGeometry(QtCore.QRect(105, 95, 135, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.tx_tarefa_data.setFont(font)
        self.tx_tarefa_data.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_tarefa_data.setCalendarPopup(True)
        self.tx_tarefa_data.setObjectName(_fromUtf8("tx_tarefa_data"))
        self.label_tarefa_3 = QtGui.QLabel(self.ct_tarefas)
        self.label_tarefa_3.setGeometry(QtCore.QRect(250, 95, 75, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_tarefa_3.setFont(font)
        self.label_tarefa_3.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.label_tarefa_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tarefa_3.setObjectName(_fromUtf8("label_tarefa_3"))
        self.tx_tarefa_hora = QtGui.QTimeEdit(self.ct_tarefas)
        self.tx_tarefa_hora.setGeometry(QtCore.QRect(345, 95, 130, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.tx_tarefa_hora.setFont(font)
        self.tx_tarefa_hora.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_tarefa_hora.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.tx_tarefa_hora.setAccelerated(False)
        self.tx_tarefa_hora.setObjectName(_fromUtf8("tx_tarefa_hora"))
        self.label_tarefa_4 = QtGui.QLabel(self.ct_tarefas)
        self.label_tarefa_4.setGeometry(QtCore.QRect(25, 130, 75, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_tarefa_4.setFont(font)
        self.label_tarefa_4.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.label_tarefa_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tarefa_4.setObjectName(_fromUtf8("label_tarefa_4"))
        self.tx_tarefa_texto = QtGui.QPlainTextEdit(self.ct_tarefas)
        self.tx_tarefa_texto.setGeometry(QtCore.QRect(105, 130, 370, 95))
        self.tx_tarefa_texto.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_tarefa_texto.setObjectName(_fromUtf8("tx_tarefa_texto"))
        self.label_tarefa_5 = QtGui.QLabel(self.ct_tarefas)
        self.label_tarefa_5.setGeometry(QtCore.QRect(25, 235, 75, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_tarefa_5.setFont(font)
        self.label_tarefa_5.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.label_tarefa_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tarefa_5.setObjectName(_fromUtf8("label_tarefa_5"))
        self.rb_pendente = QtGui.QRadioButton(self.ct_tarefas)
        self.rb_pendente.setGeometry(QtCore.QRect(105, 240, 100, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.rb_pendente.setFont(font)
        self.rb_pendente.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.rb_pendente.setCheckable(True)
        self.rb_pendente.setChecked(True)
        self.rb_pendente.setObjectName(_fromUtf8("rb_pendente"))
        self.rb_concluido = QtGui.QRadioButton(self.ct_tarefas)
        self.rb_concluido.setGeometry(QtCore.QRect(225, 240, 100, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.rb_concluido.setFont(font)
        self.rb_concluido.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.rb_concluido.setObjectName(_fromUtf8("rb_concluido"))
        self.bt_cadastrar_tarefa = QtGui.QPushButton(self.ct_tarefas)
        self.bt_cadastrar_tarefa.setGeometry(QtCore.QRect(25, 370, 90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.bt_cadastrar_tarefa.setFont(font)
        self.bt_cadastrar_tarefa.setObjectName(_fromUtf8("bt_cadastrar_tarefa"))
        self.bt_cancelar_cadastro = QtGui.QPushButton(self.ct_tarefas)
        self.bt_cancelar_cadastro.setGeometry(QtCore.QRect(125, 370, 90, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.bt_cancelar_cadastro.setFont(font)
        self.bt_cancelar_cadastro.setObjectName(_fromUtf8("bt_cancelar_cadastro"))
        self.ct_tarefas2 = QtGui.QFrame(self.ct_frame_tarefa)
        self.ct_tarefas2.setGeometry(QtCore.QRect(570, 20, 300, 423))
        self.ct_tarefas2.setStyleSheet(_fromUtf8("background: #FFF;\n"
"border: 2px solid #fff;\n"
"border-radius: 20px;"))
        self.ct_tarefas2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ct_tarefas2.setFrameShadow(QtGui.QFrame.Raised)
        self.ct_tarefas2.setObjectName(_fromUtf8("ct_tarefas2"))
        self.lb_tarefas_agendadas_2 = QtGui.QLabel(self.ct_tarefas2)
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
        self.tabela_taregas_agendadas = QtGui.QTableWidget(self.ct_tarefas2)
        self.tabela_taregas_agendadas.setGeometry(QtCore.QRect(5, 60, 290, 250))
        self.tabela_taregas_agendadas.setStyleSheet(_fromUtf8("background: #FFF; border: none; border-radius: 0"))
        self.tabela_taregas_agendadas.setObjectName(_fromUtf8("tabela_taregas_agendadas"))
        self.tabela_taregas_agendadas.setColumnCount(3)
        self.tabela_taregas_agendadas.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tabela_taregas_agendadas.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabela_taregas_agendadas.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabela_taregas_agendadas.setHorizontalHeaderItem(2, item)
        self.tx_buscar_produto = QtGui.QLineEdit(self.ct_tarefas2)
        self.tx_buscar_produto.setGeometry(QtCore.QRect(50, 370, 200, 30))
        self.tx_buscar_produto.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #0CA3D2;\n"
"border-radius:10px;\n"
"background: #FFF;\n"
"color: #000"))
        self.tx_buscar_produto.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_buscar_produto.setObjectName(_fromUtf8("tx_buscar_produto"))
        self.label = QtGui.QLabel(self.ct_tarefas2)
        self.label.setGeometry(QtCore.QRect(100, 340, 100, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: #FFF;\n"
"border: 2px solid #ff00ff;\n"
"border-radius:10px;\n"
"background: #FFF url(\'/Files/Python/AeR/Images/buscar.png\') no-repeat  right ;\n"
"color: #000;\n"
""))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))

        self.tradTarefas(frame_tarefa)
        QtCore.QMetaObject.connectSlotsByName(frame_tarefa)

    def tradTarefas(self, frame_tarefa):
        frame_tarefa.setWindowTitle(_translate("frame_tarefa", "Frame", None))
        self.lb_pedidos_agendados_2.setText(_translate("frame_tarefa", "Agendar / Editar Tarefa", None))
        self.label_tarefa.setText(_translate("frame_tarefa", "Para", None))
        self.label_tarefa_2.setText(_translate("frame_tarefa", "Data", None))
        self.label_tarefa_3.setText(_translate("frame_tarefa", "Hora", None))
        self.tx_tarefa_hora.setDisplayFormat(_translate("frame_tarefa", "HH:mm:ss", None))
        self.label_tarefa_4.setText(_translate("frame_tarefa", "Tarefa:", None))
        self.label_tarefa_5.setText(_translate("frame_tarefa", "Status", None))
        self.rb_pendente.setText(_translate("frame_tarefa", "Pendente", None))
        self.rb_concluido.setText(_translate("frame_tarefa", "Concluído", None))
        self.bt_cadastrar_tarefa.setText(_translate("frame_tarefa", "PushButton", None))
        self.bt_cancelar_cadastro.setText(_translate("frame_tarefa", "PushButton", None))
        self.lb_tarefas_agendadas_2.setText(_translate("frame_tarefa", "Tarefas Agendadas", None))
        item = self.tabela_taregas_agendadas.horizontalHeaderItem(0)
        item.setText(_translate("frame_tarefa", "Data", None))
        item = self.tabela_taregas_agendadas.horizontalHeaderItem(1)
        item.setText(_translate("frame_tarefa", "Para", None))
        item = self.tabela_taregas_agendadas.horizontalHeaderItem(2)
        item.setText(_translate("frame_tarefa", "Tarefa", None))
        self.tx_buscar_produto.setPlaceholderText(_translate("frame_tarefa", "Buscar", None))
        self.label.setText(_translate("frame_tarefa", "Pesquisar", None))

