
from abc import abstractmethod, ABC

class Laptop(ABC):        
    @abstractmethod
    def Screen(): 
        raise NotImplementedError('This method was not implemented')
    @abstractmethod
    def Keyboard(): 
        raise NotImplementedError('This method was not implemented')
    @abstractmethod
    def Touchpad(): 
        raise NotImplementedError('This method was not implemented')
    @abstractmethod
    def WebCam(): 
        raise NotImplementedError('This method was not implemented')
    @abstractmethod
    def Ports(): 
        raise NotImplementedError('This method was not implemented')
    @abstractmethod
    def Dynamics(): 
        raise NotImplementedError('This method was not implemented')
    

class HPLaptop(Laptop):
    def Screen(): 
        pass
   
    def Keyboard(): 
        pass
    
    def Touchpad(): 
        pass
    
    def WebCam(): 
        pass
    
    def Ports(): 
        pass
    
    def Dynamics(): 
        pass

mylaptop = HPLaptop()
mylaptop.Dynamics