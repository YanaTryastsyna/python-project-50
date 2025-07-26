import argparse
from hexlet_code.file_reader import read_file

def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    
    parser.add_argument(
        "-f", "--format",
        help="set format of output")
    
    args = parser.parse_args()

    data1 = read_file(args.first_file)
    data2 = read_file(args.second_file)


    print("Первый файл:", data1)
    print("Второй файл:", data2)

if __name__ == "__main__":
    main()

