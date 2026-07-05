from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QListWidgetItem,
    QLabel,
    QStackedWidget,
)

from app.core.router import Router


class DashboardWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        title = QLabel("Dashboard")
        title.setObjectName("title")
        layout.addWidget(title)
        layout.addStretch()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ConductaCRM")
        self.resize(1000, 600)

        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)

        # Sidebar
        self.sidebar = QListWidget()
        self.sidebar.setFixedWidth(220)
        for name in ("Dashboard", "Empresas", "Clientes", "Ordens de Serviço", "Financeiro", "Usuários"):
            item = QListWidgetItem(name)
            self.sidebar.addItem(item)

        # Content area
        self.stack = QStackedWidget()
        self.router = Router(self.stack)

        # Register views
        self.dashboard = DashboardWidget()
        self.router.register("dashboard", self.dashboard)

        # Add some placeholders for other routes
        self.router.register("empresas", QLabel("Empresas - em construção"))
        self.router.register("clientes", QLabel("Clientes - em construção"))
        self.router.register("ordens_servico", QLabel("Ordens de Serviço - em construção"))
        self.router.register("financeiro", QLabel("Financeiro - em construção"))
        self.router.register("usuarios", QLabel("Usuários - em construção"))

        # Layout
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.stack, 1)

        # Connect sidebar
        self.sidebar.currentRowChanged.connect(self._on_navigation_selected)
        # Default
        self.sidebar.setCurrentRow(0)

    def _on_navigation_selected(self, row: int):
        mapping = {
            0: "dashboard",
            1: "empresas",
            2: "clientes",
            3: "ordens_servico",
            4: "financeiro",
            5: "usuarios",
        }
        route = mapping.get(row)
        if route:
            self.router.navigate(route)
