from scapy.all import ARP,Ether,srp

def ag_taramasi(target_ip):
    arp = ARP(pdst=target_ip)
    etrher = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = etrher/arp
    result = srp(packet,timeout=2,verbose=0)[0]
    devices = []

    for sent,recived in result:
        devices.append({'ip':recived.psrc,'mac':recived.hwsrc})
    return devices