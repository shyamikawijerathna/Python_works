

brands = ["hp","Dell","Lenovo","Acer"]

for lap in brands:
    print(lap)

print(len(brands))

brands.append("singer")
for lap in (brands):
    print(lap)

brands.pop(3)
for lap in brands:
    print(lap)

brands.remove("Dell")
for lap in brands:
    print(lap)

if "singer" in brands:
    brands.remove("singer")
    print(brands)
