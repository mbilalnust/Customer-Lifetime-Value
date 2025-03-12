import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from typing import List, Optional, Union

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
n_samples = 500

# Generate random dates within a reasonable range
def random_date(start_date: datetime, end_date: datetime) -> datetime:
    time_between = end_date - start_date
    days_between = time_between.days
    if days_between <= 0:
        return end_date
    random_days = random.randrange(days_between)
    return start_date + timedelta(days=random_days)

# Define start and end dates
start_date = datetime(2020, 1, 1)
end_date = datetime(2024, 2, 29)

# Generate data
data: dict = {
    'master_id': [f'C{str(i).zfill(6)}' for i in range(1, n_samples + 1)],
    'order_channel': list(np.random.choice(['Android', 'iOS', 'Desktop', 'Mobile', 'Offline'], n_samples)),
}

# Generate first order dates
first_order_dates = [random_date(start_date, end_date) for _ in range(n_samples)]
data['first_order_date'] = first_order_dates

# Generate last order dates (after first order date)
last_order_dates = [random_date(first_date, end_date) for first_date in first_order_dates]
data['last_order_date'] = last_order_dates

# Set last order channel based on the last order
last_order_channels = list(np.random.choice(['Android', 'iOS', 'Desktop', 'Mobile', 'Offline'], n_samples))
data['last_order_channel'] = last_order_channels

# Generate online and offline last order dates
data['last_order_date_online'] = [
    random_date(first_date, last_date) 
    if last_channel != 'Offline' else None
    for first_date, last_date, last_channel 
    in zip(first_order_dates, last_order_dates, last_order_channels)
]

data['last_order_date_offline'] = [
    random_date(first_date, last_date) 
    if last_channel == 'Offline' else None
    for first_date, last_date, last_channel 
    in zip(first_order_dates, last_order_dates, last_order_channels)
]

# Generate order numbers (ensure they make sense with channels)
data['order_num_total_ever_online'] = [
    np.random.randint(1, 50) if channel != 'Offline' else 0
    for channel in last_order_channels
]

data['order_num_total_ever_offline'] = [
    np.random.randint(1, 20) if channel == 'Offline' else 0
    for channel in last_order_channels
]

# Generate customer values (realistic price ranges, aligned with order numbers)
online_orders = data['order_num_total_ever_online']
offline_orders = data['order_num_total_ever_offline']

data['customer_value_total_ever_offline'] = [
    round(num * np.random.uniform(50, 250), 2) 
    for num in offline_orders
]

data['customer_value_total_ever_online'] = [
    round(num * np.random.uniform(30, 200), 2) 
    for num in online_orders
]

# Generate interested categories
categories = ['Fashion', 'Electronics', 'Home', 'Books', 'Sports', 'Beauty', 'Food']
data['interested_in_categories_12'] = [
    ','.join(np.random.choice(categories, size=np.random.randint(1, 4), replace=False))
    for _ in range(n_samples)
]

# Create DataFrame
df = pd.DataFrame(data)

# Format dates
date_columns = ['first_order_date', 'last_order_date', 'last_order_date_online', 'last_order_date_offline']
for col in date_columns:
    df[col] = pd.to_datetime(df[col]).dt.strftime('%Y-%m-%d')

# Save to CSV
df.to_csv('sample_customer_data.csv', index=False)
print("Sample data has been generated and saved to 'sample_customer_data.csv'") 