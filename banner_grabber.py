import socket

def banner_grab():
    target = input("Enter Target IP: ")
    port = int(input("Enter Port Number: "))

    try:
        s = socket.socket()
        s.settimeout(3)

        print("\nConnecting to target...\n")

        s.connect((target, port))

        # Send HTTP request
        request = "HEAD / HTTP/1.1\r\nHost: {}\r\n\r\n".format(target)
        s.send(request.encode())

        banner = s.recv(1024)

        print("Banner Received:\n")
        print(banner.decode())

        s.close()

    except Exception as e:
        print("Error grabbing banner:", e)

banner_grab()
