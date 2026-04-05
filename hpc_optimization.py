import random
import time

# Generate large dataset
data_size = 1_000_000
query_size = 100_000

data_list = list(range(data_size))
queries = [random.randint(0, data_size - 1) for _ in range(query_size)]

# Unoptimized version: list lookup
start_time = time.perf_counter()

found_count_list = 0
for q in queries:
    if q in data_list:
        found_count_list += 1

list_time = time.perf_counter() - start_time

# Optimized version: set lookup
data_set = set(data_list)

start_time = time.perf_counter()

found_count_set = 0
for q in queries:
    if q in data_set:
        found_count_set += 1

set_time = time.perf_counter() - start_time

# Results
print("HPC Optimization Demo: List vs Set Lookup")
print(f"Total data items: {data_size}")
print(f"Total queries: {query_size}")
print(f"Items found using list: {found_count_list}")
print(f"Items found using set: {found_count_set}")
print(f"List lookup time: {list_time:.6f} seconds")
print(f"Set lookup time: {set_time:.6f} seconds")
print(f"Speedup: {list_time / set_time:.2f}x faster")