"""Entry point for ConductaCRM application.

Usage:
    python -m ConductaCRM.main
"""
from pathlib import Path
import sys

from app.core.application import Application


def main() -> int:
    project_root = Path(__file__).resolve().parent
    app = Application(project_root=project_root)
    return app.run()


if __name__ == "__main__":
    raise SystemExit(main())
