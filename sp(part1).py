import csv
import random

def create_million_rows(filename="large_data.csv"):
    print("lotfan sabr konid ta dataset sakhte shavad")
    
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        
        writer.writerow(["numbers"])
        
        
        for _ in range(1_000_000):
            
            num = random.uniform(10.0, 500.0) 
            writer.writerow([num])
            
    print(f"✅file tamam shod '{filename}' ba movafaghiyat sakhte shod  .")

if __name__ == "__main__":
    create_million_rows()
