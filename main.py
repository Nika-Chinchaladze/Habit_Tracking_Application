from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from Create_Class import launch_create_account
from Calendar_Class import launch_calendar_screen
from Prepare_DataBase import SqlDatabase

FONT = ("Arial", 12, "normal")


class LogIn:
    def __init__(self, window):
        self.window = window
        self.window.title("Authorization")
        self.window.geometry("300x500")
        # extra:
        self.entered_name = StringVar()
        self.entered_password = StringVar()
        # image:
        used_image = Image.open("./IMG/pixela.png")
        used_photo = ImageTk.PhotoImage(used_image)
        self.image_label = Label(self.window, image=used_photo)
        self.image_label.image = used_photo
        self.image_label.place(x=10, y=10)
        # frame:
        self.main_frame = Frame(self.window, relief=RIDGE, bd=3)
        self.main_frame.place(x=10, y=320, width=280, height=150)

        self.name_label = Label(self.main_frame, text="UserName", font=FONT, padx=5, pady=5)
        self.name_label.grid(row=0, column=0)

        self.password_label = Label(self.main_frame, text="Password", font=FONT, padx=5, pady=5)
        self.password_label.grid(row=1, column=0)

        self.name_entry = Entry(self.main_frame, font=FONT, justify="center", textvariable=self.entered_name)
        self.name_entry.grid(row=0, column=1)

        self.password_entry = Entry(self.main_frame, font=FONT, justify="center", show="*",
                                    textvariable=self.entered_password)
        self.password_entry.grid(row=1, column=1)

        self.log_button = Button(self.main_frame, text="Login", font=FONT, justify="center", width=20, height=1,
                                 bg="medium sea green", command=self.successful_login)
        self.log_button.grid(row=2, column=0, columnspan=2)

        self.create_button = Button(self.main_frame, text="Create Account", font=FONT, justify="center", width=20,
                                    height=1, bg="dodger blue", command=self.open_create_window)
        self.create_button.grid(row=3, column=0, columnspan=2, pady=5)

    # ================================= FUNCTIONALITY ========================================== #
    def open_create_window(self):
        self.window.destroy()
        launch_create_account()

    def successful_login(self):
        tool = SqlDatabase()
        try:
            personal_info = tool.return_wanted_data(username=self.entered_name.get(),
                                                    password=self.entered_password.get())
            if len(personal_info) > 0:
                tool.save_in_txt(username=self.entered_name.get(), password=self.entered_password.get())
                messagebox.showinfo(title="Success", message="Successful LogIn!")
                self.window.destroy()
                launch_calendar_screen()
            else:
                pass
        except TypeError:
            messagebox.showerror(title="Wrong", message="Wrong UserName or Password!")


def launch_login():
    app = Tk()
    LogIn(app)
    app.mainloop()


if __name__ == "__main__":
    launch_login()
