# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MaintenanceForm.ui'
#
# Created: Thu Oct 13 06:41:15 2016
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

class Ui_MaintenanceForm(object):
    def setupUi(self, MaintenanceForm):
        MaintenanceForm.setObjectName(_fromUtf8("MaintenanceForm"))
        MaintenanceForm.resize(553, 388)
        self.delete_maintenance_button = QtGui.QPushButton(MaintenanceForm)
        self.delete_maintenance_button.setGeometry(QtCore.QRect(515, 85, 25, 25))
        self.delete_maintenance_button.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/wnt/minus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_maintenance_button.setIcon(icon)
        self.delete_maintenance_button.setObjectName(_fromUtf8("delete_maintenance_button"))
        self.maintenance_twidget = QtGui.QTableWidget(MaintenanceForm)
        self.maintenance_twidget.setGeometry(QtCore.QRect(15, 25, 496, 166))
        self.maintenance_twidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.maintenance_twidget.setAlternatingRowColors(True)
        self.maintenance_twidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.maintenance_twidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.maintenance_twidget.setColumnCount(4)
        self.maintenance_twidget.setObjectName(_fromUtf8("maintenance_twidget"))
        self.maintenance_twidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.maintenance_twidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.maintenance_twidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.maintenance_twidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.maintenance_twidget.setHorizontalHeaderItem(3, item)
        self.maintenance_twidget.horizontalHeader().setVisible(True)
        self.maintenance_twidget.horizontalHeader().setDefaultSectionSize(110)
        self.maintenance_twidget.horizontalHeader().setMinimumSectionSize(35)
        self.add_maintenance_button = QtGui.QPushButton(MaintenanceForm)
        self.add_maintenance_button.setGeometry(QtCore.QRect(515, 25, 25, 25))
        self.add_maintenance_button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/wnt/plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_maintenance_button.setIcon(icon1)
        self.add_maintenance_button.setObjectName(_fromUtf8("add_maintenance_button"))
        self.label_16 = QtGui.QLabel(MaintenanceForm)
        self.label_16.setGeometry(QtCore.QRect(15, 10, 66, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.edit_maintenance_button = QtGui.QPushButton(MaintenanceForm)
        self.edit_maintenance_button.setGeometry(QtCore.QRect(515, 55, 25, 25))
        self.edit_maintenance_button.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/wnt/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_maintenance_button.setIcon(icon2)
        self.edit_maintenance_button.setObjectName(_fromUtf8("edit_maintenance_button"))

        self.retranslateUi(MaintenanceForm)
        QtCore.QMetaObject.connectSlotsByName(MaintenanceForm)
        MaintenanceForm.setTabOrder(self.maintenance_twidget, self.add_maintenance_button)
        MaintenanceForm.setTabOrder(self.add_maintenance_button, self.edit_maintenance_button)
        MaintenanceForm.setTabOrder(self.edit_maintenance_button, self.delete_maintenance_button)

    def retranslateUi(self, MaintenanceForm):
        MaintenanceForm.setWindowTitle(_translate("MaintenanceForm", "Form", None))
        self.delete_maintenance_button.setToolTip(_translate("MaintenanceForm", "Delete Maintenance", None))
        item = self.maintenance_twidget.horizontalHeaderItem(0)
        item.setText(_translate("MaintenanceForm", "Maintenance Date", None))
        item = self.maintenance_twidget.horizontalHeaderItem(1)
        item.setText(_translate("MaintenanceForm", "Maintained By", None))
        item = self.maintenance_twidget.horizontalHeaderItem(2)
        item.setText(_translate("MaintenanceForm", "Maintenance Task", None))
        item = self.maintenance_twidget.horizontalHeaderItem(3)
        item.setText(_translate("MaintenanceForm", "Note", None))
        self.add_maintenance_button.setToolTip(_translate("MaintenanceForm", "Add Maintenance", None))
        self.label_16.setText(_translate("MaintenanceForm", "Maintenance", None))
        self.edit_maintenance_button.setToolTip(_translate("MaintenanceForm", "View/Edit Maintenance Details", None))

import resources_rc
