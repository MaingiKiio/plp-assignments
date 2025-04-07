def modify_file(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as infile:
            content = infile.read()

        # Convert to uppercase for differentiation
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask the user for the input file name
input_file = input("Enter the name of the input file: ")
output_file = 'output.txt'

modify_file(input_file, output_file)
