# Install_libraries
# pip install faker pandas

import random

import pandas as pd
from faker import Faker

fake = Faker()

def generate_fake_data(num_entries=10):
    data = []
    for _ in range(num_entries):
        entry = {
            # add / remove fields that you want for your dataset
            "Name": fake.name(),
            "Address": fake.address(),
            "Email": fake.email(),
            "Phone Number": fake.phone_number(),
            "Job Title": fake.job(),
            "Company": fake.company(),
            "Lorem Ipsum Text": fake.text(),
            "Random Lucky Number": random.randint(1,100)
        }
        data.append(entry)
    return pd.DataFrame(data)

if __name__ == "__main__":
    # specify number of entries to generate, default = 10
    ENTRIES = 5
    fake_data_df = generate_fake_data(ENTRIES)
    print(fake_data_df)
