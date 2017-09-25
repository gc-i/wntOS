# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NetworkManagementDialog.ui'
#
# Created: Mon Nov 07 15:55:58 2016
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

class Ui_NetworkManagementDialog(object):
    def setupUi(self, NetworkManagementDialog):
        NetworkManagementDialog.setObjectName(_fromUtf8("NetworkManagementDialog"))
        NetworkManagementDialog.resize(564, 270)
        NetworkManagementDialog.setMinimumSize(QtCore.QSize(564, 270))
        NetworkManagementDialog.setMaximumSize(QtCore.QSize(564, 270))
        NetworkManagementDialog.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/wnt/network.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NetworkManagementDialog.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(NetworkManagementDialog)
        self.buttonBox.setGeometry(QtCore.QRect(350, 225, 191, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.delete_network_button = QtGui.QPushButton(NetworkManagementDialog)
        self.delete_network_button.setGeometry(QtCore.QRect(515, 90, 25, 25))
        self.delete_network_button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/wnt/minus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_network_button.setIcon(icon1)
        self.delete_network_button.setObjectName(_fromUtf8("delete_network_button"))
        self.edit_network_button = QtGui.QPushButton(NetworkManagementDialog)
        self.edit_network_button.setGeometry(QtCore.QRect(515, 60, 25, 25))
        self.edit_network_button.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/wnt/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_network_button.setIcon(icon2)
        self.edit_network_button.setObjectName(_fromUtf8("edit_network_button"))
        self.network_twidget = QtGui.QTableWidget(NetworkManagementDialog)
        self.network_twidget.setGeometry(QtCore.QRect(15, 30, 496, 166))
        self.network_twidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.network_twidget.setAlternatingRowColors(True)
        self.network_twidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.network_twidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.network_twidget.setObjectName(_fromUtf8("network_twidget"))
        self.network_twidget.setColumnCount(4)
        self.network_twidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.network_twidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.network_twidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.network_twidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.network_twidget.setHorizontalHeaderItem(3, item)
        self.label_16 = QtGui.QLabel(NetworkManagementDialog)
        self.label_16.setGeometry(QtCore.QRect(15, 15, 66, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.add_network_button = QtGui.QPushButton(NetworkManagementDialog)
        self.add_network_button.setGeometry(QtCore.QRect(515, 30, 25, 25))
        self.add_network_button.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/wnt/plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_network_button.setIcon(icon3)
        self.add_network_button.setObjectName(_fromUtf8("add_network_button"))

        self.retranslateUi(NetworkManagementDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NetworkManagementDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NetworkManagementDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NetworkManagementDialog)
        NetworkManagementDialog.setTabOrder(self.network_twidget, self.add_network_button)
        NetworkManagementDialog.setTabOrder(self.add_network_button, self.edit_network_button)
        NetworkManagementDialog.setTabOrder(self.edit_network_button, self.delete_network_button)

    def retranslateUi(self, NetworkManagementDialog):
        NetworkManagementDialog.setWindowTitle(_translate("NetworkManagementDialog", "Manage Networks", None))
        self.delete_network_button.setToolTip(_translate("NetworkManagementDialog", "Delete Network", None))
        self.edit_network_button.setToolTip(_translate("NetworkManagementDialog", "View/Edit Network Details", None))
        item = self.network_twidget.horizontalHeaderItem(0)
        item.setText(_translate("NetworkManagementDialog", "Network No.", None))
        item = self.network_twidget.horizontalHeaderItem(1)
        item.setText(_translate("NetworkManagementDialog", "Network Name", None))
        item = self.network_twidget.horizontalHeaderItem(2)
        item.setText(_translate("NetworkManagementDialog", "Dimensioning Pressure", None))
        item = self.network_twidget.horizontalHeaderItem(3)
        item.setText(_translate("NetworkManagementDialog", "Operating Pressure", None))
        self.label_16.setText(_translate("NetworkManagementDialog", "Networks", None))
        self.add_network_button.setToolTip(_translate("NetworkManagementDialog", "Add Network", None))

import resources_rc
