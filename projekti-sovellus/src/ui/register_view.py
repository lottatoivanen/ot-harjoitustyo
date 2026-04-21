from tkinter import ttk, constants, StringVar
from services.user_service import user_service, UsernameAlreadyExistsError

class RegisterView:
    """Käyttäjien rekisteröitymisestä vastaava näkymä."""

    def __init__(self, root, handle_create_user, handle_show_login):
        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_show_login = handle_show_login
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._password_again_entry = None
        self._error_label = None
        self._error_variable = None
        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.Y)
    
    def destroy(self):
        self._frame.destroy()
    
    def _create_user(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        password_again = self._password_again_entry.get()

        if len(username) < 4:
            self._show_error(str("Username must be at least 4 characters long"))
            return

        if len(password) < 6:
            self._error_variable.set(str("Password must be at least 6 characters long"))
            return
        
        if password != password_again:
            self._error_variable.set(str("Passwords do not match"))
            return

        try:
            user_service.create_user(username, password)
            self._handle_create_user()
        except UsernameAlreadyExistsError:
            self._error_variable.set(f"Username {username} already exists")
    
    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()
    
    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Username:")

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(row=0, column=1, padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Password:")

        self._password_entry = ttk.Entry(master=self._frame, show="*")

        password_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(row=1, column=1, padx=5, pady=5, sticky=constants.EW)
    
    def _initialize_password_again_field(self):
        password_again_label = ttk.Label(master=self._frame, text="Password again:")

        self._password_again_entry = ttk.Entry(master=self._frame, show="*")

        password_again_label.grid(row=2, column=0, padx=5, pady=5, sticky=constants.W)
        self._password_again_entry.grid(row=2, column=1, padx=5, pady=5, sticky=constants.EW)

    def _initialize_error_label(self):
        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error_variable, foreground="red"
            )
        self._error_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self._hide_error()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_username_field()
        self._initialize_password_field()
        self._initialize_password_again_field()
        self._initialize_error_label()

        create_user_button = ttk.Button(
            master=self._frame, text="Register as user", command=self._create_user
            )
        already_label = ttk.Label(master=self._frame, text="Already have an account?")
        already_label.grid(row=5, column=1, padx=5, pady=5, sticky=constants.W)
        show_login_button = ttk.Button(
            master=self._frame, text="Login", command=self._handle_show_login
            )

        create_user_button.grid(row=4, column=1, padx=5, pady=5, sticky=constants.EW)
        show_login_button.grid(row=6, column=1, padx=5, pady=5, sticky=constants.EW)