def open_file(file_name, mode):
    try:
        file = open(file_name, mode)
    except IOError:
        print(f"File {file_name} wasn't opened!")
        return None
    else:
        print(f"File {file_name} was successfully opened! Everything okey!")
        return file
    
file1 = "TF19_1"
file2 = "TF19_2"

file1_write = open_file(file1, "w+")
if file1_write != None:
    file1_write.write("I\'d l   like to  tell y you   about   m my usual r  route, how I  get t to  my f friend\'s house.\nWe  don\'t l live   f far   from  e each    other, i   i   it\'s a   about a   15  m  minute   walk.\nT The   building   where my   friend  l lives   is next to t  the    supermarket, just b before y you   reach   it.\nIt\'s t a  tall 14-storey b  building, so   you can\'t  miss  i it.")
    file1_write.close()
    print(f"File {file1} was modified and was successfully closed!")

file1_read = open_file(file1, "r")
file2_write = open_file(file2, "w+")
if file1_read != None and file2_write != None:
    new_lines = []
    for line in file1_read:
        words = line.split()
        full_words = [word for word in words if len(word) > 1]
        united_words = ' '.join(full_words)
        new_lines.append(united_words)
    for line in new_lines:
        file2_write.write(line + "\n")

    file1_read.close()
    file2_write.close()
    print(f"File {file2} was modified and two files were closed!")

file2_read = open_file(file2, "r")
if file2_read != None:
    print(f"File {file2} content:")
    for line in file2_read:
        print(line, end = '')
    file2_read.close()
    print(f"File {file2} was closed!")