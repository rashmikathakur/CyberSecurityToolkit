import nmap

network = input("\nEnter Network Range (example 192.168.1.0/24): ")

print("\nScanning Network:", network)

nm = nmap.PortScanner()

nm.scan(hosts=network, arguments='-sn')

for host in nm.all_hosts():

    print("Active Host:", host)
