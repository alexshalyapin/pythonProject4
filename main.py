import math

g = float(1.62)
M = float(2250)
m = [float(1000)]
C = float(3660)
q = float(0)
h = [float(0.0000001)]
h_min = float(0.00000001)
V_h = [float(0)]
x = [float(0)]
u = [float(0)]
a = float(0)
a_max = float(3*9.81)
al = float(0)
dm = float(0)
t = float(0)

i = int(0)
t_f = [float(0)]


def q_a():
    global q, dm, t, C, M, m, a
    q = dm / t
    a = q * C / (M + m[i])


def main_bl():
    global V_h,a,t,al,x,u,g,h
    V_h.append(V_h[i] + a * t * math.sin(al))
    x.append(x[i] + (V_h[i] + V_h[i + 1]) / 2 * t)
    u.append(u[i] + (a * math.cos(al) - g) * t)
    h.append(h[i] + (u[i + 1] + u[i]) / 2 * t)
    m.append(m[i] - q * t)


def correct_bl():
    global i, t_f, t, V_h, x, u, h, m
    main_bl()
    t_f.append(t_f[i] + t)
    i += 1
    main_bl()
    V_h[i - 1] = V_h[i]
    x[i - 1] = x[i]
    u[i - 1] = u[i]
    h[i - 1] = h[i]
    m[i - 1] = m[i]
    t_f[i - 1] = t_f[i]


def print_res():
    global i
    global t_f

    print("Высота    : ", round(h[i], 2), "V верт : ", round(u[i], 2), "Остаток т:",
          round(m[i], 2), "a:", round(a, 2))
    print("Расстояние: ", round(x[i], 2), "V гориз: ", round(V_h[i], 2), "число шагов:",
          i, "Общее время", round(t_f[i], 2), "\n")


def get_date():
    global t_f
    global i,dm, t, al, V_h, m, h,x, u, a
    date_correct = True

    while date_correct:
        q_max = a_max * (M + m[i]) / C
        print("Сек.расход не более", round(q_max, 2), "(", round(100 / q_max, 2), "c)")
        dm = float(input("\ndm:"))
        t = float(input("t:"))
        al = float(input("al:"))
        if dm == 5555 or t == 5555 or al == 5555:
            i = int(input("\nВведите номер шага для возврата \n"))
            del V_h[i+1:]
            del m[i+1:]
            del h[i+1:]
            del x[i+1:]
            del u[i+1:]
            del t_f[i+1:]
            print_res()
            get_date()
            break
        if dm > m[i]:
            t = t * m[i] / dm
            dm = m[i]
        dm = dm
        t = t
        al = math.pi / 180 * al
        if dm < 0.05 * (M + m[i]) and t != 0:
            date_correct = False
        else:
            print("\nДанные некорректны")


while abs(h[i]) > h_min:
    if h[i] < 0:
        t = 2 * h[i] / (math.sqrt(u[i] ** 2 + 2 * h[i] * (g - a * math.cos(al))) - u[i])
        correct_bl()
        print("\n------------------------------------------------------------------")
        print("|    h     |    S     |     Vv    |    Vh   |    T    |    m     |")
        print("-----------------------------------------------------------------")
        i_max = len(V_h) - 2
        for i in range(0, i_max):
            print('%10s %10s %10s %10s %10s %10s' % (round(h[i], 2), round(x[i], 2),
                                                round(u[i], 2), round(V_h[i], 2), round(t_f[i], 2), round(m[i], 2)))
        print("------------------------------------------------------------------")
        print("|    h     |    S     |     Vv    |    Vh   |    T    |    m     |")
        print("------------------------------------------------------------------")
        exit(100)
    elif h[i] > 0:
        print_res()
        get_date()
    elif abs(h[i]) < h_min:
        h[i] = 0
    q_a()
    main_bl()
    if a_max < a:
        t_f.append(t_f[i] + t)
        i += 1
        dm = 0
        t = a - a_max
        print("a>a_max", a, "\nt:", t)
        q_a()
        main_bl()
        print_res()
    t_f.append(t_f[i] + t)
    i += 1
