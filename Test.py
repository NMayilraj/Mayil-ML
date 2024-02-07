# from echo import echo
# print(echo("Please help me I'ds stuck on a mountain"))
Name1 = input("Please Enter Name 1: ")
Name2 = input("Please Enter Name 2: ")
def removeCommonWords():
#   com=[]

  if(Name1=="suriya"):
    print("love")
  else:
    N1 = [*Name1]
    N2 = [*Name2]
    for i in reversed(range(len(N1))):
      print(i)
      if N1[i] in N2:
        N1.remove(N1[i])
        N2.remove(N2[i])
    Result = len(N1 + N2) 
    print(Result) 
    finalArr = ["friends", "love", "affection", "marriage", "enemy", "sister"]

    print(finalArr[Result-1])
removeCommonWords()
