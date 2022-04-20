# N1
# def rangeee(num1, num2, num3):
#     newlist = []
#     for i in range(num1, num2 + 1, num3):
#         newlist.append(i)
#     return newlist
# print(rangeee(50, 200, 30))

# myList1 = []
# myList = input("enter numbers --> ")
# myList = myList.split(" ")
# for i in range(0, len(myList)):
#     myList1.append(int(myList[i]))
# print(myList)
# print(myList1)

# ----------------------------------------
# N2
# def myList(oldList, newList=[]):
#     for i in range(0, len(oldList) - 1):
#         res = oldList[i] * oldList[i + 1]
#         newList.append(res)
#     return newList
# oldList = [1, 2, 3, 4, 5, 6]
# print(myList(oldList))

# ----------------------------------------
# N4
# wordList = ["anymore", "raven", "me", "communicate"] 
# wordList.sort(key=len)
# # print(min(wordList))
# # for i in range(0, len(wordList)):
# res = len(wordList[0]) + len(wordList[-1])
# print(res)

# ----------------------------------------
# N5

# ----------------------------------------
# N6

# ----------------------------------------
# N8





# ##########################################################
# N7
# oldDict = { "a": 1, "b": 2, "c": 2 }
# val = sorted(oldDict)
# ke = sorted(oldDict.values())
# newDict = {}
# print(val)
# print(ke)
# for i, j in zip(val, ke):
#     if j in newDict:
#        newDict[j].append(i)
#     else:
#        newDict[j]=[i]
#     # newDict.setdefault(i,j)
# print(newDict)



# N7------------------------- 2-rd dzev ----------------------
# # Python3 code to demonstrate  
# # swap of key and value 
    
# # initializing dictionary 
# old_dict = {'A': 67, 'B': 23, 'C': 45, 'E': 12, 'F': 69, 'G': 67, 'H': 23}
  
# # Printing original dictionary 
# print ("Original dictionary is : ")
# print(old_dict) 
  
# print()
# new_dict = {}
# for key, value in old_dict.items():
# #    print("key -- ", key)
# #    print("value -- ", value)
#    if value in new_dict:
#        new_dict[value].append(key)
#    else:
#        new_dict[value]=[key]
# print(new_dict)
# # # Printing new dictionary after swapping
# # # keys and values
# # print ("Dictionary after swapping is :  ") 
# # print("keys: values")
# # for i in new_dict:
# #     print(i, " :", new_dict[i])