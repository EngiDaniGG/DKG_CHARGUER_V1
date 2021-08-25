import RPi.GPIO as GPIO

#sudo pip install sparkfun-qwiic-relay

import qwiic_relay

QUAD_SOLID_STATE_RELAY = 0x08

class ControlRelay:
    
    def __init__(self, sda_i2c, scl_i2c, rst):
               
        self.sda_i2c = sda_i2c
        
        self.scl_i2c = scl_i2c
        
        self.rst = rst
        
        self.relays = qwiic_relay.QwiicRelay(QUAD_SOLID_STATE_RELAY)
        
        
    def setups(self):
        #Read GPIO with BOARD MODE
        GPIO.setmode(GPIO.BOARD)
        
        #Set pin as I2C SDA
        GPIO.setup(self.sda_i2c, GPIO.OUT)
        
        #Set pin as I2C SCL
        GPIO.setup(self.scl_i2c, GPIO.OUT)
        
    def start(self):
        
        if self.relays.begin() == False:
            
            raise Exception("Los relés no están conectados!")
            
            return False
            
        else:
            
            return True

    def openAllRelays(self):
        
        #Turn off the 4 relays
        self.relays.set_all_relays_off()
        
    def closeAllRelays(self):
        
        #Turn on the 4 relays
        self.relays.set_all_relays_on()
        
    def openRelay(self, num):
        
        #Turn off the relay selected
        self.relays.set_relay_off(num)

    def closeRelay(self, num):
        
        #Turn on the relay selected
        self.relays.set_relay_on(num)
    
    def relayStatus(self):
        
        for relayNum in range(4):
        
            current_status = None
            
            if self.relays.get_relay_state(relayNum):
            
                current_status = "On"
            
            else:
            
                current_status = "Off"
        
            print("Status relay " + str(relayNum + 1) + ": " + current_status + "\n")
        