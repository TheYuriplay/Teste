from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QLabel, QDialogButtonBox
from app.controllers.cliente_controller import get_cliente


class ClientesForm(QDialog):
    def __init__(self, parent=None, cliente_id: int = None):
        super().__init__(parent)
        self.setWindowTitle("Cliente")
        self._cliente_id = cliente_id

        layout = QVBoxLayout(self)
        self.name = QLineEdit()
        self.email = QLineEdit()
        self.phone = QLineEdit()

        layout.addWidget(QLabel("Nome"))
        layout.addWidget(self.name)
        layout.addWidget(QLabel("Email"))
        layout.addWidget(self.email)
        layout.addWidget(QLabel("Telefone"))
        layout.addWidget(self.phone)

        buttons = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        if cliente_id:
            c = get_cliente(cliente_id)
            if c:
                self.name.setText(c.name or "")
                self.email.setText(c.email or "")
                self.phone.setText(c.phone or "")

    def get_data(self) -> dict:
        return {"name": self.name.text(), "email": self.email.text(), "phone": self.phone.text()}
