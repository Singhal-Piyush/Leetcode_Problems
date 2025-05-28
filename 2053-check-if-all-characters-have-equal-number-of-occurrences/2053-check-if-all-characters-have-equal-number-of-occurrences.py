class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        character_occ = {}

        for i in s:
            if i in character_occ.keys():
                character_occ[i] +=1
            else:
                character_occ[i] = 1

        occ = set(character_occ.values())
        if len(occ) == 1:
            return True
        return False
        