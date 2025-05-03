import os
import time

print("Ping Tester (Website or IP)")
while True:
    try:
        target = input("Enter a website or IPv4: ")

        # Ping 3 times
        for i in range(3):
            response = os.system(f"ping -c 1 {target}")
            if response == 0:
                print(f"{target} is ONLINE!")
            else:
                print(f"{target} is DOWN!")
            time.sleep(1)  # Wait 1 second between each ping

    except Exception as e:  # Check for input error
        print(f"Error: {e} - Check input!")
        continue  # Skip to the next iteration if there's an error

    # Ask if the user wants to test another
    again = input("Test another? (yes/no): ").lower()
    if again != "yes":
        print("Done testing.")
        break