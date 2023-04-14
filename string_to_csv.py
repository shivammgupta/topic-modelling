import pandas as pd
import numpy as np
def convert_csv():
    # df = pd.read_csv('bert.txt',  header=None)
    column_names = ['word', 'score']
    data = np.array([('great', 0.07478162163158093), ('work', 0.059640032423436636), ('benefit', 0.05712984417950321), ('good', 0.048183601867635054), ('pay', 0.043042900436065006), ('employee', 0.0394452330306186), ('people', 0.03701888430536077), ('management', 0.036115621671831515), ('patient', 0.03427389474262032), ('care', 0.03284382216565843)])
    my_df = pd.DataFrame(data, columns=column_names)
    my_df.to_csv('clean_text_top_words.csv')


if __name__ == '__main__':
    convert_csv()