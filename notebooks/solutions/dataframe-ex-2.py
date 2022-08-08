#solution
ddf.groupby("DayOfWeek")["DepDelay"].mean().idxmax().compute()