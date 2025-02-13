import argparse

def create_extended_wordlist(input_file, output_file, extensions):
    """
    Creates a new wordlist by appending specified extensions to each word
    in an existing wordlist.

    Args:
        input_file (str): Path to the input wordlist file.
        output_file (str): Path to the output wordlist file.
        extensions (list): A list of extensions to append (e.g., ['.zip', '.tar.gz']).
    """

    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for word in infile:
                word = word.strip()  # Remove leading/trailing whitespace, including newline
                for ext in extensions:
                    outfile.write(word + ext + '\n')  # Append extension and write to output
    except FileNotFoundError:
        print(f"Error: Input file not found: {input_file}")
        exit(1)  # Exit with an error code
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create an extended wordlist by appending extensions.")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to the input wordlist file.")
    parser.add_argument("-o", "--output", required=True, help="Path to the output wordlist file.")
    parser.add_argument("-e", "--extensions", nargs='+', default=['.zip', '.tar.gz', '.rar', '.7z', '.bak', '.old'],
                        help="List of extensions to append (default: .zip .tar.gz .rar .7z .bak .old)")

    args = parser.parse_args()

    create_extended_wordlist(args.wordlist, args.output, args.extensions)

    print(f"Extended wordlist created successfully: {args.output}")
