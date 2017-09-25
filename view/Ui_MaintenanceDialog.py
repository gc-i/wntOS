# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MaintenanceDialog.ui'
#
# Created: Thu Oct 13 06:40:30 2016
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

class Ui_MaintenanceDialog(object):
    def setupUi(self, MaintenanceDialog):
        MaintenanceDialog.setObjectName(_fromUtf8("MaintenanceDialog"))
        MaintenanceDialog.resize(588, 320)
        MaintenanceDialog.setMinimumSize(QtCore.QSize(588, 320))
        MaintenanceDialog.setMaximumSize(QtCore.QSize(588, 320))
        self.buttonBox = QtGui.QDialogButtonBox(MaintenanceDialog)
        self.buttonBox.setGeometry(QtCore.QRect(405, 280, 166, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget = QtGui.QTabWidget(MaintenanceDialog)
        self.tabWidget.setGeometry(QtCore.QRect(15, 10, 556, 261))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.maintenance_date_edit = QtGui.QDateEdit(self.tab)
        self.maintenance_date_edit.setEnabled(True)
        self.maintenance_date_edit.setGeometry(QtCore.QRect(20, 30, 196, 22))
        self.maintenance_date_edit.setCalendarPopup(True)
        self.maintenance_date_edit.setObjectName(_fromUtf8("maintenance_date_edit"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 15, 126, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.maintained_by_cbox = QtGui.QComboBox(self.tab)
        self.maintained_by_cbox.setGeometry(QtCore.QRect(20, 75, 196, 22))
        self.maintained_by_cbox.setEditable(True)
        self.maintained_by_cbox.setObjectName(_fromUtf8("maintained_by_cbox"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 60, 126, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_15 = QtGui.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(270, 15, 126, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.note_edit = QtGui.QPlainTextEdit(self.tab)
        self.note_edit.setGeometry(QtCore.QRect(270, 30, 196, 146))
        self.note_edit.setObjectName(_fromUtf8("note_edit"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(20, 105, 141, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.maintenance_task_cbox = QtGui.QComboBox(self.tab)
        self.maintenance_task_cbox.setGeometry(QtCore.QRect(20, 120, 196, 22))
        self.maintenance_task_cbox.setEditable(True)
        self.maintenance_task_cbox.setObjectName(_fromUtf8("maintenance_task_cbox"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        self.retranslateUi(MaintenanceDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MaintenanceDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MaintenanceDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(MaintenanceDialog)
        MaintenanceDialog.setTabOrder(self.tabWidget, self.maintenance_date_edit)
        MaintenanceDialog.setTabOrder(self.maintenance_date_edit, self.maintained_by_cbox)
        MaintenanceDialog.setTabOrder(self.maintained_by_cbox, self.maintenance_task_cbox)
        MaintenanceDialog.setTabOrder(self.maintenance_task_cbox, self.note_edit)
        MaintenanceDialog.setTabOrder(self.note_edit, self.buttonBox)

    def retranslateUi(self, MaintenanceDialog):
        MaintenanceDialog.setWindowTitle(_translate("MaintenanceDialog", "Add / Edit Maintenance", None))
        self.maintenance_date_edit.setDisplayFormat(_translate("MaintenanceDialog", "yyyy-MM-dd", None))
        self.label_3.setText(_translate("MaintenanceDialog", "Maintenance Date", None))
        self.label_6.setText(_translate("MaintenanceDialog", "Maintained By", None))
        self.label_15.setText(_translate("MaintenanceDialog", "Note", None))
        self.label_7.setText(_translate("MaintenanceDialog", "Maintenance Task / Activity", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MaintenanceDialog", "Description", None))

import resources_rc
