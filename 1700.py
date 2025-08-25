class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # time: O(m+n), space: O(1)
        studentCircles = studentSquares = 0
        for student in students:
            if student == 0:
                studentCircles += 1
            else:
                studentSquares += 1
        for sandwich in sandwiches:
            if sandwich == 0 and studentCircles == 0:
                return studentSquares
            elif sandwich == 1 and studentSquares == 0:
                return studentCircles
            elif sandwich == 0:
                studentCircles -= 1
            else:
                studentSquares -= 1
        return 0

        # time: O(m*n), space: O(m+n)
        # studentsQ, sandwichesQ = deque(students), deque(sandwiches)
        # lastServed = 0
        # while len(sandwichesQ) >= 1 and lastServed < len(studentsQ):
        #     if studentsQ[0] == sandwichesQ[0]:
        #         studentsQ.popleft()
        #         sandwichesQ.popleft()
        #         lastServed = 0
        #     else:
        #         studentsQ.append(studentsQ.popleft())
        #         lastServed += 1
        # return len(sandwichesQ)