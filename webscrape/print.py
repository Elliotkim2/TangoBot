# Script to create a new file and write "Hello World"
file_name = "hello_world.txt"

try:
    # Open the file in write mode (creates the file if it doesn't exist)
    with open(file_name, "w") as file:
        file.write("Hello World\n")  # Write "Hello World" to the file

    print(f"File '{file_name}' created and written successfully!")
except Exception as e:
    print(f"An error occurred: {e}")