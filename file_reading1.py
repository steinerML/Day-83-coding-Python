filename = 'File Reading/readme.txt'

#Reading an entire file AT ONCE and stores it in a string:
with open (filename) as f: #By default opened in Reading(r) mode.
    content = f.read()
    print(content) #Note that it will print a newline character \n when reaches EOF.

# #Reading an entire file AT ONCE removing the newline character.
with open (filename, 'r') as f:
    content = f.read()
    print(content.rstrip())

# #Reading the ENTIRE file with a loop and storing it in a list:
with open (filename) as f:
    contents = f.readlines()
    print('We start looping here:')
    print(contents)
    # for content in contents:
    #     print(content)
#print(type(contents)) returns a list type element.

#Reading LINE BY LINE entire file with a loop without removing newline character
with open (filename) as f:
    for line in f:
        print(line)

#Reading LINE BY LINE entire file with a loop, removing newline character.
with open (filename) as f:
    for line in f:
        print(line.rstrip())


#Reading the FIRST line of a file:
with open (filename) as f:
    content = f.readline()
    print("First line:\n",content)

#Reading the file without stripping characters

# with open ('File Reading\strip.txt') as f:
#     content = f.read()
#     print(content)

#Reading file and stripping characters (beginning and end, end, beginning)
with open ('File Reading/strip.txt') as f:
    content = f.readline()
    print(content.strip("$")) #We strip all characters