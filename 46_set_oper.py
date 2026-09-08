fruits={"apple","banana","graphes"}
new_fruits={"cherry"}
add_elem=fruits.union(new_fruits)
add_elem.remove("apple")
add_elem.discard("banana")
print(add_elem)
