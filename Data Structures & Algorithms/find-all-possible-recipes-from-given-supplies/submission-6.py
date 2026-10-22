class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        sol = []
        supply_set = set()
        recipes_hash = {}
        for supply in supplies:
            supply_set.add(supply)
        for index, recipe in enumerate(recipes):
            recipes_hash[recipe] = index
        seen = set()
        def recursion (index: int, dish: str) -> bool:
            if dish in seen:
                return False
            seen.add(dish)
            listy = ingredients[index]
            for ingredient in listy:
                if (ingredient not in recipes_hash and ingredient not in supply_set):
                    return False
                if (ingredient in supply_set):
                    continue
                if (ingredient in recipes_hash):
                    if recursion(recipes_hash[ingredient], ingredient):
                        continue
                    else:
                        return False
            supply_set.add(dish)
            return True
        for num, dish in enumerate(recipes):
            recursion(num, dish)
        return [dish for dish in recipes if dish in supply_set]