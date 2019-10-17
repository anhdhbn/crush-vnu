import chilkat
import sys
import os

class InitChilkat:
    def __init__(self):
        self.unlock_chilkat()
        self.http = chilkat.CkHttp()
        
    def unlock_chilkat(self):
        self.glob = chilkat.CkGlobal()
        success = glob.UnlockBundle(os.getenv("CHILKAT_KEY", "Anything for 30-day trial"))
        if (success != True):
            print(glob.lastErrorText())
            sys.exit()

        status = glob.get_UnlockStatus()
        if (status == 2):
            print("Unlocked using purchased unlock code.")
        else:
            print("Unlocked in trial mode.")