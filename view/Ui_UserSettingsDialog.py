# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserSettingsDialog.ui'
#
# Created: Wed Aug 03 13:51:31 2016
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

class Ui_UserSettingsDialog(object):
    def setupUi(self, UserSettingsDialog):
        UserSettingsDialog.setObjectName(_fromUtf8("UserSettingsDialog"))
        UserSettingsDialog.resize(400, 300)
        UserSettingsDialog.setMinimumSize(QtCore.QSize(400, 300))
        UserSettingsDialog.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/wnt/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UserSettingsDialog.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(UserSettingsDialog)
        self.buttonBox.setGeometry(QtCore.QRect(210, 260, 176, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget = QtGui.QTabWidget(UserSettingsDialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 376, 241))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.network_cbox = QtGui.QComboBox(self.tab)
        self.network_cbox.setGeometry(QtCore.QRect(15, 30, 286, 22))
        self.network_cbox.setObjectName(_fromUtf8("network_cbox"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(15, 15, 136, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        self.retranslateUi(UserSettingsDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), UserSettingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), UserSettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(UserSettingsDialog)
        UserSettingsDialog.setTabOrder(self.tabWidget, self.network_cbox)

    def retranslateUi(self, UserSettingsDialog):
        UserSettingsDialog.setWindowTitle(_translate("UserSettingsDialog", "User Settings", None))
        self.label.setText(_translate("UserSettingsDialog", "Default Network", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("UserSettingsDialog", "General", None))

import resources_rc
