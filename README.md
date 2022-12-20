# pandas_helpers
Functions to help working with pandas

## Functions avaiable
### pandas_helpers.df_sort_values
Does the expected behavior when using df.sort_values, but you can use the 'key' argument and works as expected

Usage for key argument: `key={'col1' : func1, 'col2' : {'cellvalue':'othervalue'}, ...}` (you don't have to specify every column)

You should specify the 'by' argument for each column selected to be sorted

Check: https://stackoverflow.com/questions/64345790/sort-a-pandas-dataframe-by-multiple-columns-using-key-argument


#### Final notes:
Problems with any function? Send a PR/Create an issue. And thanks for the report

Do you want to contribute? Send a PR/Create an issue.  And thanks for the contribution :)
