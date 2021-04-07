#
# import sys
# for line in sys.stdin:
#     def square(s):
#         return s*s
#     print(square(5))
#     """
import sys

for line in sys.stdin:

    l = line.split(" | ")


    l1 = l[0]
    l2 = l[1]
    l1_1 = l1.split()
    l2_1  =l2.split()


    # longest = max(line.split(), key=len)
    #res_list = []
    #for i in range(0, len(l1_1)):
    #    res_list.append(int(l1_1[i]) * int(l2_1[i]))
    res_list = [int(l1_1[i]) * int(l2_1[i]) for i in range(len(l1_1))]

    for j in res_list:
        print(j, end = " ")


