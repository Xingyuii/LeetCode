from typing import List
def merge(intervals: List[List[int]]) -> List[List[int]]:
    merge =[]
    intervals = sorted(intervals, key=lambda x: x[0])
    for i in intervals:
        if not merge or i[0] > merge[-1][1]:
            merge.append(i) #先append,否则merge为空会报错 out of index range
        else:
            merge[-1][1]=max(merge[-1][1],i[1])
    return merge

#test
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
