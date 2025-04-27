def typed_input():
    try:
        return input("You: ")
    except KeyboardInterrupt:
        print("\nSee Ya later!")
        return "exit"