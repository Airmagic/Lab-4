import pathlib

def alternate_case(stringInput):
    # code copied from board, clara
    out = ''
    counter = 0
    for char in stringInput:
        if counter % 2 == 0:
            out += char.lower()
        else:
            out += char.upper()
        counter +=1
    return out

def countPythonFile(files):

    # define the pattern
    currentPattern = ".py"

    total = 0

    for currentFiles in files:
        if currentFiles.lower().endswith(currentPattern):
            total +=1

    return total

if __name__ == '__main__':
    main()
