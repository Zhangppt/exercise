# 渣渣葡萄
# 开发时间：2021/10/18 9:38
profit=int(input('Show me the money:'))  # 利润
bonus=0  # 奖金
thresholds=[100000,100000,200000,200000,400000]
rates=[0.1,0.75,0.05,0.03,0.015,0.01]
for i in range(len(thresholds)):
    if profit<=thresholds[i]:
        bonus+=profit*rates[i]
        profit=0
        break
    else:
        bonus+=thresholds[i]*rates[i]
        profit-=thresholds[i]
bonus+=profit*rates[-1]
print(bonus)