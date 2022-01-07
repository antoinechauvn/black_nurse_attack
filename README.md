# BlackNurse Attack
Découverte d'un nouveau type d'attaque DoS: l'inondation ICMP (BlackNurse)


>L' attaque BlackNurse est une forme d' attaque par déni de service basée sur l' inondation ICMP . L'attaque est particulière car une bande passante modeste de 20 Mbit/s peut être efficace pour perturber le réseau d'une victime.
L'attaque consiste à envoyer des paquets Destination Unreachable vers une destination. Cela fonctionne parce que ces paquets ont amené la destination à consommer des ressources à un taux relativement élevé par rapport au trafic.

>Dans le cas de l'attaque BlackNurse, au lieu d'inonder le trafic Internet d'un système distant de trafic superflu, l'attaque profite d'un déséquilibre entre les ressources nécessaires pour envoyer le trafic et les ressources nécessaires pour le traiter.

>À savoir, les attaques BlackNurse utilisent ICMP avec des paquets de type 3 Code 3.
Il s'agit d'un paquet destiné à être envoyé lorsque le port d'une destination est inaccessible.

>Contrairement aux attaques précédentes utilisant le protocole ICMP - Smurf Attack , Ping flood , Ping of death - BlackNurse n'inonde pas la destination de trafic. Au lieu de cela, les chercheurs ont réalisé que le paquet "Destination Port Unreachable" provoque une utilisation élevée du processeur dans le pare-feu qui le traite.

>En utilisant une bande passante relativement faible de 15 à 18 Mbit/s, un attaquant peut provoquer une augmentation de l'utilisation du processeur dans un pare-feu cible, empêchant ce pare-feu de traiter davantage de demandes.

###### © Wikipedia
