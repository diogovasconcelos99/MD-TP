import pandas as pd

# Load restaurants and menus CSV files
df_restaurants = pd.read_csv("datasets/restaurants.csv")
df_menus = pd.read_csv("datasets/restaurant-menus.csv")

# Rename column so both datasets can be merged
df_restaurants = df_restaurants.rename(columns={"id": "restaurant_id"})
df_final = pd.merge(df_restaurants, df_menus, on="restaurant_id")

# Adjust columns to more suggesting names
rename_mapping = {
    "name_x": "restaurant_name",
    "ratings": "ratings_count",
    "category_x": "restaurant_category",
    "category_y": "menu_category",
    "name_y": "menu_name",
    "description": "menu_description",
    "price": "menu_price"
}
df_final = df_final.rename(columns=rename_mapping)

# Remove unwanted columns and print new columns
df_final.drop(["position"], axis=1, inplace=True)
print(df_final.columns)

# Apply categorical mapping to price range column
price_mapping = {
    '$': 'Cheap or inexpensive',
    '$$': 'Moderately expensive',
    '$$$': 'Expensive',
    '$$$$': 'Very expensive',
    '$$$$$$$$$$$$$$$$$': 'Extremely expensive'
}
df_final["price_range"] = df_final["price_range"].replace(price_mapping)

# Fill null values
df_final.fillna("None", inplace=True)

# Write result to a new CSV file
df_final.to_csv("datasets/restaurants-with-menus.csv", index=False)
