class robot_utils():
    def cookJoystickInputs(self, jsv):
        if(jsv < 0):
            return -(jsv * jsv)
        elif(jsv > 0):
            return (jsv * jsv)
        else:
            return 0
        
    def cookThrottleInputs(self, ths):
        return ((-ths+1)/2)
    def isBallIn(self, voltage1, voltage2):
        if(voltage1 > 1.6):
            bool1 = True
        else:
            bool1 = False
        if(voltage2 > 1.6):
            bool2 = True
        else:
            bool2 = False
        return bool1 and bool2            