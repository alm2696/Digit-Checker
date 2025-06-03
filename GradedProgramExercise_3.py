def check_digits(infile):
    try:
        with open(infile, 'r') as file:
            contents = file.read()
            if any(char.isdigit() for char in contents):
                print("Digit present in the file")
                return True
            else:
                print("Digit not present in the file")
                return False
    except FileNotFoundError:
        print("File not found")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

check_digits(r'C:\Users\angel\Downloads\input.txt')