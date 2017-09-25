# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FindFeatureDialog.ui'
#
# Created: Fri Jul 29 09:16:13 2016
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

class Ui_FindFeatureDialog(object):
    def setupUi(self, FindFeatureDialog):
        FindFeatureDialog.setObjectName(_fromUtf8("FindFeatureDialog"))
        FindFeatureDialog.resize(300, 285)
        FindFeatureDialog.setMinimumSize(QtCore.QSize(300, 285))
        FindFeatureDialog.setMaximumSize(QtCore.QSize(300, 285))
        FindFeatureDialog.setModal(False)
        self.buttonBox = QtGui.QDialogButtonBox(FindFeatureDialog)
        self.buttonBox.setGeometry(QtCore.QRect(160, 235, 116, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.feature_lwidget = QtGui.QListWidget(FindFeatureDialog)
        self.feature_lwidget.setGeometry(QtCore.QRect(20, 30, 256, 192))
        self.feature_lwidget.setObjectName(_fromUtf8("feature_lwidget"))
        self.list_title_label = QtGui.QLabel(FindFeatureDialog)
        self.list_title_label.setGeometry(QtCore.QRect(20, 15, 246, 16))
        self.list_title_label.setObjectName(_fromUtf8("list_title_label"))

        self.retranslateUi(FindFeatureDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), FindFeatureDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), FindFeatureDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FindFeatureDialog)

    def retranslateUi(self, FindFeatureDialog):
        FindFeatureDialog.setWindowTitle(_translate("FindFeatureDialog", "Find Features", None))
        self.list_title_label.setText(_translate("FindFeatureDialog", "Features Found", None))

