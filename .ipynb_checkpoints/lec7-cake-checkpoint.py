import numpy as np
import math
import matplotlib.pyplot as plt

price = 25000
cost = 5000

# 최대로 준비할 수 있는 케이크 수
max_cakes = 50
# 각각의 케이크 수에 대한 수익 배열
# 0개 수익, 1개 수익 ...
profit = []

# 판매된 케이크 수에 대한 확률 계산
# P[0] : 0개 확률, P[1] : 1개 확률, P[2] : 2개 확률, ...
probabilities = [math.exp(-17) * 17 ** k / math.factorial(k) for k in range(max_cakes+1)]

for num_cakes in range(1, max_cakes+1):
    # 예상 수익
    expected_profit = sum(probabilities[:num_cakes+1] * np.arange(num_cakes+1) * price) - (num_cakes * cost)
    # 첫번째가 1개 만들었을때의 수익
    profit.append(expected_profit)

# 최대 예상 수익과 그 때의 케이크 수 출력
max_profit = max(profit)
max_profit_num_cakes = profit.index(max_profit) + 1

print(f"케이크의 수: {max_profit_num_cakes}")
print(f"예상 최대 수익: {max_profit}원")

# Plotting the graph
plt.plot(range(1, max_cakes+1), profit)
plt.scatter(max_profit_num_cakes, max_profit, color='red')  # highlight the point with max profit
plt.title('Profit vs Number of Cakes')
plt.xlabel('Number of Cakes')
plt.ylabel('Profit')
plt.show()