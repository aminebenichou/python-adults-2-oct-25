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
        self.data = retrieve_elements("tasks")
        self.main_layout = QtWidgets.QHBoxLayout(self)        
        self.main_layout.addLayout(self.left_side())
        self.right_layout = self.items()
        self.main_layout.addLayout(self.right_layout)
        print(self.data)
    
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
        self.clear_layout(self.right_layout)
        self.data = retrieve_elements("tasks")
        self.right_layout = self.items()
        self.main_layout.addLayout(self.right_layout)

    def item_card(self, item):
        item_layout = QtWidgets.QVBoxLayout()
        item_title = QtWidgets.QLabel(item[1])
        item_desc = QtWidgets.QLabel(item[2])
        btn_layout = QtWidgets.QHBoxLayout()
        complete_btn = QtWidgets.QPushButton("Complete" if item[3] == 0 else "Undo")
        delete_btn = QtWidgets.QPushButton("Delete")
        item_layout.addWidget(item_title)
        item_layout.addWidget(item_desc)
        btn_layout.addWidget(complete_btn)
        btn_layout.addWidget(delete_btn)
        item_layout.addLayout(btn_layout)
        complete_btn.clicked.connect(self.complete_update)
        return item_layout
    
    def complete_update(self):
        update_element('tasks', {
            'id': 1, 
            'data':[
                {
                    'name':'title',
                    'value': 'hello from update'

                },
                {
                    'name':'status',
                    'value': 0

                }
            ]
        })

    def items(self):
        items_layout= QtWidgets.QVBoxLayout()
        for item in self.data:
            items_layout.addLayout(self.item_card(item))

        return items_layout
    

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    self.clear_layout(child.layout())


        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = TodoApp()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())