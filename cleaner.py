def filter_nmea_lines(input_file, output_file):
    with open(input_file, 'r') as infile:
        with open(output_file, 'w') as outfile:
            for line in infile:
                if 'Raw' in line:
                    outfile.write(line)

def main():
    # Example usage:
    input_file = 'campagna_outdoor_250324.txt'  # Replace 'input.txt' with the path to your input file
    output_file = 'output.txt'  # Replace 'output.txt' with the desired output file path
    filter_nmea_lines(input_file, output_file)

if __name__ == "__main__":
    main()