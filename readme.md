# DFRobot_Gesture_Touch
<pre>
--This is a sensor module integrated with the functions of gesture recognition and touch recognition.
--It has a maximum detection range of 30cm.  
--The sensor is able to recognize 7 gestures including move right, move left, forward, backward, 
  press down, stretch up, and release after stretching up and pressing down.
--It can also identify 5 way touch signal and is equipped with the functionality of auto sleep and wake up.
--The sensor features small size, low power consumption and reliable detection sensitivity with the operating current of 56.3mA and sleep current of 40uA.
--The gesture recognition algorithm and data handling program have been burned into the module, which ensures concise and reliable output data.
--The sensor can directly communicate with Arduino controller, Raspberry Pi controller and host computer via serial port.
--The packet format is 8-bit data frame.
</pre>

## DFRobot_Gesture_Touch library for Arduino
<pre>
Provides an Arduino library for reading getsture&touch event and setting to sensor.
</pre>

## Installation
<pre>
To use this library download the zip file, uncompress it to a folder named DFRobot_Gesture_Touch.
</pre>

## Methods

```C++

/*
 * set gesture induction distance
 * @param dis   unit cm, 0<dis<31
 */ 
void setGestureDistance(uint8_t dis);
 
/*
 * set sensor auto sleep time out, wake sensor when something approaching gesture sensing device
 * @param sec   unit sencond, sec cant be 1 to 254, use define DFGT_SLEEP_DISABLE to disable it
 */
void setSleep(uint8_t sec);

// functions for sensor, use with enableFunction/disableFunction
#define DFGT_FUN_RIGHT   
#define DFGT_FUN_LEFT    
#define DFGT_FUN_BACK    
#define DFGT_FUN_FORWARD 
#define DFGT_FUN_PULLUP  
#define DFGT_FUN_PULLDOWN
#define DFGT_FUN_TOUCH1  
#define DFGT_FUN_TOUCH2  
#define DFGT_FUN_TOUCH3  
#define DFGT_FUN_TOUCH4  
#define DFGT_FUN_TOUCH5  
#define DFGT_FUN_ALL     

/*
 * set sensor function enable
 * @param func    select function
 */
void enableFunction(uint16_t func);

/*
 * set sensor function disable
 * @param func    select function
 */
void disableFunction(uint16_t func);

// sensor events
#define DFGT_EVT_RIGHT        0x01
#define DFGT_EVT_LEFT         0x02
#define DFGT_EVT_BACK         0x03
#define DFGT_EVT_FORWARD      0x04
#define DFGT_EVT_PULLUP       0x05
#define DFGT_EVT_PULLDOWN     0x06
#define DFGT_EVT_PULLREMOVE   0x07
#define DFGT_EVT_TOUCH1       0x21
#define DFGT_EVT_TOUCH2       0x22
#define DFGT_EVT_TOUCH3       0x23
#define DFGT_EVT_TOUCH4       0x24
#define DFGT_EVT_TOUCH5       0x25

#define DF_OK   0
#define DF_ERR  -1

/*
 * check and get an event saved in serial buffer
 * @return an event or DF_ERR
 */
int8_t getAnEvent();

```

python lib is similar to c++ lib

```py
class Gesture_Touch:

  FUN_RIGHT = 0x01
  FUN_LEFT = 0x02
  FUN_BACK = 0x03
  FUN_FORWARD = 0x04
  FUN_PULLUP = 0x05
  FUN_PULLDOWN = 0x06
  FUN_TOUCH1 = 0x09
  FUN_TOUCH2 = 0x0A
  FUN_TOUCH3 = 0x0B
  FUN_TOUCH4 = 0x0C
  FUN_TOUCH5 = 0x0D
  FUN_ALL = 0xff

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

  def setGestureDistance(self, dis):

  def setSleep(self, sec):

  def enableFunction(self, func):
  
  def disableFunction(self, func):
  
  def getAnEvent(self):
```

## Compatibility

Arduino:

MCU                | Work Well | Work Wrong | Untested  | Remarks
------------------ | :----------: | :----------: | :---------: | ----- 
FireBeetle esp32 |       ???      |             |            |
FireBeetle esp8266 |             |      ???       |            |
Arduino uno |       ???      |             |            |
Arduino leonardo |      ???       |             |            |  a proprietary example gestureKeyboard.ino for leonardo

Python:

plaform | Work Well | Work Wrong | Untested | Remarks
------------------ | :----------: | :----------: | :---------: | ----- 
FireBeetle esp32 |       ???      |             |            |
FireBeetle esp8266 |             |      ???       |            |
Raspberry Pi |       ???      |             |            |
