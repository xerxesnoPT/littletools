from scapy.all import *
def packet_callback(packet):
    if packet[TCP].payload:
        mail_packet = bytes(packet[TCP].payload)
        print("start!!")
        #  if "user" in str(mail_packet).lower() or "pass" in str(mail_packet).lower():
        print ("[*] Server : %s" % packet[IP].dst)
        #  b = bytes(packet[TCP].payload)
        #  print ("[*]  %s" % b.decode('ascii',errors='ignore'))
        print ("[*]  %s" % packet[TCP].payload)

sniff(filter='tcp port 110 or tcp port 25 or tcp port 143',prn=packet_callback)
