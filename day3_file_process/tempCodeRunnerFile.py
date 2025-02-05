file = open(r"file_handle_day3\\test.txt", "r")
print(file.tell())
data = file.readlines(2)
file.seek(0)