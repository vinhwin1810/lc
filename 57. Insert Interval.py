class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # iterate through all elements
        # if not overlap with the previous element, check overlap with the next element
        # if no overlap => add
        # if overlap => check overlap with the next element.
        # until no overlap or next = null => merge first overlap last overlap


        answers = []

        for i in range(len(intervals)):
            if self.is_overlap(intervals[i], newInterval):
                newInterval = self.merge(intervals[i], newInterval)
                
            elif newInterval[1] < intervals[i][0]:
                answers.append(newInterval)
                return answers + intervals[i:]
            
            else:
                answers.append(intervals[i])
            
        answers.append(newInterval)
        return answers


    def is_overlap(self, a, b):
        return a[0] <= b[1] and b[0] <= a[1]

    def merge(self, a, b):
        return [min(a[0], b[0]), max(a[1], b[1])]
        res = []