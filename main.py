import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector


class ChangeRoomDetail(tk.Tk):
    def __init__(self):
        super().__init__()

        self.overrideredirect(True) 
        self.title("Edit Room Details")
        
        self.center_window(500, 675)

    def center_window(self, width, height):
        # Get the screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Calculate x and y coordinates for the center of the screen
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        # Set the position of the window
        self.geometry(f'{width}x{height}+{x}+{y}')

        # Create the main container
        self.container = tk.Frame(self, bg="white")
        self.container.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        self.container.config(relief=tk.GROOVE, bd=2)

        # Top Buttons
        self.top_frame = tk.Frame(self.container, bg="white")
        self.top_frame.pack()

        # Exit and Home buttons
        self.home_button = tk.Button(self.top_frame, text="HOME", command=self.go_home, width=9, bg="#133E87", fg="white", font=("Consolas", 12,"bold"))
        self.home_button.pack(side=tk.LEFT, padx=(10, 185), pady = (20, 0))

        self.exit_button = tk.Button(self.top_frame, text="EXIT", command=self.exit_app, width=9, bg="#133E87", fg="white", font=("Consolas", 12,"bold"))
        self.exit_button.pack(side=tk.LEFT, padx=(0, 10), pady = (20, 0))

        # Title
        self.title_label = tk.Label(self.container, text="EDIT ROOM DETAILS", font=("Consolas", 30,"bold"),fg="#133E87", bg="white")
        self.title_label.pack(pady=(15,5))

        # Create a new frame for room selection, to stack under the buttons
        self.haha = tk.Frame(self.container, bg="white")
        self.haha.pack(side=tk.TOP, pady=(10, 0))

        # Room Selection
        self.room_label = tk.Label(self.haha, text="ROOM:", fg="#133E87", bg="white", font=("Consulas", 15, "bold"))
        self.room_label.pack(side=tk.LEFT, padx= 5, pady=(0, 0))

        self.room_select = ttk.Combobox(self.haha, values=[1, 2, 3, 4, 5], width=1, foreground="#133E87",font=("Consulas", 13, "bold"))
        self.room_select.pack(side=tk.LEFT, padx= 5, pady=5)

        self.reload_button = tk.Button(self.haha, text="RELOAD", command=self.reload_data, height=1,  width=31, bg="#133E87", fg="white")
        self.reload_button.pack(side=tk.LEFT, padx= 10, pady=5)

        # Input Fields 
        self.username_label = tk.Label(self.container, text="USERNAME:", bg= "white", fg="#133E87", font=("Consulas", 15, "bold"))
        self.username_label.pack(pady=(10, 0))
        self.username_entry = tk.Entry(self.container, width=32, bd=0, relief='groove', justify='center', fg= "#133E87", font=("Consulas", 15,"bold"),highlightbackground="#133E87",highlightthickness=1)
        self.username_entry.pack(pady=0)

        self.username_label = tk.Label(self.container, text="PASSWORD:", bg= "white", fg="#133E87", font=("Consulas", 15, "bold"))
        self.username_label.pack(pady=(10, 0))
        self.password_entry = tk.Entry(self.container, width=32, bd=0, relief='groove', justify='center', fg= "#133E87", font=("Consulas", 15,"bold"),highlightbackground="#133E87",highlightthickness=1)
        self.password_entry.pack(pady=0)

        self.username_label = tk.Label(self.container, text="NAME:", bg= "white", fg="#133E87", font=("Consulas", 15, "bold"))
        self.username_label.pack(pady=(10, 0))
        self.name_entry = tk.Entry(self.container, width=32, bd=0, relief='groove', justify='center', fg= "#133E87", font=("Consulas", 15,"bold"),highlightbackground="#133E87",highlightthickness=1)
        self.name_entry.pack(pady=0)

        self.username_label = tk.Label(self.container, text="CONTACTS:", bg= "white", fg="#133E87", font=("Consulas", 15, "bold"))
        self.username_label.pack(pady=(10, 0))
        self.contacts_entry = tk.Entry(self.container, width=32, bd=0, relief='groove', justify='center', fg= "#133E87", font=("Consulas", 15,"bold"),highlightbackground="#133E87",highlightthickness=1)
        self.contacts_entry.pack(pady=0)

        self.username_label = tk.Label(self.container, text="MONTHLY BILL:", bg= "white", fg="#133E87", font=("Consulas", 15, "bold"))
        self.username_label.pack(pady=(10, 0))
        self.monthly_entry = tk.Entry(self.container, width=32, bd=0, relief='groove', justify='center', fg= "#133E87", font=("Consulas", 15,"bold"),highlightbackground="#133E87",highlightthickness=1)
        self.monthly_entry.pack(pady=0)

        self.username_label = tk.Label(self.container, text="DUEDATE:", bg= "white", fg="#133E87", font=("Consulas", 15, "bold"))
        self.username_label.pack(pady=(10, 0))
        self.duedate_entry = tk.Entry(self.container, width=32, bd=0, relief='groove', justify='center', fg= "#133E87", font=("Consulas", 15,"bold"),highlightbackground="#133E87",highlightthickness=1)
        self.duedate_entry.pack(pady=0)

        # Action Buttons
        self.button_frame = tk.Frame(self.container, bg="white")
        self.button_frame.pack(pady=20)

        self.add_button = tk.Button(self.button_frame, text="ADD", command=self.add_data, width=15, bg="#133E87", fg="white")
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.change_button = tk.Button(self.button_frame, text="UPDATE", command=self.update_data, width=15, bg="#133E87", fg="white")
        self.change_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="DELETE", command=self.delete_data, width=15, bg="#133E87", fg="white")
        self.delete_button.pack(side=tk.LEFT, padx=5)

    def create_input_label(self, text):
        label = tk.Label(self.container, text=text, bg="white", font=("Arial", 12))
        label.pack(pady=(10, 0))

    def exit_app(self):
        if messagebox.askyesno("Confirm Exit", "Do you want to exit?"):
            self.destroy()  # Use self.destroy() to close Toplevel window

    def db_connection(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="ronmel06",
            database="ronmeldb"
        )

    def go_home(self):
        # Assuming this function is intended to go to the home or main menu
        self.destroy()
        Dashboard().mainloop()

    def get_input_data(self):
        return {
            'username': self.username_entry.get(),
            'password': self.password_entry.get(),
            'name': self.name_entry.get(),
            'contacts': self.contacts_entry.get(),
            'monthly': self.monthly_entry.get(),
            'duedate': self.duedate_entry.get()
        }

    def add_data(self):
        room = self.room_select.get()
        if room == "":
            messagebox.showerror("Error", "Please select a room.")
            return
        
        data = self.get_input_data()
        if not messagebox.askyesno("Confirm", "Are you sure you want to add?"):
            return

        try:
            con = self.db_connection()
            cursor = con.cursor()
            cursor.execute("SELECT COUNT(*) FROM ronmeltb WHERE username IS NOT NULL")
            total_rooms_occupied = cursor.fetchone()[0]

            if total_rooms_occupied >= 5:
                messagebox.showerror("Error", "All rooms are occupied. Cannot add new user.")
                return
            
            cursor.execute("SELECT COUNT(*) FROM ronmeltb WHERE room = %s AND username IS NOT NULL", (room,))
            if cursor.fetchone()[0] > 0:
                messagebox.showerror("Error", "The room is already occupied.")
                return

            cursor.execute("INSERT INTO ronmeltb (room, username, password, name, contacts, monthly, duedate) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (room, data['username'], data['password'], data['name'], data['contacts'], data['monthly'], data['duedate']))

            con.commit()
            messagebox.showinfo("Success", "User Data Added Successfully!")
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.name_entry.delete(0, tk.END)
            self.contacts_entry.delete(0, tk.END)
            self.monthly_entry.delete(0, tk.END)
            self.duedate_entry.delete(0, tk.END)
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            if con.is_connected():
                cursor.close()
                con.close()

    def reload_data(self):
        room_number = self.room_select.get()
        if room_number == "":
            messagebox.showerror("Error", "Please select a room.")
            return
        try:
            con = self.db_connection()
            cursor = con.cursor()
            cursor.execute("SELECT username, password, name, contacts, monthly, duedate FROM ronmeltb WHERE room = %s", (room_number,))
            result = cursor.fetchone()
            if result:
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                self.name_entry.delete(0, tk.END)
                self.contacts_entry.delete(0, tk.END)
                self.monthly_entry.delete(0, tk.END)
                self.duedate_entry.delete(0, tk.END)
                self.username_entry.insert(0, result[0])
                self.password_entry.insert(0, result[1])
                self.name_entry.insert(0, result[2])
                self.contacts_entry.insert(0, result[3])
                self.monthly_entry.insert(0, result[4])
                self.duedate_entry.insert(0, result[5])
            else:
                messagebox.showinfo("Info", "No Client Found")
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                self.name_entry.delete(0, tk.END)
                self.contacts_entry.delete(0, tk.END)
                self.monthly_entry.delete(0, tk.END)
                self.duedate_entry.delete(0, tk.END)

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            if con.is_connected():
                cursor.close()
                con.close()

    def update_data(self):
        room = self.room_select.get()
        if room == "":
            messagebox.showerror("Error", "Please select a room.")
            return
        
        data = self.get_input_data()

        if not messagebox.askyesno("Confirm", "Are you sure you want to update?"):
            return

        try:
            con = self.db_connection()
            cursor = con.cursor()
            cursor.execute("UPDATE ronmeltb SET username = %s, password = %s, name = %s, contacts = %s, monthly = %s, duedate = %s WHERE room = %s",
                           (data['username'], data['password'], data['name'], data['contacts'], data['monthly'], data['duedate'], room))
            con.commit()
            messagebox.showinfo("Success", "User Data Updated Successfully!")
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.name_entry.delete(0, tk.END)
            self.contacts_entry.delete(0, tk.END)
            self.monthly_entry.delete(0, tk.END)
            self.duedate_entry.delete(0, tk.END)
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            if con.is_connected():
                cursor.close()
                con.close()

    def delete_data(self):
        room = self.room_select.get()
        if room == "":
            messagebox.showerror("Error", "Please select a room.")
            return

        if not messagebox.askyesno("Confirm", "Are you sure you want to delete?"):
            return

        try:
            con = self.db_connection()
            cursor = con.cursor()
            cursor.execute("DELETE FROM ronmeltb WHERE room = %s", (room,))
            con.commit()
            messagebox.showinfo("Success", "User Data Deleted Successfully!")
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.name_entry.delete(0, tk.END)
            self.contacts_entry.delete(0, tk.END)
            self.monthly_entry.delete(0, tk.END)
            self.duedate_entry.delete(0, tk.END)
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            if con.is_connected():
                cursor.close()
                con.close()


class Dashboard(tk.Tk):
    def __init__(self, toplevel=None):
        super().__init__()

        self.overrideredirect(True)
        self.configure(bg="#f7f7f7")

        self.create_header()
        self.create_rooms()

        self.set_text_pane()

        self.attributes('-fullscreen', False)

        # self.update_idletasks()
        # self.geometry(f"{self.winfo_width()}x{self.winfo_height()}+{int(self.winfo_screenwidth()/2 - self.winfo_width()/2)}+{int(self.winfo_screenheight()/2 - self.winfo_height()/2)}") 

    def create_header(self):
        header_frame = tk.Frame(self, bg="#203e8d", padx=53, pady=75)
        header_frame.pack(fill=tk.X)

        title_label = tk.Label(header_frame, text="DASHBOARD: CLIENT'S LIST", fg="white", bg="#203e8d", font=("Consolas", 48,"bold"))
        title_label.pack(side=tk.LEFT, padx=(10, 30))

        button_frame = tk.Frame(header_frame, bg="#203e8d")
        button_frame.pack(side=tk.RIGHT)

        refresh_button = tk.Button(button_frame, text="REFRESH", command=self.set_text_pane, bg="white", fg="#203e8d", font=("Segoe UI", 15,"bold"), borderwidth=0, relief="flat", width=13)
        refresh_button.pack(side=tk.LEFT, padx=10, pady=5)

        edit_button = tk.Button(button_frame, text="EDIT", command=self.edit_room, bg="white", fg="#203e8d", font=("Segoe UI", 15,"bold"), borderwidth=0, relief="flat", width=13)
        edit_button.pack(side=tk.LEFT, padx=10, pady=5)

        exit_button = tk.Button(button_frame, text="EXIT", command=self.on_exit, bg="white", fg="#203e8d", font=("Segoe UI", 15,"bold"), borderwidth=0, relief="flat", width=13)
        exit_button.pack(side=tk.LEFT, padx=10, pady=5)

    def create_rooms(self):
        self.rooms_frame = tk.Frame(self, bg="#CBDCEB", padx=10, pady=15)
        self.rooms_frame.pack(fill=tk.BOTH, expand=True)

        self.rooms = {}
        for i in range(1, 6):
            self.create_room(i)

    def create_room(self, room_number):
        room_frame = tk.Frame(self.rooms_frame, bg="white", bd=2, relief=tk.GROOVE, padx=0, pady=40)
        room_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=10)

        room_label = tk.Label(room_frame, text=f"ROOM:{room_number}", font=("Consolas", 40, "bold"), bg="white", fg="#203e8d")
        room_label.pack(anchor=tk.CENTER)

        # Create entries for each field
        status_label = tk.Label(room_frame, text="STATUS:", bg="white", anchor=tk.W, font=("Consulas", 15, "bold"), fg="#203e8d")
        status_label.pack(fill=tk.X, padx=18, pady=(30, 5))
        status_text = tk.Text(room_frame, height=1.2, width=22, bg="white", relief="groove", font=("Consulas", 15,"bold"), fg="#133E87", highlightbackground="#133E87",highlightthickness=1)
        status_text.pack(padx=5)

        name_label = tk.Label(room_frame, text="NAME:", bg="white", anchor=tk.W, font=("Consulas", 15, "bold"), fg="#203e8d")
        name_label.pack(fill=tk.X, padx=18, pady=(20, 5))
        name_text = tk.Text(room_frame, height=1.2, width=22, bg="white", relief="groove", font=("Consulas", 15,"bold"), fg="#133E87", highlightbackground="#133E87",highlightthickness=1)
        name_text.pack(padx=5)

        contacts_label = tk.Label(room_frame, text="CONTACTS:", bg="white", anchor=tk.W, font=("Consulas", 15, "bold"), fg="#203e8d")
        contacts_label.pack(fill=tk.X, padx=18, pady=(20, 5))
        contacts_text = tk.Text(room_frame, height=1.2, width=22, bg="white", relief="groove", font=("Consulas", 15,"bold"), fg="#133E87", highlightbackground="#133E87",highlightthickness=1)
        contacts_text.pack(padx=5)

        bill_label = tk.Label(room_frame, text="MONTHLY BILL:", bg="white", anchor=tk.W, font=("Consulas", 15, "bold"), fg="#203e8d")
        bill_label.pack(fill=tk.X, padx=18, pady=(20, 5))
        bill_text = tk.Text(room_frame, height=1.2, width=22, bg="white", relief="groove", font=("Consulas", 15,"bold"), fg="#133E87", highlightbackground="#133E87",highlightthickness=1)
        bill_text.pack(padx=5)

        due_date_label = tk.Label(room_frame, text="DUEDATE:", bg="white", anchor=tk.W, font=("Consulas", 15, "bold"), fg="#203e8d")
        due_date_label.pack(fill=tk.X, padx=18, pady=(20, 5))
        due_date_text = tk.Text(room_frame, height=1.2, width=22, bg="white", relief="groove", font=("Consulas", 15,"bold"), fg="#133E87", highlightbackground="#133E87",highlightthickness=1)
        due_date_text.pack(padx=5)

        self.rooms[room_number] = {
            "status": status_text,
            "name": name_text,
            "contacts": contacts_text,
            "bill": bill_text,
            "due_date": due_date_text,
        }
    
    def show(self):
        self.deiconify()

    def on_exit(self):
        if messagebox.askyesno("Confirm", "Do you want to proceed?"):
            self.destroy()

    def edit_room(self):
        
        self.withdraw()  # Hide the dashboard
        edit_window = ChangeRoomDetail()
        edit_window.mainloop()

    def set_text_pane(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="ronmel06",
                database="ronmeldb"
            )
            cursor = conn.cursor()

            for room_number in range(1, 6):
                cursor.execute(f"SELECT * FROM ronmeltb WHERE room = {room_number}")
                result = cursor.fetchone()

                room_fields = self.rooms[room_number]
                # Clear previous text
                for text_widget in room_fields.values():
                    text_widget.delete(1.0, tk.END)

                if result:
                    # Ensure that the unpacking matches the column order in your database
                    room_name, contacts, monthly, duedate = result[3], result[4], result[5], result[6]
                    room_fields["status"].insert(tk.END, "OCCUPIED")
                    room_fields["name"].insert(tk.END, room_name)
                    room_fields["contacts"].insert(tk.END, contacts)
                    room_fields["bill"].insert(tk.END, monthly)
                    room_fields["due_date"].insert(tk.END, duedate)
                else:
                    room_fields["status"].insert(tk.END, "VACANT")

            conn.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

class LogAdmin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.overrideredirect(True) 
        self.title("ADMIN LOGIN")
        self.center_window(400, 391)

    def center_window(self, width, height):
        # Get the screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Calculate x and y coordinates for the center of the screen
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        # Set the position of the window
        self.geometry(f'{width}x{height}+{x}+{y}')

    def setup_ui(self):
        self.main_frame = tk.Frame(self, bg='#cbdce1', padx=20, pady=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Exit button styled similarly
        self.exit_button = tk.Button(self.main_frame, text="X", font=("Segoe UI Black", 8), fg='white', bg='#136291',
                                     command=self.exit_app, bd=0, width=2, height=0)
        self.exit_button.pack(side=tk.TOP, anchor='ne', padx=(0, 0), pady=(5, 0))

        tk.Label(self.main_frame, text="RENTAL HOUSE", font=("STHupo", 34, 'bold'), bg='#cbdce1', fg='#136291').pack(pady=(10, 0))

        tk.Label(self.main_frame, text="ADMIN:", font=("Segoe UI Black", 16), bg='#cbdce1', fg='#136291', anchor='w').pack(anchor='w', padx=(10, 0), pady=(10, 0))
        self.admin_name = tk.Entry(self.main_frame, font=("Segoe UI", 15), fg='#136291', justify='left', width=30, bd=2, relief='groove')
        self.admin_name.pack(padx=(13, 0), pady=(0, 10))

        tk.Label(self.main_frame, text="PASSWORD:", font=("Segoe UI Black", 16), bg='#cbdce1', fg='#136291', anchor='w').pack(anchor='w', padx=(10, 0), pady=(10, 0))
        self.admin_pass = tk.Entry(self.main_frame, font=("Segoe UI", 15), fg='#136291', justify='left', show='•', width=30, bd=2, relief='groove')
        self.admin_pass.pack(padx=(13, 0), pady=(0, 10))

        self.check_var = tk.IntVar()
        self.show_check = tk.Checkbutton(self.main_frame, text="SHOW", variable=self.check_var, command=self.toggle_password, bg='#cbdce1', font=("Segoe UI", 7))
        self.show_check.pack(anchor='w', pady=(5, 5), padx=(290, 0))

        button_frame = tk.Frame(self.main_frame, bg='#cbdce1')
        button_frame.pack(pady=(5, 10), fill=tk.X)

        button_font = ("Segoe UI Black", 16)

        button_user = tk.Button(button_frame, text="USER", font=button_font, fg='#136291', bg='#e1f5fe', width=12, command=self.open_user_login, bd=0)
        button_login = tk.Button(button_frame, text="LOGIN", font=button_font, fg='white', bg='#136291', width=12, command=self.login, bd=0)

        button_user.pack(side=tk.LEFT, padx=(18, 5))
        button_login.pack(side=tk.LEFT, padx=(5, 0))

    def toggle_password(self):
        self.admin_pass.config(show='' if self.check_var.get() else '•')

    def login(self):
        username = self.admin_name.get()
        password = self.admin_pass.get()

        try:
            con = mysql.connector.connect(
                host='localhost',
                database='ronmeldb',
                user='root',
                password='ronmel06'
            )
            query = "SELECT * FROM admintb WHERE BINARY admin = %s AND BINARY password = %s"
            cursor = con.cursor()
            cursor.execute(query, (username, password))

            if cursor.fetchone():
                messagebox.showinfo("Login Successful", "Welcome admin!")
                self.destroy()
                Dashboard().mainloop()
            else:
                messagebox.showerror("Error", "Invalid Username or Password")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()

    def open_user_login(self):
        self.destroy()
        LogUser(tk.Tk()).root.mainloop()

    def exit_app(self):
        if messagebox.askyesno("Confirm Exit", "Do you want to exit?"):
            self.destroy()


class LogUser:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True) 
        self.root.title("User Login")
        self.setup_ui()  # Assuming this method is defined elsewhere
        self.center_window(400, 391)

    def center_window(self, width, height):
        # Get the screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calculate x and y coordinates for the center of the screen
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        # Set the position of the window
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def setup_ui(self):
        self.main_frame = tk.Frame(self.root, bg='#cbdce1', padx=20, pady=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Exit button styled similarly
        self.exit_button = tk.Button(self.main_frame, text="X", font=("Segoe UI Black", 8), fg='white', bg='#136291',
                                     command=self.quit, bd=0, width=2, height=0)
        self.exit_button.pack(side=tk.TOP, anchor='ne', padx=(0, 0), pady=(5, 0))

        tk.Label(self.main_frame, text="RENTAL HOUSE", font=("STHupo", 34, 'bold'), bg='#cbdce1', fg='#136291').pack(pady=(10, 0))

        tk.Label(self.main_frame, text="USERNAME:", font=("Segoe UI Black", 16), bg='#cbdce1', fg='#136291', anchor='w').pack(anchor='w', padx=(10, 0), pady=(10, 0))
        self.user_name = tk.Entry(self.main_frame, font=("Segoe UI", 15), fg='#136291', justify='left', width=30, bd=2, relief='groove')
        self.user_name.pack(padx=(13, 0), pady=(0, 10))

        tk.Label(self.main_frame, text="PASSWORD:", font=("Segoe UI Black", 16), bg='#cbdce1', fg='#136291', anchor='w').pack(anchor='w', padx=(10, 0), pady=(10, 0))
        self.user_pass = tk.Entry(self.main_frame, font=("Segoe UI", 15), fg='#136291', justify='left', show='•', width=30, bd=2, relief='groove')
        self.user_pass.pack(padx=(13, 0), pady=(0, 10))

        self.check_pass_var = tk.IntVar()
        self.show_check = tk.Checkbutton(self.main_frame, text="SHOW", variable=self.check_pass_var, command=self.toggle_password, bg='#cbdce1', font=("Segoe UI", 7))
        self.show_check.pack(anchor='w', pady=(5, 5), padx=(290,0))

        # Create a frame for buttons at the bottom
        button_frame = tk.Frame(self.main_frame, bg='#cbdce1')
        button_frame.pack(pady=(5, 10), fill=tk.X)

        button_font = ("Segoe UI Black", 16)

        # Change the order of buttons: ADMIN button first
        button_admin = tk.Button(button_frame, text="ADMIN", font=button_font, fg='#136291', bg='#e1f5fe', width=12, command=self.open_admin, bd=0)
        button_login = tk.Button(button_frame, text="LOGIN", font=button_font, fg='white', bg='#136291', width=12, command=self.login, bd=0)

        # Pack the ADMIN button first followed by the LOGIN button
        button_admin.pack(side=tk.LEFT, padx=(18, 5))  # Add padding to the right
        button_login.pack(side=tk.LEFT, padx=(5, 0))  # Add padding to the left

    def toggle_password(self):
        self.user_pass.config(show='' if self.check_pass_var.get() else '•')

    def login(self):
        username = self.user_name.get()
        password = self.user_pass.get()

        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='ronmeldb',
                user='root',
                password='ronmel06'
            )
            cursor = connection.cursor()
            query = "SELECT * FROM ronmeltb WHERE BINARY username = %s AND BINARY password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            if result:
                messagebox.showinfo("Login successful", f"Welcome, {username}!")
                self.root.destroy()
                user_dashboard = UserDashboard()
                user_dashboard.display_user(username)
            else:
                messagebox.showerror("Login failed", "Invalid Username or Password")
        except mysql.connector.Error as err:
            messagebox.showerror("Database error", f"Error: {err}")
        finally:
            if cursor:
                cursor.close()
            if connection.is_connected():
                connection.close()

    def open_admin(self):
        self.root.destroy()
        LogAdmin().mainloop()

    def quit(self):
        if messagebox.askyesno("Confirm Exit", "Do you want to exit?"):
            self.root.destroy()


class UserDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("User Dashboard")
        self.geometry("800x600")
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'ronmel06',
            'database': 'ronmeldb'
        }
        self.main_frame = tk.Frame(self, bg="#136291")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()
        self.overrideredirect(True) 
        self.title("User Login")
        self.center_window(900, 427)

    def center_window(self, width, height):
        # Get the screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Calculate x and y coordinates for the center of the screen
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        # Set the position of the window
        self.geometry(f'{width}x{height}+{x}+{y}')

    def create_widgets(self):
        self.panel2 = tk.Frame(self.main_frame, bg="#CBDBEB")
        self.panel2.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Frame for room label and room number
        room_frame = tk.Frame(self.panel2, bg="#136291")
        room_frame.pack(pady=(20, 0))

        tk.Label(room_frame, text="ROOM ", font=("Segoe UI Black", 48), fg="#136291", bg="#CBDBEB").pack(side=tk.LEFT)
        self.numPane = tk.Label(room_frame, text="5", font=("Segoe UI Black", 48), fg="#136291", bg="#CBDBEB")
        self.numPane.pack(side=tk.LEFT)

        self.create_user_info_widgets()
        self.create_landlord_info_widgets()

    def create_user_info_widgets(self):
        tk.Label(self.panel2, text="REGISTERED NAME:", font=("Segoe UI Black", 15), fg="#136291", bg="#CBDBEB").pack(pady=(20, 0), padx = (0, 150))
        self.userdashName = tk.Label(self.panel2, text="Angel Bert Gonzales", font=("Segoe UI Black", 22,"bold"),fg="#136291", bg="#CBDBEB", width=22)
        self.userdashName.pack()

        tk.Label(self.panel2, text="BILL / MONTH:", font=("Segoe UI Black", 15), fg="#136291", bg="#CBDBEB").pack(pady=(10, 0), padx = (0, 194))
        self.userdashBill = tk.Label(self.panel2, text="30,000", font=("Segoe UI Black", 22,"bold"), fg="#136291",bg="#CBDBEB", width=10)
        self.userdashBill.pack()

        tk.Label(self.panel2, text="DUEDATE:", font=("Segoe UI Black", 15), fg="#136291", bg="#CBDBEB").pack(pady=(10, 0), padx = (0, 240))
        self.userdashDate = tk.Label(self.panel2, text="2020-10-10", font=("Segoe UI Black", 22,"bold"), fg="#136291",bg="#CBDBEB", width=10)
        self.userdashDate.pack()

    def create_landlord_info_widgets(self):
        tk.Button(self.main_frame, text="EXIT", font=("Segoe UI Black", 10), bg="white", fg="#136291", command=self.confirm_exit).pack(padx=(420, 0), pady=(10, 0))

        tk.Label(self.main_frame, text="LANDLORD'S INFO", font=("Segoe UI Black", 34), fg="white", bg="#136291").pack(pady=(0, 20))
        tk.Label(self.main_frame, text="NAME:", font=("Segoe UI Black", 20), fg="white", bg="#136291").pack(padx=(0, 327))
        tk.Label(self.main_frame, text="DANILO K. GOMEZ", font=("Segoe UI Black", 35), fg="white", bg="#136291").pack()
        
        tk.Label(self.main_frame, text="CONTACTS:", font=("Segoe UI Black", 20), fg="white", bg="#136291").pack(pady=(20, 0), padx=(0, 270))
        tk.Label(self.main_frame, text="09934211274", font=("Segoe UI Black", 28), fg="white", bg="#136291").pack(padx=(0, 190))
        tk.Label(self.main_frame, text="GOMEZDANILO@GMAIL.COM", font=("Segoe UI Black", 22), fg="white", bg="#136291").pack()


    def confirm_exit(self):
        response = messagebox.askyesno("Confirm", "Do you want to proceed?")
        if response:
            self.quit()

    def display_user(self, username):
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()
            query = "SELECT room, name, monthly, duedate FROM ronmeltb WHERE username = %s"
            cursor.execute(query, (username,))

            result = cursor.fetchone()
            if result:
                room, name, monthly, duedate = result
                self.numPane.config(text=str(room))
                self.userdashName.config(text=str(name))
                self.userdashBill.config(text=str(monthly))
                self.userdashDate.config(text=str(duedate))
            else:
                messagebox.showerror("Error", "No user found with the given username.")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            if cursor:
                cursor.close()
            if conn.is_connected():
                conn.close()


if __name__ == "__main__":
    login_app = LogUser(tk.Tk())
    login_app.root.mainloop()
