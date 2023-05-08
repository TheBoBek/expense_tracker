from tkinter import *
import json
from datetime import date, datetime
import math

BACKGROUND = "f8f9fa"
from datetime import date, datetime

WHITE = "#ced4da"
BLACK = "#343a40"
GREEN = "#4f9d69"


class MainWindow(Tk):
    def __init__(self, y_values, chart_data):
        super().__init__()
        self.canvas = None
        self.chart_data = chart_data
        self. y_values = y_values
        self.trans_types = ["Domácnosť", "Strava", "Zdravie a poistenie", "Zábava", "Cestovanie", "Iné"]
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        # setting tkinter window size
        # Define a list of colors for the pie chart
        self.colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
        self.geometry("%dx%d" % (width, height))
        self.title("Expense Tracker2")
        self.config(bg="#ced4da", width=1280, height=720)
        self.eval('tk::PlaceWindow . center')
        self.config(bg=WHITE)
        self.geometry("1280x750")

        header = Canvas()
        header.config(width=1094, height=80, bg=BLACK, highlightthickness=0)
        header.pack(fill=BOTH, ipady=40, ipadx=20)
        self.left_header = Frame(header, bg=BLACK)
        self.left_header.pack(side=LEFT)
        Label(self.left_header,
              text="Šimon Bobko",
              fg=WHITE,
              bg=BLACK,
              font=("Helvetica", 25, "bold")).pack(side=LEFT, ipadx=20)
        Label(header,
              text=str(date.today()),
              fg=WHITE,
              bg=BLACK,
              font=("Helvetica", 25, "bold")).pack(side=RIGHT, ipadx=20)

        # zmen dizajn... vymen button txt za img
        self.pridaj_button = Button(self.left_header,
                                    text="Pridaj",
                                    fg=BLACK,
                                    highlightthickness=0,
                                    borderwidth=0,
                                    width=10,
                                    font=("Helvetica", 25, "bold"))
        self.pridaj_button.pack(side=RIGHT)

        self.body_frame = Frame(bg=WHITE)
        self.body_frame.pack(fill=BOTH)

        self.left_body = Frame(self.body_frame, bg=WHITE)
        self.left_body.pack(side=LEFT, ipadx=1, expand=True)
        self.money_canvas = Canvas(self.left_body)
        self.money_canvas.config(bg=GREEN, width=80, height=50, highlightthickness=0, borderwidth=30)
        self.money_canvas.pack(ipady=20, ipadx=20)
        Label(self.money_canvas,
              text=f"Tvoj zostatok na účte je:",
              fg=WHITE,
              bg=GREEN,
              font=("Helvetica", 23, "normal")).pack(ipady=20)
        self.value_label = Label(self.money_canvas,
                                 fg=WHITE,
                                 bg=GREEN,
                                 font=("Helvetica", 30, "bold"),
                                 text="")
        self.value_label.pack()

        self.empty = Canvas(self.left_body, height=1, width=1, bg=WHITE, highlightthickness=0)
        self.empty.pack(ipady=15)

        self.cake_frame = Frame(self.left_body, highlightthickness=0, bg="#ececec", borderwidth=30)
        self.cake_frame.pack()
        self.cake_graph = Canvas(self.cake_frame)
        self.cake_graph.config(width=320, height=230, highlightthickness=0, bg="#ececec")
        self.cake_graph.pack()

        self.data_graph(y_values)
        self.pie_chart_description = Frame(self.cake_frame, bg="#ececec", height=30, width=300)
        self.pie_chart_description.pack()
        self.pie_chart(chart_data)

        Label(self.pie_chart_description, text=" ", bg="#ececec").pack(side=LEFT)
        for i, tran_type in enumerate(self.trans_types):
            if i == 3:
                self.pie_chart_description = Frame(self.cake_frame, bg="#ececec", height=30, width=300)
                self.pie_chart_description.pack(ipady=5)
            Label(self.pie_chart_description, text=" ", bg=self.colors[i], highlightthickness=2).pack(side=LEFT)
            Label(self.pie_chart_description, bg="#ececec", text=tran_type, ).pack(side=LEFT, ipadx=3)


    def data_graph(self, data):
        self.canvas = Canvas(self.body_frame, width=800, height=600, highlightthickness=0)
        self.canvas.pack(side=RIGHT)

        max_value = max(data)

        # Round up the maximum value to the nearest "nice" number
        if max_value <= 1000:
            max_label = 1000
        elif max_value <= 5000:
            max_label = 5000
        elif max_value <= 10000:
            max_label = 10000
        elif max_value <= 50000:
            max_label = 50000
        elif max_value <= 100000:
            max_label = 100000
        elif max_value <= 500000:
            max_label = 500000
        elif max_value <= 1000000:
            max_label = 1000000
        elif max_value <= 5000000:
            max_label = 5000000
        else:
            max_label = 10000000

        # Create the y-axis labels
        y_labels = [max_label // 10 * i for i in range(11)]

        # Draw the y-axis labels
        for i, y_label in enumerate(y_labels):
            y = 550 - y_label / max_label * 500
            self.canvas.create_text(75, y, text=str(y_label), anchor="e")
            self.canvas.create_line(100, y, 720, y, fill="light grey")

        # Draw the y-axis line
        self.canvas.create_line(100, 50, 100, 550, width=2)

        # Draw the x-axis labels
        x_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
        for i, x_label in enumerate(x_labels):
            x = 100 + i * 125
            self.canvas.create_text(x, 570, text=x_label, anchor="n")

        # Draw the x-axis line
        self.canvas.create_line(100, 550, 725, 550, width=2)

        # Draw the lines connecting the data points
        for i in range(len(data) - 1):
            x1 = 100 + i * 125
            y1 = 550 - data[i] / max_label * 500
            x2 = 100 + (i + 1) * 125
            y2 = 550 - data[i + 1] / max_label * 500
            self.canvas.create_line(x1, y1, x2, y2, fill="red", width=2)

    def update_label(self, root, value):
        root.self.value_label.config(text=f"{value}")

    def update_graph(self, data_graph):
        self.canvas.destroy()
        self.data_graph(data_graph)

    def update_chart(self, data_pie_chart):
        self.cake_graph.delete()
        self.pie_chart(data_pie_chart)

    def pie_chart(self, pie_values):
        # Calculate the total sum of values
        total = sum(pie_values) * (-1)

        temp = 0
        for i in range(len(pie_values)):
            if pie_values[i] == 0:
                temp += 1
            else:
                color = i
        if temp == 6:
            self.cake_graph.create_oval(60, 10, 260, 210, fill="light grey")
        elif temp == 5:
            self.cake_graph.create_oval(60, 10, 260, 210, fill=self.colors[color])
        else:
            start_angle = 0
            for i in range(len(pie_values)):
                # Calculate the end angle for the current slice
                end_angle = start_angle + 360 * (pie_values[i] * (-1)) / total
                # Draw the slice
                self.cake_graph.create_arc(60, 10, 260, 210, start=start_angle, extent=end_angle - start_angle,
                                           fill=self.colors[i])
                # Update the start angle for the next slice
                start_angle = end_angle








class DataManagerWindow:
    def __init__(self, root):
        self.pridaj_win = Toplevel(root)
        self.pridaj_win.config(width=500,
                               height=400,
                               bg=WHITE)
        self.var = IntVar()
        self.pridaj_end = False
        Label(self.pridaj_win,
              text="Pridaj transakciu",
              bg=WHITE,
              fg=BLACK,
              font=("Helvetica", 32, "bold")).pack(expand=True, ipadx=200, ipady=20)

        self.frame_upper = Frame(self.pridaj_win, bg=WHITE)
        self.frame_upper.pack()

        self.frame_upper_left = Frame(self.frame_upper, bg=WHITE)
        self.frame_upper_left.pack(side=LEFT)
        self.frame_upper_right = Frame(self.frame_upper, bg=WHITE)
        self.frame_upper_right.pack(side=RIGHT)
        Label(self.frame_upper_left,
              text="Typ transakcie: ",
              bg=WHITE,
              fg=BLACK,
              font=("Helvetica", 17, "bold")).pack()
        self.frame_transact_tp = Frame(self.frame_upper_right, bg=WHITE)
        self.frame_transact_tp.pack()
        r1 = Radiobutton(self.frame_transact_tp,
                         text="Prijatie",
                         bg=WHITE,
                         fg=BLACK,
                         font=("Helvetica", 16, "bold"),
                         variable=self.var,
                         command=self.update_var_income,
                         value=1)
        r1.pack(side=RIGHT)

        r1 = Radiobutton(self.frame_transact_tp,
                         text="Odoslanie",
                         bg=WHITE,
                         fg=BLACK,
                         font=("Helvetica", 16, "bold"),
                         variable=self.var,
                         command=self.update_var_outcome,
                         value=2)
        r1.pack(side=RIGHT)

        Label(self.frame_upper_left,
              text="Názov transakcie",
              bg=WHITE,
              fg=BLACK,
              font=("Helvetica", 17, "bold")).pack(ipadx=40)
        self.input1 = Entry(self.frame_upper_right,
                            font=("Helvetica", 16, "bold"),
                            highlightthickness=0)
        self.input1.insert(0, "(Nepovinne)")
        self.input1.pack()

        Label(self.frame_upper_left,
              text="Hodnota:",
              bg=WHITE,
              fg=BLACK,
              font=("Helvetica", 17, "bold")).pack(ipadx=40)

        self.input2 = Entry(self.frame_upper_right,
                            font=("Helvetica", 16, "bold"),
                            highlightthickness=0)
        self.input2.insert(-1, "€")
        self.input2.pack()

        self.var2 = IntVar()
        self.frame = Frame(self.pridaj_win, bg=WHITE)
        self.frame.pack(ipady=20)
        self.frame_radio_left = Frame(self.frame, bg=WHITE)
        self.frame_radio_left.pack(side=LEFT)
        self.frame_radio_right = Frame(self.frame, bg=WHITE)
        self.frame_radio_right.pack(side=RIGHT)

        self.ro1 = Radiobutton(self.frame_radio_left,
                               bg=WHITE,
                               fg=BLACK,
                               text="Domácnosť           ",
                               font=("Helvetica", 17, "bold"),
                               variable=self.var2,
                               value=1)
        self.ro1.pack()

        self.ro2 = Radiobutton(self.frame_radio_left,
                               bg=WHITE,
                               fg=BLACK,
                               text="Strava                    ",
                               font=("Helvetica", 17, "bold"),
                               variable=self.var2,
                               value=2)
        self.ro2.pack()

        self.ro3 = Radiobutton(self.frame_radio_left,
                               bg=WHITE,
                               fg=BLACK,
                               text="Zdravie a poistenie",
                               font=("Helvetica", 17, "bold"),
                               variable=self.var2,
                               value=3)
        self.ro3.pack()

        self.ro4 = Radiobutton(self.frame_radio_right,
                               bg=WHITE,
                               fg=BLACK,
                               text="Zábava      ",
                               font=("Helvetica", 17, "bold"),
                               variable=self.var2,
                               value=4)
        self.ro4.pack()

        self.ro5 = Radiobutton(self.frame_radio_right,
                               bg=WHITE,
                               fg=BLACK,
                               text="Cestovanie",
                               font=("Helvetica", 17, "bold"),
                               variable=self.var2,
                               value=5)
        self.ro5.pack()

        self.ro6 = Radiobutton(self.frame_radio_right,
                               bg=WHITE,
                               text="Iné            ",
                               fg=BLACK,
                               font=("Helvetica", 17, "bold"),
                               variable=self.var2,
                               value=6)
        self.ro6.pack()

        self.pridaj_button = Button(self.pridaj_win,
                                    text="Pridaj",
                                    bg=GREEN,
                                    fg=WHITE,
                                    borderwidth=0,
                                    width=8,
                                    font=("Helvetica", 20, "bold"))
        self.pridaj_button.pack(side=RIGHT, ipadx=50, ipady=20)


    def update_var_income(self):
        self.ro1.config(text="Zamestnanie   ", value=7)
        self.ro2.config(text="Pasívny príjem", value=8)
        self.ro3.config(text="Iné                   ", value=9)
        self.frame_radio_right.pack_forget()

    def update_var_outcome(self):
        self.ro1.config(text="Domácnosť           ", value=1)
        self.ro2.config(text="Strava                    ", value=2)
        self.ro3.config(text="Zdravie a poistenie", value=3)
        self.frame_radio_right.pack(side=RIGHT)
