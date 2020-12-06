import pyvjoy
import time

j = pyvjoy.VJoyDevice(1)


for i in range(8, 0, -1):
    print(i)
    time.sleep(1)



j.set_button(0, 1)
