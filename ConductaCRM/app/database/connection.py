from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


_engine = None
_SessionLocal = None


def get_engine(project_root: Path):
    global _engine, _SessionLocal
    if _engine is None:
        db_path = project_root / "database" / "app.db"
        db_path.parent.mkdir(parents=True, exist_ok=True)
        sqlite_url = f"sqlite:///{db_path.as_posix()}"
        _engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})
        _SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)
    return _engine


def get_session():
    global _SessionLocal
    if _SessionLocal is None:
        raise RuntimeError("Engine not initialized. Call get_engine(project_root) first.")
    return _SessionLocal()
