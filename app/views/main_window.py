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
    QToolBar,
    QAction,
    QLineEdit,
    QPushButton,
    QFrame,
    QSizePolicy,
)

from app.core.router import Router
from modules.dashboard.view import DashboardPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ConductaCRM")
        self.resize(1100, 700)

        # Top toolbar
        toolbar = QToolBar("Main")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        title_label = QLabel("ConductaCRM")
        title_label.setObjectName("appTitle")
        toolbar.addWidget(title_label)
        toolbar.addSeparator()

        self.search = QLineEdit()
        self.search.setPlaceholderText("Buscar...")
        self.search.setFixedWidth(250)
        toolbar.addWidget(self.search)
        toolbar.addSeparator()

        collapse_action = QAction("Toggle Sidebar", self)
        collapse_action.triggered.connect(self._toggle_sidebar)
        toolbar.addAction(collapse_action)

        # Central layout
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Sidebar
        self.sidebar = QListWidget()
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setFixedWidth(240)
        for name in ("Dashboard", "Empresas", "Clientes", "Ordens de Serviço", "Financeiro", "Usuários"):
            item = QListWidgetItem(name)
            self.sidebar.addItem(item)

        # Content area
        self.stack = QStackedWidget()
        self.router = Router(self.stack)

        # Register views
        self.dashboard = DashboardPage()
        self.router.register("dashboard", self.dashboard)

        # Add some placeholders for other routes
        self.router.register("empresas", QLabel("Empresas - em construção"))
        self.router.register("clientes", QLabel("Clientes - em construção"))
        self.router.register("ordens_servico", QLabel("Ordens de Serviço - em construção"))
        self.router.register("financeiro", QLabel("Financeiro - em construção"))
        self.router.register("usuarios", QLabel("Usuários - em construção"))

        # Layout
        main_layout.addWidget(self.sidebar)

        # Content wrapper (to allow paddings)
        content_wrapper = QFrame()
        content_wrapper.setObjectName("contentWrapper")
        content_layout = QVBoxLayout(content_wrapper)
        content_layout.setContentsMargins(16, 16, 16, 16)
        content_layout.addWidget(self.stack)

        main_layout.addWidget(content_wrapper, 1)

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

    def _toggle_sidebar(self):
        if self.sidebar.isVisible():
            self.sidebar.hide()
        else:
            self.sidebar.show()
