import subprocess
import time

while True:
	subprocess.call(['/home/pi/temp.sh'], shell=True)
	time.sleep(2)
