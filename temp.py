import subprocess
import time

while True:
	subprocess.call(['./temp.sh'], shell=True)
	time.sleep(2)
