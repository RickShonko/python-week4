
# Read from original file and write modified content to a new file
def modify_file(input_file, output_file):
    try:
        with open(input_file, "r") as f:
            content = f.read()

        # modifies to uppercase
        modified = content.upper()

        with open(output_file, "w") as f:
            f.write(modified)

        print(f"Modified content written to {output_file}")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Run program
if __name__ == "__main__":
    modify_file("input.txt", "output.txt")
