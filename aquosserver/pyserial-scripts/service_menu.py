import serial
import time

ser = serial.Serial(
	port='/dev/ttyUSB0',
	baudrate=9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

ser.close()
ser.open()
ser.isOpen()

SERVICE_MENU = "\x10000\x00000010\x10\x01\x40"
# SERVICE_MENU = "\x0000\x006d\x0000\x0020\x000a\x0047\x000a\x001e\x000a\x001e\x000a\x001e\x000a\x001e\x000a\x001e\x000a\x001e\x000a\x001e\x000a\x001e\x000a\x001e\x000a\x001e\x000a\x0047\x000a\x001e\x000a\x0047\x000a\x001e\x000a\x068b\x000a\x0047\x000a\x001e\x000a\x001e\x000a\x001e\x000a\x001e\x000a\x0047\x000a\x0047\x000a\x0047\x000a\x0047\x000a\x0047\x000a\x0047\x000a\x001e\x000a\x0047\x000a\x001e\x000a\x0047\x000a\x068b"
# SERVICE_MENU = "\x00\x00\x18\x00\xD3\x03\x00\x84\x03\x9C\x00\x84\x01\x8C\x00\x84\x55\x14\x90\x01\x11\x11\x11\x11\x10\x10\x12\r"
# SERVICE_MENU = "00 00 18 00 D3 03 00 84 03 9C 00 84 01 8C 00 84 55 14 90 01 11 11 11 11 10 10 12"
# SERVICE_MENU = "\x00\x00\x20\x00\xD3\x03\x00\x84\x03\x9C\x00\x84\x01\x8C\x00\x84\x55\x14\xA0\x01\x11\x11\x11\x11\x10\x10\x12\x01\x11\x10\x00\x00\x01\x01\x02\r"
# SERVICE_MENU = "00 00 20 00 D3 03 00 84 03 9C 00 84 01 8C 00 84 55 14 A0 01 11 11 11 11 10 10 12 01 11 10 00 00 01 01 02"

POWER_OFF = "\x10001\x11010010\x10\x11\x1\x4B"
# POWER_OFF = "\x0000\x006D\x0000\x0020\x000A\x0046\x000A\x001E\x000A\x001E\x000A\x001E\x000A\x0046\x000A\x0046\x000A\x0046\x000A\x001E\x000A\x0046\x000A\x001E\x000A\x001E\x000A\x0046\x000A\x001E\x000A\x0046\x000A\x001E\x000A\x0679\x000A\x0046\x000A\x001E\x000A\x001E\x000A\x001E\x000A\x0046\x000A\x001E\x000A\x001E\x000A\x0046\x000A\x001E\x000A\x0046\x000A\x0046\x000A\x001E\x000A\x0046\x000A\x001E\x000A\x0046\x000A\x0679"

ser.write(SERVICE_MENU)
# ser.write(SERVICE_MENU.decode('hex')+'\r\n')
REPLY = ser.read(1)
print(REPLY)
ser.close()