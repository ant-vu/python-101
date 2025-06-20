class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # time: O(n), space: O(n)
        max_deque = deque()
        min_deque = deque()
        left = 0
        max_length = 0
        for right in range(len(nums)):
            while max_deque and max_deque[-1] < nums[right]:
                max_deque.pop()
            max_deque.append(nums[right])
            while min_deque and min_deque[-1] > nums[right]:
                min_deque.pop()
            min_deque.append(nums[right])
            while max_deque[0] - min_deque[0] > limit:
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length

        # time: O(nlogn), space: O(n)
        # window = SortedDict()
        # left = 0
        # max_length = 0
        # for right in range(len(nums)):
        #     window[nums[right]] = window.get(nums[right], 0) + 1
        #     while window.peekitem(-1)[0] - window.peekitem(0)[0] > limit:
        #         window[nums[left]] -= 1
        #         if window[nums[left]] == 0:
        #             window.pop(nums[left])
        #         left += 1
        #     max_length = max(max_length, right - left + 1)
        # return max_length

        # time: O(nlogn), space: O(n)
        # max_heap = []
        # min_heap = []
        # left = 0
        # max_length = 0
        # for right in range(len(nums)):
        #     heapq.heappush(max_heap, (-nums[right], right))
        #     heapq.heappush(min_heap, (nums[right], right))
        #     while -max_heap[0][0] - min_heap[0][0] > limit:
        #         left = min(max_heap[0][1], min_heap[0][1]) + 1
        #         while max_heap[0][1] < left:
        #             heapq.heappop(max_heap)
        #         while min_heap[0][1] < left:
        #             heapq.heappop(min_heap)
        #     max_length = max(max_length, right - left + 1)
        # return max_length