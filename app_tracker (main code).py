import time
from datetime import datetime
import win32gui
import os
from pynput import keyboard
from threading import Thread, Lock

typed_string = ''
trigger = False
target_value = "Spy_mode"
trigger_lock = Lock()

def toggle_trigger():
    # Toggle the trigger state.
    global trigger
    with trigger_lock:
        trigger = not trigger
        print(f"Trigger is now {trigger}")

def on_press(key):
    # Handle key press events.
    global typed_string
    try:
        if hasattr(key, 'char') and key.char:
            typed_string += key.char
            if typed_string == target_value:
                toggle_trigger()
    except AttributeError:
        pass

def on_release(key):
    # Handle key release events.
    global typed_string
    if key == keyboard.Key.space:
        typed_string = ""
    elif key == keyboard.Key.enter:
        return False

def get_active_window():
    """Get the title of the currently active window."""
    try:
        return win32gui.GetWindowText(win32gui.GetForegroundWindow())
    except Exception as e:
        return f"Error: {str(e)}"

def monitor_app_usage():
    """Monitor active window usage and log it when trigger is off."""
    log_file_path = os.path.join(os.path.expanduser("~"), "Documents", f"app_usage_log_{datetime.now().strftime('%Y-%m-%d')}.txt")
    last_app = None

    while True:
        with trigger_lock:
            if not trigger:
                active_window = get_active_window()
                if active_window and active_window != last_app:
                    log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {active_window}\n"
                    with open(log_file_path, "a") as log_file:
                        log_file.write(log_entry)
                    print(log_entry.strip())
                    last_app = active_window
        time.sleep(0.5)
def get_active_window():
    """Get the title of the currently active window."""
    try:
        return win32gui.GetWindowText(win32gui.GetForegroundWindow())
    except Exception as e:
        return f"Error: {str(e)}"

def monitor_app_usage():
    """Monitor active window usage and log it when trigger is off."""
    log_file_path = os.path.join(os.path.expanduser("~"), "Documents", f"app_usage_log_{datetime.now().strftime('%Y-%m-%d')}.txt")
    last_app = None

    while True:
        with trigger_lock:
            if not trigger:
                active_window = get_active_window()
                if active_window and active_window != last_app:
                    log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {active_window}\n"
                    with open(log_file_path, "a") as log_file:
                        log_file.write(log_entry)
                    print(log_entry.strip())
                    last_app = active_window
        time.sleep(0.5)
if __name__ == "__main__":
    print(f"Start typing. Press 'Enter' to finish. Press 'Space' to reset. Trigger toggles when typing '{target_value}'.")

    # Start key listener in a separate thread
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener_thread = Thread(target=listener.start, daemon=True)
    listener_thread.start()

    # Start app usage monitoring
    monitor_app_usage()
