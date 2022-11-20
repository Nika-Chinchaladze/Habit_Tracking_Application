from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
from API_Class import ApiWorker
from Prepare_DataBase import SqlDatabase
from datetime import datetime

FONT = ("Arial", 12, "normal")
COLORS = ("green", "red", "blue", "purple", "yellow", "black")
WIDTH = 10
BNT_FONT = ("Helvetica", 10, "normal")


class CreateScreen:
    def __init__(self, screen):
        self.screen = screen
        self.screen.title("Track Habit")
        self.screen.geometry("500x450")
        self.quantity = StringVar()

        self.head_label = Label(self.screen, text="Track Your Habit", font=("Helvetica", 20, "bold"), justify="center",
                                fg="dark slate gray")
        self.head_label.place(x=22, y=10, width=450, height=40)

        self.calendar_frame = Frame(self.screen, bd=5, relief=RIDGE, width=450, height=250)
        self.calendar_frame.place(x=22, y=60)

        self.calendar_object = Calendar(self.calendar_frame, selectmode="day", year=2022, month=11, day=20)
        self.calendar_object.place(x=5, y=10, width=430, height=225)

        self.date_label = Label(self.screen, text="Chosen Date", font=FONT, bd=1, relief=RIDGE)
        self.date_label.place(x=22, y=320, width=220)

        self.chosen_label = Label(self.screen, text="", font=FONT, bd=1, relief=RIDGE)
        self.chosen_label.place(x=255, y=320, width=218)

        self.quantity_label = Label(self.screen, text="Quantity", font=FONT, bd=1, relief=RIDGE)
        self.quantity_label.place(x=22, y=350, width=220)

        self.quantity_entry = Entry(self.screen, justify="center", width=150, font=FONT, textvariable=self.quantity)
        self.quantity_entry.place(x=255, y=350, width=218)

        self.button_frame = Frame(self.screen, highlightthickness=0, bd=0, width=400, height=30)
        self.button_frame.place(x=25, y=385)

        self.date_button = Button(self.button_frame, text="Get Date", justify="center", width=WIDTH, font=BNT_FONT,
                                  bg="pale green", command=self.grab_chosen_date)
        self.date_button.grid(row=0, column=0)

        self.add_button = Button(self.button_frame, text="Add Pixel", justify="center", font=BNT_FONT, width=WIDTH,
                                 bg="cornflower blue", command=self.add_pixel_method)
        self.add_button.grid(row=0, column=1)

        self.update_button = Button(self.button_frame, text="Update Pixel", justify="center", font=BNT_FONT,
                                    width=WIDTH, bg="dark khaki", command=self.update_pixel)
        self.update_button.grid(row=0, column=2)

        self.delete_button = Button(self.button_frame, text="Delete Pixel", justify="center", font=BNT_FONT,
                                    width=WIDTH, bg="coral", command=self.delete_existing_pixel)
        self.delete_button.grid(row=0, column=3)

        self.close_button = Button(self.button_frame, text="Close App", justify="center", width=WIDTH, font=BNT_FONT,
                                   bg="plum", command=self.close_main_window)
        self.close_button.grid(row=0, column=4)

    # =========================================== FUNCTIONALITY ======================================== #
    def grab_chosen_date(self):
        self.chosen_label.config(text=self.calendar_object.get_date())

    def add_pixel_method(self):
        hand = SqlDatabase()
        # transform date:
        chosen_date = self.calendar_object.get_date().split("/")
        current_date = datetime(year=int(f"20{chosen_date[-1]}"), month=int(chosen_date[0]), day=int(chosen_date[1]))
        wanted_date = current_date.strftime("%Y%m%d")
        # current user:
        current_user_info = hand.read_from_txt()
        # user information:
        information = hand.return_wanted_data(username=current_user_info[0], password=current_user_info[-1])
        # add pixel
        tool = ApiWorker()
        answer = tool.create_pixel(username=information[0], password=information[1], graph_id=information[2],
                                   chosen_date=wanted_date, chosen_quantity=self.quantity.get())
        if answer == 503:
            messagebox.showinfo(title="Repeat", message="Please Press Again to add new pixel?")
        else:
            messagebox.showinfo(title="Confirm", message="Pixel has been added, Successfully!")

    def update_pixel(self):
        hand = SqlDatabase()
        # transform date:
        chosen_date = self.calendar_object.get_date().split("/")
        current_date = datetime(year=int(f"20{chosen_date[-1]}"), month=int(chosen_date[0]), day=int(chosen_date[1]))
        wanted_date = current_date.strftime("%Y%m%d")
        # current user:
        current_user_info = hand.read_from_txt()
        # user information:
        information = hand.return_wanted_data(username=current_user_info[0], password=current_user_info[-1])
        # update pixel:
        tool = ApiWorker()
        answer = tool.update_existing_pixel(username=information[0], password=information[1], graph_id=information[2],
                                            chosen_date=wanted_date, chosen_quantity=self.quantity.get())
        if answer == 503:
            messagebox.showinfo(title="Repeat", message="Please Press Again to update existing pixel?")
        else:
            messagebox.showinfo(title="Confirm", message="Pixel has been updated, Successfully!")

    def delete_existing_pixel(self):
        hand = SqlDatabase()
        # transform date:
        chosen_date = self.calendar_object.get_date().split("/")
        current_date = datetime(year=int(f"20{chosen_date[-1]}"), month=int(chosen_date[0]), day=int(chosen_date[1]))
        wanted_date = current_date.strftime("%Y%m%d")
        # current user:
        current_user_info = hand.read_from_txt()
        # user information:
        information = hand.return_wanted_data(username=current_user_info[0], password=current_user_info[-1])
        # delete pixel:
        tool = ApiWorker()
        answer = tool.delete_pixel(username=information[0], password=information[1], graph_id=information[2],
                                   chosen_date=wanted_date)
        if answer == 503:
            messagebox.showinfo(title="Repeat", message="Please Press Again to delete existing pixel?")
        else:
            messagebox.showinfo(title="Confirm", message="Pixel has been deleted, Successfully!")

    def close_main_window(self):
        self.screen.destroy()


def launch_calendar_screen():
    app_4 = Tk()
    CreateScreen(app_4)
    app_4.mainloop()


if __name__ == "__main__":
    launch_calendar_screen()
