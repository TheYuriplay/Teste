from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem, QPushButton, QMessageBox
from app.controllers.cliente_controller import list_clientes, create_cliente, delete_cliente
from app.views.clientes_form import ClientesForm


class ClientesList(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)

        toolbar = QHBoxLayout()
        btn_new = QPushButton("Novo")
        btn_edit = QPushButton("Editar")
        btn_delete = QPushButton("Remover")
        btn_refresh = QPushButton("Atualizar")
        toolbar.addWidget(btn_new)
        toolbar.addWidget(btn_edit)
        toolbar.addWidget(btn_delete)
        toolbar.addWidget(btn_refresh)
        layout.addLayout(toolbar)

        self.list = QListWidget()
        layout.addWidget(self.list)

        btn_new.clicked.connect(self._on_new)
        btn_edit.clicked.connect(self._on_edit)
        btn_delete.clicked.connect(self._on_delete)
        btn_refresh.clicked.connect(self.refresh)

        self.refresh()

    def refresh(self):
        self.list.clear()
        clientes = list_clientes()
        for c in clientes:
            item = QListWidgetItem(f"{c.id} — {c.name}")
            item.setData(1, c.id)
            self.list.addItem(item)

    def _on_new(self):
        dlg = ClientesForm(parent=self)
        if dlg.exec():
            data = dlg.get_data()
            create_cliente(data)
            self.refresh()

    def _on_edit(self):
        item = self.list.currentItem()
        if not item:
            return
        cid = item.data(1)
        dlg = ClientesForm(parent=self, cliente_id=cid)
        if dlg.exec():
            data = dlg.get_data()
            from app.controllers.cliente_controller import update_cliente

            update_cliente(cid, data)
            self.refresh()

    def _on_delete(self):
        item = self.list.currentItem()
        if not item:
            return
        cid = item.data(1)
        ok = QMessageBox.question(self, "Confirmar", "Remover cliente selecionado?")
        if ok == QMessageBox.StandardButton.Yes:
            delete_cliente(cid)
            self.refresh()
