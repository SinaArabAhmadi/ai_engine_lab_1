import csv
import psutil
import os

def read_numbers_one_by_one(filename):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield float(row['numbers'])

def calculate_with_memory_check(filename):
    process = psutil.Process(os.getpid())
    
    total_sum = 0
    count = 0
    
    print(f"shoro kar  ...")

    for number in read_numbers_one_by_one(filename):
        total_sum += number
        count += 1
        
        if count % 200000 == 0:
            mem_usage = process.memory_info().rss / (1024 * 1024)
            print(f" satr ha {count}:  masraf ram  {mem_usage:.2f} MB .")

    final_mem = process.memory_info().rss / (1024 * 1024)
    avg = total_sum / count if count > 0 else 0
    
    print("-" * 30)
    print(f"✅ miyangin: {avg:.2f}")
    print(f"📊   masraf nahayi ram: {final_mem:.2f} MB")

if __name__ == "__main__":
    calculate_with_memory_check("large_data.csv")

