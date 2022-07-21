if __name__ == "__main__":
    while True:
        try:
            input_line = input()
            print(input_line)
        except EOFError:
            break
