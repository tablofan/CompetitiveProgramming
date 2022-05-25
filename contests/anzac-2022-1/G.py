def solve():
	return

def main():
	r, c = map(int, input().split())
	grid = []
	for _ in range(r):
		grid.append(input())
	dp = [[0 for _ in range(c+1)] for _ in range(r+1)]
	for i in range(r+1):
		dp[i][0] = i
	for i in range(c+1):
		dp[0][i] = i
	for i in range(r):
		for j in range(c):
			if grid[i][j] == '#':
				dp[i+1][j+1] = min(dp[i][j+1],dp[i+1][j])+1
			else:
				dp[i+1][j+1] = min(dp[i+1][j]+1, dp[i][j] + 2**0.5, dp[i][j+1]+1)
				ind = 0
				while i-ind>0 and grid[i-ind-1][j] == '.':
					print(f'{ind = }')
					print(f'{i = }')
					print(f'{j = }')
					print(f'{dp[i][j-ind] = }')
					dp[i+1][j+1] = min(dp[i+1][j+1], dp[i-ind-1][j]+((ind+1)**2+1)**0.5)
					ind += 1
				ind = 0
				while j-ind>0 and grid[i][j-ind-1] == '.':
					print(f'{ind = }')
					print(f'{i = }')
					print(f'{j = }')
					print(f'{dp[i][j-ind] = }')
					dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j-ind-1]+((ind+1)**2+1)**0.5)
					ind += 1
	print(dp)
	print(dp[r][c])


if __name__=="__main__":
	main()