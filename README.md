# Customer Lifetime Value Prediction

A comprehensive project for predicting Customer Lifetime Value (CLV) using probabilistic models BG/NBD and Gamma-Gamma.

## Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Analysis Process](#analysis-process)
- [Results](#results)

## Introduction

Customer Relationship Management (CRM) analytics is crucial for businesses to understand and enhance customer interactions. This project focuses on Customer Lifetime Value (CLV), a key metric that represents the total value a customer brings to a business throughout their relationship.

### What is CLV?
CLV helps estimate the expected revenue a customer will generate from their first purchase to their last. By understanding CLV, businesses can:
- Develop targeted marketing strategies
- Optimize customer acquisition costs
- Improve customer retention
- Enhance overall customer satisfaction

## Project Overview

This project implements a CLV prediction system using two probabilistic models:
1. **BG/NBD Model**: Predicts customer purchasing behavior
2. **Gamma-Gamma Model**: Estimates customer monetary value

The combination of these models provides accurate CLTV predictions: `CLTV = BG/NBD Model * Gamma-Gamma Submodel`

## Dataset

### Generated Sample Data
We've created a synthetic dataset of 500 customers with realistic shopping patterns, including:
- Online and offline purchase behavior
- Multiple shopping channels (Android, iOS, Desktop, Mobile, Offline)
- Purchase history from 2020 to 2024
- Category preferences
- Monetary values

### Variables
- `master_id`: Unique customer identifier
- `order_channel`: Shopping channel used
- `last_order_channel`: Channel of last purchase
- `first_order_date`: First purchase date
- `last_order_date`: Most recent purchase date
- `last_order_date_online`: Last online purchase date
- `last_order_date_offline`: Last offline purchase date
- `order_num_total_ever_online`: Total online purchases
- `order_num_total_ever_offline`: Total offline purchases
- `customer_value_total_ever_offline`: Total offline spending
- `customer_value_total_ever_online`: Total online spending
- `interested_in_categories_12`: Shopping categories in last 12 months

## Methodology

### Data Preparation
1. Data cleaning and formatting
2. Feature engineering
3. Recency and T-score calculations

### Model Implementation
1. BG/NBD Model for purchase frequency prediction
2. Gamma-Gamma Model for monetary value prediction
3. Combined CLTV calculation

### Customer Segmentation
- Segmentation based on CLTV scores
- Creation of customer segments (A, B, C, D)
- Development of segment-specific strategies

## Project Structure
```
├── README.md
├── requirements.txt
├── .gitignore
├── generate_sample_data.py
├── prepare_cltv_data.py
├── fit_cltv_model.py
├── sample_customer_data.csv
├── prepared_cltv_data.csv
└── cltv_predictions.csv
```

## Getting Started

### Prerequisites
- Python 3.x
- Virtual Environment (recommended)

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/Customer-Lifetime-Value.git
cd Customer-Lifetime-Value
```

2. Create and activate virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Analysis Process

1. **Data Generation**:
   - Run `generate_sample_data.py` to create synthetic customer data
   - Generates 500 customer records with realistic patterns

2. **Data Preparation**:
   - Run `prepare_cltv_data.py` to process raw data
   - Calculates necessary metrics for CLTV prediction

3. **Model Fitting and Prediction**:
   - Run `fit_cltv_model.py` to:
     - Fit BG/NBD and Gamma-Gamma models
     - Calculate CLTV predictions
     - Generate customer segments

## Results

The analysis provides:
- Customer lifetime value predictions for different time periods (30, 90, 180, 365 days)
- Customer segmentation (A, B, C, D segments)
- Segment-specific marketing strategies
- Purchase predictions for different time horizons