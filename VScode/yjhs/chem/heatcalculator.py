import matplotlib.pyplot as plt

# ���� ��� ����, ��� ����, ����ȭ��Ʈ�� ���� �Է� �ޱ�
molality = float(input("Enter the molarity of the hydrochloric acid (in mol/L): "))
volume = float(input("Enter the volume of the hydrochloric acid solution (in mL): "))
mass_naoh = float(input("Enter the mass of the sodium hydroxide (in g): "))

# ����ȭ��Ʈ�� ���� ����ϱ�
molar_mass_naoh = 40.0  # ����ȭ��Ʈ���� �� ���� (g/mol)
n_naoh = mass_naoh / molar_mass_naoh

# ���뷮, �е� ����ϱ�
heat_capacity = 4.18  # ���뷮 (J/g��C)
density = 1.0  # �е� (g/mL)

# �ʱ� �µ� �Է� �ޱ�
initial_temp = float(input("Enter the initial temperature (in ��C): "))

# �ð�, �µ�, ���� ���൵ ����Ʈ �ʱ�ȭ
time_list = []
temp_list = []
naoh_list = []

# �ʱ� �µ��� ����ȭ��Ʈ�� ���� ����Ʈ�� �߰�
time_list.append(0)
temp_list.append(initial_temp)
naoh_list.append(n_naoh)

# �ùķ��̼� �ð� ����
simulation_time = 5  # �ùķ��̼� �ð� (��)

# �ð� ���� ����
dt = 0.01  # �ð� ���� (��)

# ���� �ùķ��̼�
time = 0
while time < simulation_time:
    # ���� ���൵ ���
    progress = n_naoh / (molality * volume)

    # ���� ���
    q = n_naoh * heat_capacity * density * (temp_list[-1] - initial_temp)

    # �µ� ��ȭ�� ���
    delta_T = q / (molality * volume * heat_capacity * density)

    # �µ� ����
    temp = temp_list[-1] + delta_T
    temp_list.append(temp)

    # �ð�, ���� ���൵ ����
    time += dt
    time_list.append(time)
    naoh_list.append(naoh_list[-1] - molality * volume * progress * dt)

# �׷��� ���
plt.plot(naoh_list, temp_list)
plt.xlabel("Sodium hydroxide (mol)")
plt.ylabel("Temperature (��C)")
plt.show()
