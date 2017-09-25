# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RepairMaterialForm.ui'
#
# Created: Tue Oct 04 20:11:32 2016
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

class Ui_RepairMaterialForm(object):
    def setupUi(self, RepairMaterialForm):
        RepairMaterialForm.setObjectName(_fromUtf8("RepairMaterialForm"))
        RepairMaterialForm.resize(554, 340)
        self.material_twidget = QtGui.QTableWidget(RepairMaterialForm)
        self.material_twidget.setGeometry(QtCore.QRect(15, 25, 496, 166))
        self.material_twidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.material_twidget.setAlternatingRowColors(True)
        self.material_twidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.material_twidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.material_twidget.setObjectName(_fromUtf8("material_twidget"))
        self.material_twidget.setColumnCount(3)
        self.material_twidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.material_twidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.material_twidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.material_twidget.setHorizontalHeaderItem(2, item)
        self.delete_material_button = QtGui.QPushButton(RepairMaterialForm)
        self.delete_material_button.setGeometry(QtCore.QRect(515, 85, 25, 25))
        self.delete_material_button.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/wnt/minus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_material_button.setIcon(icon)
        self.delete_material_button.setObjectName(_fromUtf8("delete_material_button"))
        self.add_material_button = QtGui.QPushButton(RepairMaterialForm)
        self.add_material_button.setGeometry(QtCore.QRect(515, 25, 25, 25))
        self.add_material_button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/wnt/plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_material_button.setIcon(icon1)
        self.add_material_button.setObjectName(_fromUtf8("add_material_button"))
        self.edit_material_button = QtGui.QPushButton(RepairMaterialForm)
        self.edit_material_button.setGeometry(QtCore.QRect(515, 55, 25, 25))
        self.edit_material_button.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/wnt/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_material_button.setIcon(icon2)
        self.edit_material_button.setObjectName(_fromUtf8("edit_material_button"))
        self.label_16 = QtGui.QLabel(RepairMaterialForm)
        self.label_16.setGeometry(QtCore.QRect(15, 10, 131, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))

        self.retranslateUi(RepairMaterialForm)
        QtCore.QMetaObject.connectSlotsByName(RepairMaterialForm)

    def retranslateUi(self, RepairMaterialForm):
        RepairMaterialForm.setWindowTitle(_translate("RepairMaterialForm", "Form", None))
        item = self.material_twidget.horizontalHeaderItem(0)
        item.setText(_translate("RepairMaterialForm", "Amount", None))
        item = self.material_twidget.horizontalHeaderItem(1)
        item.setText(_translate("RepairMaterialForm", "Material", None))
        item = self.material_twidget.horizontalHeaderItem(2)
        item.setText(_translate("RepairMaterialForm", "Total Cost [TZS]", None))
        self.delete_material_button.setToolTip(_translate("RepairMaterialForm", "Delete Material", None))
        self.add_material_button.setToolTip(_translate("RepairMaterialForm", "Add Material", None))
        self.edit_material_button.setToolTip(_translate("RepairMaterialForm", "View/Edit Material Details", None))
        self.label_16.setText(_translate("RepairMaterialForm", "Repair Material", None))

import resources_rc
