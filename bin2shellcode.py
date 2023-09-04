import sys

def print_help():
    print("Usage: python binary_to_hex.py <path_to_binary_file> <output_format>")
    print("Arguments:")
    print("<path_to_binary_file>: Path to the binary file you want to convert.")
    print("<output_format>: Output format (choose 'C' or 'C#').")

def main():
    if len(sys.argv) != 3:
        print_help()
        return

    input_file = sys.argv[1]
    output_format = sys.argv[2]

    try:
        with open(input_file, 'rb') as file:
            data = file.read()
            hex_data = bytes_to_hex(data, output_format)
            print(output_format + " shellcode \n")
            print(hex_data + "\n")
            print(output_format + " base64 encoded shellcode \n")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

def bytes_to_hex(data, output_format):
    if output_format == "C":
        return ''.join([f'\\x{byte:02x}' for byte in data])
    elif output_format == "C#":
        return ''.join([f'0x{byte:02x}, ' for byte in data])
    else:
        return "Unsupported output format. Use 'C' or 'C#'."

if __name__ == "__main__":
    main()