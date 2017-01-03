import wpilib
class TripleMotorGearbox():
    def __init__(self, channel1, channel2, channel3):
        self.motor1 = wpilib.VictorSP(channel1)
        self.motor2 = wpilib.VictorSP(channel2)
        self.motor3 = wpilib.VictorSP(channel3)
        self.isInverted = False
        
    def pidWrite(self, output):
        self.motor1.set(output)
        self.motor2.set(output)
        self.motor3.set(output)
        
        
    def set(self, value):
        if(self.isInverted == True):
            self.motor1.set(-value)
            self.motor2.set(-value)
            self.motor3.set(-value)
        else:
            self.motor1.set(value)
            self.motor2.set(value)
            self.motor3.set(value)
    
    def setInverted(self, bool):
        self.isInverted = bool
        
    def get(self):
        return self.motor1.get()
    
    def getInverted(self):
        return self.isInverted
        
    