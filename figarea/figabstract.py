from abc import ABC, abstractproperty


class BaseABCFigure(ABC):
    """
    Абстрактный класс фигур
    """
    @abstractproperty
    def area(self) -> None:
        pass