#!/bin/bash

cont=1

if [ "$1" == "" ] #testa o argumento
then
        echo "Siga o exemplo abaixo para passagem de parametros. INTERFACE + SSID + RANGE IP"
        echo "$0 [wlan1 | wlan0] SSID 192.168.1."

else

	echo "#################################"
	echo "######### HIJACK HOTSPOT ########"
	echo "#################################"
	
	iwconfig $1 essid $2
	
	while [ $cont -lt 254 ]; do
		ip_target=$3$cont;
		ping $ip_target -c1;
		mac_target=$(arp -n | grep $ip_target | grep -v incomplete | awk '{print $3}');

		if [ -z $mac_target]
		then
			let cont=cont+1
		else
			echo $ip_target " - " $mac_target >> bola.txt
			let cont=cont+1
		fi
		
	done;

fi
