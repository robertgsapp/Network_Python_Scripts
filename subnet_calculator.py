print("Subnet Calculator - Find network details.")
ip = input("Enter an IP address (e.g., 192.168.1.0): ")
mask = int(input("Enter subnet mask (e.g., 24 for /24): "))

  # Calculate network and broadcast
octets = [int(x) for x in ip.split('.')]
host_bits = 32 - mask
hosts = 2 ** host_bits - 2  # Subtract 2 for network and broadcast
network = '.'.join(str((octets[i] & (0xff << (24 - i * 8))) >> (24 - i * 8)) for i in range(4))
broadcast = '.'.join(str((octets[i] & (0xff << (24 - i * 8))) | (~(0xff << (24 - mask + i * 8)) & 0xff)) for i in range(4))

print(f"Network Address: {network}/{mask}")
print(f"Broadcast Address: {broadcast}")
print(f"Number of Usable Hosts: {hosts}")
again = input("Calculate another? (yes/no): ").lower()
if again != "yes":
    print("Done calculating.")