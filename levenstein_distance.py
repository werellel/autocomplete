''' https://www.geeksforgeeks.org/edit-distance-dp-5/ '''

# minimum number를 찾기 위한 단순한 방법
# s1을 s2로 변환하기 위한 operations
def editDistance(s1, s2, m, n):    
    # print(s1[:m])    
    # print(s2[:n])    
    # 첫번째 문자열이 empty라면,    
    # 두번째 문자열의 모든 문자열을 첫번째 문자열에 insert.    
    if m == 0:    
        return n
        
    # 두번째 문자열이 empty라면,    
    # 첫번째 문자열의 모든 문자열을 지운다.     
    if n == 0:    
    	return m
    
    # 만약 마지막의 두 문자열이 같다면,     
    # 할거 없다. 마지막 문자열을 무시하고 나머지 문자열을 계산한다.    
    if s1[m-1] == s2[n-1]:    
        return editDistance(s1, s2, m-1, n-1)
    
    # 만약 문자열이 같지 않으면, 세 가지 연산에 대해서 고려해야 한다.    
    # 첫번째 문자열의 마지막 문자에 대한 연산을 계산해야 한다.     
    # 세 가지 연산에 대해서 제일 적은 비용을 재귀적으로 계산하여    
    # 세 가지의 값 중 최소값을 취한다.    
    # print('minimum')    
    return 1 + min(editDistance(s1, s2, m, n-1),   # Insert    
                   editDistance(s1, s2, m-1, n),   # Remove    
                   editDistance(s1, s2, m-1, n-1), # Replace    
                   )

    # Driver program to test the above function 

# This code is contributed by Bhavya Jain

# 최악의 경우는 두 문자열 모두가 다를 때로 3^m의 시간복잡도를 가진다.
# 위의 예만 실행해 보더라도 속도가 매우 느린 것을 알 수 있다.


# 우리는 많은 subproblem들이 해결되는 것을 볼 수 있다. 
# 예를 들어, eD(2, 2)는 세 번 실행한다. 같은 문제가 반복해서 불려지기 때문에, 이 문제는 하나의 문제로 겹쳐서 풀어야 한다. 
# 따라서 편집 거리 문제는 DP 문제의 속성(Optimal Substructure, Tabulation, Memoization)을 가지고 있다. 
# 다른 전형적인 DP 문제와 마찬가지로, 
# subproblem의 결과를 저장하는 temporary array을 구성함으로써 동일한 하위 문제의 재추정을 피할 수 있다.


# DP를 기반으로 한 Python program for edit distance problem 
def editDistBasicDP(s1, s2, m, n): 
    # subproblems의 결과를 저장할 테이블 생성
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)] 
  
    # bottom up 방법으로 dp[][]를 채운다.
    for i in range(m + 1): 
        for j in range(n + 1):
            # 만약 첫번째 문자열이 비어있다면, 두번째 문자열의 모든 문자를 insert.
            if i == 0: 
                dp[i][j] = j    # Min. operations = j 

        	# 만약 두번째 문자열이 비어있다면, 첫번째 문자열의 모든 문자를 remove.
            elif j == 0: 
                dp[i][j] = i    # Min. operations = i 
            
            # 만약 두 문자열의 마지막이 같다면, 마지막 문자는 무시하고 남은 문자열에 대해 recur
            elif s1[i-1] == s2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 

            # 마지막 문자가 다르면 모든 가능성을 고려하여 minimum을 찾습니다
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])      # Replace 
    # print(dp)
    return dp[m][n] 

# Driver program
# This code is contributed by Bhavya Jain 
# 위 예의 시간, 공간 복잡도: m * n
# 위의 방법에선 m*n의 공간복잡도가 필요하다. 
# 만약 2000*2000의 배열까지 만들 수 있다면 문자열의 길이가 2000이 넘을 경우 적합하지 않다.
# DP array에서 row를 채우려면 상단의 row 하나만 필요하다.
# 예를 들어, DP array에서 i=10 row를 채우는 경우 9번째 row만 필요하다.
# str1 길이의 2개의 DP array만 있으면 된다. 
# 공간 복잡도를 낮춘다.

# 위에서 언급한 방법의 구현
def editDistDP(s1, s2):
    len1 = len(s1)
    len2 = len(s2)

    # 이전에 계산의 결과를 Memoize할 DP array 생성
    DP = [[0 for x in range(len1+1)] for x in range(2)]

    # Base condition 두번째 문자열이 empty면 모든 문자열을 지운다.
    for i in range(len(DP[0])):
        DP[0][i] = i

    # DP 채우기 시작. 이 루프는 두 번째 문자열의 모든 문자에 대해 실행
    for i in range(1, len2+1):
        # 이 루프는 두 번째 문자열의 문자를 첫 번째 문자열 문자와 비교
        for j in range(0, len1+1):
            # 만약 첫 번째 문자열이 비어있다면 문자를 추가해야 하므로 두 번째 문자열을 가져온다.
            if j == 0:
                DP[i%2][j] = i

            # 만약 두 문자열이 같다면 어떠한 연산도 하지 않는다. i%2는 row number와 묶여있다.
            elif s1[j-1] == s2[i-1]:
                DP[i%2][j] = DP[(i-1) % 2][j-1]

            # 만약 두 문자열이 다르면 세가지의 연산에서 minimum을 취한다.
            else:
                DP[i%2][j] = 1 + min(DP[(i - 1) % 2][j], 
                                     DP[i % 2][j - 1], 
                                     DP[(i - 1) % 2][j - 1])

    # DP array를 완성한 후 
    # len2가 짝수이면 0번째 row로 끝나게 된다. 
    # 그렇지 않으면 1번째 row로 끝나게 된다.
    # len2 % 2를 통해 row를 구한다.
    return DP[len2%2][len1]
    # This code is contributed by werellel
    # 공간 복잡도 O(m)

if __name__ == '__main__':
    import time
    import random
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    s1 = 'food'
    s2 = 'money'
    start_time = time.time()
    print(editDistance(s1, s2, len(s1), len(s2)))
    end_time = time.time()
    print("WorkingTime: {} sec".format(end_time-start_time))

    start_time = time.time()
    print(editDistBasicDP(s1, s2, len(s1), len(s2))) 
    end_time = time.time()
    print("WorkingTime: {} sec".format(end_time-start_time))

    start_time = time.time()
    print(editDistDP(s1, s2))
    end_time = time.time()
    print("WorkingTime: {} sec".format(end_time-start_time))
    