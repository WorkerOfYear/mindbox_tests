from typing import Protocol

class FigureProtocol(Protocol):
    """
    Интерфейс, определяющий набор методов,
    которые должны быть реализованы
    """
    def area(self) -> None:
        pass

def compute_area(figure: FigureProtocol) -> float:
    return figure.area
