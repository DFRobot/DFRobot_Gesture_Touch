# DFRobot_Gesture_Touch

- [English Version](./README.md)

这款是一款集成了手势识别功能和触摸识别功能的传感器模块，它的最大检测距离为30cm，距离0-30cm可调。其中，能够识别向右、向左、向后、向前、下压、上拉及上拉下压后手松开共7种手势，以及5路的触摸信号，并具有自动睡眠和唤醒的功能。
模块自带手势识别算法，输出数据简洁可靠，可通过串口直接与arduino及树莓派等控制器或上位机通讯。用于智能灯、人机交互、智能小车、趣味游戏等多功能远距离手势控制端。传感器板载5路触摸片，不仅可以直接实现触摸还可以利用导线连接方式延长触摸端.

![正反面svg效果图](./resources/images/SEN0285.png)

## 产品链接(https://www.dfrobot.com.cn/goods-1994.html)

    SKU：SEN0285

## 目录

* [概述](#概述)
* [库安装](#库安装)
* [方法](#方法)
* [兼容性](#兼容性y)
* [历史](#历史)
* [创作者](#创作者)

## 概述

兼容Arduino平台的手势检测和触摸检测的传感器库

## 库安装

使用此库前，请首先下载库文件，将其粘贴到\Arduino\libraries目录中，然后打开examples文件夹并在该文件夹中运行演示。

## 方法

```C++

  /**
   * @fn setGestureDistance
   * @brief 设置手势距离
   * @param dis Distance
   */
  void    setGestureDistance(uint8_t dis);

  /**
   * @fn setSleep
   * @brief 设置自动休眠时间，在休眠模式下，接近会使其变弱  
   * @param sec time  
   */
  void    setSleep(uint8_t sec);

  /**
   * @fn enableFunction
   * @brief 设置传感器识别哪些手势 
   * @param func function number
   */
  void    enableFunction(uint16_t func);

  /**
   * @fn disableFunction
   * @brief 设置传感器不识别哪些手势 
   * @param func function number
   */
  void    disableFunction(uint16_t func);

  /**
   * @fn getAnEvent
   * @brief 获取传感器识别到的是手势或哪个按键被触摸
   * @return int8_t  event number
   */
  int8_t    getAnEvent(void);
```

## 兼容性

主板               | 通过  | 未通过   | 未测试   | 备注
------------------ | :----------: | :----------: | :---------: | -----
FireBeetle-ESP32  |      √       |             |            | 
FireBeetle-ESP8266|      √       |              |             | 
Mega2560  |      √       |             |            | 
Arduino uno |       √      |             |            | 
Leonardo  |      √       |              |             | 
Micro：bit  |      √       |              |             | 
M0  |      √       |              |             | 

## 历史

- 2022/3/29 - 1.0.0 版本

## 创作者

Written by PengKaixing(kaixing.peng@dfrobot.com), 2021. (Welcome to our [website](https://www.dfrobot.com/))