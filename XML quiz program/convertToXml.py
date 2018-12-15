import os
os.chdir('/Users/anderskolvraa/Documents/GitRepos/XML quiz')

os.listdir()

fil=open('Test of push-pull.txt')

content=fil.read()

print(content)

print(repr(content))

contents=content

contents=contents.replace('\n\t\t','INNERMOST BREAK')

contents=contents.replace('\n\t','MIDDLE BREAK')

contents=contents.replace('\n\n\n','OUTER BREAK')