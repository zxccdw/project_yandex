import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from math import factorial, sqrt
import sqlite3


class Calc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.st = ""
        self.first = ""
        self.second = ""
        self.flag = False
        self.tochka_first = False
        self.tochka_second = False
        self.znak = ""
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 100, 100)
        self.setWindowTitle('Шестая программа')
        uic.loadUi('untitled.ui', self)
        self.zero.clicked.connect(self.number)
        self.double_zero.clicked.connect(self.number)
        self.one.clicked.connect(self.number)
        self.two.clicked.connect(self.number)
        self.three.clicked.connect(self.number)
        self.four.clicked.connect(self.number)
        self.five.clicked.connect(self.number)
        self.six.clicked.connect(self.number)
        self.seven.clicked.connect(self.number)
        self.eight.clicked.connect(self.number)
        self.nine.clicked.connect(self.number)

        self.plus.clicked.connect(self.operator)
        self.minus.clicked.connect(self.operator)
        self.delenie.clicked.connect(self.operator)
        self.mnozh.clicked.connect(self.operator)
        self.procent.clicked.connect(self.operator)

        self.reset.clicked.connect(self.res)

        self.fact.clicked.connect(self.factor)

        self.tochka.clicked.connect(self.flo)

        self.result.clicked.connect(self.resul)

        self.sqr.clicked.connect(self.sq)

        self.si.clicked.connect(self.sinys)

        self.t.clicked.connect(self.off)

        self.co.clicked.connect(self.cos)

    def number(self):  # +
        self.st += self.sender().text()
        self.label.setText(self.st)
        if self.flag:
            self.second += self.sender().text()
        else:
            self.first += self.sender().text()

    def operator(self):  # +
        if self.flag or self.first == "" or self.znak != "":
            return
        self.flag = True
        if self.sender().text() == "+":
            self.znak = "+"
            self.st += "+"
        elif self.sender().text() == "-":
            self.znak = "-"
            self.st += "-"
        elif self.sender().text() == "/":
            self.znak = "/"
            self.st += "/"
        elif self.sender().text() == "*":
            self.znak = "*"
            self.st += "*"
        elif self.sender().text() == "%":
            self.znak = "%"
            self.st += "%"
        self.label.setText(self.st)

    def res(self, first=""):  # ?
        self.second = ""
        self.flag = False
        self.tochka_first = False
        self.tochka_second = False
        self.znak = ""
        if not first:
            first = ""
        self.first = first
        self.st = first
        if self.first != "":
            self.first = str(round(float(self.first), 2))
            self.tochka_first = True
        self.label.setText(self.first)

    def factor(self):  # +
        if self.flag or self.first == "" or float(self.first) < 0:
            return

        self.first = (float(self.first))
        if self.first < 2147483647:
            self.synchronization("{}!".format(self.first))
            self.get_labels()
            self.first = factorial(self.first)
            self.label.setText(str(self.first))
            self.res(str(self.first))

    def resul(self):  # vrode robit :D
        self.synchronization(self.st)
        self.get_labels()
        if self.znak == "+":
            self.first = str(float(self.first) + float(self.second))
            self.label.setText(self.first)
            self.st = self.first
            self.res(self.first)
        if self.znak == "-":
            self.first = str(float(self.first) - float(self.second))
            self.label.setText(self.first)
            self.st = self.first
            self.res(self.first)
        if self.znak == "*":
            self.first = str(float(self.first) * float(self.second))
            self.label.setText(self.first)
            self.st = self.first
            self.res(self.first)
        elif self.znak == "/" or self.znak == "%":
            if float(self.second) != 0:
                if self.znak == "/":
                    self.first = str(float(self.first) / float(self.second))
                    self.label.setText(self.first)
                    self.st = self.first
                    self.res(self.first)
                else:
                    self.first = str(float(self.first) % float(self.second))
                    self.label.setText(self.first)
                    self.st = self.first
                    self.res(self.first)
            else:
                self.label.setText("ERROR")
                self.res()

    def flo(self):  # +
        if not self.flag and not self.tochka_first and self.first != "":
            self.first += "."
            self.st += "."
            self.tochka_first = True
        elif self.flag and not self.tochka_second and self.second != "":
            self.st += "."
            self.second += "."
            self.tochka_second = True
        self.label.setText(self.st)

    def sq(self):  # +
        if self.flag or self.first == "" or float(self.first) < 0:
            return

        self.synchronization("sqrt({})".format(self.first))
        self.get_labels()
        self.first = round(sqrt(float(self.first)), 2)
        self.label.setText(str(self.first))
        self.res(str(self.first))

    def sinys(self):
        if self.flag or self.first == "":
            return
        self.flag = True
        self.first = int(float(self.first))
        if self.first < 1 or self.first > 180:
            return
        self.synchronization("sin({})".format(self.first))
        self.get_labels()
        if self.first > 90:
            self.first = 180 - self.first
        self.label.setText(str(bradis_sin[self.first]))
        self.res(str(bradis_sin[self.first]))

    def off(self):
        sys.exit()

    def synchronization(self, st):
        con = sqlite3.connect(name)  # hello.db
        cur = con.cursor()
        cur.execute("""
        UPDATE results
        SET result = (SELECT result FROM results WHERE id = 2)
        WHERE id = 1""").fetchall()
        cur.execute("""
         UPDATE results
         SET result = '{}'
         WHERE id = 2""".format(st)).fetchall()
        con.commit()
        con.close()

    def get_labels(self):
        con = sqlite3.connect(name)  # hello.db
        cur = con.cursor()
        res_first = cur.execute("""
        SELECT result FROM results WHERE id = 1
        """).fetchall()
        res_second = cur.execute("""
        SELECT result FROM results WHERE id = 2""").fetchall()
        self.label_first.setText(str(res_first[0][0]))
        self.label_second.setText(str(res_second[0][0]))
        con.commit()
        con.close()

    def cos(self):
        if self.flag or self.first == "":
            return
        self.first = int(float(self.first))
        if self.first < 1 or self.first > 180:
            return
        self.synchronization("cos({})".format(self.first))
        self.get_labels()
        self.flag = True
        k = 1
        if self.first > 90:
            self.first = 180 - self.first
            k = -1
        self.label.setText(str(k * bradis_cos[self.first]))
        self.res(str(k * bradis_cos[self.first]))


name = "hello.db"

bradis_sin = dict()
bradis_sin[0] = 0
bradis_sin[1] = 0.0175
bradis_sin[2] = 0.0349
bradis_sin[3] = 0.0523
bradis_sin[4] = 0.0698
bradis_sin[5] = 0.0872
bradis_sin[6] = 0.1045
bradis_sin[7] = 0.1219
bradis_sin[8] = 0.1392
bradis_sin[9] = 0.1564
bradis_sin[10] = 0.1736
bradis_sin[11] = 0.1908
bradis_sin[12] = 0.2079
bradis_sin[13] = 0.2250
bradis_sin[14] = 0.2419
bradis_sin[15] = 0.2588
bradis_sin[16] = 0.2756
bradis_sin[17] = 0.2924
bradis_sin[18] = 0.3090
bradis_sin[19] = 0.3256
bradis_sin[20] = 0.3420
bradis_sin[21] = 0.3584
bradis_sin[22] = 0.3746
bradis_sin[23] = 0.3907
bradis_sin[24] = 0.4067
bradis_sin[25] = 0.4226
bradis_sin[26] = 0.4384
bradis_sin[27] = 0.4540
bradis_sin[28] = 0.4695
bradis_sin[29] = 0.4848
bradis_sin[30] = 0.5000
bradis_sin[31] = 0.5150
bradis_sin[32] = 0.5299
bradis_sin[33] = 0.5446
bradis_sin[34] = 0.5592
bradis_sin[35] = 0.5736
bradis_sin[36] = 0.5878
bradis_sin[37] = 0.6018
bradis_sin[38] = 0.6157
bradis_sin[39] = 0.6293
bradis_sin[40] = 0.6428
bradis_sin[41] = 0.6561
bradis_sin[42] = 0.6691
bradis_sin[43] = 0.6820
bradis_sin[44] = 0.6947
bradis_sin[45] = 0.7071
bradis_sin[46] = 0.7193
bradis_sin[47] = 0.7314
bradis_sin[48] = 0.7431
bradis_sin[49] = 0.7547
bradis_sin[50] = 0.7660
bradis_sin[51] = 0.7771
bradis_sin[52] = 0.7880
bradis_sin[53] = 0.7986
bradis_sin[54] = 0.8090
bradis_sin[55] = 0.8192
bradis_sin[56] = 0.8290
bradis_sin[57] = 0.8387
bradis_sin[58] = 0.8480
bradis_sin[59] = 0.8572
bradis_sin[60] = 0.8660
bradis_sin[61] = 0.8746
bradis_sin[62] = 0.8829
bradis_sin[63] = 0.8910
bradis_sin[64] = 0.8988
bradis_sin[65] = 0.9063
bradis_sin[66] = 0.9135
bradis_sin[67] = 0.9205
bradis_sin[68] = 0.9272
bradis_sin[69] = 0.9336
bradis_sin[70] = 0.9397
bradis_sin[71] = 0.9455
bradis_sin[72] = 0.9511
bradis_sin[73] = 0.9553
bradis_sin[74] = 0.9613
bradis_sin[75] = 0.9659
bradis_sin[76] = 0.9703
bradis_sin[77] = 0.9744
bradis_sin[78] = 0.9781
bradis_sin[79] = 0.9816
bradis_sin[80] = 0.9848
bradis_sin[81] = 0.9877
bradis_sin[82] = 0.9903
bradis_sin[83] = 0.9925
bradis_sin[84] = 0.9945
bradis_sin[85] = 0.9962
bradis_sin[86] = 0.9976
bradis_sin[87] = 0.9986
bradis_sin[88] = 0.9994
bradis_sin[89] = 0.9998
bradis_sin[90] = 1.0000

bradis_cos = dict()
bradis_cos[0] = 1
bradis_cos[1] = 0.9998
bradis_cos[2] = 0.9994
bradis_cos[3] = 0.9996
bradis_cos[4] = 0.9976
bradis_cos[5] = 0.9962
bradis_cos[6] = 0.9945
bradis_cos[7] = 0.9925
bradis_cos[8] = 0.9903
bradis_cos[9] = 0.9877
bradis_cos[10] = 0.9848
bradis_cos[11] = 0.9816
bradis_cos[12] = 0.9781
bradis_cos[13] = 0.9744
bradis_cos[14] = 0.9703
bradis_cos[15] = 0.9659
bradis_cos[16] = 0.9613
bradis_cos[17] = 0.9563
bradis_cos[18] = 0.9511
bradis_cos[19] = 0.9455
bradis_cos[20] = 0.9397
bradis_cos[21] = 0.9336
bradis_cos[22] = 0.9272
bradis_cos[23] = 0.9205
bradis_cos[24] = 0.9135
bradis_cos[25] = 0.9063
bradis_cos[26] = 0.8988
bradis_cos[27] = 0.8910
bradis_cos[28] = 0.8829
bradis_cos[29] = 0.8746
bradis_cos[30] = 0.8660
bradis_cos[31] = 0.8572
bradis_cos[32] = 0.8480
bradis_cos[33] = 0.8387
bradis_cos[34] = 0.8290
bradis_cos[35] = 0.8192
bradis_cos[36] = 0.8090
bradis_cos[37] = 0.7986
bradis_cos[38] = 0.7880
bradis_cos[39] = 0.7771
bradis_cos[40] = 0.7660
bradis_cos[41] = 0.7547
bradis_cos[42] = 0.7431
bradis_cos[43] = 0.7314
bradis_cos[44] = 0.7193
bradis_cos[45] = 0.7071
bradis_cos[46] = 0.6947
bradis_cos[47] = 0.6820
bradis_cos[48] = 0.6691
bradis_cos[49] = 0.6561
bradis_cos[50] = 0.6428
bradis_cos[51] = 0.6293
bradis_cos[52] = 0.6157
bradis_cos[53] = 0.6018
bradis_cos[54] = 0.5878
bradis_cos[55] = 0.5736
bradis_cos[56] = 0.5592
bradis_cos[57] = 0.5446
bradis_cos[58] = 0.5299
bradis_cos[59] = 0.5150
bradis_cos[60] = 0.5000
bradis_cos[61] = 0.4848
bradis_cos[62] = 0.4695
bradis_cos[63] = 0.4540
bradis_cos[64] = 0.4384
bradis_cos[65] = 0.4226
bradis_cos[66] = 0.4067
bradis_cos[67] = 0.3907
bradis_cos[68] = 0.3746
bradis_cos[69] = 0.3584
bradis_cos[70] = 0.3420
bradis_cos[71] = 0.3256
bradis_cos[72] = 0.3090
bradis_cos[73] = 0.2924
bradis_cos[74] = 0.2756
bradis_cos[75] = 0.2588
bradis_cos[76] = 0.2419
bradis_cos[77] = 0.2250
bradis_cos[78] = 0.2079
bradis_cos[79] = 0.1908
bradis_cos[80] = 0.1736
bradis_cos[81] = 0.1564
bradis_cos[82] = 0.1392
bradis_cos[83] = 0.1219
bradis_cos[84] = 0.1045
bradis_cos[85] = 0.0872
bradis_cos[86] = 0.0698
bradis_cos[87] = 0.0523
bradis_cos[88] = 0.0349
bradis_cos[89] = 0.0175
bradis_cos[90] = 0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calc()
    ex.show()
    sys.exit(app.exec())
