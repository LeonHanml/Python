def print_dptable(P):
    print("   ", end='  ')
    for i in range(len(P)):
        print("%7d" % i, end=' ')
    print('\n')

    for y in P[0].keys():
        print("%.5s: " % y, end='  ')
        for t in range(len(P)):
            print("%.7s" % ("%f" % P[t][y]), end=' ')
        print('\n')


def viterbi(X, Y, pi, A, B):
    """
    :param obs     X  :观测序列
    :param states  Y  :隐状态
    :param start_p pi :初始概率（隐状态）
    :param trans_p A  :转移概率（隐状态）
    :param emit_p: B  :发射概率（隐状态表现为显状态的概率）
    :return:
    """

    # 路径概率表 P[时间t][隐状态y] = 概率
    P = [{}]
    path = {}
    # 初始化 初始状态
    for y in Y :
    # 每个隐含状态
        P[0][y] = pi[y] * B[y][X[0]]
        path[y] = [y]


    T = len(X)
    for t in range(1, T):
        P.append({})
        print("*****")
        print(P)

        new_path = {}

        for y in Y:
            (p, state) = max([(P[t - 1][y0] * A[y0][y] * B[y][X[t]], y0) for y0 in Y])
            print("-----")
            print((p, state))

            P[t][y] = p
            print("*****")
            print(P)
            print("+++++")
            print(path[state])
            new_path[y] = path[state] + [y]
            print("=======")
            print(new_path)
        path = new_path

    print_dptable(P)
    (p, state) = max([(P[T - 1][y], y) for y in Y])
    return ( p ,path[state])

def main():
    # hidden series
    Y = ('Rainy', 'Sunny')
    # observations
    X = ('walk', 'shop', 'clean')
    pi = {'Rainy': 0.6, 'Sunny': 0.4}
    # transition_probability
    A ={
        'Rainy' : {'Rainy': 0.7, 'Sunny': 0.3},
        'Sunny' : {'Rainy': 0.4, 'Sunny': 0.6},
    }
    # emission_probability
    B = {
        'Rainy' : {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
        'Sunny' : {'walk': 0.6, 'shop': 0.3, 'clean': 0.1},
    }

    result = viterbi(X,
                     Y,
                     pi,
                     A,
                     B)
    return result


result = main()
print(result)

