# -*- coding: utf-8 -*
'''!
  @file DFRobot_Gesture_Touch.py
  @brief This is a Raspberry Pi library for gesture and touch detection.
  @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author      PengKaixing(kaixing.peng@dfrobot.com)
  @version  V1.0.0
  @date  2022-03-28
  @url https://github.com/DFRobot/DFRobot_Gesture_Touch
'''

import serial
import time
import os
import math
import RPi.GPIO as GPIO

def DF_BIT_OFFSET(x):
  return (0x0001 << (x))

class DFRobot_Gesture_Touch:
  '''
    @brief This is a Raspberry Pi class for gesture and touch detection.
  '''
  def __init__(self ,Baud):
    self.DF_OK  = 0
    self.DF_ERR = -1
    self.DFGT_SEND_HEAD  =  0xaa
    self.DFGT_SEND_END  =   0x55
    self.DFGT_RECV_HEAD  = 0xaa
    self.DFGT_RECV_END  =  0x55
    self.DFGT_CMD_INTERVAL =  0x51
    self.DFGT_CMD_SLEEP    =  0x52
    self.DFGT_CMD_DISTANCE  = 0x54
    self.DFGT_CMD_ENABLE =    0x55
    self.GT_FUN_RIGHT   =   0x01
    self.GT_FUN_LEFT   =    0x02
    self.GT_FUN_BACK    =   0x03
    self.GT_FUN_FORWARD =   0x04
    self.GT_FUN_PULLUP   =  0x05
    self.GT_FUN_PULLDOWN =  0x06
    self.GT_FUN_TOUCH1  =   0x09
    self.GT_FUN_TOUCH2  =   0x0A
    self.GT_FUN_TOUCH3  =   0x0B
    self.GT_FUN_TOUCH4  =   0x0C
    self.GT_FUN_TOUCH5  =   0x0D
    #self.DF_BIT_OFFSET(x) = (0x0001 << (x))
    self.DFGT_FUN_RIGHT    =  DF_BIT_OFFSET(0)
    self.DFGT_FUN_LEFT     =  DF_BIT_OFFSET(1)
    self.DFGT_FUN_BACK     =  DF_BIT_OFFSET(2)
    self.DFGT_FUN_FORWARD  =  DF_BIT_OFFSET(3)
    self.DFGT_FUN_PULLUP   =  DF_BIT_OFFSET(4)
    self.DFGT_FUN_PULLDOWN =  DF_BIT_OFFSET(5)
    self.DFGT_FUN_START1   =  0x01
    self.DFGT_FUN_PART1    =  0x3f
    self.DFGT_FUN_OFFSET1  =  0x00
    self.DFGT_FUN_TOUCH1   =  DF_BIT_OFFSET(6)
    self.DFGT_FUN_TOUCH2   =  DF_BIT_OFFSET(7)
    self.DFGT_FUN_TOUCH3   =  DF_BIT_OFFSET(8)
    self.DFGT_FUN_TOUCH4   =  DF_BIT_OFFSET(9)
    self.DFGT_FUN_TOUCH5   =  DF_BIT_OFFSET(10)
    self.DFGT_FUN_START2   =  0x09
    self.DFGT_FUN_PART2    =  0x07ff
    self.DFGT_FUN_OFFSET2  =  0x06
    self.DFGT_FUN_ALL      =  0x07ff
    self.DFGT_EVT_RIGHT      =  0x01
    self.DFGT_EVT_LEFT       =  0x02
    self.DFGT_EVT_BACK       =  0x03
    self.DFGT_EVT_FORWARD    =  0x04
    self.DFGT_EVT_PULLUP     =  0x05
    self.DFGT_EVT_PULLDOWN   =  0x06
    self.DFGT_EVT_PULLREMOVE =  0x07
    self.DFGT_EVT_TOUCH1     =  0x21
    self.DFGT_EVT_TOUCH2     =  0x22
    self.DFGT_EVT_TOUCH3     =  0x23
    self.DFGT_EVT_TOUCH4     =  0x24
    self.DFGT_EVT_TOUCH5     =  0x25
    self.DFGT_SLEEP_DISABLE  =  0xff
    self.ser = serial.Serial("/dev/ttyAMA0" ,baudrate=Baud)
    if self.ser.isOpen == False:
      self.ser.open()

  def set_gesture_distance(self,dis):
    '''!
      @brief Set the Gesture Distance 
      @param dis Distance
    '''
    if(dis > 30):
      return
    if(dis == 30):
      dis -= 2
    self.set(self.DFGT_CMD_DISTANCE, 0xff)
    self.set(self.DFGT_CMD_DISTANCE, int(0x20 + (0xfe - 0x20) / 30 * dis))

  def set_sleep(self,sec):
    '''
      @brief set auto sleep time out, in sleep mode, something approaching will wake it up
      @param sec time  
    '''
    if(sec == 1):
      return
    self.set(self.DFGT_CMD_SLEEP, 1)
    self.set(self.DFGT_CMD_SLEEP, sec)

  def enable_function(self, func):
    '''
      @brief Set which gestures the sensor recognizes
      @param func function number
    '''
    self.enable_function_helper(self.DFGT_FUN_START1 | 0x10, (func & self.DFGT_FUN_PART1) >> self.DFGT_FUN_OFFSET1)
    self.enable_function_helper(self.DFGT_FUN_START2 | 0x10, (func & self.DFGT_FUN_PART2) >> self.DFGT_FUN_OFFSET2)

  def disable_function(self, func):
    '''
      @brief Set which gestures the sensor does not recognize
      @param func function number
    '''
    self.enable_function_helper(self.DFGT_FUN_START1, (func & self.DFGT_FUN_PART1) >> self.DFGT_FUN_OFFSET1)
    self.enable_function_helper(self.DFGT_FUN_START2, (func & self.DFGT_FUN_PART2) >> self.DFGT_FUN_OFFSET2)

  def get_an_event(self):
    '''
      @brief Get whether the sensor recognizes a gesture or which button is being touched
      @return int8_t  event number
    '''
    timenow = time.time()
    while(time.time() - timenow) <= 2:
      count = self.ser.inWaiting()
      if count != 0:
        pRecv = self.ser.read(count)
        self.ser.flushInput()
        time.sleep(0.1)
        pRecv =[ord(c) for c in pRecv]
        if((pRecv[0] == self.DFGT_RECV_HEAD) and (pRecv[3] == self.DFGT_RECV_END) and (pRecv[1] == (0xff - pRecv[2]))):
          return pRecv[1]
        return self.DF_ERR
      self.ser.flushInput()

  def set(self, cmd, value):
    '''
      @brief  set command
      @param  cmd command
      @param  value parameter setting
    '''
    buf = [self.DFGT_SEND_HEAD,0,0,0,self.DFGT_SEND_END]
    buf[1]=cmd
    buf[2]=value
    buf[3]=cmd ^ value
    self.ser.write(buf)
    time.sleep(0.1)

  def enable_function_helper(self , start,  func):  
    ''' 
      @brief Enable some sensor functions
      @param  start Enable or not
      @param  Sensor functions to be enabled
    '''
    while(func): 
      if(func & 0x01):
        self.set(self.DFGT_CMD_ENABLE, start)
      start += 1
      func >>= 1
