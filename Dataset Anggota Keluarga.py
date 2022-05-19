
import pandas as pd

pizza = {'Nama': ['Amir', 'Fadli', 'Fatya', 'aldi', 'ahmad', 'peri', 'wahyu', 'jaka', 'yepan', 'putu'],
'Tinggi Badan': [167, 158, 159, 176, 155, 157, 185, 144, 153, 166], 'Berat Badan' : [45, 56, 35, 55, 64, 56, 53, 51, 57, 66]
}

pizza_df = pd.DataFrame(pizza)
pizza_df

print(pizza_df)