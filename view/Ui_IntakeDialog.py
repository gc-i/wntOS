# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IntakeDialog.ui'
#
# Created: Tue Sep 27 09:09:54 2016
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

class Ui_IntakeDialog(object):
    def setupUi(self, IntakeDialog):
        IntakeDialog.setObjectName(_fromUtf8("IntakeDialog"))
        IntakeDialog.resize(588, 410)
        IntakeDialog.setMinimumSize(QtCore.QSize(588, 410))
        IntakeDialog.setMaximumSize(QtCore.QSize(588, 480))
        self.buttonBox = QtGui.QDialogButtonBox(IntakeDialog)
        self.buttonBox.setGeometry(QtCore.QRect(405, 360, 166, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget = QtGui.QTabWidget(IntakeDialog)
        self.tabWidget.setGeometry(QtCore.QRect(15, 10, 556, 331))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.intake_no_edit = QtGui.QLineEdit(self.tab)
        self.intake_no_edit.setGeometry(QtCore.QRect(20, 40, 196, 20))
        self.intake_no_edit.setObjectName(_fromUtf8("intake_no_edit"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(280, 25, 126, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 25, 126, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.status_change_date_edit = QtGui.QDateEdit(self.tab)
        self.status_change_date_edit.setEnabled(False)
        self.status_change_date_edit.setGeometry(QtCore.QRect(305, 130, 171, 22))
        self.status_change_date_edit.setCalendarPopup(True)
        self.status_change_date_edit.setObjectName(_fromUtf8("status_change_date_edit"))
        self.status_change_date_chbox = QtGui.QCheckBox(self.tab)
        self.status_change_date_chbox.setGeometry(QtCore.QRect(280, 135, 26, 17))
        self.status_change_date_chbox.setText(_fromUtf8(""))
        self.status_change_date_chbox.setObjectName(_fromUtf8("status_change_date_chbox"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(280, 115, 126, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.height_sbox = QtGui.QDoubleSpinBox(self.tab)
        self.height_sbox.setGeometry(QtCore.QRect(280, 175, 196, 22))
        self.height_sbox.setMinimum(-100.0)
        self.height_sbox.setMaximum(2000.0)
        self.height_sbox.setObjectName(_fromUtf8("height_sbox"))
        self.label_14 = QtGui.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(280, 160, 126, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(280, 205, 126, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.network_cbox = QtGui.QComboBox(self.tab)
        self.network_cbox.setGeometry(QtCore.QRect(280, 220, 196, 22))
        self.network_cbox.setObjectName(_fromUtf8("network_cbox"))
        self.installation_year_sbox = QtGui.QDoubleSpinBox(self.tab)
        self.installation_year_sbox.setGeometry(QtCore.QRect(280, 40, 196, 22))
        self.installation_year_sbox.setDecimals(0)
        self.installation_year_sbox.setMaximum(3000.0)
        self.installation_year_sbox.setProperty("value", 0.0)
        self.installation_year_sbox.setObjectName(_fromUtf8("installation_year_sbox"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 126, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.intake_source_cbox = QtGui.QComboBox(self.tab)
        self.intake_source_cbox.setGeometry(QtCore.QRect(20, 85, 196, 22))
        self.intake_source_cbox.setObjectName(_fromUtf8("intake_source_cbox"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 115, 126, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.intake_type_cbox = QtGui.QComboBox(self.tab)
        self.intake_type_cbox.setGeometry(QtCore.QRect(20, 130, 196, 22))
        self.intake_type_cbox.setObjectName(_fromUtf8("intake_type_cbox"))
        self.label_16 = QtGui.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(20, 205, 126, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.capacity_sbox = QtGui.QDoubleSpinBox(self.tab)
        self.capacity_sbox.setGeometry(QtCore.QRect(20, 220, 196, 22))
        self.capacity_sbox.setMinimum(0.0)
        self.capacity_sbox.setMaximum(200000.0)
        self.capacity_sbox.setObjectName(_fromUtf8("capacity_sbox"))
        self.operating_state_cbox = QtGui.QComboBox(self.tab)
        self.operating_state_cbox.setGeometry(QtCore.QRect(280, 85, 196, 22))
        self.operating_state_cbox.setObjectName(_fromUtf8("operating_state_cbox"))
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(280, 70, 126, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(20, 160, 126, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.capacity_unit_cbox = QtGui.QComboBox(self.tab)
        self.capacity_unit_cbox.setGeometry(QtCore.QRect(20, 175, 196, 22))
        self.capacity_unit_cbox.setObjectName(_fromUtf8("capacity_unit_cbox"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        self.retranslateUi(IntakeDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), IntakeDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), IntakeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(IntakeDialog)
        IntakeDialog.setTabOrder(self.tabWidget, self.intake_no_edit)
        IntakeDialog.setTabOrder(self.intake_no_edit, self.intake_source_cbox)
        IntakeDialog.setTabOrder(self.intake_source_cbox, self.intake_type_cbox)
        IntakeDialog.setTabOrder(self.intake_type_cbox, self.capacity_unit_cbox)
        IntakeDialog.setTabOrder(self.capacity_unit_cbox, self.capacity_sbox)
        IntakeDialog.setTabOrder(self.capacity_sbox, self.installation_year_sbox)
        IntakeDialog.setTabOrder(self.installation_year_sbox, self.operating_state_cbox)
        IntakeDialog.setTabOrder(self.operating_state_cbox, self.status_change_date_chbox)
        IntakeDialog.setTabOrder(self.status_change_date_chbox, self.status_change_date_edit)
        IntakeDialog.setTabOrder(self.status_change_date_edit, self.height_sbox)
        IntakeDialog.setTabOrder(self.height_sbox, self.network_cbox)

    def retranslateUi(self, IntakeDialog):
        IntakeDialog.setWindowTitle(_translate("IntakeDialog", "Add / Edit Intake", None))
        self.label_3.setText(_translate("IntakeDialog", "Installation Year", None))
        self.label.setText(_translate("IntakeDialog", "Intake Number", None))
        self.status_change_date_edit.setDisplayFormat(_translate("IntakeDialog", "yyyy-MM-dd", None))
        self.label_8.setText(_translate("IntakeDialog", "Date of Status Change", None))
        self.label_14.setText(_translate("IntakeDialog", "Height [m]", None))
        self.label_15.setText(_translate("IntakeDialog", "Network", None))
        self.label_2.setText(_translate("IntakeDialog", "Intake Source", None))
        self.label_5.setText(_translate("IntakeDialog", "Intake Type", None))
        self.label_16.setText(_translate("IntakeDialog", "Capacity", None))
        self.label_9.setText(_translate("IntakeDialog", "Operating State", None))
        self.label_10.setText(_translate("IntakeDialog", "Capacity Unit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("IntakeDialog", "Description", None))

import resources_rc
