from PySide6.QtCore import Qt
from PySide6.QtWidgets import QStackedWidget
from typing import Dict


class Router:
    """Simple router managing a QStackedWidget and registered views."""

    def __init__(self, stacked: QStackedWidget):
        self._stacked = stacked
        self._routes: Dict[str, int] = {}

    def register(self, name: str, widget) -> None:
        index = self._stacked.addWidget(widget)
        self._routes[name] = index

    def navigate(self, name: str) -> None:
        index = self._routes.get(name)
        if index is not None:
            self._stacked.setCurrentIndex(index)
