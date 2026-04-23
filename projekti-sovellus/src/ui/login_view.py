from tkinter import ttk, constants, StringVar
from src.services.user_service import user_service, InvalidCredentialsError

class LoginView:
    def __init__(self, root, handle_login, handle_show_register):
        self._root = root
        self._handle_login = handle_login
        self._handle_show_register = handle_show_register
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_label = None
        self._error_variable = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.Y)

    def destroy(self):
        self._frame.destroy()

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            user_service.login(username, password)
            self._handle_login()
        except InvalidCredentialsError:
            self._show_error(str("Invalid username or password"))

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Username:")

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(row=1, column=0, padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Password:")

        self._password_entry = ttk.Entry(master=self._frame, show="*")

        password_label.grid(row=2, column=0, padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(row=3, column=0, padx=5, pady=5, sticky=constants.EW)
    
    def _initialize_error_label(self):
        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error_variable, foreground="red"
            )
        self._error_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        self._hide_error()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_error_label()
        self._initialize_username_field()
        self._initialize_password_field()

        show_login_button = ttk.Button(
            master=self._frame, text="Login", command=self._login_handler
            )
        not_user_label = ttk.Label(master=self._frame, text="Do you not have an account yet?")
        not_user_label.grid(row=6, column=0, padx=5, pady=5, sticky=constants.W)
        create_user_button = ttk.Button(
            master=self._frame, text="Register as user", command=self._handle_show_register
            )

        show_login_button.grid(row=5, column=0, padx=5, pady=5, sticky=constants.EW)
        create_user_button.grid(row=7, column=0, padx=5, pady=5, sticky=constants.EW)
