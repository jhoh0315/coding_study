import matplotlib.pyplot as plt

# 염산 용액 몰농도, 용액 부피, 수산화나트륨 무게 입력 받기
molality = float(input("Enter the molarity of the hydrochloric acid (in mol/L): "))
volume = float(input("Enter the volume of the hydrochloric acid solution (in mL): "))
mass_naoh = float(input("Enter the mass of the sodium hydroxide (in g): "))

# 수산화나트륨 몰량 계산하기
molar_mass_naoh = 40.0  # 수산화나트륨의 몰 질량 (g/mol)
n_naoh = mass_naoh / molar_mass_naoh

# 열용량, 밀도 계산하기
heat_capacity = 4.18  # 열용량 (J/g°C)
density = 1.0  # 밀도 (g/mL)

# 초기 온도 입력 받기
initial_temp = float(input("Enter the initial temperature (in °C): "))

# 시간, 온도, 반응 진행도 리스트 초기화
time_list = []
temp_list = []
naoh_list = []

# 초기 온도와 수산화나트륨 양을 리스트에 추가
time_list.append(0)
temp_list.append(initial_temp)
naoh_list.append(n_naoh)

# 시뮬레이션 시간 설정
simulation_time = 5  # 시뮬레이션 시간 (분)

# 시간 간격 설정
dt = 0.01  # 시간 간격 (분)

# 반응 시뮬레이션
time = 0
while time < simulation_time:
    # 반응 진행도 계산
    progress = n_naoh / (molality * volume)

    # 열량 계산
    q = n_naoh * heat_capacity * density * (temp_list[-1] - initial_temp)

    # 온도 변화량 계산
    delta_T = q / (molality * volume * heat_capacity * density)

    # 온도 갱신
    temp = temp_list[-1] + delta_T
    temp_list.append(temp)

    # 시간, 반응 진행도 갱신
    time += dt
    time_list.append(time)
    naoh_list.append(naoh_list[-1] - molality * volume * progress * dt)

# 그래프 출력
plt.plot(naoh_list, temp_list)
plt.xlabel("Sodium hydroxide (mol)")
plt.ylabel("Temperature (°C)")
plt.show()
