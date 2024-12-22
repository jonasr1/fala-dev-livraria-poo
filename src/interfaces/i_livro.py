from abc import ABC, abstractmethod


class ILivro(ABC):
    @property
    @abstractmethod
    def titulo(self) -> str:
        pass
    
    @property
    @abstractmethod
    def autor(self) -> str:
        pass
    
    @property
    @abstractmethod
    def preco(self) -> float:
        pass
    
    @abstractmethod
    def exibir_detalhes(self) -> str:
        pass