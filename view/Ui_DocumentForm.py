# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DocumentForm.ui'
#
# Created: Tue Oct 04 20:07:31 2016
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

class Ui_DocumentForm(object):
    def setupUi(self, DocumentForm):
        DocumentForm.setObjectName(_fromUtf8("DocumentForm"))
        DocumentForm.resize(548, 200)
        self.doc_twidget = QtGui.QTableWidget(DocumentForm)
        self.doc_twidget.setGeometry(QtCore.QRect(15, 25, 496, 151))
        self.doc_twidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.doc_twidget.setAlternatingRowColors(True)
        self.doc_twidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.doc_twidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.doc_twidget.setObjectName(_fromUtf8("doc_twidget"))
        self.doc_twidget.setColumnCount(6)
        self.doc_twidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.doc_twidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.doc_twidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.doc_twidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.doc_twidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.doc_twidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.doc_twidget.setHorizontalHeaderItem(5, item)
        self.label_18 = QtGui.QLabel(DocumentForm)
        self.label_18.setGeometry(QtCore.QRect(15, 10, 66, 16))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.add_doc_button = QtGui.QPushButton(DocumentForm)
        self.add_doc_button.setGeometry(QtCore.QRect(515, 25, 25, 25))
        self.add_doc_button.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/wnt/plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_doc_button.setIcon(icon)
        self.add_doc_button.setObjectName(_fromUtf8("add_doc_button"))
        self.edit_doc_button = QtGui.QPushButton(DocumentForm)
        self.edit_doc_button.setGeometry(QtCore.QRect(515, 55, 25, 25))
        self.edit_doc_button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/wnt/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_doc_button.setIcon(icon1)
        self.edit_doc_button.setObjectName(_fromUtf8("edit_doc_button"))
        self.view_doc_button = QtGui.QPushButton(DocumentForm)
        self.view_doc_button.setGeometry(QtCore.QRect(515, 115, 25, 25))
        self.view_doc_button.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/wnt/eye.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.view_doc_button.setIcon(icon2)
        self.view_doc_button.setObjectName(_fromUtf8("view_doc_button"))
        self.delete_doc_button = QtGui.QPushButton(DocumentForm)
        self.delete_doc_button.setGeometry(QtCore.QRect(515, 85, 25, 25))
        self.delete_doc_button.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/wnt/minus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_doc_button.setIcon(icon3)
        self.delete_doc_button.setObjectName(_fromUtf8("delete_doc_button"))

        self.retranslateUi(DocumentForm)
        QtCore.QMetaObject.connectSlotsByName(DocumentForm)
        DocumentForm.setTabOrder(self.doc_twidget, self.add_doc_button)
        DocumentForm.setTabOrder(self.add_doc_button, self.edit_doc_button)
        DocumentForm.setTabOrder(self.edit_doc_button, self.delete_doc_button)
        DocumentForm.setTabOrder(self.delete_doc_button, self.view_doc_button)

    def retranslateUi(self, DocumentForm):
        DocumentForm.setWindowTitle(_translate("DocumentForm", "Form", None))
        item = self.doc_twidget.horizontalHeaderItem(0)
        item.setText(_translate("DocumentForm", "Doc No.", None))
        item = self.doc_twidget.horizontalHeaderItem(1)
        item.setText(_translate("DocumentForm", "Creation Date", None))
        item = self.doc_twidget.horizontalHeaderItem(2)
        item.setText(_translate("DocumentForm", "Author", None))
        item = self.doc_twidget.horizontalHeaderItem(3)
        item.setText(_translate("DocumentForm", "File Name", None))
        item = self.doc_twidget.horizontalHeaderItem(4)
        item.setText(_translate("DocumentForm", "Doc Type", None))
        item = self.doc_twidget.horizontalHeaderItem(5)
        item.setText(_translate("DocumentForm", "Note", None))
        self.label_18.setText(_translate("DocumentForm", "Documents", None))
        self.add_doc_button.setToolTip(_translate("DocumentForm", "Add Document", None))
        self.edit_doc_button.setToolTip(_translate("DocumentForm", "View/Edit Document Details", None))
        self.view_doc_button.setToolTip(_translate("DocumentForm", "View Document", None))
        self.delete_doc_button.setToolTip(_translate("DocumentForm", "Delete Document", None))

import resources_rc
