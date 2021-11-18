import pandas as pd


def file_to_dataframe(fn : str):
    file1 = pd.read_table(fn,header=None,index_col=False)
    return file1

def wordfile_differences_linear_search(fn1,fn2):
    file1 = file_to_dataframe(fn1)
    file2 = file_to_dataframe(fn2)

    retlst = []

    for word in file1:
        if file2.str.contains(word).any:
            retlst.append(word)


    return retlst

