from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QLabel, QDialogButtonBox
from app.controllers.empresa_controller import get_empresa


class EmpresasForm(QDialog):
    def __init__(self, parent=None, empresa_id: int = None):
        super().__init__(parent)
        self.setWindowTitle("Empresa")
        self._empresa_id = empresa_id

        layout = QVBoxLayout(self)
        self.name = QLineEdit()
        self.cnpj = QLineEdit()
        self.address = QLineEdit()

        layout.addWidget(QLabel("Nome"))
        layout.addWidget(self.name)
        layout.addWidget(QLabel("CNPJ"))
        layout.addWidget(self.cnpj)
        layout.addWidget(QLabel("Endereço"))
        layout.addWidget(self.address)

        buttons = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        if empresa_id:
            emp = get_empresa(empresa_id)
            if emp:
                self.name.setText(emp.name or "")
                self.cnpj.setText(emp.cnpj or "")
                self.address.setText(emp.address or "")

    def get_data(self) -> dict:
        return {"name": self.name.text(), "cnpj": self.cnpj.text(), "address": self.address.text()}
