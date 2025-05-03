import os
import time

print("Uptime Checker - Monitor website or IP availability!")
while True:
    target = input("Enter a website or IP (e.g., google.com or 8.8.8.8): ")
    start_time = time.time()

      # Ping to check uptime
    response = os.system(f"ping -c 4 {target}")  # 4 pings for reliability
    end_time = time.time()
    duration = end_time - start_time

    if response == 0:
          print(f"{target} is UP! Response time: {duration:.2f} seconds")
    else:
          print(f"{target} is DOWN! Check connectivity.")

    again = input("Check another? (yes/no): ").lower()
    if again != "yes":
          print("Done checking.")
          break