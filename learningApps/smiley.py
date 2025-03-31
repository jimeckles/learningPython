from rich import print
from rich.console import Console
import time

console = Console()
slot = 0
goingup = 1


for x in range(50):
    time.sleep(.2)
    if slot == 0:
        goingup = 1
        # slot += 1
    elif slot > 10:
        # slot -= 1
        goingup = 0
    if goingup:
        slot += 1
    else:
        slot -= 1
    
    console.print(" :smiley: " * slot)


