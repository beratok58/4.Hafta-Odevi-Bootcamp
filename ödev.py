import pandas as pd
data = pd.read_csv('Housing.csv')
import matplotlib.pyplot as plt

plt.scatter(data['area'], data['price'])
plt.title('Area vs Price')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()

plt.scatter(data['bedrooms'], data['price'])
plt.title('Bedrooms vs Price')
plt.xlabel('Bedrooms')
plt.ylabel('Price')
plt.show()

plt.scatter(data['stories'], data['price'])
plt.title('Stories vs Price')
plt.xlabel('Stories')
plt.ylabel('Price')
plt.show()

avg_price_bathrooms = data.groupby('bathrooms')['price'].mean()
avg_price_bathrooms.plot(kind='bar')
plt.title('Average Price by Number of Bathrooms')
plt.xlabel('Number of Bathrooms')
plt.ylabel('Average Price')
plt.show()

avg_price_furnishing = data.groupby('furnishingstatus')['price'].mean()
avg_price_furnishing.plot(kind='bar')
plt.title('Average Price by Furnishing Status')
plt.xlabel('Furnishing Status')
plt.ylabel('Average Price')
plt.show()

corr_matrix = data.corr()
plt.figure(figsize=(10, 8))
plt.matshow(corr_matrix, cmap='coolwarm', fignum=1)
plt.colorbar()
plt.title('Correlation Matrix', pad=20)
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
plt.show()