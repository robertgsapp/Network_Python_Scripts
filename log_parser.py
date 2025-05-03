print("Log Parser - Find errors in network logs!")
log_text = input("Paste a log entry (e.g., 'ERROR: Connection failed'): ")

if "ERROR" in log_text.upper():
      print("Error detected! Check the log for issues.")
      error_count = log_text.upper().count("ERROR")
      print(f"Found {error_count} error(s).")
else:
      print("No errors found in this log entry.")

again = input("Parse another log? (yes/no): ").lower()
if again != "yes":
      print("Done parsing.")