from robotpy_ext.autonomous import StatefulAutonomous, timed_state
from robot_systems.TripleMotorGearbox import TripleMotorGearbox

class SecondAuto(StatefulAutonomous):
    
    MODE_NAME = 'Triple Motor Gearbox Testing'
    
    def initialize(self):
        pass
    
    @timed_state(duration=2.5, next_state='turn', first=True)
    def drive_start(self):
        self.LDT.set(0.75)
        self.RDT.set(0.75)
        
    @timed_state(duration=2.5)
    def turn(self):
        self.LDT.set(0.75)
        self.RDT.set(-0.75)
        