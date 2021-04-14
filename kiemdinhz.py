import numpy as np
import pandas as pd
import random
from scipy import stats
from statsmodels.stats.weightstats import ztest


#kiểm định 1 đuôi
#Sinh ngẫu nhiên một mẫu 50 phần tử có trung bình mẫu là 110, độ lệch chuẩn là 15
sp = np.random.normal(110, 15, 50)
print(sp[:10])
#Xác định các thông số
null_mean = 100
alpha1 = 0.05
#Kiểm định z
ztest_Score, p_value1= ztest(sp, value = null_mean, alternative='larger')
if(p_value1 <  alpha1):
  print("Có bằng chứng để bác bỏ giả thuyết H0")
else:
  print("Chưa có bằng chứng để bác bỏ giả thuyết H0")

print("------------------------------------------------------------------------")

#Kiểm định 2 đuôi
#Sinh ngẫu nhiên một mẫu 50 phần tử có trung bình mẫu là 15, độ lệch chuẩn là 6
sp1 = np.random.normal(15, 6, 50)
print(sp1[:5])
#Sinh ngẫu nhiên một mẫu 60 phần tử có trung bình mẫu là 19, độ lệch chuẩn là 7
sp2 = np.random.normal(19, 7, 60)
print(sp2[:5])
#Kiểm định giả thuyết 
alpha2 = 0.05
ztest_score, p_value2 = ztest(x1 = sp1, x2 = sp2, value = 15 - 19, alternative = 'two-sided')
print('z = ', ztest_score, '; p = ', p_value2)
if(p_value2 <  alpha2):
  print("Có bằng chứng để bác bỏ giả thuyết H0")
else: 
  print("Chưa có bằng chứng để bác bỏ giả thuyết H0")





