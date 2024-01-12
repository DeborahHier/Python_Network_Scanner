from scapy.all import ARP, Ether, srp
import os

# script may need to be run with 'sudo'
# Replace with your target IP range. Only use on networks that you have permission to do so!
target_ip = os.getenv('MY_NETWORK_SCANNER_IP') # "xx.x.x.x/24"
arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp

result, _ = srp(packet, timeout=3, verbose=0)

devices = []
for sent, received in result:
    devices.append({'ip': received.psrc, 'mac': received.hwsrc})

print("IP" + " "*18+"MAC")
for device in devices:
    print("{:16}    {}".format(device['ip'], device['mac']))

