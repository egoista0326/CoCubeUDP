# UDP通信-PC端
## CoCubeUDP.py
> 定义了CoCUbeUDP类，用于UDP通信。
* connected: 用于检测能否连接
* message_general: 模仿BLE通信的request

## CoCbubePC.py
> 小的demo

* robotNum: 机器人数量
* CoCubeUDP.CoCubeUDP：初始化
  * ip_head: ip端口除去最后两位数字，例如：'192.168.3.1'
  * port_head = 5000
  * local_ip: 主机地址，例如：'192.168.3.70'

# UDP通信-micro端: UDP-712.ubl
## wifi-connect
> 连接wifi

![image-20240715152506492](https://cdn.jsdelivr.net/gh/egoista0326/markdown_pic@master/uPic/2024_07/image-20240715152506492_15.png)

* 黄框的两处要根据自己的ip地址更改
* robotid要根据机器人编号更改

# TODO
1. 机器人编号在烧录的时候需要手动更改，比较麻烦
2. 可能会出现收不到信息的情况，原因不清楚，今天没有再出现。不确定是否应该模仿种瓜的BLE实现，即将信息接受放到一个线程中，时刻准备信息接受。
3. 目前可以同时连8个，机器人数量不够了。
4. micro端设置ip地址有些麻烦