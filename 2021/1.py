def read():
    import fileinput
    file = "input1.txt"
    inputs=[]
    with fileinput.input(files=file,encoding="utf-8") as f:
        for line in f:
            inputs.push(line)
    fileinput.close()



def main():
    inputs = read()
    for num in inputs:
        print(num)


if __name__== "__main__":
    main()