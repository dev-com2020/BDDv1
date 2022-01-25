import pandas as pd

def before_feature(context,feature):

    if 'test-data-from-excel' in feature.tags:
        path_to_file = '*<path/to/file/here.xlsx>*'
        df = pd.read_excel(path_to_file)
        example = next(sc.example[0] for sc in feature.scenarios if sc.name == 'Test')
        test_table = example.table
        for row in df.itertuples(index=False):
            test_table.add_row(row)
