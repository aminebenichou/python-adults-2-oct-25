import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from functools import partial

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.operation = {
            'number_one': None,
            'number_two': None,
            'operation': '+',
            'result': None
        }
        self.btns = [
            ({'label': '1', 'value':1},
            {'label': '2', 'value':2},
            {'label': '3', 'value':3}),
            ({'label': '4', 'value':4},
            {'label': '5', 'value':5},
            {'label': '6', 'value':6}),
            ({'label': '7', 'value':7},
            {'label': '8', 'value':8},
            {'label': '9', 'value':9}),
            (
                {'label': '0', 'value':0}, 
                {'label': '=', 'value':'='}, 
                {'label': '+', 'value':'+'}, 
                {'label': '-', 'value':'-'}, 
             
             )
        ]
        # TODO: Create numbers buttons and result display
        self.main_layout=QtWidgets.QVBoxLayout(self)
        self.result=QtWidgets.QLabel("Result")
        
        
        self.equal = QtWidgets.QPushButton("=")

        self.main_layout.addWidget(self.result)
        for row in self.btns:
            self.row_layout = QtWidgets.QHBoxLayout()
            for btn in row:
                numberBtn = QtWidgets.QPushButton(btn['label'])
                numberBtn.clicked.connect(partial(self.addNumber, btn['value']))
                self.row_layout.addWidget(numberBtn)
            self.main_layout.addLayout(self.row_layout)
        
        


        self.equal.clicked.connect(self.calculate)

    def addNumber(self, value):
        if value=='=':
            self.calculate()
            return

        if self.operation['number_one']==None :
            self.operation['number_one'] = value  
        else:
            self.operation['number_two'] = value
        print(self.operation)

    def calculate(self):
        result = self.operation['number_one'] + self.operation['number_two']
        self.operation['result'] = result
        self.result.setText(str(result))
        print(self.operation)
        self.operation = {
            'number_one': None,
            'number_two': None,
            'operation': '+',
            'result': None
        }


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(500, 500)
    widget.show()

    sys.exit(app.exec())