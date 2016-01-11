from abc import ABCMeta, abstractmethod

class PatcherInterface:
    __metaclass__=ABCMeta
    
    @abstractmethod
    def patch(self):
        pass
