# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NetworkDialog.ui'
#
# Created: Tue Sep 27 09:10:51 2016
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

class Ui_NetworkDialog(object):
    def setupUi(self, NetworkDialog):
        NetworkDialog.setObjectName(_fromUtf8("NetworkDialog"))
        NetworkDialog.resize(588, 480)
        NetworkDialog.setMinimumSize(QtCore.QSize(588, 480))
        NetworkDialog.setMaximumSize(QtCore.QSize(588, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/wnt/network.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NetworkDialog.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(NetworkDialog)
        self.buttonBox.setGeometry(QtCore.QRect(405, 440, 166, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget = QtGui.QTabWidget(NetworkDialog)
        self.tabWidget.setGeometry(QtCore.QRect(15, 10, 556, 411))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.network_no_edit = QtGui.QLineEdit(self.tab)
        self.network_no_edit.setGeometry(QtCore.QRect(20, 30, 196, 20))
        self.network_no_edit.setObjectName(_fromUtf8("network_no_edit"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 15, 126, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.dim_pressure_cbox = QtGui.QComboBox(self.tab)
        self.dim_pressure_cbox.setGeometry(QtCore.QRect(255, 30, 196, 22))
        self.dim_pressure_cbox.setObjectName(_fromUtf8("dim_pressure_cbox"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(255, 15, 126, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(255, 60, 126, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.op_pressure_cbox = QtGui.QComboBox(self.tab)
        self.op_pressure_cbox.setGeometry(QtCore.QRect(255, 75, 196, 22))
        self.op_pressure_cbox.setObjectName(_fromUtf8("op_pressure_cbox"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 126, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.network_name_edit = QtGui.QLineEdit(self.tab)
        self.network_name_edit.setGeometry(QtCore.QRect(20, 75, 196, 20))
        self.network_name_edit.setObjectName(_fromUtf8("network_name_edit"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        self.retranslateUi(NetworkDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NetworkDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NetworkDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NetworkDialog)
        NetworkDialog.setTabOrder(self.network_no_edit, self.network_name_edit)
        NetworkDialog.setTabOrder(self.network_name_edit, self.dim_pressure_cbox)
        NetworkDialog.setTabOrder(self.dim_pressure_cbox, self.op_pressure_cbox)
        NetworkDialog.setTabOrder(self.op_pressure_cbox, self.tabWidget)

    def retranslateUi(self, NetworkDialog):
        NetworkDialog.setWindowTitle(_translate("NetworkDialog", "Add / Edit Network", None))
        self.label.setText(_translate("NetworkDialog", "Network Number", None))
        self.label_6.setText(_translate("NetworkDialog", "Dimensioning Pressure", None))
        self.label_7.setText(_translate("NetworkDialog", "Operating Pressure", None))
        self.label_2.setText(_translate("NetworkDialog", "Network Name", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("NetworkDialog", "Description", None))

import resources_rc
