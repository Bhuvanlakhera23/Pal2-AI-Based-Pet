#**************************************************************************************************************************************

#                                                          MAIN.py WITHOUT WATCHDOG

# from core.brain import AIMLBrain
# from core.speech import speak, listen

# def main():
#     # Initialize the AIML brain
#     brain = AIMLBrain()

#     print("Pal2 is ready! Say or type something. Say 'exit' to quit.\n")

#     while True:
#         mode = input("[T]ype or [V]oice: ").strip().lower()

#         if mode == "exit":
#             speak("See You Later!!")
#             break

#         elif mode == "t":
#             user_input = input("You: ")
#             if user_input.lower() == "exit":
#                 speak("See You Later!!")
#                 break
#             response = brain.get_response(user_input.upper())  # Get response from AIMLBrain
#             speak(response)

#         elif mode == "v":
#             user_input = listen()
#             if user_input:
#                 if user_input.lower() == "exit":
#                     speak("See You Later!!")
#                     break
#                 response = brain.get_response(user_input.upper())  # Get response from AIMLBrain
#                 speak(response)
#             else:
#                 continue  # In case listen() returns None (e.g., speech not recognized)

#         else:
#             print("Invalid mode. Please choose [T] or [V].")

# if __name__ == "__main__":
#     main()

# ***************************************************************************************************************************************

#                                                          MAIN.py WITH WATCHDOG

from core.brain import AIMLLoader, stop_watcher  # Import AIMLLoader and stop_watcher from brain.py
from core.speech import speak, listen

def main():
    print("Pal2 is ready! Say or type something. Say 'exit' to quit.\n")
    speak("I am ready! How can I help you?")

    while True:
        mode = input("[T]ype or [V]oice: ").strip().lower()

        if mode == "exit":
            speak("See You Later!")
            stop_watcher(loader)  # Pass loader to stop the watcher gracefully
            break

        elif mode == "t":
            user_input = input("You: ")
            if user_input.lower() == "exit":
                speak("See You Later!")
                stop_watcher(loader)  # Pass loader to stop the watcher gracefully
                break
            response = loader.get_response(user_input.upper())
            speak(response)

        elif mode == "v":
            user_input = listen()
            if user_input:
                if user_input.lower() == "exit":
                    speak("See You Later!")
                    stop_watcher(loader)  # Pass loader to stop the watcher gracefully
                    break
                response = loader.get_response(user_input.upper())
                speak(response)
            else:
                continue  # In case listen() returns None (e.g., speech not recognized)

        else:
            print("Invalid mode. Please choose [T] or [V].")

if __name__ == "__main__":
    loader = AIMLLoader()  # Start AIMLLoader and file watcher
    main()


# ***************************************************************************************************************************************