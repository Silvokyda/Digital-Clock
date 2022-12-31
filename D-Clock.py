import tkinter as tk
import time

# Create the main window
window = tk.Tk()
window.title("Digital Clock")

# Create a label to display the time
time_label = tk.Label(window, font=("Helvetica", 60))
time_label.pack()

# Function to update the time display
def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    time_label.configure(text=current_time)
    window.after(1000, update_time)

# Call the update_time function to start the clock
update_time()

# Run the main loop
window.mainloop()
