from oops_proj import ChatBook
user1 = ChatBook()
print(user1.id)

# using static methods from class rather than objects 
ChatBook.set_id(10)
user2 = ChatBook()
print(user2.id)

# user2 = ChatBook()
# print(user2.id)

# user3 = ChatBook()
# print(user3.id)




# getter and setter 
# print(user.get_name())
# user.set_name("Barry Allen")
# print(user.get_name())