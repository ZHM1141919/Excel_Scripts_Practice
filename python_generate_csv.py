import pandas as pd
from faker import Faker

# Build Faker instance
fake = Faker()

# List to hold the data
data = []

# Generate 10,000 random data entries
for _ in range(10000):
    data.append({
        "Name": fake.name(),
        "City": fake.city(),
        "Email": fake.email(),
        "Salary": fake.random_int(min=30000, max=120000),
        "Date": fake.date_this_year()
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save as CSV file
df.to_csv("data.csv", index=False)

print("CSV file has been successfully generated: data.csv")