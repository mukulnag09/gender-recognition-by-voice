def max_package_value(N, K, packages, capacities):
    dp = [[0] * (K+1) for _ in range(N+1)]
    for i in range(1, N+1):
        weight, value = packages[i-1]
        for j in range(1, K+1):
            if weight > capacities[j-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + value)
    return dp[N][K]


"""Line1=input()
N=int(Line1.split()[0])
k=int(Line1.split()[1])

packages=[]
for i in range(N):
    line=input()
    packages.append((int(line.split()[0]),int(line.split()[1])))
capacities=[]

line=input()
for i in range(k):
    capacities.append(int(line.split()[i]))"""

N = 4
K = 2
packages = [(1, 10), (2, 5), (3, 12), (4, 7)]
capacities = [3, 5]


max_value = max_package_value(N, K, packages, capacities)
print(str(max_value))