import pydirectinput
import time
import random
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("sim_driver")

print("switch to the game window.")
for i in range(5, 0, -1):
    print(f"Start in {i} seconds...    ", end="\r", flush=True)
    time.sleep(1)
print("press \"Ctrl+C\" to stop")

try:
    while True:
        pydirectinput.keyDown('enter')
        time.sleep(0.1)
        pydirectinput.keyUp('enter')
        print("'enter' pressed")

        race_countdown = 4.0 + random.uniform(0.0, 1.5)
        print(f"race starting in {race_countdown}")
        time.sleep(race_countdown)

        drive_time = 25.5 + random.uniform(-0.5, 2.0)
        print(f"'w' keyDown for {drive_time:.2f}s.")
        pydirectinput.keyDown('w')
        time.sleep(drive_time)
        pydirectinput.keyUp('w')
        print("'w' keyUp")
        
        restart_delay = 8 + random.uniform(1.5, 2.0)
        print(f"restarting race in {restart_delay:.2f}s")
        time.sleep(restart_delay)
        
        print("restarting")
        
        pydirectinput.keyDown('x')
        time.sleep(0.1)
        pydirectinput.keyUp('x')
        print("'x' pressed")
        time.sleep(random.uniform(0.5, 1))
        pydirectinput.keyDown('enter')
        time.sleep(0.1)
        pydirectinput.keyUp('enter')
        print("'enter' pressed")

        print(f"lap done, starting next round in {restart_delay:.2f}")
        time.sleep(restart_delay)
except KeyboardInterrupt:
    pydirectinput.keyUp('w')
    print("program stopped by user")