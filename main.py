from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout, QPlainTextEdit, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6 import QtCore, QtGui, QtWidgets

from matrix import MatrixFunc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(1100, 530)
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("background-color: rgb(56, 62, 84);\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input2 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.input2.setGeometry(QtCore.QRect(750, 10, 340, 250))
        self.input2.setStyleSheet("background-color: rgb(28, 33, 52);\n"
                                  "    border-radius: 10px;\n"
                                  "    font-size: 20px;\n"
                                  "    padding: 5px;\n"
                                  "    color: #f3f3f3;\n"
                                  "\n"
                                  "")
        self.input2.setPlainText("")
        self.input2.setOverwriteMode(False)
        self.input2.setBackgroundVisible(False)
        self.input2.setObjectName("input2")
        self.input1 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.input1.setGeometry(QtCore.QRect(10, 10, 340, 250))
        self.input1.setStyleSheet("    background-color: rgb(28, 33, 52);\n"
                                  "    border-radius: 10px;\n"
                                  "    font-size: 20px;\n"
                                  "    padding: 5px;\n"
                                  "    color: #f3f3f3;")
        self.input1.setPlainText("")
        self.input1.setCenterOnScroll(False)
        self.input1.setObjectName("input1")
        self.result = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.result.setEnabled(True)
        self.result.setGeometry(QtCore.QRect(380, 260, 340, 250))
        self.result.setStyleSheet("    background-color: rgb(36, 41, 61);\n"
                                  "    border-radius: 10px;\n"
                                  "    font-size: 20px;\n"
                                  "    padding: 5px;\n"
                                  "    color: #f3f3f3;")
        self.result.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.result.setReadOnly(True)
        self.result.setPlainText("")
        self.result.setCursorWidth(1)
        self.result.setBackgroundVisible(False)
        self.result.setCenterOnScroll(False)
        self.result.setObjectName("result")
        self.AdditionBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.AdditionBtn.setGeometry(QtCore.QRect(510, 10, 100, 32))
        self.AdditionBtn.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(52, 80, 175);\n"
                                       "    color: white;\n"
                                       "    border-radius: 10px;\n"
                                       "    font-size: 20px;\n"
                                       "    font-family: \"Nunito Sans\", sans-serif;\n"
                                       "    border: 2px solid;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(26, 44, 105);\n"
                                       "    color: white;\n"
                                       "    border: 2px solid;\n"
                                       "}")
        self.AdditionBtn.setObjectName("AdditionBtn")
        self.SubtractionBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SubtractionBtn.setGeometry(QtCore.QRect(510, 50, 100, 32))
        self.SubtractionBtn.setStyleSheet("QPushButton {\n"
                                          "    background-color: rgb(52, 80, 175);\n"
                                          "    color: white;\n"
                                          "    border-radius: 10px;\n"
                                          "    font-size: 20px;\n"
                                          "    font-family: \"Nunito Sans\", sans-serif;\n"
                                          "    border: 2px solid;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover{\n"
                                          "    background-color: rgb(26, 44, 105);\n"
                                          "    color: white;\n"
                                          "    border: 2px solid;\n"
                                          "}")
        self.SubtractionBtn.setObjectName("SubtractionBtn")
        self.MultiplyBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.MultiplyBtn.setGeometry(QtCore.QRect(510, 90, 100, 32))
        self.MultiplyBtn.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(52, 80, 175);\n"
                                       "    color: white;\n"
                                       "    border-radius: 10px;\n"
                                       "    font-size: 20px;\n"
                                       "    font-family: \"Nunito Sans\", sans-serif;\n"
                                       "    border: 2px solid;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "    background-color: rgb(26, 44, 105);\n"
                                       "    color: white;\n"
                                       "    border: 2px solid;\n"
                                       "}")
        self.MultiplyBtn.setObjectName("MultiplyBtn")
        self.DeterminantBnt = QtWidgets.QPushButton(parent=self.centralwidget)
        self.DeterminantBnt.setGeometry(QtCore.QRect(10, 310, 280, 40))
        self.DeterminantBnt.setStyleSheet("QPushButton {\n"
                                          "    background-color: rgb(52, 80, 175);\n"
                                          "    color: white;\n"
                                          "    border-radius: 10px;\n"
                                          "    font-size: 20px;\n"
                                          "    font-family: \"Nunito Sans\", sans-serif;\n"
                                          "    border: 2px solid;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover{\n"
                                          "    background-color: rgb(26, 44, 105);\n"
                                          "    color: white;\n"
                                          "    border: 2px solid;\n"
                                          "}")
        self.DeterminantBnt.setObjectName("DeterminantBnt")
        self.DeterminantBnt2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.DeterminantBnt2.setGeometry(QtCore.QRect(740, 310, 280, 40))
        self.DeterminantBnt2.setStyleSheet("QPushButton {\n"
                                           "    background-color: rgb(52, 80, 175);\n"
                                           "    color: white;\n"
                                           "    border-radius: 10px;\n"
                                           "    font-size: 20px;\n"
                                           "    font-family: \"Nunito Sans\", sans-serif;\n"
                                           "    border: 2px solid;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover{\n"
                                           "    background-color: rgb(26, 44, 105);\n"
                                           "    color: white;\n"
                                           "    border: 2px solid;\n"
                                           "}")
        self.DeterminantBnt2.setObjectName("DeterminantBnt2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, 260, 400, 50))
        self.label.setStyleSheet("font-size: 25px;\n"
                                 "font-family: \'Nunito Sans\', serif;\n"
                                 "    color: white;\n"
                                 "\n"
                                 "")
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(720, 260, 400, 50))
        self.label_2.setStyleSheet("font-size: 25px;\n"
                                   "font-family: \'Nunito Sans\', serif;\n"
                                   "    color: white;\n"
                                   "\n"
                                   "")
        self.label_2.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.intInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.intInput.setPlaceholderText('Число')
        self.intInput.setGeometry(QtCore.QRect(260, 360, 100, 40))
        self.intInput.setStyleSheet("    background-color: rgb(28, 33, 52);\n"
                                    "    border-radius: 10px;\n"
                                    "    font-size: 20px;\n"
                                    "    padding: 5px;\n"
                                    "    color: #f3f3f3;")
        self.intInput.setObjectName("intInput")
        self.MultiplyToIntBtn2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.MultiplyToIntBtn2.setGeometry(QtCore.QRect(740, 360, 241, 40))
        self.MultiplyToIntBtn2.setStyleSheet("QPushButton {\n"
                                             "    background-color: rgb(52, 80, 175);\n"
                                             "    color: white;\n"
                                             "    border-radius: 10px;\n"
                                             "    font-size: 20px;\n"
                                             "    font-family: \"Nunito Sans\", sans-serif;\n"
                                             "    border: 2px solid;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover{\n"
                                             "    background-color: rgb(26, 44, 105);\n"
                                             "    color: white;\n"
                                             "    border: 2px solid;\n"
                                             "}")
        self.MultiplyToIntBtn2.setObjectName("MultiplyToIntBtn2")
        self.intInput2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.intInput2.setPlaceholderText('Число')
        self.intInput2.setGeometry(QtCore.QRect(990, 360, 100, 40))
        self.intInput2.setStyleSheet("    background-color: rgb(28, 33, 52);\n"
                                     "    border-radius: 10px;\n"
                                     "    font-size: 20px;\n"
                                     "    padding: 5px;\n"
                                     "    color: #f3f3f3;")
        self.intInput2.setObjectName("intInput2")

        self.MultiplyToIntBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.MultiplyToIntBtn.setGeometry(QtCore.QRect(10, 360, 241, 40))
        self.MultiplyToIntBtn.setStyleSheet("QPushButton {\n"
                                            "    background-color: rgb(52, 80, 175);\n"
                                            "    color: white;\n"
                                            "    border-radius: 10px;\n"
                                            "    font-size: 20px;\n"
                                            "    font-family: \"Nunito Sans\", sans-serif;\n"
                                            "    border: 2px solid;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "    background-color: rgb(26, 44, 105);\n"
                                            "    color: white;\n"
                                            "    border: 2px solid;\n"
                                            "}")
        self.MultiplyToIntBtn.setObjectName("MultiplyToIntBtn")
        self.TransposeBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.TransposeBtn.setGeometry(QtCore.QRect(10, 410, 280, 40))
        self.TransposeBtn.setStyleSheet("QPushButton {\n"
                                        "    background-color: rgb(52, 80, 175);\n"
                                        "    color: white;\n"
                                        "    border-radius: 10px;\n"
                                        "    font-size: 20px;\n"
                                        "    font-family: \"Nunito Sans\", sans-serif;\n"
                                        "    border: 2px solid;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(26, 44, 105);\n"
                                        "    color: white;\n"
                                        "    border: 2px solid;\n"
                                        "}")
        self.TransposeBtn.setObjectName("TransposeBtn")
        self.TransposeBtn2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.TransposeBtn2.setGeometry(QtCore.QRect(740, 410, 280, 40))
        self.TransposeBtn2.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(52, 80, 175);\n"
                                         "    color: white;\n"
                                         "    border-radius: 10px;\n"
                                         "    font-size: 20px;\n"
                                         "    font-family: \"Nunito Sans\", sans-serif;\n"
                                         "    border: 2px solid;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "    background-color: rgb(26, 44, 105);\n"
                                         "    color: white;\n"
                                         "    border: 2px solid;\n"
                                         "}")
        self.TransposeBtn2.setObjectName("TransposeBtn2")
        self.ClearBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ClearBtn.setGeometry(QtCore.QRect(510, 220, 100, 32))
        self.ClearBtn.setStyleSheet("QPushButton {\n"
                                    "    background-color: #cc4040;\n"
                                    "    color: white;\n"
                                    "    border-radius: 10px;\n"
                                    "    font-size: 20px;\n"
                                    "    font-family: \"Nunito Sans\", sans-serif;\n"
                                    "    border: 2px solid;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: #832727;\n"
                                    "    color: white;\n"
                                    "    border: 2px solid;\n"
                                    "}")
        self.ClearBtn.setObjectName("TransposeBtn2")
        self.AdditionBtn.raise_()
        self.SubtractionBtn.raise_()
        self.MultiplyBtn.raise_()
        self.DeterminantBnt.raise_()
        self.DeterminantBnt2.raise_()
        self.intInput2.raise_()
        self.MultiplyToIntBtn.raise_()
        self.TransposeBtn.raise_()
        self.TransposeBtn2.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.input2.raise_()
        self.input1.raise_()
        self.result.raise_()
        self.intInput.raise_()
        self.MultiplyToIntBtn2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.AdditionBtn.clicked.connect(self.AdditionBtnClick)
        self.SubtractionBtn.clicked.connect(self.SubtractionClick)
        self.MultiplyBtn.clicked.connect(self.MultiplyClick)
        self.DeterminantBnt.clicked.connect(self.DeterminantClick)
        self.DeterminantBnt2.clicked.connect(self.Determinant2Click)
        self.TransposeBtn.clicked.connect(self.TransposeClick)
        self.TransposeBtn.clicked.connect(self.Transpose2Click)
        self.MultiplyToIntBtn.clicked.connect(self.MultiplyToIntClick)
        self.MultiplyToIntBtn2.clicked.connect(self.MultiplyToInt2Click)
        self.ClearBtn.clicked.connect(self.ClearClick)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор Матриц"))
        self.input2.setPlaceholderText(_translate("MainWindow", "Введите матрицу"))
        self.input1.setPlaceholderText(_translate("MainWindow", "Введите матрицу"))
        self.result.setPlaceholderText(_translate("MainWindow", "Результат"))
        self.AdditionBtn.setText(_translate("MainWindow", "A + B"))
        self.SubtractionBtn.setText(_translate("MainWindow", "A - B"))
        self.MultiplyBtn.setText(_translate("MainWindow", "A * B"))
        self.DeterminantBnt.setText(_translate("MainWindow", "Найти определитель \'А\'"))
        self.DeterminantBnt2.setText(_translate("MainWindow", "Найти определитель \'Б\'"))
        self.label.setText(_translate("MainWindow", "Матрица А"))
        self.label_2.setText(_translate("MainWindow", "Матрица Б"))
        self.MultiplyToIntBtn2.setText(_translate("MainWindow", "Умножить \'Б\' на число"))
        self.MultiplyToIntBtn.setText(_translate("MainWindow", "Умножить \'А\' на число"))
        self.TransposeBtn.setText(_translate("MainWindow", "Транспонировать \'А\'"))
        self.TransposeBtn2.setText(_translate("MainWindow", "Транспонировать \'Б\'"))
        self.ClearBtn.setText(_translate("MainWindow", "Очистить"))

    def ClearClick(self, checked):
        self.result.setPlainText("")

    def AdditionBtnClick(self, checked):
        try:
            mtrixA = [[int(x) for x in y] for y in [x.split(" ") for x in self.input1.toPlainText().split("\n")]]
            mtrixB = [[int(x) for x in y] for y in [x.split(" ") for x in self.input2.toPlainText().split("\n")]]

            matrix_a = MatrixFunc(len(mtrixA), len(mtrixA[0]))
            matrix_a.create(mtrixA)

            matrix_b = MatrixFunc(len(mtrixB), len(mtrixB[0]))
            matrix_b.create(mtrixB)

            self.result.setPlainText("\n".join([" ".join([str(x) for x in y]) for y in matrix_a.addition(matrix_b)]))

        except Exception as error:
            QMessageBox.about(MainWindow, "Error", "Произошла ошибка, попробуйте снова")
            print(error)

    def SubtractionClick(self, checked):
        try:
            mtrixA = [[int(x) for x in y] for y in [x.split(" ") for x in self.input1.toPlainText().split("\n")]]
            mtrixB = [[int(x) for x in y] for y in [x.split(" ") for x in self.input2.toPlainText().split("\n")]]

            matrix_a = MatrixFunc(len(mtrixA), len(mtrixA[0]))
            matrix_a.create(mtrixA)

            matrix_b = MatrixFunc(len(mtrixB), len(mtrixB[0]))
            matrix_b.create(mtrixB)

            self.result.setPlainText("\n".join([" ".join([str(x) for x in y]) for y in matrix_a.subtraction(matrix_b)]))

        except Exception as error:
            QMessageBox.about(MainWindow, "Error", "Произошла ошибка, попробуйте снова")
            print(error)

    def MultiplyClick(self, checked):
        try:
            mtrixA = [[int(x) for x in y] for y in [x.split(" ") for x in self.input1.toPlainText().split("\n")]]
            mtrixB = [[int(x) for x in y] for y in [x.split(" ") for x in self.input2.toPlainText().split("\n")]]

            matrix_a = MatrixFunc(len(mtrixA), len(mtrixA[0]))
            matrix_a.create(mtrixA)

            matrix_b = MatrixFunc(len(mtrixB), len(mtrixB[0]))
            matrix_b.create(mtrixB)

            if len(mtrixA) != len(mtrixB):
                QMessageBox.about(MainWindow, "Error", "Матрицы должны быть одного размера")
                return 0
            self.result.setPlainText(
                "\n".join([" ".join([str(x) for x in y]) for y in matrix_a.multiply_matrices(matrix_b)]))

        except Exception as error:
            QMessageBox.about(MainWindow, "Error", "Произошла ошибка, попробуйте снова")
            print(error)

    def DeterminantClick(self, checked):
        try:
            mtrixA = [[int(x) for x in y] for y in [x.split(" ") for x in self.input1.toPlainText().split("\n")]]

            matrix_a = MatrixFunc(len(mtrixA), len(mtrixA[0]))
            matrix_a.create(mtrixA)

            self.result.setPlainText(str(matrix_a.determinant(matrix_a.matrix)))

        except Exception as error:
            QMessageBox.about(MainWindow, "Error", "Произошла ошибка, попробуйте снова")
            print(error)

    def Determinant2Click(self, checked):
        try:
            mtrixA = [[int(x) for x in y] for y in [x.split(" ") for x in self.input2.toPlainText().split("\n")]]

            matrix_a = MatrixFunc(len(mtrixA), len(mtrixA[0]))
            matrix_a.create(mtrixA)

            self.result.setPlainText(str(matrix_a.determinant(matrix_a.matrix)))

        except Exception as error:
            QMessageBox.about(MainWindow, "Error", "Произошла ошибка, попробуйте снова")
            print(error)

    def TransposeClick(self, checked):
        try:
            mtrixA = [[int(x) for x in y] for y in [x.split(" ") for x in self.input1.toPlainText().split("\n")]]

            matrix_a = MatrixFunc(len(mtrixA), len(mtrixA[0]))
            matrix_a.create(mtrixA)

            self.result.setPlainText("\n".join([" ".join([str(x) for x in y]) for y in matrix_a.transpose()]))

        except Exception as error:
            QMessageBox.about(MainWindow, "Error", "Произошла ошибка, попробуйте снова")
            print(error)

    def Transpose2Click(self, checked):
        try:
            mtrixA = [[int(x) for x in y] for y in [x.split(" ") for x in self.input2.toPlainText().split("\n")]]

            matrix_a = MatrixFunc(len(mtrixA), len(mtrixA[0]))
            matrix_a.create(mtrixA)

            self.result.setPlainText("\n".join([" ".join([str(x) for x in y]) for y in matrix_a.transpose()]))

        except Exception as error:
            QMessageBox.about(MainWindow, "Error", "Произошла ошибка, попробуйте снова")
            print(error)

    def MultiplyToIntClick(self, checked):
        try:
            mtrixA = [[int(x) for x in y] for y in [x.split(" ") for x in self.input1.toPlainText().split("\n")]]

            matrix_a = MatrixFunc(len(mtrixA), len(mtrixA[0]))
            matrix_a.create(mtrixA)

            self.result.setPlainText(
                "\n".join(
                    [" ".join([str(x) for x in y]) for y in matrix_a.multiply(int(self.intInput.text()))]))

        except Exception as error:
            QMessageBox.about(MainWindow, "Error", "Произошла ошибка, попробуйте снова")
            print(error)

    def MultiplyToInt2Click(self, checked):
        try:
            mtrixA = [[int(x) for x in y] for y in [x.split(" ") for x in self.input2.toPlainText().split("\n")]]

            matrix_a = MatrixFunc(len(mtrixA), len(mtrixA[0]))
            matrix_a.create(mtrixA)

            self.result.setPlainText(
                "\n".join(
                    [" ".join([str(x) for x in y]) for y in matrix_a.multiply(int(self.intInput2.text()))]))

        except Exception as error:
            QMessageBox.about(MainWindow, "Error", "Произошла ошибка, попробуйте снова")
            print(error)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
