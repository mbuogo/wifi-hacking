#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import sys
import os
import requests
import datetime
import requests
import time
import json
import uuid
from time import strftime

dic_wf = {}
dic_wfclient = {}
arquivo = 'testexml.xml'
intwf = sys.argv[1]

def airmonng(interface):
    subprocess.check_output('sudo airmon-ng start '+interface, shell=True)

def airodumpng ():
    subprocess.check_output('sudo airodump-ng wlan0mon -w wfxml --output-format netxml', shell=True)

def parse_xml_wf(filexml):
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


def parse_xml_wf_client(filexml):
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
    xml = arquivo
    while (int(op) > 0):
        print("###############################")
        print(" 1 - Mostrar lista de Redes\n")
        print(" 2 - Mostrar lista de Clientes\n")
        print(" 0 - Sair\n")
        op = input(" > Digite um número: ")

        os.system('clear')
        print("###############################")

        if(op == '1'):
            parse_xml_wf(xml)
        if(op == '2'):
            parse_xml_wf_client(xml)
        if(op == '0'):
            os.system('clear')

if __name__ == '__main__':
    main()
