#Given: A string s of length at most 200 letters and four integers a, b, c and d.

#Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d]
in our slice.

s = 'FRcxh96UrzAK5rKhwJS0nvD8g6ZC1Xksz1IfjP58iKmbk7IU7QG6pMF1b0BYA21K4pEtzS51lNmrcdg7JgDRosaliaw0clypeatus9Yv6oG37ZNPnGgxcJLW5RqII36Dm9pEruvWdOn3adSAOJpmqebA0UUKXe4iVDUb7ghatMuUaDO'
a = 83
b = 90
c = 92
d = 101
print (s[a:b] + ' ' + s[c:d])