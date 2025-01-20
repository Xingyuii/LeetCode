# 595. Big Countries
import pandas as pd
def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world.area >= 3000000) | (world.population >= 25000000)] # 1. 条件是写在括号里 not[ ]
    return df[['name', 'population', 'area']]

# 1757. Recyclable and Low Fat Products
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df=products[(products.low_fats=='Y') & (products.recyclable=='Y')] # 2. 只能用&,不能用and，条件用（）括起来
    return df[['product_id']]

# 183. Customers Who Never Order
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Select the customers whose 'id' is not present in the orders DataFrame's 'customerId' column.
    df = customers[~customers['id'].isin(orders['customerId'])]
    # Build a DataFrame that only contains the 'name' column and rename it as 'Customers'.
    df = df[['name']].rename(columns={'name': 'Customers'})
    return df

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers.merge(orders, how='left', right_on='customerId', left_on='id')
    df = df[df.customerId.isnull()].rename(columns = {"name": "Customers"})
    return df[['Customers']]

# 1148. Article Views I
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # 过滤作者和观众相同的行
    df = views[views['author_id'] == views['viewer_id']]
    # 选择 'author_id' 列，去除重复值并重命名为 'id'
    df = df[['author_id']].drop_duplicates().rename(columns={'author_id': 'id'})
    df = df.sort_values(by='id', ascending=True)
    return df