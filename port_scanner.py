import nmap

target = input("\nEnter Target IP Address: ")

print("\nScanning Target:", target)

nm = nmap.PortScanner()

nm.scan(target, '1-1024', '-sV')

for host in nm.all_hosts():

    print("\nHost:", host)

    for proto in nm[host].all_protocols():

        ports = nm[host][proto].keys()

        for port in ports:

            service = nm[host][proto][port]['name']

            print(f"Port {port} → {service}")

            if port == 21:
                print("⚠ FTP Risk")

            elif port == 22:
                print("⚠ SSH Risk")

            elif port == 23:
                print("⚠ Telnet Risk")

            elif port == 80:
                print("⚠ HTTP Risk")

            elif port == 443:
                print("✔ HTTPS Secure")
