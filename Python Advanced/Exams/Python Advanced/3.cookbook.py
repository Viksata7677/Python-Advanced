def cookbook(*recipes):
    cuisines = {}
    for name, cuisine, ingredients in recipes:
        if cuisine not in cuisines:
            cuisines[cuisine] = [(name,ingredients)]
        else:
            cuisines[cuisine].append((name,ingredients))
    for recipes in cuisines.values():
        recipes.sort()
    cuisines = sorted(cuisines.items(), key=lambda C: (-len(C[1]),C[0]))
    lines = []
    for cuisine, recipes in cuisines:
        lines.append(f"{cuisine} cuisine contains {len(recipes)} recipes:")
        for name, ingredients in recipes:
            ingredients = ", ".join(ingredients)
            lines.append(f"  * {name} -> Ingredients: {ingredients}")
    return "\n".join(lines)

