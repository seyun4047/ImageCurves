import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 삼차함수 모델 정의
def cubic_function(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

# 예제 데이터 (x, y)
x_data = np.array([0,95,130,180,255])
y_data = np.array([0,63,127,200,255])

# x=[0,95,130,180,255]
# y=[0,63,127,200,255]
# 최소 제곱법을 사용하여 삼차함수의 계수 추정
coefficients, _ = curve_fit(cubic_function, x_data, y_data)

# 결과 출력
print("추정된 계수:", coefficients)

# 그래프 플로팅
x_range = np.linspace(min(x_data), max(x_data), 100)  # 예측할 범위의 x 값 생성
y_predicted = cubic_function(x_range, *coefficients)    # 추정된 모델을 이용하여 y 예측

plt.scatter(x_data, y_data, label='data')              # 데이터 포인트 플로팅
plt.plot(x_range, y_predicted, label="est eq", color='red')  # 추정된 삼차함수 플로팅
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('est eq, data')
plt.show()
