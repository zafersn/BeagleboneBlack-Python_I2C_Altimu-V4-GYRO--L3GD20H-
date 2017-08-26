from Adafruit_I2C import Adafruit_I2C
from time import sleep


CTRL_REG4= 0x23 # D20H
CTRL_REG1= 0x20 # D20, 4200D
OUT_X_L        = 0x28
OUT_X_H        = 0x29

i2c = Adafruit_I2C(0x6b)


i2c.write8(CTRL_REG4, 0x20)
i2c.write8(CTRL_REG1, 0x0F)

print("X axis accelerations (in g's)")

for x in range(0, 100):
        # getting values from the registers
        b = i2c.readS8(0x28)
        s = i2c.readU8(0x29)
        # converting 2 8 bit words into a 16 bit
        # signed "raw" value
        raw = b * 256 + s
        # still needs to be converted into G-forces

	
#        g = raw / 16384.
        print (str(raw))
        sleep(0.1)
