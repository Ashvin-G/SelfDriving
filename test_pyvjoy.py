import pyvjoy
import time

j = pyvjoy.VJoyDevice(1)

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

j.set_button(2, 1)
j.set_button(2, 0)

j.update()

j.reset()