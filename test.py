from datetime import datetime

# Get the current date and time
now = datetime.now()

# Extract the time component
current_time = now.strftime("%H:%M:%S")

print(f"Current System Time: {current_time}")