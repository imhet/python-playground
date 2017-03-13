import random
import bubble_sort
import select_sort
import insert_sort
import shell_sort
import merge_sort
import quick_sort
import heap_sort

random_array = [random.randint(1, 99) for i in range(20)]

print("before sort :" + str(random_array))

# sorted_array = bubble_sort.bubble_sort(random_array)¡
# sorted_array = select_sort.select_sort(random_array)
# sorted_array = insert_sort.insert_sort(random_array)
# sorted_array = shell_sort.shell_sort(random_array)
# sorted_array = merge_sort.merge_sort(random_array)
# sorted_array = quick_sort.quick_sort(random_array)
sorted_array = heap_sort.heap_sort(random_array)

print("after sort :" + str(sorted_array))
