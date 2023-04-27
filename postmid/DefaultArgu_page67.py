def ask_ok(prompt, retries=4, reminder="please try again!"):
    while True:
        ok = input(prompt)
        if ok.lower() in ("y", "ye", "yes"):
            return True
        if ok.lower() in ("n", "no", "nop", "nope"):
            return False
        retries = retries - 1
        if retries <= 0:
            print("invalid user response")
            break
        print(reminder)


ask_ok("enter yes or no : ")
