import pandas as pd
import numpy as np


conversion_df = pd.read_csv("5_class/data/prepared_ad_conversion.csv", index_col=0)


# print(conversion_df.dtypes)
# print()


gender_group = pd.pivot_table(
    conversion_df,
    index=["gender", "age", "color scheme"],
    values=["seen count", "followed ad", "made purchase", "user rating", "ad effectiveness"],
    aggfunc=np.mean,
)
print(gender_group)
print()

# print(conversion_df)
