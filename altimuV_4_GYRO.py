from Adafruit_I2C import Adafruit_I2C
from time import sleep

# initialize i2c connection to MPU6050
# i2c address is 0x68
#LOW_ODR=0x39  # D20H
CTRL_REG4= 0x23 # D20H
CTRL_REG1= 0x20 # D20, 4200D
OUT_X_L        = 0x28
OUT_X_H        = 0x29

i2c = Adafruit_I2C(0x6b)

# wake up the device (out of sleep mode)
# bit 6 on register 0x6B set to 0
#i2c.write8(, 0)
#i2c.write8(LOW_ODR, 0x00)
i2c.write8(CTRL_REG4, 0x20)
i2c.write8(CTRL_REG1, 0x0F)

print("X axis accelerations (in g's)")

# read and print acceleration on x axis
# Most significant byte on 0x3b
# Least significant byte on 0x3c
# Combined to obtain raw acceleration data
for x in range(0, 100):
        # getting values from the registers
        b = i2c.readS8(0x28)
        s = i2c.readU8(0x29)
        # converting 2 8 bit words into a 16 bit
        # signed "raw" value
        raw = b * 256 + s
        # still needs to be converted into G-forces
#	i2c.writeReg(LOW_ODR, 0x00)
#        i2c.writeReg(CTRL_REG4, 0x20)
#        i2c.writeReg(CTRL_REG1, 0x0F)
	
#        g = raw / 16384.
        print (str(raw))
        sleep(0.1)
