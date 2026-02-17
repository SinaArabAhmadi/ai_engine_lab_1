import csv

def read_numbers_one_by_one(filename):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:

            yield float(row['numbers'])

def calculate_average(filename):
    total_sum = 0
    count = 0
    
    print("dar hal mosahebe ")
    
    for number in read_numbers_one_by_one(filename):
        total_sum += number
        count += 1
    
    if count == 0:
        return 0
    return total_sum / count

if __name__ == "__main__":
    avg = calculate_average("large_data.csv")
    print(f"gereftan miyangin 1 milion adad {avg:.2f}")

