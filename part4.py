import csv
import psutil
import os
from pydantic import BaseModel

class Row(BaseModel):
    numbers: float

def get_data(filename):
    with open(filename, mode='r') as file:
        for row in csv.DictReader(file):
            yield Row(**row).numbers

def main():
    total, count = 0, 0
    process = psutil.Process(os.getpid()) 
    
    print("pardazesh...")

    for val in get_data("large_data.csv"):
        total += val
        count += 1

    avg = total / count
    mem = process.memory_info().rss / (1024 * 1024) # تبدیل به مگابایت

    print(f"miyangin: {avg:.2f}")
    print(f" estefade az ram: {mem:.2f} MB")

if __name__ == "__main__":
    main()