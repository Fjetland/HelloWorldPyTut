import converters
from converters import kg_to_lbs
from utils import find_max

print(converters.lbs_to_kg(2))
print(kg_to_lbs(2))

# Max list test
my_list = [1, 4, 8, 90, 2, 4, 1, 7, 12]
print(find_max(my_list))