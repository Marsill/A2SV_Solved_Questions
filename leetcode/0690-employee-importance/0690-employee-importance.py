"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mp = {}
        
        for emp in employees:
            mp[emp.id] = emp
        
        def dfs(emp_id):
            employee = mp[emp_id]
            
            total = employee.importance
            
            for sub in employee.subordinates:
                total += dfs(sub)
            
            return total
        
        return dfs(id)