import pandas as pd

sample = [9.76, 11.1, 10.7, 10.72, 11.8, 6.15, 10.52, 14.83, 13.03, 16.46, 10.84, 12.45]
gender = ["Female"]*7 + ["Male"]*5

my_tab2 = pd.DataFrame({"score": sample, "gender": gender})
# print(my_tab2)


# ttest_independent
from scipy.stats import ttest_ind

male = my_tab2[my_tab2['gender'] == 'Male']
female = my_tab2[my_tab2['gender'] == 'Female']

# 단측검정 (큰 쪽)
# alternative를 설정할때는 대립가설의 형태를 정확히 살펴보고 그에 맞춰서 값을 대입해야한다. (greater, less, two-sided)
# alternative='greater'의 의미는 대립가설이 첫번째 그룹의 평균이 두번째 그룹의 평균보다 높닫고 설정되어 있다는 의미이다.
# equal_var는 해당 집단이 동일한 분산을 가진다고 가정할때  True로 설정하고 아니면 False로 설정한다.
t_statistic, p_value = ttest_ind(male['score'], female['score'], equal_var = True, alternative='greater')
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")

print()