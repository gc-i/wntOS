# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DocumentDialog.ui'
#
# Created: Tue Sep 27 09:09:15 2016
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

class Ui_DocumentDialog(object):
    def setupUi(self, DocumentDialog):
        DocumentDialog.setObjectName(_fromUtf8("DocumentDialog"))
        DocumentDialog.resize(369, 410)
        DocumentDialog.setMinimumSize(QtCore.QSize(369, 410))
        DocumentDialog.setMaximumSize(QtCore.QSize(369, 410))
        self.buttonBox = QtGui.QDialogButtonBox(DocumentDialog)
        self.buttonBox.setGeometry(QtCore.QRect(170, 370, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.filename_edit = QtGui.QLineEdit(DocumentDialog)
        self.filename_edit.setGeometry(QtCore.QRect(35, 40, 266, 20))
        self.filename_edit.setReadOnly(True)
        self.filename_edit.setObjectName(_fromUtf8("filename_edit"))
        self.date_edit = QtGui.QDateEdit(DocumentDialog)
        self.date_edit.setGeometry(QtCore.QRect(35, 165, 141, 22))
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setObjectName(_fromUtf8("date_edit"))
        self.note_edit = QtGui.QPlainTextEdit(DocumentDialog)
        self.note_edit.setGeometry(QtCore.QRect(35, 255, 266, 106))
        self.note_edit.setObjectName(_fromUtf8("note_edit"))
        self.label = QtGui.QLabel(DocumentDialog)
        self.label.setGeometry(QtCore.QRect(35, 25, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(DocumentDialog)
        self.label_2.setGeometry(QtCore.QRect(35, 105, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(DocumentDialog)
        self.label_3.setGeometry(QtCore.QRect(35, 150, 111, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_8 = QtGui.QLabel(DocumentDialog)
        self.label_8.setGeometry(QtCore.QRect(35, 240, 111, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.select_file_button = QtGui.QPushButton(DocumentDialog)
        self.select_file_button.setGeometry(QtCore.QRect(315, 38, 25, 25))
        self.select_file_button.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/wnt/select.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_file_button.setIcon(icon)
        self.select_file_button.setObjectName(_fromUtf8("select_file_button"))
        self.author_cbox = QtGui.QComboBox(DocumentDialog)
        self.author_cbox.setGeometry(QtCore.QRect(35, 120, 266, 22))
        self.author_cbox.setEditable(True)
        self.author_cbox.setObjectName(_fromUtf8("author_cbox"))
        self.label_4 = QtGui.QLabel(DocumentDialog)
        self.label_4.setGeometry(QtCore.QRect(35, 65, 111, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.doc_no_edit = QtGui.QLineEdit(DocumentDialog)
        self.doc_no_edit.setGeometry(QtCore.QRect(35, 80, 266, 20))
        self.doc_no_edit.setReadOnly(False)
        self.doc_no_edit.setObjectName(_fromUtf8("doc_no_edit"))
        self.doc_type_cbox = QtGui.QComboBox(DocumentDialog)
        self.doc_type_cbox.setGeometry(QtCore.QRect(35, 210, 266, 22))
        self.doc_type_cbox.setEditable(False)
        self.doc_type_cbox.setObjectName(_fromUtf8("doc_type_cbox"))
        self.label_5 = QtGui.QLabel(DocumentDialog)
        self.label_5.setGeometry(QtCore.QRect(35, 195, 111, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(DocumentDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DocumentDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DocumentDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DocumentDialog)
        DocumentDialog.setTabOrder(self.filename_edit, self.select_file_button)
        DocumentDialog.setTabOrder(self.select_file_button, self.doc_no_edit)
        DocumentDialog.setTabOrder(self.doc_no_edit, self.author_cbox)
        DocumentDialog.setTabOrder(self.author_cbox, self.date_edit)
        DocumentDialog.setTabOrder(self.date_edit, self.doc_type_cbox)
        DocumentDialog.setTabOrder(self.doc_type_cbox, self.note_edit)

    def retranslateUi(self, DocumentDialog):
        DocumentDialog.setWindowTitle(_translate("DocumentDialog", "Add / Edit Document", None))
        self.date_edit.setDisplayFormat(_translate("DocumentDialog", "yyyy-MM-dd", None))
        self.label.setText(_translate("DocumentDialog", "Filename", None))
        self.label_2.setText(_translate("DocumentDialog", "Author", None))
        self.label_3.setText(_translate("DocumentDialog", "Creation Date", None))
        self.label_8.setText(_translate("DocumentDialog", "Notes", None))
        self.select_file_button.setToolTip(_translate("DocumentDialog", "Select FIle To Upload", None))
        self.label_4.setText(_translate("DocumentDialog", "Document Number", None))
        self.label_5.setText(_translate("DocumentDialog", "Document Type", None))

import resources_rc
