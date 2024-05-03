import math

def bucket_sort(array):
    number_of_buckets = round(math.sqrt(len(array)))   # counting buckets from 1 
    max_value = max(array)
    new_array = [[] for _ in range(number_of_buckets)]

    # Distribute elements into buckets
    for num in array:
        appropriate_bucket = math.ceil(num * number_of_buckets / max_value)
        new_array[appropriate_bucket - 1].append(num)

    # Sort elements within each bucket
    for bucket in new_array:
        bucket.sort()

    # Merge buckets
    sorted_array = []
    for bucket in new_array:
        sorted_array.extend(bucket)

    return sorted_array

arr = [5, 3, 9, 1, 2, 8, 4, 7, 6, 5, 6, 5, 20]
print(bucket_sort(arr))
