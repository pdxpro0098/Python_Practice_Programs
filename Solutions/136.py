def append_display(filename,append_content):
    with open(filename,'a') as f:
        f.write(append_content)

    with open(filename, 'r') as f:
        content = f.read()
        print("The file Content:")
        print(content)

filename = 'dalip.txt'
append_content = "alone "

append_display(filename,append_content)
