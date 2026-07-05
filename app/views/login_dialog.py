from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QLabel, QPushButton, QMessageBox
from app.services.auth_service import authenticate


class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login")
        layout = QVBoxLayout(self)

        self.user = QLineEdit()
        self.user.setPlaceholderText("Usuário")
        self.pw = QLineEdit()
        self.pw.setPlaceholderText("Senha")
        self.pw.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(QLabel("Usuário"))
        layout.addWidget(self.user)
        layout.addWidget(QLabel("Senha"))
        layout.addWidget(self.pw)

        btn_login = QPushButton("Entrar")
        btn_login.clicked.connect(self._on_login)
        layout.addWidget(btn_login)

    def _on_login(self):
        username = self.user.text().strip()
        password = self.pw.text()
        user = authenticate(username, password)
        if user:
            # store on instance for caller
            self._user = user
            self.accept()
        else:
            QMessageBox.warning(self, "Falha", "Usuário ou senha inválidos")

    def user_authenticated(self):
        return getattr(self, "_user", None)
