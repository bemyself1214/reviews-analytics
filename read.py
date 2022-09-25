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
#print(data[0]) #印出第一筆
#cls cmd畫面清掉

#print('--------------')
#print(data[1])