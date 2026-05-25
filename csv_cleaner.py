import pandas as pd
df = pd.read_csv("employees.csv")

print("Original Data:")
print(df)

df = df.fillna("Unknown")

df.to_csv("cleaned_employees.csv", index=False)

print("\nCleaned Data:")
print(df)

print("\nCleaned CSV saved successfully!")