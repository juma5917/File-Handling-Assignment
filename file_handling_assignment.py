try:
    # File Creation
    with open("my_file.txt", "w") as file:
        file.write("This is line 1.\n")
        file.write("12345\n")
        file.write("Another line with some text and numbers: 42\n")

    # File Reading and Display
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        for line in file:
            print(line.strip())

    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("Appending line 1.\n")
        file.write("Appending line 2.\n")
        file.write("Appending line 3.\n")

except FileNotFoundError:
    print("File not found error.")
except PermissionError:
    print("Permission error. You don't have the required permissions.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Script execution completed.")

