import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from manageDb import *

class TodoApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        create_table("tasks", [
            ("title", "TEXT"),
            ("desc", "TEXT"),
            ("status", "INTEGER NOT NULL CHECK (status IN (0, 1)) DEFAULT 0")
        ])
        self.main_layout = QtWidgets.QHBoxLayout(self)        
        self.main_layout.addLayout(self.left_side())
    
    def left_side(self):
        layout = QtWidgets.QVBoxLayout(self)
        self.title_input_field= QtWidgets.QLineEdit(self, placeholderText="Title of task")
        
        self.desc_input_field= QtWidgets.QTextEdit(self, placeholderText="Description of task")
        self.desc_input_field.setFixedHeight(300)

        save_btn=QtWidgets.QPushButton(self, text="Add Task")
        save_btn.clicked.connect(self.save_task)

        layout.addWidget(self.title_input_field)
        layout.addWidget(self.desc_input_field)
        layout.addWidget(save_btn)

        return layout

    def save_task(self):
        title_value= self.title_input_field.text()
        desc_value = self.desc_input_field.toPlainText()

        create_element('tasks', [
            {'name':'title', 'value':title_value},
            {'name':'desc', 'value': desc_value}
        ])



        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = TodoApp()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())