from rich import print


#removing spaces
def CleanInput(Input: str):
    LInput: list = list(Input)
    NList: list = []
    for  i in LInput:
        if i != ' ':
            NList.append(i)
    print(NList)
    return NList

# Replace elements
def replaceElement(List:list, OldElement:any, NewElement:any):
    Nlist = []
    for i in range(len(List)):
        if List[i] == OldElement:
            List[i] = NewElement
            Nlist.append(List[i])
        else:
            Nlist.append(List[i])
    List = Nlist

# concatinating numbers:
def ConcatinateNumbers(List: list):
    x: str = ""
    vlist: list = []
    print(List)
    i = 0
    while i < len(List):
        if i < len(List) - 1 and List[i].isdigit() and List[i+1].isdigit():
            print("first statement")
            vlist.append(List[i])
            vlist.append(List[i+1])
            x = "".join(vlist)
            List[i] = "?"
            List.pop(i + 1)
            replaceElement(List,"?",x)
            print(List)
            print(x)
            print(vlist)
            x = ""
            vlist = []
        elif i > 0 and i < len(List) and List[i].isdigit() and List[i-1].isdigit():
            print("second statement")
            vlist.append(List[i-1])
            vlist.append(List[i])
            x = "".join(vlist)
            List[i] = "?"
            List.pop(i - 1)
            replaceElement(List,"?",x)
            print(List)
            print(x)
            x = ""
            vlist = []
        else:
            i += 1
    print("FINISHED INTEGERS")
    j = 0
    while j < len(List):
        if j < len(List) - 1 and List[j] == ".":
            print("First statement!")
            vlist.append(List[j-1])
            vlist.append(List[j])
            vlist.append(List[j+1])
            print(vlist)
            x = "".join(vlist)
            print(x)
            List[j] = "?"
            List.pop(j + 1)
            List.pop(j - 1)
            replaceElement(List, "?", float(x))
            x = ""
            vlist: list = []
        else:
            j += 1
    print("Final results after concatination:")
    print(List)
