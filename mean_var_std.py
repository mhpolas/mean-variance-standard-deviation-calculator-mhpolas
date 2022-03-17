import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError( "List must contain nine numbers." )
  else:

    lst=np.array(list)

    mean_rows_cal=[lst[0:3].mean(), lst[3:6].mean(), lst[6:9].mean()]
    mean_cols_cal=([lst[[0,3,6]].mean(),lst[[1,4,7]].mean(),lst[[2,5,8]].mean()])

    var_rows_cal=[lst[0:3].var(), lst[3:6].var(), lst[6:9].var()]
    var_cols_cal=([lst[[0,3,6]].var(),lst[[1,4,7]].var(),lst[[2,5,8]].var()])

    std_rows_cal=[lst[0:3].std(), lst[3:6].std(), lst[6:9].std()]
    std_cols_cal=([lst[[0,3,6]].std(),lst[[1,4,7]].std(),lst[[2,5,8]].std()])

    min_rows_cal=[lst[0:3].min(), lst[3:6].min(), lst[6:9].min()]
    min_cols_cal=([lst[[0,3,6]].min(),lst[[1,4,7]].min(),lst[[2,5,8]].min()])
    
    max_rows_cal=[lst[0:3].max(), lst[3:6].max(), lst[6:9].max()]
    max_cols_cal=([lst[[0,3,6]].max(),lst[[1,4,7]].max(),lst[[2,5,8]].max()])

    sum_rows_cal=[lst[0:3].sum(), lst[3:6].sum(), lst[6:9].sum()]
    sum_cols_cal=([lst[[0,3,6]].sum(),lst[[1,4,7]].sum(),lst[[2,5,8]].sum()])
    
  
    

    




    return{
      'mean':[mean_cols_cal,mean_rows_cal,lst.mean()],
      'variance': [var_cols_cal, var_rows_cal, lst.var()],
      'standard deviation': [std_cols_cal, std_rows_cal, lst.std()],
      'max': [max_cols_cal, max_rows_cal, lst.max()],
      'min': [min_cols_cal, min_rows_cal, lst.min()],
      'sum': [sum_cols_cal,sum_rows_cal, lst.sum()]
      
    }