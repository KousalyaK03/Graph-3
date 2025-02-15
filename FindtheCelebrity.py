# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        """
        Approach:
        - The problem is solved using a **two-pass** approach.
        - Step 1: Identify a potential celebrity using elimination (single pass).
        - Step 2: Verify if the candidate is a real celebrity (second pass).
        - A celebrity is a person who:
          1. Is known by everyone.
          2. Does not know anyone else.
        
        Time Complexity: O(n) (since we make at most 3n calls to `knows`).
        Space Complexity: O(1) (only a few integer variables used).
        """

        # Step 1: Find the potential celebrity
        candidate = 0  # Assume the first person (0) is the celebrity
        for i in range(1, n):
            if knows(candidate, i):  
                # If candidate knows i, then candidate cannot be a celebrity.
                # i might be the celebrity, so update candidate to i.
                candidate = i  

        # Step 2: Verify if the candidate is a real celebrity
        for i in range(n):
            if i != candidate:
                # Celebrity should not know anyone & everyone should know the celebrity
                if knows(candidate, i) or not knows(i, candidate):
                    return -1  # No celebrity found
        
        return candidate  # Return the confirmed celebrity