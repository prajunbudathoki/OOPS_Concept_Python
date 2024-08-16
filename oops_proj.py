class ChatBook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to chatBook ! How would you like to procced your request?
                     1. Press 1 to signup:
                     2. Press 2 to signin:
                      3. Press 3 to write a post:
                      4. Press 4 to message a friend:
                      5. Press anyother key to terminate """)
        
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            exit()

    def signup(self):
        email = input("Enter your email: ")
        pd = input("Enter your password here: ")
        self.username = email
        self.password = pd
        print("sign up successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("You haven't signup yet please follow the procedure")
        else:
            uname = input("enter your email/username here: ")
            pwd = input("enter your password: ")
            if self.username == uname and self.password == pwd:
                print("Sign in successfully")
                self.loggedin = True
            else:
                print("Wrong credentials given :(")

obj = ChatBook()


