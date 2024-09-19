# file_handling_assignment.py

def create_and_write_file(filename):
    try:
        # Create a new file and write initial content
        with open(filename, 'w') as file:
            file.write("This is the first line of text.\n")
            file.write("Here is the second line with a number: 123\n")
            file.write("And this is the third line with some more text.\n")
        print("File created and initial content written successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
    finally:
        print("File writing operation finished.")

def read_and_display_file(filename):
    try:
        # Read the content of the file and display it
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile Content:")
            print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
    finally:
        print("File reading operation finished.")

def append_to_file(filename):
    try:
        # Append additional content to the file
        with open(filename, 'a') as file:
            file.write("This is the fourth line of text appended.\n")
            file.write("Here is the fifth line with another number: 456\n")
            file.write("And the sixth line with more text.\n")
        print("Additional lines appended to the file successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
    finally:
        print("File appending operation finished.")

def main():
    filename = "my_file.txt"
    
    create_and_write_file(filename)
    read_and_display_file(filename)
    append_to_file(filename)
    read_and_display_file(filename)  # Display the content again to show appended lines

if __name__ == "__main__":
    main()
