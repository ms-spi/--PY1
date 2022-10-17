src = not False and True or False and not True

result = True and True or False or False  # избавляемся от отрицаний
result = True or False or False # избавляемся от И
result = True # избавляемся от ИЛИ

print(src == result)
