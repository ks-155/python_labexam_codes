file1 = open("file1.txt", "w")
file1.write("File 1 - Line 1\nFile 1 - Line 2\nFile 1 - Line 3\nFile 1 - Line 4")
file1.close()

file2 = open("file2.txt", "w")
file2.write("File 2 - Line A\nFile 2 - Line B")
file2.close()
f1 = open("file1.txt", "r")
lines1 = f1.readlines()  # List of lines from file 1
f1.close()

f2 = open("file2.txt", "r")
lines2 = f2.readlines()  # List of lines from file 2
f2.close()
f3 = open("target.txt", "w")

max_length=max(len(lines1), len(lines))
for i in range(max_length):
    if i < len(lines1):
        f3.write(lines1[i])
        #
    if i < len(lines2):
        f3.write(lines2[i])
f3.close()
print("Dono files alternately target.txt mein merge ho chuki hain!")
print("\n--- Target File ka Result ---")
f_result = open("target.txt", "r")
print(f_result.read())
f_result.close()

