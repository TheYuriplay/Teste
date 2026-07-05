from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtWidgets import QHBoxLayout, QSizePolicy
from app.widgets.cards import StatCard


class DashboardPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        header = QLabel("Painel de Controle")
        header.setObjectName("pageHeader")
        layout.addWidget(header)

        # Stats row
        stats_row = QHBoxLayout()
        stats_row.setSpacing(12)
        stats = [
            ("Clientes", "120"),
            ("Empresas", "8"),
            ("Ordens de Serviço", "34"),
            ("Faturamento (Mês)", "R$ 45.200"),
        ]
        for title, value in stats:
            card = StatCard(title=title, value=value)
            card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            stats_row.addWidget(card)

        layout.addLayout(stats_row)

        # Placeholder for charts / lists
        placeholder = QLabel("Gráficos e listas serão adicionados aqui — Entrega 3.")
        placeholder.setObjectName("placeholder")
        placeholder.setFixedHeight(220)
        layout.addWidget(placeholder)
        layout.addStretch()
