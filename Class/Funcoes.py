# -*- coding: utf-8 -*-
from PyQt4 import QtGui

class Funcoes(object):

    def limpa_frame(self, frame):
        for i in range(len(frame.children())):
            frame.children()[i].deleteLater()

    def desativa_botao(self, frame, botao):
        for filho in frame.findChildren(QtGui.QPushButton):
            filho.setEnabled(True)

        botao.setEnabled(False)

    def estilo_botao_acao(self, ok, cancelar):
        ok.setStyleSheet("QPushButton{color: #FFF; border: 2px solid #0CA3D2; border-radius:10px;"
                                               "background: #FFF; color: #000}"
                         "QPushButton:hover {border: 2px solid #000;}")
        cancelar.setStyleSheet("QPushButton{color: #FFF; border: 2px solid red; border-radius:10px;"
                                              "background: #FFF; color: #000}"
                               "QPushButton:hover {border: 2px solid #000;}")

    def botao_padrao(self, frame):
        for filho in frame.findChildren(QtGui.QPushButton):
            efeito = QtGui.QGraphicsDropShadowEffect()
            efeito.setColor(QtGui.QColor("#ff00ff"))
            efeito.setOffset(0, 0)
            efeito.setBlurRadius(15)
            filho.setGraphicsEffect(efeito)
            filho.setStyleSheet(" QPushButton{border-radius: 10px; border: none; background: #00ffff;}"
                                "QPushButton:disabled {background: #FFF}")