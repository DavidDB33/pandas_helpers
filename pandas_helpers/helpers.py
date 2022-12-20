from itertools import count, filterfalse, product, islice
from operator import eq, itemgetter
import math
import string
from typing import Callable

def df_sort_values(df:pd.DataFrame, by:list=None, key:dict[str,dict|Callable]|None=None, ascending=True, inplace=False, reset=True) -> pd.DataFrame:
    """Key must be a dict for each column. If a column is not in key, then lambda x:x is used instead
    Use reset=False if you do not want to take into account the columns in the index for sorting
    Key is a dict of form {<colname>:<function>|<dict>} that goes in df[<colname>.map(<here>)>
    inplace argument does not work yet

    Args:
        df: The input dataframe.
        by: The columns selected to be sorted.
        key: A dict for each column in by that wants to be modified to be better sortable (default: None).
        ascending: Same functinallity as in many pandas functions (default: True).
        inplace: To be implemented (default: False).
        reset: If the index want to be taked into account or not (default: True).
    Returns:
        The dataframe sorted.
    """
    if inplace:
        raise NotImplementedError('Inplace parameter is not implemented yet, Sorry. Please add an issue here: https://github.com/DavidDB33/pandas_helpers')
    if by is None:
        raise ValueError("'by' parameter must contain some values (in a list)")
    if key is None:
        key = {b:lambda x:x for b in by}
    else:
        key = {k:key[k] for k in key if k in set(by)} | {b:lambda x:x for b in by if b not in key}
    assert len(key) == len(by), 'An error in pandas_helper.df_sort_values function happend. Please, report it in: https://github.com/DavidDB33/pandas_helpers'
    # minimum colname length to embrace all keys
    min_len = math.ceil(math.log10(max(1, len(key)))/math.log10(len(string.printable)))
    # min_colname_len is the minimal len that does not match with the len of any dataframe's column
    min_colname_len = next(filterfalse(itemgetter(0), zip(
            map(eq, sorted(set(map(len, df.columns))), count(min_len)),
            count(min_len)
        )))[1]
    # newcols are new names that does not match with any column
    newcols = [f'{{:>0{min_colname_len}}}'.format(''.join(name))
               for name in islice(product(*[string.printable]*min_len), len(key))]
    newcol_rels = dict(zip(key, newcols))
    newcol_sorted = sorted(newcols, key={newcol_rels[colname]: idx for idx, colname in enumerate(by)}.get)

    # Reset, sort, and undo reset
    if reset:
        reset_cols = df.index.names
        df = df.reset_index()
    newcol_values = {
        newcol: df[k].map(v) for newcol, (k, v) in zip(newcols, key.items())
    }
    df = df.assign(**newcol_values).sort_values(by=newcol_sorted, ascending=ascending)#.drop(columns=newcols)

    if reset:
        df = df.set_index(reset_cols)
    return df
