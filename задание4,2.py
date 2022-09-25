
count_lines = {}

for line in open(r"q4_urls.txt",'rb'):
    clear_line = line.rstrip()
    if clear_line not in count_lines:
        count_lines[clear_line.rstrip()] = 0
    count_lines[clear_line.rstrip()] += 1
num = 0
out = open(r"выход.txt",'w')
for line in open(r"q4_urls.txt",'rb'):
    count = count_lines [line.rstrip()]
    out.write(f'№{num} кол-во: {count};  {line} \n')
    num += 1

print(count_lines, count)

out.close()




