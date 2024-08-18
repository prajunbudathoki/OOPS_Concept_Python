class ChatBook:
    __user_id = 0
    def __init__(self):
        self.__name = "hello"
        self.id = ChatBook.__user_id
        ChatBook.__user_id += 1
        self.username = ''
        self.password = ''
        self.loggedin = False
        # self.menu()

    def get_name(self):
        return self.__name
    
    def set_name(self,value):
        self.__name = value

    @staticmethod
    def get_id(val):
        return ChatBook.__user_id
    
    @staticmethod
    def set_id(val):
        ChatBook.__user_id = val 

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
            self.post()
        elif user_input == '4':
            self.message_to_friend()
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
                print("\n")
                self.menu()
            else:
                print("Wrong credentials given :(")

    def post(self):
        if self.loggedin == True:
            text = input("Enter your post here: ")
            print(f"The message has been posted {text}")
        else:
            print("You need to be logged in first")
        print("\n")
        self.menu()
    
    def message_to_friend(self):
        if self.loggedin == True:
            txt = input("Enter your message here: ")
            frnd = input("To whom this message concerned? ")
            print(f"Message has been delivered successfully to {frnd}")
        else:
            print("You need to be logged in first")
            print("\n")
            self.menu()

obj = ChatBook()


