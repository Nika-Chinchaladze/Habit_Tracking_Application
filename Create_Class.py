from tkinter import *
from tkinter import messagebox
from Graph_Class import launch_create_graph
from Prepare_DataBase import SqlDatabase
from API_Class import ApiWorker

FONT = ("Arial", 12, "normal")


class CreateAccount:
    def __init__(self, account):
        self.account = account
        self.account.title("Create New Account")
        self.account.geometry("360x250")
        self.account.configure(bg="light blue")
        # extra variables;
        self.username = StringVar()
        self.user_password = StringVar()

        self.head_label = Label(self.account, text="Personal Information", font=("Helvetica", 15, "bold"),
                                justify="center", fg="dark slate gray", bg="light blue")
        self.head_label.place(x=10, y=10, width=340, height=30)
        # frame:
        self.main_frame = Frame(self.account, relief=RIDGE, bd=3, bg="light blue")
        self.main_frame.place(x=10, y=50, width=340, height=180)

        self.name_label = Label(self.main_frame, text="UserName", bg="light blue", font=FONT, padx=5, pady=5)
        self.name_label.grid(row=0, column=0)

        self.password_label = Label(self.main_frame, text="Password", bg="light blue", font=FONT, padx=5, pady=5)
        self.password_label.grid(row=1, column=0)

        self.repeat_label = Label(self.main_frame, text="Repeat Password", bg="light blue", font=FONT, padx=5, pady=5)
        self.repeat_label.grid(row=2, column=0)

        self.name_entry = Entry(self.main_frame, font=FONT, justify="center", textvariable=self.username)
        self.name_entry.grid(row=0, column=1)

        self.password_entry = Entry(self.main_frame, font=FONT, justify="center", show="*",
                                    textvariable=self.user_password)
        self.password_entry.grid(row=1, column=1)

        self.repeat_entry = Entry(self.main_frame, font=FONT, justify="center", show="*")
        self.repeat_entry.grid(row=2, column=1)

        self.submit_button = Button(self.main_frame, text="Submit", font=FONT, justify="center", width=20, height=1,
                                    bg="yellow green", command=self.save_client_data)
        self.submit_button.grid(row=3, column=0, columnspan=2)

        self.next_button = Button(self.main_frame, text="Next", font=FONT, justify="center", width=20, height=1,
                                  bg="goldenrod", command=self.open_graph_window)
        self.next_button.grid(row=4, column=0, columnspan=2, pady=5)

    # ========================================== FUNCTIONALITY =================================== #
    def save_client_data(self):
        tool = SqlDatabase()
        tool.insert_into_table(self.username.get(), self.user_password.get())
        tool.save_in_txt(username=self.username.get(), password=self.user_password.get())
        # create account:
        hand = ApiWorker()
        hand.create_account(username=self.username.get(), password=self.user_password.get())
        messagebox.showinfo(title="SQL", message="Information has been Submitted, Successfully!")

    def open_graph_window(self):
        self.account.destroy()
        launch_create_graph()


def launch_create_account():
    app_2 = Tk()
    CreateAccount(app_2)
    app_2.mainloop()


if __name__ == "__main__":
    launch_create_account()
