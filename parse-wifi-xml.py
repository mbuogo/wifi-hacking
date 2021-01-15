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

dic_wf = {}
dic_wfclient = {}
dic_apchannel = {}
arquivo = '/tmp/wpa/dump-01.kismet.netxml'

def parse_xml_wf():
    file = open('/tmp/wpa/wifi.txt', 'w')
    filecsv = open('/tmp/wpa/wifi.csv', 'w')
    tree = ET.parse(arquivo)
    root = tree.getroot()
    for i in root.iter('detection-run'):
        for j in i:
            for h in j:
                if(h.tag == 'SSID'):
                    for y in h:
                        if(y.tag == 'essid'):
                            dic_wf[y.tag] = y.text
                        if(y.tag == 'encryption'):
                            dic_wf[y.tag] = y.text
                        if('encryption' not in dic_wf):
                            dic_wf['encryption'] = 'None'
                if(h.tag == 'BSSID'):
                    dic_wf[h.tag] = h.text
                if(h.tag == 'channel'):
                    dic_wf[h.tag] = h.text
            print(dic_wf)
            print("ESSID - "+str(dic_wf['essid'])+" | BSSID - "+str(dic_wf['BSSID'])+" | CHANNEL - "+str(dic_wf['channel'])+" | ENC - "+str(dic_wf['encryption'])+"\n")
            file.write("ESSID - "+str(dic_wf['essid'])+" | BSSID - "+str(dic_wf['BSSID'])+" | CHANNEL - "+str(dic_wf['channel'])+" | ENC - "+str(dic_wf['encryption'])+"\n")
            filecsv.write(str(dic_wf['essid'])+","+str(dic_wf['BSSID'])+","+str(dic_wf['channel'])+","+str(dic_wf['encryption'])+"\n")
    file.close()
    filecsv.close()
           
def parse_xml_wf_client():

    file = open('/tmp/wpa/wifi_clients.txt', 'w')
    filecsv = open('/tmp/wpa/wifi_clients.csv', 'w')
    tree = ET.parse(arquivo)
    root = tree.getroot()
    for i in root.iter('detection-run'):
        for j in i:
            for h in j:
                if(h.tag == 'SSID'):
                    for y in h:
                        if(y.tag == 'essid'):
                            dic_wfclient[y.tag] = y.text
                        if(y.tag == 'encryption'):
                            dic_wfclient[y.tag] = y.text
                if(h.tag == 'BSSID'):
                    dic_wfclient[h.tag] = h.text
                if(h.tag == 'wireless-client'):
                    dic_wfclient['type'] = h.attrib['type']
                    for w in h:
                        if(w.tag == 'client-mac'):
                            dic_wfclient[w.tag] = w.text
                        if(w.tag == 'client-manuf'):
                            dic_wfclient[w.tag] = w.text
                    if(dic_wfclient['essid'] != None):
                        print(dic_wfclient)
                        print("ESSID - "+str(dic_wfclient['essid'])+" | BSSID - "+str(dic_wfclient['BSSID'])+" | CLIENTE MAC - "+str(dic_wfclient['client-mac'])+" | Cliente EQP - "+str(dic_wfclient['client-manuf'])+" | Status - "+str(dic_wfclient['type'])+"\n")
                        file.write("ESSID - "+str(dic_wfclient['essid'])+" | BSSID - "+str(dic_wfclient['BSSID'])+" | Cliente MAC - "+str(dic_wfclient['client-mac'])+" | Cliente EQP - "+str(dic_wfclient['client-manuf'])+" | Status - "+str(dic_wfclient['type'])+"\n")
                        filecsv.write(str(dic_wfclient['essid'])+","+str(dic_wfclient['BSSID'])+","+str(dic_wfclient['client-mac'])+","+str(dic_wfclient['client-manuf'])+","+str(dic_wfclient['type'])+"\n")
    file.close()
    filecsv.close()

def main():
    op = 99
    while (int(op) > 0):
        print("\n 1 - Mostrar lista de Redes\n")
        print(" 2 - Mostrar lista de Clientes\n")
        print(" 0 - Sair\n")
        op = input(" > Digite um número: ")
        os.system('clear')
        if(op == '1'):
            parse_xml_wf()
        if(op == '2'):
            parse_xml_wf_client()

if __name__ == '__main__':
    main()
