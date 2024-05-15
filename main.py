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
    testSmallerTn()
    # testTn()
    # testUperBoundT()
