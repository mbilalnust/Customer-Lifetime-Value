# Customer Lifetime Value Prediction

This project implements Customer Lifetime Value (CLV) prediction using BG/NBD and Gamma-Gamma models.

## CRM analytics
Customer Relationship Management (CRM) encompasses the process of managing and enhancing interactions with a business's customers. Its aim is to increase customer satisfaction, foster loyalty, and boost the company's revenues. CRM analytics provides businesses with the opportunity to gain deeper insights into their customers by analyzing customer data extensively. This analysis assists in understanding customer preferences, shopping habits, and more. As a result, businesses can enhance customer relationships by creating personalized marketing strategies.

## Project Overview

The project focuses on predicting customer lifetime value using probabilistic models. 
Customer Lifetime Value (CLV) represents the total value that a customer provides to a business throughout their relationship. CLV helps estimate the revenue a customer is expected to generate for the business from their initial purchase to their final one. Businesses can focus on delivering more value to customers while managing customer relationships by considering CLV.

Customer Lifetime Value Prediction (CLTV) is an analytical method used to forecast a customer's future value. This prediction leverages historical data to understand a customer's future purchasing behavior and spending habits. Businesses can strive to increase their customers' lifetime value by creating customer-specific marketing strategies and enhancing customer satisfaction.

Process:

When calculating Customer Lifetime Value (CLTV), we use two separate models: the BG/NBD Model and the Gamma Gamma Submodel. As a result, CLTV is derived from the combination of these two models, as follows:
CLTV = BG/NBD Model * Gamma Gamma Submodel
The BG/NBD Model probabilistically models customers' purchasing behavior. This model considers two processes: the Purchase Process and the Purchase-Until-Death Process.
The Gamma Gamma Submodel is used to predict a customer's average revenue per transaction.

## Business problem
FLO aims to establish a roadmap for its sales and marketing activities. In order for the company to make medium to long-term plans, it is necessary to forecast the potential value that existing customers will bring to the company in the future.

Story:
The dataset consists of information obtained from the past shopping behaviors of customers who made their last purchases from Flo in 2020-2021 through OmniChannel, which means both online and offline shopping.
* Number of Observations: 19,945
* Number of Variables: 12

Varibles:
* master_id: Unique customer identifier
* order_channel: The channel used for shopping (Android, iOS, Desktop, Mobile, Offline)
* last_order_channel: The channel used for the last purchase
* first_order_date: The date of the customer's first purchase
* last_order_date: The date of the customer's last purchase
* last_order_date_online: The date of the customer's last online purchase
* last_order_date_offline: The date of the customer's last offline purchase
* order_num_total_ever_online: The total number of purchases made by the customer online
* order_num_total_ever_offline: The total number of purchases made by the customer offline
* customer_value_total_ever_offline: The total amount paid by the customer in offline purchases
* customer_value_total_ever_online: The total amount paid by the customer in online purchases
* interested_in_categories_12: The list of categories the customer shopped in the last 12 months.

### Data Analysis
- Exploration of data distribution
- Normality testing using Shapiro-Wilk and Kolmogorov-Smirnov tests
  - Note: For datasets with N > 5000, p-value accuracy may be affected

### Models Used
- BG/NBD (Beta Geometric/Negative Binomial Distribution) model
- Gamma-Gamma model

### Overall tasks
* TASK 1: DATA PREPARATION
* TASK 2: CREATING CLTV METRICS
* TASK 3: ESTABLISHING BG/NBD AND GAMMA-GAMMA MODELS, CALCULATING CLTV
* TASK 4: CREATING SEGMENTS BASED ON CLTV
* TASK 5: HYPOTHESIS FORMULATION AND HYPOTHESIS TESTING
* TASK 6: CREATING STRATEGIES FOR CUSTOMER SEGMENTS

## Getting Started

### Prerequisites
- Python 3.x
- Jupyter Notebook

### Installation
1. Clone the repository
2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure
- `cltv-prediction-with-bg-nbd-and-gamma-gamma.ipynb`: Main analysis notebook
- `requirements.txt`: Python dependencies
- `.gitignore`: Git ignore rules

## credits
https://www.kaggle.com/code/aylinzgr/cltv-prediction-with-bg-nbd-and-gamma-gamma/notebook