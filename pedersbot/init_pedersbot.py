import subprocess
import time

connected = False
while connected == False:
        time.sleep( 5 )
        try:
            subprocess.check_call(["python3", "/home/ubuntu/scripts/pedersbot/pedersbot.py"])


        except subprocess.CalledProcessError:
            # grep did not match any lines
            connected = False
