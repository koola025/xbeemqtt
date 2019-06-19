# import os
# os.system("istats all")
import subprocess
import serial
import time





# XBee setting
serdev = '/dev/tty.usbserial-AC00CNOV'
s = serial.Serial(serdev, 9600)

# s.write("+++".encode())
# char = s.read(2)
# print("Enter AT mode.")
# print(char.decode())

# s.write("ATMY 0x270\r\n".encode())
# char = s.read(3)
# print("Set MY 0x270.")
# print(char.decode())

# s.write("ATDL 0x170\r\n".encode())
# char = s.read(3)
# print("Set DL 0x170.")
# print(char.decode())

# s.write("ATWR\r\n".encode())
# char = s.read(3)
# print("Write config.")
# print(char.decode())

# s.write("ATMY\r\n".encode())
# char = s.read(4)
# print("MY :")
# print(char.decode())

# s.write("ATDL\r\n".encode())
# char = s.read(4)
# print("DL : ")
# print(char.decode())

# s.write("ATCN\r\n".encode())
# char = s.read(3)
# print("Exit AT mode.")

# print(char.decode())
first = True
while True:
    if first:
        line = s.read(13)
        first = False
    else:
        line = s.read(13)
    print('Get:', line.decode())
    time.sleep(1)
    # s.write(fan.encode())
    # line = s.read(20)
    # print('Get:', line.decode())

    # s.write(battery.encode())
    # line = s.read(21)
    # print('Get:', line.decode())

    # s.close()

