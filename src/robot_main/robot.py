#!/usr/bin/env python3
import wpilib
import robot_main.robot_map
import robot_main.robot_pathfinder
import robot_main.robot_utils
import robot_main.robot_vision
import robot_systems.DualMotorGearbox
import robot_systems.TripleMotorGearbox
import robot_systems.InvertedDualMotorGearbox
import robot_systems.DualPiston
from robot_main.robot_map import robot_map
from robot_main.robot_pathfinder import PathFinder
from robot_main.robot_utils import robot_utils
from robot_main.robot_vision import robot_vision
from robot_systems.DualMotorGearbox import DualMotorGearbox
from robot_systems.TripleMotorGearbox import TripleMotorGearbox
from robot_systems.InvertedDualMotorGearbox import InvertedDualMotorGearbox
from robot_systems.DualPiston import DualPiston
from robotpy_ext.control.xbox_controller import XboxController
from robotpy_ext.autonomous import AutonomousModeSelector
from networktables import NetworkTable
class MyRobot(wpilib.IterativeRobot):
    
    def robotInit(self):
        #Motors
        self.LeftDriveTrain = DualMotorGearbox(6, 7)
        self.RightDriveTrain = DualMotorGearbox(4, 5)
        self.Intake = wpilib.VictorSP(3)
        self.Shooter = InvertedDualMotorGearbox(1, 2, False, True)
        #Controllers
        self.LeftJoystick = wpilib.Joystick(0)
        self.RightJoystick = wpilib.Joystick(1)
        #Sensors
        self.IntakeSensorLeft = wpilib.AnalogInput(0)
        self.IntakeSensorRight = wpilib.AnalogInput(1)
        #Pneumatics
        
        #Smart Dashboard
        self.sd = NetworkTable.getTable('Smart Dashboard')
        #Autonomous
    
    def autonomousInit(self):
        pass
    
    def autonomousPeriodic(self):
        pass
    
    def teleopInit(self):
        self.motorUpdatePeriod = 0.005
        self.networkUpdatePeriod = 0.25
        
        self.timer = wpilib.Timer()
    
    def teleopPeriodic(self):
        while self.isOperatorControl() and self.isEnabled():
            
            self.sd.putDouble('Intake Sensor Left', self.IntakeSensorLeft.getAverageVoltage())
            self.sd.putDouble('Intake Sensor Right', self.IntakeSensorRight.getAverageVoltage())
            self.sd.putBoolean('is Ball in?', robot_utils.isBallIn(self, self.IntakeSensorLeft.getAverageVoltage()), self.IntakeSensorRight.getAverageVoltage())
            
            self.LeftYValue = robot_utils.cookJoystickInputs(self, self.LeftJoystick.getY)
            self.RightYValue = robot_utils.cookJoystickInputs(self, self.RightJoystick.getY)
            
            self.LeftDriveTrain.set(self.LeftYValue)
            self.RightDriveTrain.set(self.RightYValue)
            
            if(self.RightJoystick.getRawButton(4)):
                self.Intake.set(0.65)
            elif(self.RightJoystick.getRawButton(5)):
                self.Intake.set(-1)
            elif(self.RightJoystick.getRawButton(3)):
                self.Shooter.set(0.85)
                if(self.RightJoystick.getRawButton(1)):
                    self.Shooter.set(1)
                    self.Intake.set(1)
            else:
                self.Intake.set(0)
                self.Shooter.set(0)
            
            
        self.timer.delay(self.motorUpdatePeriod)
    
    def disabledInit(self):
        pass
    
    def disabledPeriodic(self):
        pass
    
    def testInit(self):
        pass
    
    def testPeriodic(self):
        pass
    
if __name__ == "__main__":
    wpilib.run(MyRobot)
