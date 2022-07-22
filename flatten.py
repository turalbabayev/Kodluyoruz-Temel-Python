inputList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
outputList = list()
def flatten(a):

    for i in a:
        if isinstance(i,list):
            flatten(i)
        else:
            outputList.append(i)

flatten(inputList)
print(outputList)