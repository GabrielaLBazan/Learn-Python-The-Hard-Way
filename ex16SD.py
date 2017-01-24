from sys import argv

script, filename = argv

print "Let's try erasing %r again." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want it though, hit RETURN."

raw_input("?")

print "Opening file again..."
target = open(filename, 'w')

print "Let's try these three lines again, shall we?"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Ok, let's try printing this stuff without all those lines."

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "And let's close the file again."
target.close()

# file = open('filename.file')
# print open.read()

# ^^ that will check your work in python in powershell
