Name1 = input("Please enter name 1: ")
Name2 = input("Please enter name 2: ")
N1 = [*Name1]
N2 = [*Name2]
def remove_common(N1, N2):
    for i in N1:
        if i in N2:
            N1.remove(i)
            N2.remove(i)
remove_common(N1, N2)
# print(N1,N2)
con = len(N1) + len(N2)
print(con)
flames = ["friends", "love", "affection", "marriage", "enemy", "sister"]
# print(len(flames))

inde = con % len(flames)
print(inde)
while len(flames) > 1:
   flames.pop(inde)
   inde = (inde + con) % len(flames)


