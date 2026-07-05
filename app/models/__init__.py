# models package
# Import submodules so SQLAlchemy models are registered when app.models is imported
from .user import User  # noqa: F401
from .empresa import Empresa  # noqa: F401
from .cliente import Cliente  # noqa: F401
from .ordem_servico import OrdemServico  # noqa: F401
