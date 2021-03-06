from tkinter import Tk
from tkinter import StringVar
from tkinter import ttk
from tkinter import messagebox
import os


class ShutdownTimerApp:
    def __init__(self, parent):
        # Fields
        self.minutesEntryValue = StringVar(parent, value="10")

        # Labels
        titleLabelText = "Schedule the computer to power off"
        self.titleLabel = ttk.Label(parent, text=titleLabelText)
        self.titleLabel.grid(row=0, column=0, columnspan=2)

        self.minutesLabel = ttk.Label(parent, text="Minutes")
        self.minutesLabel.grid(row=1, column=0)

        # Minutes input/entry
        self.minutesEntry = ttk.Entry(parent,
                                      textvariable=self.minutesEntryValue)
        self.minutesEntry.grid(row=1, column=1)

        # Buttons
        self.cancelButton = ttk.Button(parent, text="[ESC] Cancel Shutdown",
                                       command=self.cancel_shutdown)
        self.cancelButton.grid(row=2, column=0)
        self.startButton = ttk.Button(parent, text="Start Shutdown Timer",
                                      command=self.shutdown)
        self.startButton.grid(row=2, column=1)

        parent.bind('<KeyPress>', self.on_key_pressed)

    def on_key_pressed(self, event):
        if event.keycode == 27:  # 27 = escape keycode
            self.cancel_shutdown()

    def shutdown(self):
        try:
            val = int(self.minutesEntryValue.get())
        except ValueError:
            errorTitle = "Value error"
            errorMsg = "Minutes must be a whole number"
            messagebox.showerror(errorTitle, errorMsg)
            return

        if val <= 0:
            messagebox.showerror("Value error", "Minutes must be positive")
            return

        os.system("shutdown -s -t {}".format(val*60))

    def cancel_shutdown(self):
        os.system("shutdown /a")


def main():
    root = Tk()
    ShutdownTimerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
