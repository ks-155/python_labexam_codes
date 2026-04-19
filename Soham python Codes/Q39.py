import os, sys

# 1. Source file ka naam lena aur check karna
flrname = input("Enter source File Name to read: ")
if os.path.isfile(flrname):
    fr = open(flrname, "r")
else:
    print(flrname, "doesn't exist.")
    sys.exit()

# 2. Destination file ka naam lena
flwname = input("Enter destination File Name to write: ")
fw = open(flwname, "w") # "w" mode purani file ko overwrite kar dega

# 3. Pehla character read karna
ch = fr.read(1)

# 4. Jab tak file khatam na ho (empty string na mile) loop chalana
while ch != "":
    # Character ko uppercase mein convert karke write karna
    fw.write(ch.upper()) 
    
    # Next character read karna
    ch = fr.read(1)

# 5. Buffer clear karne ke liye dono files ko close karna
fr.close()
fw.close()

print(flrname, "is copied to", flwname, "in UPPERCASE successfully.")
