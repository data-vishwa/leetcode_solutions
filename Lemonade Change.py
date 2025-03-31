class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Create Count of five and tens
        five = ten = 0 
        for bill in bills:
            if bill == 5:
                five = five + 1
            elif bill == 10:
                if five == 0:
                    return False
                # Remove one five and one 10
                five = five -1 
                ten = ten + 1
            else:
                # remove first 10 then 4
                if ten > 0 and five > 0:
                    ten = ten - 1
                    five = five - 1
                elif five >= 3:
                    five = five - 3
                else:
                    return False
        return True

            
            
        
