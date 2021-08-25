import RPi.GPIO as GPIO


class ProximityPin:
    
    def __init__(self, read_proximity):
        
        self.read_proximity = read_proximity

        
    def setups(self):
        #Read GPIO with BOARD MODE
        GPIO.setmode(GPIO.BOARD)
        
        #Set pin as digital input
        GPIO.setup(self.read_proximity, GPIO.IN)
        
    def detection(self):
        
        if self.read_proximity < 1.5:
            return True
        
        else:
            return False
    
    def tension(self):
        
        return self.read_proximity

