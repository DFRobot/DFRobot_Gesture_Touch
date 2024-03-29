# -*- coding:utf-8 -*-
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
import sys
import time

def do_nothing(*argvs, **kargvs):
  return

class Gesture_Touch:
  '''
    @brief This is a Raspberry Pi class for gesture and touch detection.
  '''
  OK = 0
  ERR = -1
  SEND_HEAD = 0xaa
  SEND_END = 0x55
  RECV_HEAD = 0xaa
  RECV_END = 0x55
  CMD_INTERVAL = 0x51
  CMD_SLEEP = 0x52
  CMD_DISTANCE = 0x54
  CMD_ENABLE = 0x55
  MASK_RIGHT = 0x01
  MASK_LEFT = 0x02
  MASK_BACK = 0x03
  MASK_FORWARD = 0x04
  MASK_PULLUP = 0x05
  MASK_PULLDOWN = 0x06
  MASK_TOUCH1 = 0x09
  MASK_TOUCH2 = 0x0A
  MASK_TOUCH3 = 0x0B
  MASK_TOUCH4 = 0x0C
  MASK_TOUCH5 = 0x0D
  FUN_RIGHT = 0x01
  FUN_LEFT = 0x02
  FUN_BACK = 0x04
  FUN_FORWARD = 0x08
  FUN_PULLUP = 0x10
  FUN_PULLDOWN = 0x20
  FUN_TOUCH1 = 0x40
  FUN_TOUCH2 = 0x80
  FUN_TOUCH3 = 0x100
  FUN_TOUCH4 = 0x200
  FUN_TOUCH5 = 0x400
  FUN_ALL = 0x7ff
  EVT_RIGHT = 0x01
  EVT_LEFT = 0x02
  EVT_BACK = 0x03
  EVT_FORWARD = 0x04
  EVT_PULLUP = 0x05
  EVT_PULLDOWN = 0x06
  EVT_PULLREMOVE = 0x07
  EVT_TOUCH1 = 0x21
  EVT_TOUCH2 = 0x22
  EVT_TOUCH3 = 0x23
  EVT_TOUCH4 = 0x24
  EVT_TOUCH5 = 0x25 
  SLEEP_DISABLE = 0xff

  def __init__(self, txPin = None, rxPin = None):
    self._ser = None
    self._serWrite = lambda x : x
    self._serRead = do_nothing
    self._serAvailable = do_nothing
    self.sleep = do_nothing
    self._recvBuf = bytearray([])
    if sys.platform.find("linux") >= 0:
      import serial
      self._ser = serial.Serial("/dev/ttyAMA0", 9600)
      self._serAvailable = self._ser.inWaiting
      self._serWrite = self._ser.write
      self._serRead = self._ser.read
      self.sleep = lambda t : time.sleep(t)
      self._ser.flushInput()
    elif sys.platform == "esp32":
      import machine
      import os
      self._os = os
      self._ser = machine.UART(1, baudrate = 9600, rx = rxPin, tx = txPin)
      self._serAvailable = self._ser.any
      self._serWrite = self._ser.write
      self._serRead = self._ser.read
      self.sleep = lambda t : time.sleep(t)
    else:
      print("unsupport platform")
      exit()

  def set_cmd(self, cmd, value):
    '''
      @brief  set command
      @param  cmd command
      @param  value parameter setting
    '''
    self._serWrite(bytearray([self.SEND_HEAD, cmd, value & 0xff, (cmd ^ value) & 0xff, self.SEND_END]))
    self.sleep(0.002)

  def set_gesture_distance(self, dis):
    '''!
      @brief Set the Gesture Distance 
      @param dis Distance
    '''
    if dis > 30:
      return
    self.set_cmd(self.CMD_DISTANCE, 0xff)
    self.set_cmd(self.CMD_DISTANCE, 0x20 + (0xfe - 0x20) // 30 * dis)

  def set_sleep(self, sec):
    '''
      @brief set auto sleep time out, in sleep mode, something approaching will wake it up
      @param sec time  
    '''
    if sec == 1 or sec > 255:
      return
    self.set_cmd(self.CMD_SLEEP, sec)
    
  def enable_func_helper(self, start, func):
    ''' 
      @brief Enable some sensor functions
      @param  start Enable or not
      @param  func Sensor functions to be enabled
    '''
    while func > 0:
      if func & 0x01:
        self.set_cmd(self.CMD_ENABLE, func)
      start += 1
      func >>= 1

  def enable_function(self, func):
    '''
      @brief Set which gestures the sensor recognizes
      @param func function number
    '''
    self.enable_func_helper(self.MASK_RIGHT | 0x10, func & 0x3f)
    self.enable_func_helper(self.MASK_TOUCH1 | 0x10, (func & 0x7ff) >> 6)
  
  def disable_function(self, func):
    '''
      @brief Set which gestures the sensor does not recognize
      @param func function number
    '''
    self.enable_func_helper(self.MASK_RIGHT, func & 0x3f)
    self.enable_func_helper(self.MASK_TOUCH1, (func & 0x7ff) >> 6)
  
  def get_an_event(self):
    '''
      @brief Get whether the sensor recognizes a gesture or which button is being touched
      @return int8_t  event number
    '''
    rslt = self.ERR
    if self._serAvailable():
      self._recvBuf += self._serRead(self._serAvailable())
      bufLen = len(self._recvBuf)
      while self._recvBuf[0] != 0xaa and bufLen > 0:
        self._recvBuf = self._recvBuf[1 : bufLen]
        bufLen -= 1
      if bufLen >= 4:
        if self._recvBuf[0] == self.RECV_HEAD and self._recvBuf[3] == self.RECV_END and self._recvBuf[1] == (0xff - self._recvBuf[2]):
          rslt = self._recvBuf[1]
        self._recvBuf = self._recvBuf[4 : bufLen]
    return rslt

