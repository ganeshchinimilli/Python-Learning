count_sub = int(input())
roll_num = list(map(int,input().split()))
count_fr = int(input())
roll_fr = list(map(int,input().split()))
new_list = list();
for i in roll_num:
    if(i in roll_fr):
        new_list.append(i)

print(len(new_list))