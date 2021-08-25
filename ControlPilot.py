import RPi.GPIO as GPIO


OFFSET = 0.15


class ControlPilot:
    
    def __init__(self, read_input, pwm_output, max_amp):
        
        if max_amp > 32 or max_amp < 6:
            
            raise Exception("El amperaje no está dentro de los limites de 6-32A!")
        
        self.read_input = read_input
        
        self.pwm_output = pwm_output
        
        self.max_amp = max_amp
        
        self.duty_cycle = None
        
        
    
    def setups(self):
        #Read GPIO with BOARD MODE
        GPIO.setmode(GPIO.BOARD)
        
        #Set pin as PWM signal output
        GPIO.setup(self.pwm_output, GPIO.OUT)
        
        #Set pin as Read Car voltage
        GPIO.setup(self.read_input, GPIO.IN)
        
    def setDutyCycle(self):
        #Duty Cycle: PWM signal tells the car how much current she can draw.
        #This can be a number from 6A to 80A. In the range from 6A to 51A, 
        #the value is calculated as DutyCycle = Ampere / 0.6
        self.duty_cycle = self.max_amp/0.6
        
    def changeDutyCycle(self, new_max_amp):
        
        #Check if the currente is between the limits
        if new_max_amp > 32 or new_max_amp < 6:
            
            raise Exception("El amperaje no está dentro de los limites de 6-32A!")
        
        else:
            #Assign new max current
            self.max_amp = new_max_amp
        
            duty_cycle = self.max_amp/0.6
        
            self.pwm_out.changeDutyCycle(duty_cycle)
        
    def generatePWM(self):
        
        if self.duty_cycle == None:
            self.setDutyCycle()
            
        #Create PWM instance with frequency 1000 Hz and de duty cycle calculated
        pwm_out = GPIO.PWM(self.pwm_output, 1000)
        
        pwm_out.start(self.duty_cycle)
        
    def stopPWM(self):
        self.pwm_out.stop()
        
        
    def generate12v(self):
        
        GPIO.output(self.pwm_output, GPIO.HIGH)
        
        
    def generate0v(self):
        
        GPIO.output(self.pwm_output, GPIO.LOW)
        
    
    def readVoltage(self):
        
        return self.read_input
        
    def read9v(self):
        
        if self.read_input <= 2.74 + OFFSET and self.read_input <= 2.74 + OFFSET:
            
            return True
        
        else:
            return False
        
    
    def read6v(self):
        
        if self.read_input <= 2.39 + OFFSET and self.read_input <= 2.39 + OFFSET:
            
            return True
        
        else:
            return False
    
    
