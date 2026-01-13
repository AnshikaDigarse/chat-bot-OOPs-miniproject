from classes.chat_classes import User, ChatRoom

if __name__ == "__main__":
    room = ChatRoom("OOP Chill Zone 😄")

    u1 = User("Anshika")
    u2 = User("Teju")
    u3 = User("Sanu")

    # Users joining
    u1.join_chatroom(room)
    u2.join_chatroom(room)

    # Chat starts
    u1.send_message("Heyyy everyone 👋")
    u2.send_message("Hii Anshika! What's up? 😄")
    u1.send_message("Just revising OOP concepts 😂 You?")
    u2.send_message("Same here 😭 Python is fun but confusing sometimes")

    # Another user joins
    u3.join_chatroom(room)
    u3.send_message("Hey guys! Am I late? 😅")

    u1.send_message("Nopeee, perfect timing 👍")
    u2.send_message("Welcome Sanu! We were just talking about OOP 🤓")
    u3.send_message("Niceee!  ")


    # Show full chat history
    room.show_chat_history()

    # Users leaving
    u1.leave_chatroom()
    u2.leave_chatroom()
    u3.leave_chatroom()
