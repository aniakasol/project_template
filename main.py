from app.io import input 
from app.io import output

def main():
    try:
        input1 = input.input_from_console()
        write(input1)
        input2 = input.read_file("data/data_for_input.txt")
        write(input2)
        input3 = input.read_file_with_pandas("data/data_for_input.txt")
        write(input3)
    except Exception as e:
        print(e)

def write(input:str):
    output.output_to_console(input)
    output.write_to_file("data/data_output.txt", input)

if __name__ == "__main__":
    main()
