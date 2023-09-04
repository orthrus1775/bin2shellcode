def main():
    input_file = input("Enter the path to the binary file: ")

    try:
        with open(input_file, 'rb') as file:
            data = file.read()
            hex_data = bytes_to_hex(data)
            print("Hex representation in \\x## format:")
            print(hex_data)
            print("\nHex representation in 0x## format:")
            print(hex_data.replace('\\x', '0x'))
    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

def bytes_to_hex(data):
    return ''.join([f'\\x{byte:02x},' for byte in data])

if __name__ == "__main__":
    main()

