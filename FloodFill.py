class Solution:
    def floodFill(self, image, sr, sc, color):
        orig = image[sr][sc]
        if orig == color:
            return image

        def dfs(r, c):
            if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == orig:
                image[r][c] = color
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)

        dfs(sr, sc)
        return image
image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]
sr, sc, color = 1, 1, 2

print("Input image:")
for row in image:
    print(row)

result = Solution().floodFill(image, sr, sc, color)

print("\nOutput image:")
for row in result:
    print(row)
