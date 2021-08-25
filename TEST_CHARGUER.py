import RPi.GPIO as GPIO

from ControlPilot import ControlPilot

from ProximityPin import ProximityPin

from ControlRelay import ControlRelay

import LCD_display.py as display

from leds_status import leds_status

import time

def test_relays():
    
    relays = ControlRelay(3, 5, 29)
  
    #Relays set up?
    relays.setups()
    
    
    
    if relays.start():
        print(" HA detectado los relés!\n")
        
        #Assure the relays are Turn Off
        relays.openAllRelays()
    while True:
        print("En 5 segundos se cierran los relés\n")
        
        time.sleep(5)
        
        relays.closeAllRelays()
        print("Cerrados!\n")
        
        print("En 10 segundos se abren los relés\n")
        time.sleep(10)
        
        relays.openAllRelays()
        print("Abiertos!\n")
        
    
def test_pp():
    
    proximity = ProximityPin(11)
    
    proximity.setups()
    
    while True:
        
        
        tension = proximity.tension()
        print("La tension en PP es: " + str(tension) + " V\n")
        
        time.sleep(1)
    

def test_display():
    
    lcd = display.LCD()
    
    while True:
        lcd.clear()
        lcd.message("DKG CHARGÜER \nPRUEBA LCD")
        time.sleep(5)
        
        lcd.clear()
        lcd.message("Cargando... \nEn verdad no :(")
        time.sleep(5)
        
        lcd.clear()
        lcd.message("Ahora numeros \nAmperios: 16A :(")
        time.sleep(5)

      
    
    #lcd.destroy()
    
def test_leds():
    
    leds = leds_status(31, 33, 37)
    
    
    while True:
        
        leds.status_no_connect(True)
        print("Estado: NO CONECTADO\n")
        time.sleep(5)
        
        leds.status_no_connect(False)
        leds.status_comunicating(True)
        print("Estado: COMUNICANDO\n")
        time.sleep(5)
        
        
        leds.status_comunicating(False)
        leds.charging(True)
        print("Estado: CARGANDO\n")
        time.sleep(5)
        
        leds.charging(False)
    



def main():
    
    test_relays()
    
    #test_pp()
    
    #test_display()
    
    #test_leds()
    
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
