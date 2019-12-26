#!/bin/bash

if [ "$1" == "" ] #testa o argumento
then
        echo "Siga o exemplo abaixo para passagem de parametros. INTERFACE + SSID + RANGE IP"
        echo "$0 [wlan1 | wlan0] SSID 192.168.1.0"

else

	echo "#################################"
	echo "######### HIJACK HOTSPOT ########"
	echo "#################################"

	echo "\n
