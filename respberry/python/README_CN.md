# DFRobot_Gesture_Touch

- [English Version](./README.md)

这款是一款集成了手势识别功能和触摸识别功能的传感器模块，它的最大检测距离为30cm，距离0-30cm可调。其中，能够识别向右、向左、向后、向前、下压、上拉及上拉下压后手松开共7种手势，以及5路的触摸信号，并具有自动睡眠和唤醒的功能。
模块自带手势识别算法，输出数据简洁可靠，可通过串口直接与arduino及树莓派等控制器或上位机通讯。用于智能灯、人机交互、智能小车、趣味游戏等多功能远距离手势控制端。传感器板载5路触摸片，不仅可以直接实现触摸还可以利用导线连接方式延长触摸端。

![正反面svg效果图](../../resources/images/SEN0285.png)

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

要使用这个库，首先将库下载到Raspberry Pi，然后打开例程文件夹。要执行一个例程demo_gesture_touch.py，请在命令行中输入python demo_gesture_touch.py。

## 方法

```python
  '''!
    @brief 设置手势距离
    @param dis 距离
  '''
  def set_gesture_distance(self,dis):

  '''
    @brief 设置自动休眠时间，在休眠模式下，接近会使其变弱
    @param sec 时间  
  '''
  def set_sleep(self,sec):

  '''
    @brief 设置传感器可以识别的手势
    @param func 功能编号
  '''
  def enable_function(self, func):

  '''
    @brief 设置传感器不能识别的手势
    @param func 功能编号
  '''
  def disable_function(self, func):

  '''
    @brief 获取传感器是否识别手势或正在触摸哪个按钮
    @return int8_t  事件编号
  '''
  def get_an_event(self):

  '''
    @brief  设置传感器寄存器参数
    @param  设置命令
    @param  value 参数
  '''
  def set(self, cmd, value):

  ''' 
    @brief 开启部分传感器功能
    @param  start 启用或不启用
    @param  func 事件编号
  '''
  def enable_function_helper(self , start,  func):  

```

## 兼容性

| Mainboard         | Pass | Miss | No Test | Note |
| ------------ | :--: | :----: | :----: | :--: |
| RaspberryPi2 |      |        |   √    |      |
| RaspberryPi3 |      |        |   √    |      |
| RaspberryPi4 |  √   |        |        |      |

* Python Version

| Python  | Pass | Miss | No Test | Note |
| ------- | :--: | :----: | :----: | ---- |
| Python2 |  √   |        |        |      |
| Python3 |  √   |        |        |      |

## 历史

- 2022/3/29 - 1.0.0 版本

## 创作者

Written by PengKaixing(kaixing.peng@dfrobot.com), 2021. (Welcome to our [website](https://www.dfrobot.com/))
