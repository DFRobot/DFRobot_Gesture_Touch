# -*- coding: utf-8 -*
'''!
  @file demo_gesture_touch.py
  @brief Sensor event will print on your serial monitor
  @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author      PengKaixing(kaixing.peng@dfrobot.com)
  @version  V1.0.0
  @date  2022-03-28
  @url https://github.com/DFRobot/DFRobot_Gesture_Touch
'''
import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from DFRobot_Gesture_Touch import *

DFGT = DFRobot_Gesture_Touch(9600)

def setup():
  #suggest default value
  DFGT.set_gesture_distance(20)
  #enable all functions
  DFGT.enable_function(DFGT.DFGT_FUN_ALL)
  #disable function test
  DFGT.disable_function(DFGT.DFGT_FUN_RIGHT | DFGT.DFGT_FUN_LEFT)
  #enable function test
  #DFGT.enable_function(DFGT.DFGT_FUN_RIGHT | DFGT.DFGT_FUN_LEFT)
  #set auto sleep time out, in sleep mode, something approaching will wake it up
  #DFGT.set_sleep(4)
  print("simple Gesture!")

def loop():
  while(1):
    #get an event that data saved in serial buffer
    rslt = DFGT.get_an_event()
    if(rslt != DFGT.DF_ERR): 
      if(rslt == DFGT.DFGT_EVT_BACK):
        print("get event back")
      elif(rslt ==DFGT.DFGT_EVT_FORWARD):
        print("get event forward")  
      elif(rslt ==DFGT.DFGT_EVT_RIGHT):
        print("get event right")
      elif(rslt ==DFGT.DFGT_EVT_LEFT):
        print("get event left")
      elif(rslt ==DFGT.DFGT_EVT_PULLUP):
        print("get event pull up")
      elif(rslt ==DFGT.DFGT_EVT_PULLDOWN):
        print("get event pull down")
      elif(rslt ==DFGT.DFGT_EVT_PULLREMOVE):  
        print("get event pull and remove")  
      elif(rslt ==DFGT.DFGT_EVT_TOUCH1): 
        print("get event touch1")
      elif(rslt ==DFGT.DFGT_EVT_TOUCH2):
        print("get event touch2")    
      elif(rslt ==DFGT.DFGT_EVT_TOUCH3): 
        print("get event touch3")  
      elif(rslt ==DFGT.DFGT_EVT_TOUCH4):
        print("get event touch4")    
      elif(rslt ==DFGT.DFGT_EVT_TOUCH5): 
        print("get event touch5")  

if __name__ == "__main__":
  setup()
  loop()
