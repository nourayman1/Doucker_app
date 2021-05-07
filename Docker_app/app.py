
f1 = open('Beyond the Wall of Sleep.txt', encoding="utf8")
B= f1.read()
f2 = open('Pride and Prejudice.txt', encoding="utf8")
P= f2.read()
marcks = '''!()-[]{};:”'"“—\,<>./?@#$%^&*_~'''
n='                               '
B= B.translate(str.maketrans(marcks, n))   
P = P.translate(str.maketrans(marcks, n))   
B=B.lower().split()
P=P.lower().split()
comm = set(B) & set(p)
print(comm)
f1.close()
f2.close()