import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

plt.axis([0,255,0,255])

# plt.xticks([0,63,127,191,255], labels=[])
# plt.yticks([0,63,127,191,255], labels=[])

plt.xticks([0,63,127,191,255])
plt.yticks([0,63,127,191,255])

# 가로선
plt.axhline(y=63, color='black', linestyle='-', linewidth=0.7)
plt.axhline(y=127, color='black', linestyle='-', linewidth=0.7)
plt.axhline(y=191, color='black', linestyle='-', linewidth=0.7)

#세로선
plt.axvline(x=63, color='black', linestyle='-', linewidth=0.7)
plt.axvline(x=127, color='black', linestyle='-', linewidth=0.7)
plt.axvline(x=191, color='black', linestyle='-', linewidth=0.7)

# only use 5 dots
# y=[0,63,127,191,255]
# 원본이미지
# plt.plot([0, 255], [0, 255], color="black", linestyle="-", label="curve line", linewidth=2)

#-----------------------------------------------------------------
# S Curve
x=[0,95,130,180,255]
y=[0,63,127,200,255]

# plt.plot(x, y, color="black", linestyle="-", label="curve line", linewidth=2)


# 삼차함수 모델 정의
def cubic_function(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

# 예제 데이터 (x, y)
x_data = np.array([0,20,95,130,180,235,255])
y_data = np.array([0,20,63,127,200,235,255])

# x=[0,95,130,180,255]
# y=[0,63,127,200,255]
# 최소 제곱법을 사용하여 삼차함수의 계수 추정
coefficients, _ = curve_fit(cubic_function, x_data, y_data)

# 결과 출력
print("추정된 계수:", coefficients)

# 그래프 플로팅
x_range = np.linspace(min(x_data), max(x_data), 100)  # 예측할 범위의 x 값 생성
y_predicted = cubic_function(x_range, *coefficients)
print(y_predicted)# 추정된 모델을 이용하여 y 예측

plt.scatter(x_data, y_data, label='data')              # 데이터 포인트 플로팅
plt.plot(x_range, y_predicted, label="est eq", color='red')  # 추정된 삼차함수 플로팅

plt.legend()
plt.show()