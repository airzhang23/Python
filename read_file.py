# Define a filename.
filename = "hosts"
 
# Open the file as f.
# The function readlines() reads the file.             
with open(filename) as f:
    content = f.readlines()
 
# Show the file contents line by line.
# We added the comma to print single newlines and not double newlines.
# This is because the lines contain the newline character '\n'. 
for line in content:
    newline = line.replace('localhost', 'MBP')
    print newline,
