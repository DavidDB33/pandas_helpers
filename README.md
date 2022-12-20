# pandas_helpers
Functions to help working with pandas

## Installation
WIP. If you want to use these function (now there is only 1) as a package, please let me know by opening an issue and I'll put my hands on the keyboard

## Functions avaiable
### pandas_helpers.df_sort_values
Does the expected behavior when using df.sort_values, but you can use the 'key' argument and works as expected

Usage for key argument: `key={'col1' : func1, 'col2' : {'cellvalue':'othervalue'}, ...}` (you don't have to specify every column)

You should specify the 'by' argument for each column selected to be sorted

Check: https://stackoverflow.com/questions/64345790/sort-a-pandas-dataframe-by-multiple-columns-using-key-argument


#### Final notes:
Problems with any function? Send a PR/open an issue. And thanks for the report

Do you want to contribute? Send a PR/open an issue.  And thanks for the contribution :)
