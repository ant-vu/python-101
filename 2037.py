class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # time: O(n+k), space: O(k)
        def countingSort(arr):
            maxVal = max(arr)
            cnts = [0] * (maxVal + 1)
            for val in arr:
                cnts[val] += 1
            idx = 0
            for val in range(maxVal + 1):
                while cnts[val] >= 1:
                    arr[idx] = val
                    idx += 1
                    cnts[val] -= 1
        
        countingSort(seats)
        countingSort(students)
        res = 0
        for seat, student in zip(seats, students):
            res += abs(seat - student)
        return res

        # time: O(nlogn), space: O(n)
        # seats.sort(), students.sort()
        # res = 0
        # for seat, student in zip(seats, students):
        #     res += abs(seat - student)
        # return res