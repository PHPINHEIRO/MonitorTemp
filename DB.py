import serial


arduino = serial.Serial("/dev/cu.usbmodem1421")


while(1):

    print arduino.readline()