import logging
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication

from app.views.main_window import MainWindow
from app.database.connection import get_engine
from app.database.base import init_db


class Application:
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.logger = logging.getLogger("ConductaCRM")
        logging.basicConfig(level=logging.INFO)
        self._qapp = None

        # Database
        self.engine = get_engine(self.project_root)

        # Import models so that SQLAlchemy Base has metadata before creating tables
        # Models are imported for their side-effects (declarative base registration)
        import app.models  # noqa: F401

        init_db(self.engine)

    def _create_qapp(self):
        self._qapp = QApplication(sys.argv)
        # Load stylesheet
        qss_path = self.project_root / "assets" / "styles" / "dark.qss"
        if qss_path.exists():
            with open(qss_path, "r", encoding="utf-8") as f:
                self._qapp.setStyleSheet(f.read())

    def run(self) -> int:
        self._create_qapp()
        window = MainWindow()
        window.show()
        return self._qapp.exec()
