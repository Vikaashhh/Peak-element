class Solution:   
    def peakElement(self, arr):
        # Start karte hain binary search approach se
        low = 0
        high = len(arr) - 1

        while low <= high:
            # Mid calculate karo
            mid = (low + high) // 2

            # Check karo agar mid element peak hai
            # arr[mid-1] aur arr[mid+1] ke comparison me dekho
            # Pehla check left boundary ke liye, dusra right ke liye
            left = arr[mid - 1] if mid > 0 else float('-inf')
            right = arr[mid + 1] if mid < len(arr) - 1 else float('-inf')

            # Agar current element dono neighbors se bada hai toh ye peak hai
            if arr[mid] >= left and arr[mid] >= right:
                return mid
            # Agar right bada hai toh right side me peak hoga
            elif arr[mid] < right:
                low = mid + 1
            # Nahi toh left me peak hoga
            else:
                high = mid - 1

        # Edge case agar koi bhi peak nahi mila (jo practically nahi hoga is problem me)
        return -1
