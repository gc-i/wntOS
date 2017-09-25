# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RepairMaterialDialog.ui'
#
# Created: Tue Oct 11 10:52:48 2016
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

class Ui_RepairMaterialDialog(object):
    def setupUi(self, RepairMaterialDialog):
        RepairMaterialDialog.setObjectName(_fromUtf8("RepairMaterialDialog"))
        RepairMaterialDialog.resize(300, 200)
        RepairMaterialDialog.setMinimumSize(QtCore.QSize(300, 200))
        RepairMaterialDialog.setMaximumSize(QtCore.QSize(300, 200))
        self.buttonBox = QtGui.QDialogButtonBox(RepairMaterialDialog)
        self.buttonBox.setGeometry(QtCore.QRect(105, 155, 166, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.cost_sbox = QtGui.QDoubleSpinBox(RepairMaterialDialog)
        self.cost_sbox.setGeometry(QtCore.QRect(20, 115, 251, 22))
        self.cost_sbox.setMaximum(5000000.0)
        self.cost_sbox.setObjectName(_fromUtf8("cost_sbox"))
        self.label = QtGui.QLabel(RepairMaterialDialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 126, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(RepairMaterialDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 55, 126, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.material_cbox = QtGui.QComboBox(RepairMaterialDialog)
        self.material_cbox.setGeometry(QtCore.QRect(20, 70, 251, 22))
        self.material_cbox.setEditable(True)
        self.material_cbox.setObjectName(_fromUtf8("material_cbox"))
        self.amount_sbox = QtGui.QSpinBox(RepairMaterialDialog)
        self.amount_sbox.setGeometry(QtCore.QRect(20, 25, 251, 22))
        self.amount_sbox.setMinimum(1)
        self.amount_sbox.setMaximum(200)
        self.amount_sbox.setObjectName(_fromUtf8("amount_sbox"))
        self.label_14 = QtGui.QLabel(RepairMaterialDialog)
        self.label_14.setGeometry(QtCore.QRect(20, 100, 126, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))

        self.retranslateUi(RepairMaterialDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), RepairMaterialDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), RepairMaterialDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(RepairMaterialDialog)
        RepairMaterialDialog.setTabOrder(self.amount_sbox, self.material_cbox)
        RepairMaterialDialog.setTabOrder(self.material_cbox, self.cost_sbox)

    def retranslateUi(self, RepairMaterialDialog):
        RepairMaterialDialog.setWindowTitle(_translate("RepairMaterialDialog", "Add / Edit Repair Material", None))
        self.label.setText(_translate("RepairMaterialDialog", "Amount", None))
        self.label_2.setText(_translate("RepairMaterialDialog", "Material", None))
        self.label_14.setText(_translate("RepairMaterialDialog", "Total Cost [TZS]", None))

import resources_rc
