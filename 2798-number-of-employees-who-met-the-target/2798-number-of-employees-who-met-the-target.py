class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours , target ):
        count = 0
        for i in range(0,len(hours)):
            if hours[i] >= target:
                count += 1
        return count
        