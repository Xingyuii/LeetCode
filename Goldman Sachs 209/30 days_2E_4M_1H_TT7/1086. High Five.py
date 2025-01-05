from typing import List
from collections import defaultdict
def highFive(items: List[List[int]]) -> List[List[int]]:
    # Group scores by student ID
    scores =defaultdict(list)
    for ID,score in items:
        scores[ID].append(score)
    result=[]
    for ID in sorted(scores.keys()):
        scores_=sum(sorted(scores[ID],reverse=True)[:5])//5
        result.append([ID,scores_])
    print(result)
    return result

items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
highFive(items)