import serial

opencr = serial.Serial(port='/dev/ttyACM0')

while True:
    str = input ('ENTER')
    opencr.write(bytes(str,'utf-8'))
    value= opencr.readline()
    print('Result:', value)