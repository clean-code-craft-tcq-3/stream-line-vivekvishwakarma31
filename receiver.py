if __name__ == "__main__":
    print("Reciever Started")
    while True:
        try:
            input_line = input()
            print(input_line)
        except EOFError:
            break
