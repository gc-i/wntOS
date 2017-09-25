# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DamageForm.ui'
#
# Created: Thu Oct 13 06:53:45 2016
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

class Ui_DamageForm(object):
    def setupUi(self, DamageForm):
        DamageForm.setObjectName(_fromUtf8("DamageForm"))
        DamageForm.resize(553, 388)
        self.damage_twidget = QtGui.QTableWidget(DamageForm)
        self.damage_twidget.setGeometry(QtCore.QRect(15, 25, 496, 166))
        self.damage_twidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.damage_twidget.setAlternatingRowColors(True)
        self.damage_twidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.damage_twidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.damage_twidget.setObjectName(_fromUtf8("damage_twidget"))
        self.damage_twidget.setColumnCount(11)
        self.damage_twidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.damage_twidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.damage_twidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.damage_twidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.damage_twidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.damage_twidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.damage_twidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.damage_twidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.damage_twidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.damage_twidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.damage_twidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.damage_twidget.setHorizontalHeaderItem(10, item)
        self.label_16 = QtGui.QLabel(DamageForm)
        self.label_16.setGeometry(QtCore.QRect(15, 10, 66, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.view_maxcom_button = QtGui.QPushButton(DamageForm)
        self.view_maxcom_button.setGeometry(QtCore.QRect(515, 55, 25, 25))
        self.view_maxcom_button.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/wnt/eye.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.view_maxcom_button.setIcon(icon)
        self.view_maxcom_button.setObjectName(_fromUtf8("view_maxcom_button"))
        self.edit_damage_button = QtGui.QPushButton(DamageForm)
        self.edit_damage_button.setGeometry(QtCore.QRect(515, 25, 25, 25))
        self.edit_damage_button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/wnt/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_damage_button.setIcon(icon1)
        self.edit_damage_button.setObjectName(_fromUtf8("edit_damage_button"))

        self.retranslateUi(DamageForm)
        QtCore.QMetaObject.connectSlotsByName(DamageForm)
        DamageForm.setTabOrder(self.damage_twidget, self.edit_damage_button)
        DamageForm.setTabOrder(self.edit_damage_button, self.view_maxcom_button)

    def retranslateUi(self, DamageForm):
        DamageForm.setWindowTitle(_translate("DamageForm", "Form", None))
        item = self.damage_twidget.horizontalHeaderItem(0)
        item.setText(_translate("DamageForm", "Control No.", None))
        item = self.damage_twidget.horizontalHeaderItem(1)
        item.setText(_translate("DamageForm", "Received From", None))
        item = self.damage_twidget.horizontalHeaderItem(2)
        item.setText(_translate("DamageForm", "Occurrence TS", None))
        item = self.damage_twidget.horizontalHeaderItem(3)
        item.setText(_translate("DamageForm", "Registration TS", None))
        item = self.damage_twidget.horizontalHeaderItem(4)
        item.setText(_translate("DamageForm", "Repair TS", None))
        item = self.damage_twidget.horizontalHeaderItem(5)
        item.setText(_translate("DamageForm", "Repaired By", None))
        item = self.damage_twidget.horizontalHeaderItem(6)
        item.setText(_translate("DamageForm", "Repair Task", None))
        item = self.damage_twidget.horizontalHeaderItem(7)
        item.setText(_translate("DamageForm", "Type", None))
        item = self.damage_twidget.horizontalHeaderItem(8)
        item.setText(_translate("DamageForm", "Cause", None))
        item = self.damage_twidget.horizontalHeaderItem(9)
        item.setText(_translate("DamageForm", "Status", None))
        item = self.damage_twidget.horizontalHeaderItem(10)
        item.setText(_translate("DamageForm", "Note", None))
        self.label_16.setText(_translate("DamageForm", "Damages", None))
        self.view_maxcom_button.setToolTip(_translate("DamageForm", "View Complaint Details at MAXCOM", None))
        self.edit_damage_button.setToolTip(_translate("DamageForm", "View/Edit Damage Details", None))

import resources_rc
