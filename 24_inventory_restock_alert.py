items = [('Milk', 3), ('Bread', 7), ('Eggs', 2), ('Rice', 5)]
threshold = 5

for item, qty in items:
    if qty < threshold:
        print(f"{item} needs restock left quantity {qty}")
    
      
