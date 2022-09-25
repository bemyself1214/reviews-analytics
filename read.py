data = []
count = 0
sum_len = 0
avg_len = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		#if count % 1000 == 0:
			#print(len(data))

print('檔案讀取完了，總共有', len(data), '筆資料')

for d in data:
	sum_len += len(d)

avg_len = sum_len / len(data)
print('留言平均長度為', avg_len)

new = []
for d in data: #for loop的意思是[把清單中的東西一個一個拿出來]
	if len(d) < 100:
		new.append(d)
print('一定有', len(new), '比留言長度小於100')
print(new[0])
print(new[1])

# good = []
# for d in data: #for loop的意思是[把清單中的東西一個一個拿出來]
# 	if 'good' in d:
# 		good.append(d)
# print('一共有', len(good), '比留言提到good')
#==清單快寫法
good = [1 for d in data if 'good' in d]
       #^把1的裝進good
print(good)

bad = ['bad' in d for d in data]
print(bad)

#不是快寫法的bad
# bad = []
# for d in data:
# 	bad.append('bad' in d)

#print(data[0]) #印出第一筆
#cls cmd畫面清掉

#print('--------------')
#print(data[1])