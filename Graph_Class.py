from tkinter import *
from tkinter import ttk, messagebox
import pyperclip
from Calendar_Class import launch_calendar_screen
from Prepare_DataBase import SqlDatabase
from API_Class import ApiWorker, color_transformer

FONT = ("Arial", 12, "normal")
COLORS = ("green", "red", "blue", "purple", "yellow", "black")


class CreateGraph:
    def __init__(self, graph):
        self.graph = graph
        self.graph.title("Create New Graph")
        self.graph.geometry("500x430")
        # extra variables:
        self.client_name = None
        self.my_endpoint = "https://pixe.la/v1/users"
        self.current_id = StringVar()
        self.current_name = StringVar()
        self.current_unit = StringVar()
        self.current_type = StringVar()
        self.current_color = StringVar()

        self.head_label = Label(self.graph, text="Graph Information", font=("Helvetica", 20, "bold"), justify="center",
                                fg="dark slate gray")
        self.head_label.place(x=10, y=10, width=480, height=40)

        # frame:
        self.main_frame = Frame(self.graph, relief=RIDGE, bd=3, pady=10)
        self.main_frame.place(x=10, y=60, width=480, height=190)

        self.id_label = Label(self.main_frame, text="ID", font=FONT, padx=5, pady=5, width=20)
        self.id_label.grid(row=0, column=0)

        self.name_label = Label(self.main_frame, text="Name", font=FONT, padx=5, pady=5, width=20)
        self.name_label.grid(row=1, column=0)

        self.unit_label = Label(self.main_frame, text="Unit", font=FONT, padx=5, pady=5, width=20)
        self.unit_label.grid(row=2, column=0)

        self.type_label = Label(self.main_frame, text="Type", font=FONT, padx=5, pady=5, width=20)
        self.type_label.grid(row=3, column=0)

        self.color_label = Label(self.main_frame, text="Color", font=FONT, padx=5, pady=5, width=20)
        self.color_label.grid(row=4, column=0)

        self.id_entry = Entry(self.main_frame, font=FONT, justify="center", textvariable=self.current_id)
        self.id_entry.grid(row=0, column=1)

        self.name_entry = Entry(self.main_frame, font=FONT, justify="center", textvariable=self.current_name)
        self.name_entry.grid(row=1, column=1)

        self.unit_entry = Entry(self.main_frame, font=FONT, justify="center", textvariable=self.current_unit)
        self.unit_entry.grid(row=2, column=1)

        self.type_entry = Entry(self.main_frame, font=FONT, justify="center", textvariable=self.current_type)
        self.type_entry.grid(row=3, column=1)

        self.color_entry = ttk.Combobox(self.main_frame, width=18, font=FONT, justify="center",
                                        textvariable=self.current_color)
        self.color_entry["values"] = COLORS
        self.color_entry['state'] = 'readonly'
        self.color_entry.current(0)
        self.color_entry.grid(row=4, column=1)

        self.warning_label = Label(self.graph, text="", font=FONT, padx=5, pady=5, fg="red", bd=1, relief=RIDGE)
        self.warning_label.place(x=10, y=300, width=480, height=20)

        self.link_label = Label(self.graph, text="", font=FONT, padx=5, pady=5, fg="maroon", bd=1, relief=RIDGE)
        self.link_label.place(x=10, y=330, width=480, height=20)

        self.submit_button = Button(self.graph, text="Submit", font=FONT, justify="center", bg="coral",
                                    command=self.add_graph_information)
        self.submit_button.place(x=10, y=260, width=480, height=30)

        self.copy_button = Button(self.graph, text="copy address", font=FONT, justify="center", bg="rosy brown",
                                  command=self.copy_url_html)
        self.copy_button.place(x=10, y=360, width=230, height=30)

        self.next_button = Button(self.graph, text="next", font=FONT, justify="center", bg="dark sea green",
                                  command=self.open_calendar_window)
        self.next_button.place(x=260, y=360, width=230, height=30)

    # ===================================== FUNCTIONALITY ================================== #
    def add_graph_information(self):
        tool = SqlDatabase()
        personal_info = tool.read_from_txt()
        tool.update_table(client_name=personal_info[0], graph_id=self.current_id.get(),
                          graph_name=self.current_name.get(), unit=self.current_unit.get(),
                          unit_type=self.current_type.get(), color=self.current_color.get())
        # define color:
        chosen_color = color_transformer(self.current_color.get())
        # create pixela graph:
        hand = ApiWorker()
        hand.create_graph(username=personal_info[0], password=personal_info[-1], graph_id=self.current_id.get(),
                          graph_name=self.current_name.get(), unit=self.current_unit.get(),
                          unit_type=self.current_type.get(), color=chosen_color)
        messagebox.showinfo(title="Update", message="Information Has Been Submitted, Successfully!")
        self.warning_label.config(text="WARNING: Do not forget to copy URL below!")
        self.link_label.config(text=f"{self.my_endpoint}/{personal_info[0]}/graphs/{self.current_id.get()}.html")

    def copy_url_html(self):
        pyperclip.copy(self.link_label.cget("text"))
        messagebox.showinfo(title="Copied", message="URL has been copied!")

    def open_calendar_window(self):
        self.graph.destroy()
        launch_calendar_screen()


def launch_create_graph():
    app_3 = Tk()
    CreateGraph(app_3)
    app_3.mainloop()


if __name__ == "__main__":
    launch_create_graph()
