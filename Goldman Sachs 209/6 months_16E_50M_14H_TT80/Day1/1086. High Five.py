class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # Group scores by student ID
        scores = defaultdict(list)
        for ID, score in items:
            scores[ID].append(score)
        re=[]
        for ID in sorted(scores.keys()):
            re.append([ID,sum(sorted(scores[ID])[-5:])//5])
        return re