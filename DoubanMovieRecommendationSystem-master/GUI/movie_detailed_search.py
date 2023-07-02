# -*- coding: utf-8 -*-
"""
Created on Mon July 3
@author: yangmm
"""

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

from movie_detailed import MovieDetailed


class MovieDetailedSearch(QWidget):
    def __init__(self):
        super(MovieDetailedSearch, self).__init__()  # 使用super函数可以实现子类使用父类的方法
        self.setWindowTitle("Movie detail info")
        self.setWindowIcon(QIcon('../Data/douban.jpg'))  # 设置窗口图标
        self.resize(500, 150)

        self.search_label = QLabel("Input movie name: ", self)
        self.search_line = QLineEdit(self)
        self.search_button = QPushButton("Search", self)

        self.h_layout = QHBoxLayout()

        self.h_layout.addWidget(self.search_label)
        self.h_layout.addWidget(self.search_line)
        self.h_layout.addWidget(self.search_button)

        self.setLayout(self.h_layout)

        self.search_button.clicked.connect(lambda: self.search(self.search_line.text()))

    def search(self, name):
        self.detailed = MovieDetailed(name)
        self.detailed.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    search = MovieDetailedSearch()
    search.show()
    sys.exit(app.exec_())
