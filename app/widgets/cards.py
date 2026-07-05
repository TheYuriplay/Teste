from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QFont


class StatCard(QWidget):
    def __init__(self, title: str, value: str, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setSpacing(4)
        self.setObjectName("statCard")

        title_lbl = QLabel(title)
        title_lbl.setObjectName("statTitle")
        val_lbl = QLabel(value)
        val_lbl.setObjectName("statValue")
        val_lbl.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))

        layout.addWidget(title_lbl)
        layout.addWidget(val_lbl)
