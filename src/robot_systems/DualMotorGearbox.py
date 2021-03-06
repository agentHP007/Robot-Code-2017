import wpilib
class DualMotorGearbox():
    def __init__(self, channel1, channel2):
        self.motor1 = wpilib.VictorSP(channel1)
        self.motor2 = wpilib.VictorSP(channel2)
        self.isInverted = False
        
    def pidWrite(self, output):
        self.motor1.set(output)
        self.motor2.set(output)
        
        
    def set(self, value):
        if(self.isInverted == True):
            self.motor1.set(-value)
            self.motor2.set(-value)
        else:
            self.motor1.set(value)
            self.motor2.set(value)
    
    def setInverted(self, bool):
        self.isInverted = bool
        
    def get(self):
        return self.motor1.get()
    
    def getInverted(self):
        return self.isInverted
        
    