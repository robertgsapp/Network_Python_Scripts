import socket

print("Port Scanner - Check open ports!")
target = input("Enter a target IP (e.g., 8.8.8.8): ")
port = int(input("Enter a port to scan (e.g., 80): "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)  # 2-second timeout
result = sock.connect_ex((target, port))

if result == 0:
    print(f"Port {port} is OPEN on {target}!")
else:
    print(f"Port {port} is CLOSED on {target}!")
sock.close()

again = input("Scan another? (yes/no): ").lower()
if again != "yes":
    print("Done scanning.")