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
		let cont=cont+1;
		
	done;

fi






CONTADOR=0
while [  $CONTADOR -lt 5 ]; do
      echo "$CONTADOR";
      let CONTADOR=CONTADOR+1; 
done
