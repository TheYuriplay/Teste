from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QMessageBox,
)
from app.controllers.empresa_controller import list_empresas, create_empresa, delete_empresa
from app.views.empresas_form import EmpresasForm


class EmpresasList(QWidget):
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
        empresas = list_empresas()
        for e in empresas:
            item = QListWidgetItem(f"{e.id} — {e.name}")
            item.setData(1, e.id)
            self.list.addItem(item)

    def _on_new(self):
        dlg = EmpresasForm(parent=self)
        if dlg.exec():
            data = dlg.get_data()
            create_empresa(data)
            self.refresh()

    def _on_edit(self):
        item = self.list.currentItem()
        if not item:
            return
        eid = item.data(1)
        dlg = EmpresasForm(parent=self, empresa_id=eid)
        if dlg.exec():
            data = dlg.get_data()
            # re-use controller
            from app.controllers.empresa_controller import update_empresa

            update_empresa(eid, data)
            self.refresh()

    def _on_delete(self):
        item = self.list.currentItem()
        if not item:
            return
        eid = item.data(1)
        ok = QMessageBox.question(self, "Confirmar", "Remover empresa selecionada?")
        if ok == QMessageBox.StandardButton.Yes:
            delete_empresa(eid)
            self.refresh()
