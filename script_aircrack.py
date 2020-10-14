#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import sys
import os
import requests
import datetime
import requests
import time
import subprocess
import json
import uuid
from time import strftime

if len(sys.argv) < 2:
    print("\n Exemplo: python3 "+ sys.argv[0] + " interface de rede (wlan). \n")
    sys.exit(0)
dic_wf = {}
dic_wfclient = {}
intwf = sys.argv[1]
diretorio = 'temp/'
white_list_aps = ['74:3C:18:94:10:B9', '94:2C:B3:80:D4:EF', 'B8:19:04:EB:9E:69', '94:46:96:97:03:FD', '74:3C:18:6D:3E:A9', '74:3C:18:94:11:69', '18:0D:2C:34:BF:DF']


def airmonng(interface):
    try:
        subprocess.check_output('sudo airmon-ng start '+interface, shell=True)
    except:
        print("\n>> Erro nara subir o modo de Monitoramento.\n")

def airodumpng ():
    os.system('rm -rf temp/*')
    subprocess.check_output('sudo airodump-ng wlan0mon -w temp/wfxml --write-interval 10 --output-format netxml >> /dev/null &', shell=True)

def rogue_ap():

    for u in os.listdir(diretorio):
        filexml  = diretorio+u.rstrip('\n')
        tree = ET.parse(filexml)
        root = tree.getroot()
        for i in root.iter('detection-run'):
            for j in i:
                for h in j:
                    if(h.tag == 'SSID'):
                        for y in h:
                            if(y.tag == 'essid'):
                                dic_wf['essid'] = y.text
                            if(y.tag == 'encryption'):
                                dic_wf['encryption'] = y.text
                    if(h.tag == 'BSSID'):
                        dic_wf['BSSID'] = h.text
                    if(h.tag == 'channel'):
                        dic_wf['channel'] = h.text
                if(dic_wf['BSSID'] not in white_list_aps):
                    print("\n>>> ROGUE AP Detectado - BSSID: "+str(dic_wf['BSSID'])+" | ESSID: "+str(dic_wf['essid'])+" | Channel: "+str(dic_wf['channel']))

def parse_xml_wf():

    for u in os.listdir(diretorio):
        filexml  = diretorio+u.rstrip('\n')
        tree = ET.parse(filexml)
        root = tree.getroot()
        for i in root.iter('detection-run'):
            for j in i:
                for h in j:
                    if(h.tag == 'SSID'):
                        for y in h:
                            if(y.tag == 'essid'):
                                dic_wf['essid'] = y.text
                            if(y.tag == 'encryption'):
                                dic_wf['encryption'] = y.text
                    if(h.tag == 'BSSID'):
                        dic_wf['BSSID'] = h.text
                    if(h.tag == 'channel'):
                        dic_wf['channel'] = h.text
                print(dic_wf)


def parse_xml_wf_client():
    
    for u in os.listdir(diretorio):
        filexml  = diretorio+u.rstrip('\n')
        tree = ET.parse(filexml)
        root = tree.getroot()
        for i in root.iter('detection-run'):
            for j in i:
                for h in j:
                    if(h.tag == 'SSID'):
                        for y in h:
                            if(y.tag == 'essid'):
                                dic_wfclient['essid'] = y.text
                            if(y.tag == 'encryption'):
                                dic_wfclient['encryption'] = y.text
                    if(h.tag == 'BSSID'):
                        dic_wfclient['BSSID'] = h.text
                    if(h.tag == 'channel'):
                        dic_wfclient['channel'] = h.text
                    if(h.tag == 'wireless-client'):
                        dic_wfclient['statusclient'] = h.attrib['type']
                        for w in h:
                            if(w.tag == 'client-mac'):
                                dic_wfclient['macclient'] = w.text
                            if(w.tag == 'client-manuf'):
                                dic_wfclient['equipclient'] = w.text
                        print(dic_wfclient)

def main():

    op = 99
    while (int(op) > 0):
        print("\n 1 - Mostrar lista de Redes\n")
        print(" 2 - Mostrar lista de Clientes\n")
        print(" 3 - Subir modo Monitoramento\n")
        print(" 4 - Realizar o Dump\n")
        print(" 5 - Parar o Dump\n")
        print(" 6 - Identificar Rogue AP\n")
        print(" 0 - Sair\n")
        op = input(" > Digite um número: ")

        os.system('clear')

        if(op == '1'):
            parse_xml_wf()
        if(op == '2'):
            parse_xml_wf_client()
        if(op == '3'):
            airmonng(intwf)
        if(op == '4'):
            airodumpng()
        if(op == '5'):
            os.system("killall airodump-ng")
        if(op == '6'):
            rogue_ap()   
        if(op == '0'):
            os.system('clear')

if __name__ == '__main__':
    main()
