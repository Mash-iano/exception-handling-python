def modify_file_content(content):
    """Convert content to uppercase."""
    return content.upper()

def main():
    filename = input("Enter the filename to read from: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File read successfully!")

        modified_content = modify_file_content(content)

        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            print(f"Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
