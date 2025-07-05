from pathlib import Path

# Define the cleaned and modernized main_ui.py code with ttkbootstrap styling
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from ttkbootstrap import Style, Window
from ttkbootstrap.constants import *

import ttkbootstrap as ttk

sys.path.append(os.path.relpath("First-Come-First-Serve-scheduling"))
sys.path.append(os.path.relpath("Priority-Scheduling"))
sys.path.append(os.path.relpath("Round-Robin-scheduling"))
sys.path.append(os.path.relpath("Shortest-Job-First-scheduling"))

from FCFS import simulate_fcfs_algorithm
from RR import simulate_rr_algorithm
from SJF_np import simulate_sjf_np_algorithm
from SJF_p import simulate_sjf_p_algorithm
from priority_np import simulate_priority_np_algorithm
from priority_p import simulate_priority_p_algorithm

LARGE_FONT = ("Arial", 25)
awt_arr = []
att_arr = []
art_arr = []

class tkinterApp(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = Style("cyborg")

        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, FCFS, SJF_np, SJF_p, RR, PriorityNP, PriorityP, Chart):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(style="secondary.TFrame")

        title = ttk.Label(self, text="🧠 CPU Scheduling Simulator", font=("Helvetica", 28, "bold"), bootstyle="primary")
        title.pack(pady=30)

        buttons = [
            ("FCFS", FCFS),
            ("SJF NP", SJF_np),
            ("SJF P", SJF_p),
            ("RR", RR),
            ("Priority NP", PriorityNP),
            ("Priority P", PriorityP),
            ("Chart", Chart)
        ]

        for text, frame in buttons:
            b = ttk.Button(self, text=text, bootstyle="info", width=20, command=lambda f=frame: controller.show_frame(f))
            b.pack(pady=10)


def print_result(root, result):
    y = 100
    for label_text in [
        f"Number of processes = {result['n']}",
        f"Throughput = {result['throughput']}",
        f"CPU utilization = {result['cpu_util']}",
        f"Average waiting time = {result['awt']}",
        f"Average turn around time = {result['att']}",
        f"Average response time = {result['art']}"
    ]:
        label = ttk.Label(root, text=label_text, font=LARGE_FONT, bootstyle="warning")
        label.place(x=20, y=y)
        y += 50


def set_data_for_chart(result):
    awt_arr.append(float(result['awt']))
    att_arr.append(float(result['att']))
    art_arr.append(float(result['art']))


class FCFS(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(style="dark.TFrame")
        ttk.Label(self, text="First Come First Served algorithm:", font=LARGE_FONT, bootstyle="info").pack(pady=20)
        result = simulate_fcfs_algorithm(data)
        set_data_for_chart(result)
        print_result(self, result)
        ttk.Button(self, text="Back", bootstyle="danger", command=lambda: controller.show_frame(StartPage)).pack(pady=20)


class SJF_np(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(style="dark.TFrame")
        ttk.Label(self, text="SJF non-preemptive algorithm:", font=LARGE_FONT, bootstyle="info").pack(pady=20)
        result = simulate_sjf_np_algorithm(data)
        set_data_for_chart(result)
        print_result(self, result)
        ttk.Button(self, text="Back", bootstyle="danger", command=lambda: controller.show_frame(StartPage)).pack(pady=20)


class SJF_p(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(style="dark.TFrame")
        ttk.Label(self, text="SJF preemptive algorithm:", font=LARGE_FONT, bootstyle="info").pack(pady=20)
        result = simulate_sjf_p_algorithm(data)
        set_data_for_chart(result)
        print_result(self, result)
        ttk.Button(self, text="Back", bootstyle="danger", command=lambda: controller.show_frame(StartPage)).pack(pady=20)


class RR(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(style="dark.TFrame")
        ttk.Label(self, text="Round-Robin algorithm:", font=LARGE_FONT, bootstyle="info").pack(pady=20)
        result = simulate_rr_algorithm(data, 1)
        set_data_for_chart(result)
        print_result(self, result)
        ttk.Button(self, text="Back", bootstyle="danger", command=lambda: controller.show_frame(StartPage)).pack(pady=20)


class PriorityNP(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(style="dark.TFrame")
        ttk.Label(self, text="Priority non-preemptive algorithm:", font=LARGE_FONT, bootstyle="info").pack(pady=20)
        result = simulate_priority_np_algorithm(data)
        set_data_for_chart(result)
        print_result(self, result)
        ttk.Button(self, text="Back", bootstyle="danger", command=lambda: controller.show_frame(StartPage)).pack(pady=20)


class PriorityP(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(style="dark.TFrame")
        ttk.Label(self, text="Priority preemptive algorithm:", font=LARGE_FONT, bootstyle="info").pack(pady=20)
        result = simulate_priority_p_algorithm(data)
        set_data_for_chart(result)
        print_result(self, result)
        ttk.Button(self, text="Back", bootstyle="danger", command=lambda: controller.show_frame(StartPage)).pack(pady=20)


class Chart(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(style="dark.TFrame")
        ttk.Label(self, text="Chart:", font=LARGE_FONT, bootstyle="info").pack(pady=20)

        df = pd.DataFrame(
            {
                'avg_waiting_time': awt_arr,
                'avg_turnaround_time': att_arr,
                'avg_response_time': art_arr
            },
            index=['fcfs', 'sjf_np', 'sjf_p', 'rr', 'priority_np', 'priority_p']
        )

        def bar_plot():
            df.plot.bar(rot=0)
            plt.title('Scheduling Algorithms Chart')
            plt.xlabel('Algorithms')
            plt.ylabel('Time (seconds)')
            plt.grid()
            plt.show()

        ttk.Button(self, text="Show Chart", bootstyle="success", command=bar_plot).pack(pady=10)
        ttk.Button(self, text="Back", bootstyle="danger", command=lambda: controller.show_frame(StartPage)).pack(pady=10)


if __name__ == "__main__":
    csv_path = os.path.join(os.path.dirname(__file__), "db", "data_set.csv")
    data = pd.read_csv(csv_path)

    app = tkinterApp()
    app.wm_geometry("600x500")
    app.title("CPU Scheduling Algorithms Simulator")
    app.resizable(False, False)
    app.mainloop()


# Save the cleaned-up UI code to main_ui_refactored.py
output_path = Path("/mnt/data/main_ui.py")
output_path.write_text(main_ui_code)

output_path.name

