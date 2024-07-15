import CoCubeUDP
import time

#set robotNum to the number of robots you have
robotNum = 8

if __name__ == '__main__':
    robots = {}
    for i in range(1, robotNum+1):
        robot = CoCubeUDP.CoCubeUDP(i)
        if robot.connected():
            print(robot.robotIP)
            robots[i] = robot
    j = 0
    while True:
        for i, robot in robots.items():
            x = (robot.message_general("position_X", [],  debug=True))
            y = (robot.message_general("position_Y", [],  debug=False))
            yaw = (robot.message_general("position_Yaw", [],  debug=False))
            print(f"robot {i}: x={x}, y={y}, yaw={yaw}")
            # robot.message_general("Rotate to Target", [x+10, y+20, 10], debug=True)
            robot.message_general("Rotate to Angle", [j, 10], debug=False)
            # robot.message_general("displayCharacter", [j], debug=True)
            # print(x)

            time.sleep(1)
            j = (j+27) % 360
            # getdata = robot.receive_position(debug=True)
            # print(type(getdata))
