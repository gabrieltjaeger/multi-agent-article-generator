from .services import ServicesContainer
from .use_cases import UseCasesContainer


class AppContainer():
    services = ServicesContainer()
    use_cases = UseCasesContainer()
