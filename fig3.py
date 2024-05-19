import matplotlib.pyplot as plt
import math


def T(n):
    """sum(2^k * Log_2(n/2^k)) ; 0 <= k <= Log_2(n)"""
    Tn_i = []
    for k in range(math.ceil(math.log2(n)) + 1):
        t = (2 ** k) * math.log2(n / 2 ** k)
        Tn_i.append(t)
        # print(f"k = {k}\t: sum(2^k * Log_2(n/2^k)) = {t:.4f}")
    TnSolution = sum(Tn_i)
    AbsDiff = abs(TnSolution-n)
    # print(f"T(n) = {TnSolution:.3e} for n = {n:3e}; difference = {AbsDiff:.3e}")
    return TnSolution, AbsDiff


def testTn():
    """1 million data points; range 1000 to 1 billion; interval 1000"""
    N = [i * i for i in range(1000, int(1e9)+1, 1000)]
    # N = [i for i in range(10, 1001, 50)]
    Tn = []
    dif = []
    twoN = [i * 2 for i in N]
    for n in N:
        tn = T(n)
        Tn.append(tn[0])
        dif.append(tn[1])

    avg_dif = sum(dif)/len(dif)
    avg_n = sum(N)/len(N)
    avg_tn = sum(Tn)/len(Tn)
    avg_2n = sum(twoN)/len(twoN)
    print(f"\nAverage n-size: {avg_n:.3e}\nAverage Difference: {avg_dif:.3e}")

    plt.rcParams.update({"font.size": 14})

    plt.plot(N, Tn, label=r"$\omega(n)$")
    plt.plot(N, dif, label=r"$Abs(\omega(n) - n)$")
    plt.plot(N, N, label=r"$n$")
    plt.plot(N, twoN, label=r"$2n$")
    plt.xlabel(r"$n$-values")
    plt.title(r"Stronger Bounds of $\omega(n)$")
    plt.legend()

    stats = (f"Averages:\n"
             f"$\omega(n)$ = {avg_tn:.3e}\n"
             f"$Abs(\omega(n) - n)$ = {avg_dif:.3e}\n"
             f"$n$-size = {avg_n:.3e}\n"
             f"$2n$ = {avg_2n:.3e}")
    bbox = dict(boxstyle="round", fc="blanchedalmond", ec="orange", alpha=0.5)
    plt.text(N[int(0.375*len(N))], 0.8725*max(twoN), stats, bbox=bbox, horizontalalignment="left")

    plt.show()

    return N, Tn


def testSmallerTn():
    """1 million data points; range 1000 to 1 billion; interval 1000"""
    N = [i for i in range(90, 101)]
    Tn = []
    dif = []
    for n in N:
        tn = T(n)
        Tn.append(tn[0])
        dif.append(tn[1])
    print(f"\nAverage n-size: {sum(N)/len(N):.3e}\nAverage Difference: {sum(dif)/len(dif):.3e}")

    plt.plot(N, Tn, label=" ω(n)")
    plt.plot(N, dif, label="Abs(ω(n) - n)")
    plt.plot(N, N, label="n")
    plt.xlabel("n-values")
    plt.title("Empirical Bounds of  ω(n)")
    plt.legend()
    plt.show()

    return N, Tn


def testUperBoundT():
    """sum(2^k * Log_2(n/2^k))"""
    for i in range(int(1e6), int(10e9)+1, int(100e6)):     # range(10, 1001, 50):
        k = math.log2(i)
        t = (2 ** k) * math.log2(i / 2 ** k)
        print(f"For n = {i}, k = {k}\t: 2^k * Log_2(n/2^k) = {t:.3e}")


if __name__ == "__main__":
    testTn()
    # testSmallerTn()
    # testUperBoundT()
