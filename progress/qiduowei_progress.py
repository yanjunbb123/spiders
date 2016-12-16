import subprocess
import os

def get_info(url,filename):
    downloadcmd = 'wget -O '+filename+url
    return_code = subprocess.call(downloadcmd, shell=True)
    if not return_code:
        readcmd = 'cat '+filename
        read = os.popen(readcmd).read()
        #download = os.popen(downloadcmd)
        deletecmd ='rm -rf '+filename
        subprocess.call(deletecmd, shell=True)
        return read
