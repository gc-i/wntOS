# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DistributionPointDialog.ui'
#
# Created: Sun Oct 09 20:03:15 2016
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

class Ui_DistributionPointDialog(object):
    def setupUi(self, DistributionPointDialog):
        DistributionPointDialog.setObjectName(_fromUtf8("DistributionPointDialog"))
        DistributionPointDialog.resize(588, 460)
        DistributionPointDialog.setMinimumSize(QtCore.QSize(588, 460))
        DistributionPointDialog.setMaximumSize(QtCore.QSize(588, 460))
        self.buttonBox = QtGui.QDialogButtonBox(DistributionPointDialog)
        self.buttonBox.setGeometry(QtCore.QRect(355, 425, 216, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget = QtGui.QTabWidget(DistributionPointDialog)
        self.tabWidget.setGeometry(QtCore.QRect(15, 10, 556, 411))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.inspection_intervall_sbox = QtGui.QDoubleSpinBox(self.tab)
        self.inspection_intervall_sbox.setGeometry(QtCore.QRect(20, 115, 196, 22))
        self.inspection_intervall_sbox.setObjectName(_fromUtf8("inspection_intervall_sbox"))
        self.installation_date_edit = QtGui.QDateEdit(self.tab)
        self.installation_date_edit.setEnabled(False)
        self.installation_date_edit.setGeometry(QtCore.QRect(45, 75, 171, 22))
        self.installation_date_edit.setCalendarPopup(True)
        self.installation_date_edit.setObjectName(_fromUtf8("installation_date_edit"))
        self.installation_date_chbox = QtGui.QCheckBox(self.tab)
        self.installation_date_chbox.setGeometry(QtCore.QRect(20, 80, 26, 17))
        self.installation_date_chbox.setText(_fromUtf8(""))
        self.installation_date_chbox.setObjectName(_fromUtf8("installation_date_chbox"))
        self.dist_point_number_edit = QtGui.QLineEdit(self.tab)
        self.dist_point_number_edit.setGeometry(QtCore.QRect(20, 30, 196, 20))
        self.dist_point_number_edit.setObjectName(_fromUtf8("dist_point_number_edit"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 126, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 126, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 15, 126, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.inspection_intervall_unit_cbox = QtGui.QComboBox(self.tab)
        self.inspection_intervall_unit_cbox.setGeometry(QtCore.QRect(20, 160, 196, 22))
        self.inspection_intervall_unit_cbox.setObjectName(_fromUtf8("inspection_intervall_unit_cbox"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 145, 126, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(270, 15, 126, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.operating_state_cbox = QtGui.QComboBox(self.tab)
        self.operating_state_cbox.setGeometry(QtCore.QRect(270, 30, 196, 22))
        self.operating_state_cbox.setObjectName(_fromUtf8("operating_state_cbox"))
        self.status_change_date_edit = QtGui.QDateEdit(self.tab)
        self.status_change_date_edit.setEnabled(False)
        self.status_change_date_edit.setGeometry(QtCore.QRect(295, 75, 171, 22))
        self.status_change_date_edit.setCalendarPopup(True)
        self.status_change_date_edit.setObjectName(_fromUtf8("status_change_date_edit"))
        self.status_change_date_chbox = QtGui.QCheckBox(self.tab)
        self.status_change_date_chbox.setGeometry(QtCore.QRect(270, 80, 26, 17))
        self.status_change_date_chbox.setText(_fromUtf8(""))
        self.status_change_date_chbox.setObjectName(_fromUtf8("status_change_date_chbox"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(270, 60, 126, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.height_sbox = QtGui.QDoubleSpinBox(self.tab)
        self.height_sbox.setGeometry(QtCore.QRect(270, 117, 196, 22))
        self.height_sbox.setMinimum(-100.0)
        self.height_sbox.setMaximum(2000.0)
        self.height_sbox.setObjectName(_fromUtf8("height_sbox"))
        self.label_14 = QtGui.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(270, 102, 126, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(270, 147, 126, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.network_cbox = QtGui.QComboBox(self.tab)
        self.network_cbox.setGeometry(QtCore.QRect(270, 162, 196, 22))
        self.network_cbox.setObjectName(_fromUtf8("network_cbox"))
        self.date_of_last_inspection_edit = QtGui.QDateEdit(self.tab)
        self.date_of_last_inspection_edit.setEnabled(False)
        self.date_of_last_inspection_edit.setGeometry(QtCore.QRect(45, 205, 171, 22))
        self.date_of_last_inspection_edit.setCalendarPopup(True)
        self.date_of_last_inspection_edit.setObjectName(_fromUtf8("date_of_last_inspection_edit"))
        self.date_of_last_inspection_chbox = QtGui.QCheckBox(self.tab)
        self.date_of_last_inspection_chbox.setGeometry(QtCore.QRect(20, 210, 26, 17))
        self.date_of_last_inspection_chbox.setText(_fromUtf8(""))
        self.date_of_last_inspection_chbox.setObjectName(_fromUtf8("date_of_last_inspection_chbox"))
        self.label_13 = QtGui.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(20, 190, 126, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        self.retranslateUi(DistributionPointDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DistributionPointDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DistributionPointDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DistributionPointDialog)
        DistributionPointDialog.setTabOrder(self.tabWidget, self.dist_point_number_edit)
        DistributionPointDialog.setTabOrder(self.dist_point_number_edit, self.installation_date_chbox)
        DistributionPointDialog.setTabOrder(self.installation_date_chbox, self.installation_date_edit)
        DistributionPointDialog.setTabOrder(self.installation_date_edit, self.inspection_intervall_sbox)
        DistributionPointDialog.setTabOrder(self.inspection_intervall_sbox, self.inspection_intervall_unit_cbox)
        DistributionPointDialog.setTabOrder(self.inspection_intervall_unit_cbox, self.date_of_last_inspection_chbox)
        DistributionPointDialog.setTabOrder(self.date_of_last_inspection_chbox, self.date_of_last_inspection_edit)
        DistributionPointDialog.setTabOrder(self.date_of_last_inspection_edit, self.operating_state_cbox)
        DistributionPointDialog.setTabOrder(self.operating_state_cbox, self.status_change_date_chbox)
        DistributionPointDialog.setTabOrder(self.status_change_date_chbox, self.status_change_date_edit)
        DistributionPointDialog.setTabOrder(self.status_change_date_edit, self.height_sbox)
        DistributionPointDialog.setTabOrder(self.height_sbox, self.network_cbox)

    def retranslateUi(self, DistributionPointDialog):
        DistributionPointDialog.setWindowTitle(_translate("DistributionPointDialog", "Add / Edit Distribution Point", None))
        self.installation_date_edit.setDisplayFormat(_translate("DistributionPointDialog", "yyyy-MM-dd", None))
        self.label_3.setText(_translate("DistributionPointDialog", "Installation Date", None))
        self.label_5.setText(_translate("DistributionPointDialog", "Inspection Interval", None))
        self.label.setText(_translate("DistributionPointDialog", "Distribution Point Number", None))
        self.label_6.setText(_translate("DistributionPointDialog", "Inspection Interval Unit", None))
        self.label_7.setText(_translate("DistributionPointDialog", "Operating State", None))
        self.status_change_date_edit.setDisplayFormat(_translate("DistributionPointDialog", "yyyy-MM-dd", None))
        self.label_8.setText(_translate("DistributionPointDialog", "Date of Status Change", None))
        self.label_14.setText(_translate("DistributionPointDialog", "Height [m]", None))
        self.label_15.setText(_translate("DistributionPointDialog", "Network", None))
        self.date_of_last_inspection_edit.setDisplayFormat(_translate("DistributionPointDialog", "yyyy-MM-dd", None))
        self.label_13.setText(_translate("DistributionPointDialog", "Date of Last Inspection", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DistributionPointDialog", "Description", None))

import resources_rc
