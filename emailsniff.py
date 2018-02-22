from scapy.all import *
def packet_callback(packet):
    if packet[TCP].payload:
        mail_packet = packet[TCP].payload
        print(mail_packet)
        #  if "user" in mail_packet.lower() or "pass" in mail_packet.lower():
            #  print ("[*] Server : %s" % packet[IP].dst)
            #  print ("[*]  %s" % packet[TCP].payload)

sniff(filter='tcp port 110 or tcp port 25 or tcp port 143',prn=packet_callback)
