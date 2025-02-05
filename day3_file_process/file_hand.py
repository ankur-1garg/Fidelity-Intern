file = open(r"day3\\test.txt", "r")

# Print the current file position
print("Current file position:", file.tell())

# Read the first 2 lines
data = file.readlines(2)
print("First 2 lines:", data)

# Move the file pointer to the beginning
file.seek(0)

# Read the first 5 characters
data = file.read(5)
print("First 5 characters:", data)

# Move the file pointer to the beginning again
file.seek(0)

# Read the entire file line by line
print("Reading the entire file line by line:")
for line in file:
    print(line.strip())

# Move the file pointer to the beginning again
file.seek(0)

# Count the number of lines and words
line_count = 0
word_count = 0
for line in file:
    line_count += 1
    word_count += len(line.split())

print("Number of lines:", line_count)
print("Number of words:", word_count)

# Close the file
file.close()
