LOAD DATA INFILE '/Users/phoebegunter/Documents/FinTech-Workspace/valuation_bot/data/FS_sp500_merged_cleaned_stats.csv'
 INTO TABLE `data_table`
 FIELDS TERMINATED BY ','
 ENCLOSED BY '"'
 LINES TERMINATED BY '\n';