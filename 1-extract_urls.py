# Copy your column containing the hyperlinks and paste it into a Word document.
# Save your Word document as Web Page and name it Hyperlinks.
# Save this Python script in a python file .py
# Move the Python file and htm file to the same location.
# Run the Script!
# Python script will create a txt file with the links.

def extract_hyperlinks_txt_file():
    txt_file = open('Hyperlinks.htm', 'r')
    read = txt_file.read()
    lines = read.split()

    links = ''
    for i in lines:
        # if 'href=http' in i:
        links += i
    print(links)
    split_quote_m = links.split('"')

    f = open('links.txt', 'a')
    for i in split_quote_m:
        if 'http' in i:
            f.write(i)
            f.write('\n')

extract_hyperlinks_txt_file()