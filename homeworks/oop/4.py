
from abc import abstractmethod, ABC

class Laptop(ABC):        
    @abstractmethod
    def screen(self): 
        raise NotImplementedError('This method was not implemented')
    @abstractmethod
    def keyboard(self): 
        raise NotImplementedError('This method was not implemented')
    @abstractmethod
    def touchpad(self): 
        raise NotImplementedError('This method was not implemented')
    @abstractmethod
    def web_cam(self): 
        raise NotImplementedError('This method was not implemented')
    @abstractmethod
    def ports(self): 
        raise NotImplementedError('This method was not implemented')
    @abstractmethod
    def dynamics(self): 
        raise NotImplementedError('This method was not implemented')
    

class HPLaptop(Laptop):
    def screen(self): 
        pass
   
    def keyboard(self): 
        pass
    
    def touchpad(self): 
        pass
    
    def web_cam(self): 
        pass
    
    def ports(self): 
        pass
    
    def dynamics(self): 
        print ("Hp laptop make beeps")

mylaptop = HPLaptop()
mylaptop.dynamics()