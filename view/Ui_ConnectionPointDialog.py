# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConnectionPointDialog.ui'
#
# Created: Tue Sep 27 09:08:26 2016
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

class Ui_ConnectionPointDialog(object):
    def setupUi(self, ConnectionPointDialog):
        ConnectionPointDialog.setObjectName(_fromUtf8("ConnectionPointDialog"))
        ConnectionPointDialog.resize(588, 360)
        ConnectionPointDialog.setMinimumSize(QtCore.QSize(588, 360))
        ConnectionPointDialog.setMaximumSize(QtCore.QSize(588, 360))
        self.buttonBox = QtGui.QDialogButtonBox(ConnectionPointDialog)
        self.buttonBox.setGeometry(QtCore.QRect(405, 310, 166, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget = QtGui.QTabWidget(ConnectionPointDialog)
        self.tabWidget.setGeometry(QtCore.QRect(15, 10, 556, 281))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.installation_date_edit = QtGui.QDateEdit(self.tab)
        self.installation_date_edit.setEnabled(False)
        self.installation_date_edit.setGeometry(QtCore.QRect(45, 120, 171, 22))
        self.installation_date_edit.setCalendarPopup(True)
        self.installation_date_edit.setObjectName(_fromUtf8("installation_date_edit"))
        self.installation_length_sbox = QtGui.QDoubleSpinBox(self.tab)
        self.installation_length_sbox.setGeometry(QtCore.QRect(20, 75, 196, 22))
        self.installation_length_sbox.setDecimals(1)
        self.installation_length_sbox.setMaximum(500.0)
        self.installation_length_sbox.setObjectName(_fromUtf8("installation_length_sbox"))
        self.installation_date_chbox = QtGui.QCheckBox(self.tab)
        self.installation_date_chbox.setGeometry(QtCore.QRect(20, 125, 26, 17))
        self.installation_date_chbox.setText(_fromUtf8(""))
        self.installation_date_chbox.setObjectName(_fromUtf8("installation_date_chbox"))
        self.conn_point_number_edit = QtGui.QLineEdit(self.tab)
        self.conn_point_number_edit.setGeometry(QtCore.QRect(20, 30, 196, 20))
        self.conn_point_number_edit.setObjectName(_fromUtf8("conn_point_number_edit"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 126, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 105, 126, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 15, 126, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(20, 150, 126, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.conn_point_type_cbox = QtGui.QComboBox(self.tab)
        self.conn_point_type_cbox.setGeometry(QtCore.QRect(20, 165, 196, 22))
        self.conn_point_type_cbox.setObjectName(_fromUtf8("conn_point_type_cbox"))
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(270, 15, 126, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.mounting_type_cbox = QtGui.QComboBox(self.tab)
        self.mounting_type_cbox.setGeometry(QtCore.QRect(270, 30, 196, 22))
        self.mounting_type_cbox.setObjectName(_fromUtf8("mounting_type_cbox"))
        self.label_13 = QtGui.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(270, 60, 126, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.nominal_width_cbox = QtGui.QComboBox(self.tab)
        self.nominal_width_cbox.setGeometry(QtCore.QRect(270, 75, 196, 22))
        self.nominal_width_cbox.setObjectName(_fromUtf8("nominal_width_cbox"))
        self.height_sbox = QtGui.QDoubleSpinBox(self.tab)
        self.height_sbox.setGeometry(QtCore.QRect(270, 120, 196, 22))
        self.height_sbox.setMinimum(-100.0)
        self.height_sbox.setMaximum(2000.0)
        self.height_sbox.setObjectName(_fromUtf8("height_sbox"))
        self.label_14 = QtGui.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(270, 105, 126, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(270, 150, 126, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.network_cbox = QtGui.QComboBox(self.tab)
        self.network_cbox.setGeometry(QtCore.QRect(270, 165, 196, 22))
        self.network_cbox.setObjectName(_fromUtf8("network_cbox"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        self.retranslateUi(ConnectionPointDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ConnectionPointDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ConnectionPointDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConnectionPointDialog)
        ConnectionPointDialog.setTabOrder(self.tabWidget, self.conn_point_number_edit)
        ConnectionPointDialog.setTabOrder(self.conn_point_number_edit, self.installation_length_sbox)
        ConnectionPointDialog.setTabOrder(self.installation_length_sbox, self.installation_date_chbox)
        ConnectionPointDialog.setTabOrder(self.installation_date_chbox, self.installation_date_edit)
        ConnectionPointDialog.setTabOrder(self.installation_date_edit, self.conn_point_type_cbox)
        ConnectionPointDialog.setTabOrder(self.conn_point_type_cbox, self.mounting_type_cbox)
        ConnectionPointDialog.setTabOrder(self.mounting_type_cbox, self.nominal_width_cbox)
        ConnectionPointDialog.setTabOrder(self.nominal_width_cbox, self.height_sbox)
        ConnectionPointDialog.setTabOrder(self.height_sbox, self.network_cbox)

    def retranslateUi(self, ConnectionPointDialog):
        ConnectionPointDialog.setWindowTitle(_translate("ConnectionPointDialog", "Add / Edit Connection Point", None))
        self.installation_date_edit.setDisplayFormat(_translate("ConnectionPointDialog", "yyyy-MM-dd", None))
        self.label_2.setText(_translate("ConnectionPointDialog", "Installation Length [cm]", None))
        self.label_3.setText(_translate("ConnectionPointDialog", "Installation Date", None))
        self.label.setText(_translate("ConnectionPointDialog", "Connection Point Number", None))
        self.label_10.setText(_translate("ConnectionPointDialog", "Connection Point Type", None))
        self.label_11.setText(_translate("ConnectionPointDialog", "Mounting Type", None))
        self.label_13.setText(_translate("ConnectionPointDialog", "Nominal Width", None))
        self.label_14.setText(_translate("ConnectionPointDialog", "Height [m]", None))
        self.label_15.setText(_translate("ConnectionPointDialog", "Network", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ConnectionPointDialog", "Description", None))

import resources_rc
