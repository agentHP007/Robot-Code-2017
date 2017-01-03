import wpilib
from wpilib.doublesolenoid import DoubleSolenoid
class DualPiston():
    def __init__(self, fwc1, rvc1, fwc2, rvc2):
        self.DS1 = wpilib.DoubleSolenoid(fwc1,rvc1)
        self.DS2 = wpilib.DoubleSolenoid(fwc2,rvc2)
        
    def set(self, value):
        self.DS1.set(value)
        self.DS2.set(value)
    
    def get(self):
        return self.DS1.get()