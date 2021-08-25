#import RPi.GPIO as GPIO

from ControlPilot import ControlPilot

from ProximityPin import ProximityPin

from ControlRelay import ControlRelay

import time


""" GPIO definition """
"""
gpioPins = {0: "3V3 ProtoBoard",
            1: None,
            2: None,
            3: "Relé SDA",
            4: None,
            5: "Relé SCL",
            6: None,
            7: None,
            8: None,
            9: None,
            10: None,
            11: "PP Read",
            12: None,
            13: "CP Read",
            14: None,
            15: None,
            16: None,
            17: "Relé 3V3",
            18: None,
            19: None,
            20: None,
            21: None,
            22: None,
            23: None,
            24: None,
            25: None,
            26: None,
            27: None,
            28: None,
            29: "Relé RST",
            30: "Relé GND",
            31: None,
            32: "PWM",
            33: None,
            34: "GND Protoboard",
            35: None,
            36: None,
            37: None,
            38: None,
            39: None,
            40: None,
            
        } 
"""

def main():
    """"""""""""""""""""""""""""""
    """   CLASSES DEFINITION   """
    """"""""""""""""""""""""""""""
    
    pilot = ControlPilot(13, 32, 16)
    proximity = ProximityPin(11)
    relays = ControlRelay(3, 5, 29)

    
    """"""""""""""""""""""""""""""
    """ SET UPS -->  """
    """"""""""""""""""""""""""""""
    
    #Display set up
    
        
    #Control Pilot set up
    pilot.setups()
    
    #Proximity pin set up
    proximity.setups()
    
    #Relays set up
    relays.setups()
    
    #Other set ups?



    #Comprobaciones de conexiones?
    

    """"""""""""""""""""""""""""""
    """   BODY   """
    """"""""""""""""""""""""""""""
    #CP in 0V
    pilot.generate0v()
    
    #If relays are no conected, The program wont start for security
    if relays.start():
        
        #Assure the relays are Turn Off
        relays.openAllRelays()
        
    
        while True:
            
            #CP in 0V
            pilot.generate0v()
            
            #Assure the relays are Turn Off
            relays.openAllRelays()
            
            comunication = False
            charging = False
            
            time_proximity = 0
            time_comunication = 0
            time_charging = 0
            
            while proximity.detection:
                
                time_proximity = time.time()
                
                if not comunication:
                    pilot.generate12v()
                
                if pilot.read9v() and not comunication:
                    
                    #The EVSE start comunication with EV
                    pilot.setDutyCycle()
                    pilot.generatePWM()
                    comunication = True
                    time_comunication = time.time()
                
                if pilot.read6v() and comunication and not charging:
                    
                    #Right now the EV is prepared for charge
                    relays.closeAllRelays()
                    charging = True
                    time_charging = time.time()
                    
                if not pilot.read6v() and charging:
                    
                    #The EV want to stop charging
                    relays.openAllRelays()
                    charging = False
                    comunication = False
                    
                if not charging:
                    
                    total_time_proximity = time.time() - time_proximity
                    total_time_comunication = time.time() - time_comunication
                    
                    
                total_time_charging = time.time() - time_charging
                
                if total_time_proximity > 30:
                    
                    print("Maximum time exceeded trying conection, just proximity pin detected.\n")
                    break
                
                if total_time_comunication > 15:
                    
                    print("Maximum time exceeded trying to comunicate with EV, unknow error ocurred.\n")
                    break
                
                if total_time_charging > 120:
                    
                    print("Maximum charge time exceeded.\n")
                    break
        

if __name__ == '__main__':

    main()

