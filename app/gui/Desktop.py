import tkinter as tk

class Desktop:
    def __init__(self, root):
        self.root = root
        self.root.geometry("640x480")
        self.root.title("Sterowanie Piecykiem")
        
        self.off_delay = 0
        self.on_delay = 0

        self.freq_var = tk.StringVar()
        self.cycle_var = tk.StringVar()
        self.voltage_var = tk.StringVar()
        self.current_var = tk.StringVar()
        self.power_var = tk.StringVar()
        self.energy_var = tk.StringVar()
        self.temperature = tk.StringVar()

        self.create_widgets()

    def set_impulses(self):
        self.off_delay = float(self.spinbox_impulse_prev.get())
        self.on_delay = float(self.spinbox_impulse_after.get())

    def clear_inputs(self):
        self.spinbox_impulse_prev.delete(0, 'end')
        self.spinbox_impulse_prev.insert(0, '0')
        self.spinbox_impulse_after.delete(0, 'end')
        self.spinbox_impulse_after.insert(0, '0')

    def set_inputs(self):
        self.off_delay = float(self.spinbox_impulse_prev.get())
        self.on_delay = float(self.spinbox_impulse_after.get())

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=(10, 10))

        tk.Label(frame, text="Frequency (Hz):", anchor="center").grid(row=0, column=0, padx=(10, 10), pady=(10, 10))
        tk.Label(frame, textvariable=self.freq_var, anchor="center").grid(row=0, column=1, padx=(10, 10), pady=(10, 10))

        tk.Label(frame, text="Cycle (ms):", anchor="center").grid(row=1, column=0, padx=(10, 10))
        tk.Label(frame, textvariable=self.cycle_var, anchor="center").grid(row=1, column=1, padx=(10, 10))

        tk.Label(frame, text="TRIAC OFF DELAY (ms):", anchor="center").grid(row=2, column=0, padx=(10, 10), pady=(10, 10))
        self.impulse_prev_var = tk.DoubleVar(value=0)
        self.spinbox_impulse_prev = tk.Spinbox(frame, from_=0, to=5000, increment=1, textvariable=self.impulse_prev_var, width=5)
        self.spinbox_impulse_prev.grid(row=2, column=1, padx=(10, 10), pady=(10, 10))

        tk.Label(frame, text="TRIAC ON DELAY (ms):", anchor="center").grid(row=3, column=0, padx=(10, 10), pady=(10, 10))
        self.impulse_after_var = tk.DoubleVar(value=0)
        self.spinbox_impulse_after = tk.Spinbox(frame, from_=0, to=5000, increment=1, textvariable=self.impulse_after_var, width=5)
        self.spinbox_impulse_after.grid(row=3, column=1, padx=(10, 10), pady=(10, 10))

        tk.Button(frame, text="CLEAR", command=self.clear_inputs, anchor="center").grid(row=3, column=2, padx=(10, 10), pady=(10, 10))
        tk.Button(frame, text="SET", command=self.set_inputs, anchor="center").grid(row=3, column=3, padx=(10, 10), pady=(10, 10))

        tk.Label(frame, text="Voltage (V):", anchor="center").grid(row=4, column=0, padx=(10, 10), pady=(10, 10))
        tk.Label(frame, textvariable=self.voltage_var, anchor="center").grid(row=4, column=1, padx=(10, 10), pady=(10, 10))

        tk.Label(frame, text="Current (A):", anchor="center").grid(row=5, column=0, padx=(10, 10), pady=(10, 10))
        tk.Label(frame, textvariable=self.current_var, anchor="center").grid(row=5, column=1, padx=(10, 10), pady=(10, 10))

        tk.Label(frame, text="Power (W):", anchor="center").grid(row=6, column=0, padx=(10, 10), pady=(10, 10))
        tk.Label(frame, textvariable=self.power_var, anchor="center").grid(row=6, column=1, padx=(10, 10), pady=(10, 10))

        tk.Label(frame, text="Energy (Wh):", anchor="center").grid(row=7, column=0, padx=(10, 10), pady=(10, 10))
        tk.Label(frame, textvariable=self.energy_var, anchor="center").grid(row=7, column=1, padx=(10, 10), pady=(10, 10))

        tk.Label(frame, text="Temperature ('C):", anchor="center").grid(row=8, column=0, padx=(10, 10), pady=(10, 10))
        tk.Label(frame, textvariable=self.temperature, anchor="center").grid(row=8, column=1, padx=(10, 10), pady=(10, 10))

        tk.Button(frame, text="FINISH", command=self.stop_program, anchor="center").grid(row=9, column=0, columnspan=4, padx=(10, 10), pady=(10, 10))

    def stop_program(self):
        self.root.quit()
        self.root.destroy()
        