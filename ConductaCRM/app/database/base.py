from sqlalchemy.orm import declarative_base

Base = declarative_base()


def init_db(engine):
    """Create all tables. Call during application start."""
    Base.metadata.create_all(bind=engine)
