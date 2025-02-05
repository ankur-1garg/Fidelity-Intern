import os
print(os.listdir("."))
print(os.walk("."))
for dirpath, dirnames, filenames in os.walk("."):
    # print(f"Found directory: {dirpath}")
    # for file_name in filenames:
    #     print(file_name)
    # for dir_name in dirnames:
    #     print(dir_name)
    for i in filenames:
        if i.endswith(".py"):
            print(i)
