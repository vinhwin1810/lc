class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()  # Sort the people array in ascending order
        left, right = 0, len(people) - 1  # Initialize pointers
        boats = 0  # Initialize the number of boats

        while left <= right:
            # Try to pair the heaviest person with the lightest person
            if people[left] + people[right] <= limit:
                left += 1  # Move the left pointer
            right -= 1  # Move the right pointer
            boats += 1  # Increment the number of boats

        return boats