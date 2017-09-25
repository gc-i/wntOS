# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DMADialog.ui'
#
# Created: Fri Oct 14 06:21:35 2016
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_DMADialog(object):
    def setupUi(self, DMADialog):
        DMADialog.setObjectName(_fromUtf8("DMADialog"))
        DMADialog.resize(588, 400)
        DMADialog.setMinimumSize(QtCore.QSize(588, 400))
        DMADialog.setMaximumSize(QtCore.QSize(588, 400))
        self.buttonBox = QtGui.QDialogButtonBox(DMADialog)
        self.buttonBox.setGeometry(QtCore.QRect(404, 350, 166, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget = QtGui.QTabWidget(DMADialog)
        self.tabWidget.setGeometry(QtCore.QRect(15, 10, 556, 321))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.dma_number_edit = QtGui.QLineEdit(self.tab)
        self.dma_number_edit.setGeometry(QtCore.QRect(30, 30, 196, 20))
        self.dma_number_edit.setObjectName(_fromUtf8("dma_number_edit"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 15, 126, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_15 = QtGui.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(260, 59, 126, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_14 = QtGui.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(260, 14, 161, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.network_cbox = QtGui.QComboBox(self.tab)
        self.network_cbox.setGeometry(QtCore.QRect(260, 74, 196, 22))
        self.network_cbox.setObjectName(_fromUtf8("network_cbox"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 126, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.dma_name_edit = QtGui.QLineEdit(self.tab)
        self.dma_name_edit.setGeometry(QtCore.QRect(30, 75, 196, 20))
        self.dma_name_edit.setObjectName(_fromUtf8("dma_name_edit"))
        self.area_edit = QtGui.QLineEdit(self.tab)
        self.area_edit.setGeometry(QtCore.QRect(260, 30, 196, 20))
        self.area_edit.setReadOnly(True)
        self.area_edit.setObjectName(_fromUtf8("area_edit"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        self.retranslateUi(DMADialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DMADialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DMADialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DMADialog)
        DMADialog.setTabOrder(self.tabWidget, self.dma_number_edit)
        DMADialog.setTabOrder(self.dma_number_edit, self.dma_name_edit)
        DMADialog.setTabOrder(self.dma_name_edit, self.area_edit)
        DMADialog.setTabOrder(self.area_edit, self.network_cbox)
        DMADialog.setTabOrder(self.network_cbox, self.buttonBox)

    def retranslateUi(self, DMADialog):
        DMADialog.setWindowTitle(_translate("DMADialog", "Add / Edit DMA", None))
        self.label.setText(_translate("DMADialog", "DMA Number", None))
        self.label_15.setText(_translate("DMADialog", "Network", None))
        self.label_14.setText(_translate("DMADialog", "Calculated Area [km2]", None))
        self.label_2.setText(_translate("DMADialog", "DMA Name", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DMADialog", "Description", None))

import resources_rc
