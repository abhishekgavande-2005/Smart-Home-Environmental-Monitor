import random
import tkinter as tk
from tkinter import ttk
from datetime import datetime

class MonitorDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Home Environmental Monitor — Software Simulation")
        self.root.geometry("720x500")
        self.root.minsize(620, 440)
        self.running = True
        self.event_mode = False
        self.temp_limit = tk.DoubleVar(value=32.0)
        self.humidity_limit = tk.DoubleVar(value=70.0)
        self.air_limit = tk.IntVar(value=65)
        self.temp = 25.0
        self.humidity = 48.0
        self.air = 25
        self.status = tk.StringVar(value="NORMAL")
        self._build_ui()
        self._tick()

    def _build_ui(self):
        outer = ttk.Frame(self.root, padding=18)
        outer.pack(fill="both", expand=True)
        ttk.Label(outer, text="SMART HOME ENVIRONMENT MONITOR", font=("Segoe UI", 16, "bold")).pack(anchor="w")
        ttk.Label(outer, text="Desktop simulation — values are synthetic, not physical sensor readings.",
                  foreground="#9b3d19").pack(anchor="w", pady=(2, 14))

        cards = ttk.Frame(outer)
        cards.pack(fill="x")
        self.temp_label = self._card(cards, "Temperature", "25.0 °C", 0)
        self.hum_label = self._card(cards, "Humidity", "48.0 %RH", 1)
        self.air_label = self._card(cards, "Air-quality indicator", "25 / 100", 2)

        settings = ttk.LabelFrame(outer, text="Alert thresholds", padding=10)
        settings.pack(fill="x", pady=14)
        ttk.Label(settings, text="Temperature °C").grid(row=0, column=0, sticky="w")
        ttk.Spinbox(settings, from_=15, to=50, increment=0.5, textvariable=self.temp_limit, width=8).grid(row=0, column=1, padx=8)
        ttk.Label(settings, text="Humidity %RH").grid(row=0, column=2, sticky="w")
        ttk.Spinbox(settings, from_=20, to=95, increment=1, textvariable=self.humidity_limit, width=8).grid(row=0, column=3, padx=8)
        ttk.Label(settings, text="Air index").grid(row=0, column=4, sticky="w")
        ttk.Spinbox(settings, from_=10, to=100, increment=5, textvariable=self.air_limit, width=8).grid(row=0, column=5, padx=8)

        status_frame = ttk.Frame(outer)
        status_frame.pack(fill="x", pady=(0, 10))
        ttk.Label(status_frame, text="SYSTEM STATUS:", font=("Segoe UI", 10, "bold")).pack(side="left")
        self.status_label = ttk.Label(status_frame, textvariable=self.status, font=("Segoe UI", 11, "bold"))
        self.status_label.pack(side="left", padx=8)
        self.time_label = ttk.Label(status_frame, text="")
        self.time_label.pack(side="right")

        buttons = ttk.Frame(outer)
        buttons.pack(fill="x", pady=5)
        ttk.Button(buttons, text="Simulate threshold event", command=self.trigger_event).pack(side="left")
        self.pause_btn = ttk.Button(buttons, text="Pause", command=self.toggle_pause)
        self.pause_btn.pack(side="left", padx=8)
        ttk.Button(buttons, text="Reset values", command=self.reset_values).pack(side="left")

        self.log = tk.Text(outer, height=5, wrap="word", state="disabled")
        self.log.pack(fill="both", expand=True, pady=(10, 0))
        self._log("Simulation initialized. All readings are generated in software.")

    def _card(self, parent, title, value, col):
        frame = ttk.LabelFrame(parent, text=title, padding=12)
        frame.grid(row=0, column=col, sticky="nsew", padx=(0 if col == 0 else 8, 0))
        parent.columnconfigure(col, weight=1)
        label = ttk.Label(frame, text=value, font=("Segoe UI", 16, "bold"))
        label.pack(pady=8)
        return label

    def _log(self, message):
        self.log.configure(state="normal")
        self.log.insert("end", f"[{datetime.now().strftime('%H:%M:%S')}] {message}\n")
        self.log.see("end")
        self.log.configure(state="disabled")

    def trigger_event(self):
        self.event_mode = True
        self.temp = max(self.temp, float(self.temp_limit.get()) + 2.5)
        self.humidity = max(self.humidity, float(self.humidity_limit.get()) + 5)
        self.air = max(self.air, int(self.air_limit.get()) + 10)
        self._log("Test event injected: synthetic readings raised above configured thresholds.")
        self._update_display()

    def toggle_pause(self):
        self.running = not self.running
        self.pause_btn.configure(text="Pause" if self.running else "Resume")
        self._log("Simulation resumed." if self.running else "Simulation paused.")

    def reset_values(self):
        self.event_mode = False
        self.temp, self.humidity, self.air = 25.0, 48.0, 25
        self._log("Synthetic readings reset to normal-range demo values.")
        self._update_display()

    def _update_display(self):
        self.temp_label.configure(text=f"{self.temp:.1f} °C")
        self.hum_label.configure(text=f"{self.humidity:.1f} %RH")
        self.air_label.configure(text=f"{self.air} / 100")
        alert = (self.temp >= self.temp_limit.get() or
                 self.humidity >= self.humidity_limit.get() or
                 self.air >= self.air_limit.get())
        self.status.set("ALERT — THRESHOLD EXCEEDED" if alert else "NORMAL")
        self.status_label.configure(foreground="#b22222" if alert else "#187a3b")
        self.time_label.configure(text=datetime.now().strftime("Updated %H:%M:%S"))

    def _tick(self):
        if self.running and not self.event_mode:
            self.temp = min(38, max(18, self.temp + random.uniform(-0.45, 0.45)))
            self.humidity = min(85, max(25, self.humidity + random.uniform(-1.2, 1.2)))
            self.air = min(90, max(5, self.air + random.randint(-4, 4)))
            self._update_display()
        elif self.running and self.event_mode:
            self._update_display()
        self.root.after(1500, self._tick)

if __name__ == "__main__":
    root = tk.Tk()
    app = MonitorDashboard(root)
    root.mainloop()
