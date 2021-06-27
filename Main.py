#----------------Kütüphane---------------#
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from AnaSayfaUI import *
#----------------------------------------#

#----------------Uygulama Oluşturma---------------#
Uygulama = QApplication(sys.argv)
penAna = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()


sys.exit(Uygulama.exec_())
#-------------------------------------------------#


#----------------Veritabanı Oluşturma---------------#
import sqlite3

global curs
global connection
connection = sqlite3.connect('spor.db')
curs = connection.cursor()
sorguCreateTblSpor = ("CREATE TABLE IF NOT EXISTS spor (   \
                        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,  \
                        TCNo TEXT NOT NULL UNIQUE,  \
                        SporcuAdi TEXT NOT NULL,    \
                        SporcuSoyAdi TEXT NOT NULL,  \
                        KulupAdi TEXT NOT NULL,  \
                        Brans TEXT NOT NULL,   \
                        Cinsiyet TEXT NOT NULL,  \
                        DTarihi TEXT NOT NULL,    \
                        MHal TEXT NOT NULL,   \
                        Kilo TEXT NOT NULL)")
curs.execute(sorguCreateTblSpor)
connection.commit()

#-------------------------------------------------#


#-------------------Kaydet------------------------#
def Ekle():
    _lneTCK = ui.lneTCK.text()
    _lneSporcuAdi = ui.lneSporcuAdi.text()
    _lneSporcuSoyadi= ui.lneSporcuSoyadi.text()
    _cmbSporKulubu= ui.cmbSporKulubu.currentText()
    _lwBrans= ui.lwBrans.currentItem().text()
    _cmbCinsiyet= ui.cmbCinsiyet.currentText()
    _cwDTarihi= ui.cwDTarihi.selectedDate().toString(QtCore.Qt.DateFormat.ISODate)
    if ui.chkMedeniHal.isChecked():
        _medeniHal = "Evli"
    else:
        _medeniHal = "Bekar"
    _spnKilo= ui.spnKilo.value()


    curs.execute("INSERT INTO spor (TCNo,SporcuAdi,SporcuSoyAdi,KulupAdi,Brans,Cinsiyet,DTarihi,MHal,Kilo)  VALUES (?,?,?,?,?,?,?,?,?)", (_lneTCK,_lneSporcuAdi,_lneSporcuSoyadi,_cmbSporKulubu,_lwBrans,_cmbCinsiyet,_cwDTarihi,_medeniHal,_spnKilo))
    connection.commit()

#-------------------------------------------------#


#---------------------Sinyal-Slot------------------#
ui.btnEkle.clicked.connect(Ekle)

#-------------------------------------------------#




