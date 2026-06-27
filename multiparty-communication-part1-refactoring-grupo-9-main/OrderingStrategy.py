from abc import ABC, abstractmethod 

class OrderingStrategy(ABC):
    @abstractmethod
    def deliver(self, msg, log):
        # Decide oq fazer com uma mensagem recebida
        pass
    
class NoOrdering(OrderingStrategy):
    # Comportamento atual: entrega na ordem de chegada
    def deliver(self, msg, log):
        log.append(msg)

