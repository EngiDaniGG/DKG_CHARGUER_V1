import RPi.GPIO as GPIO

class leds_status:
    def __init__(self, red, orange, green, breath = None):
        
        self.red = red
        self.orange = orange
        self.green = green
        self.breath = breath
    
    def setups_led(self):
        #Read GPIO with BOARD MODE
        GPIO.setmode(GPIO.BOARD)
        
        GPIO.setup(self.red, GPIO.OUT)
        GPIO.setup(self.orange, GPIO.OUT)
        GPIO.setup(self.green, GPIO.OUT)
        
        #Inicializamos las salidas para que solo se encienda el rojo
        GPIO.output(self.red, GPIO.LOW) #Encendido
        GPIO.output(self.orange, GPIO.HIGH) #Apagado
        GPIO.output(self.green, GPIO.HIGH) #Apagado
        
        
    def status_no_connect(self, status):
        
        if status:
            #Enciendo el LED
            GPIO.output(self.red, GPIO.LOW)
        
        else:
            #Apago el LED
            GPIO.output(self.red, GPIO.HIGH)
            
    def status_comunicating(self, status):
        
        if status:
            #Enciendo el LED
            GPIO.output(self.orange, GPIO.LOW)
            
            self.breath = GPIO.PWM(self.orange, 100) #PWM con frequencia 100 HZ
            self.breath.start(50)
        
        else:
            #Apago el LED
            self.breath.stop()
            #GPIO.output(self.orange, GPIO.HIGH)        
    
    def status_charging(self, status):
        
        if status:
            #Enciendo el LED
            GPIO.output(self.green, GPIO.LOW)
        
        else:
            #Apago el LED
            GPIO.output(self.green, GPIO.HIGH)      