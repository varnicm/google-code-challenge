# import math 
# def solution(area):
#     square_list=[]
#     while(area != 0):
#         a=math.sqrt(area)
#         if(isinstance(a, int) == False):
#             square_list.append((math.floor(a)**2))
#             area=area-(math.floor(a)**2)
#         else:
#             square_list.append((math.floor(a)**2))
#     return square_list

# sd=int(input("please inter area: "))
# print(solution(sd))

import math
def solution(area):
    square_list=[]
    while(area != 0):
        a=math.sqrt(area)
        if abs(a - math.floor(a)) > 1e-9:
            square = math.floor(a) ** 2
            square_list.append(square)
            area=area-square
        else:
            square_list.append((math.floor(a)**2))
            break

    return ','.join(map(str, square_list))

print(solution(15324))