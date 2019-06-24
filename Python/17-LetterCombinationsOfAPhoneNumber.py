class Solution:
    def list_list(self,lista,listb):
        combination = list()
        for x in lista:
            for y in listb:
                combination.append(x + y)
        return combination
        
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()
        map_n_a = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        options = list(map_n_a[digits[0]])
        for x in digits[1:]:
            options = self.list_list(options, map_n_a[x])
        return options