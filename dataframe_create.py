import pandas as pd
import numpy as np




texture_features = list(range(0,256))
print(texture_features)

df_texture = pd.DataFrame(columns=texture_features)

print(df_texture)

data = pd.Series(range(0,256))

df_texture = df_texture.append(data, ignore_index=True)
print(df_texture)

