#25
x = input('alpha bravo charlie delta echo forxtrot golf 입력 : ').split()
y = map(int,input('30 40 50 60 70 80 90 입력 :').split())
xy = {key: value for key, value in zip(x,y) if key != 'alpha' and key != 'delta'}
print(xy)

#26
park = {'korean':94,'english':91,'mathematics':89,'science':83}
a = park.get('english')
a1 = park.get('science')
print('english 점수 : %d, science 점수 : %d' % (a,a1))

#27
kim = {'korean':94,'english':91,'mathematics':89,'science':83}
x = dict.fromkeys(kim, 100)
print(x)

#28
lee = {'korean':94,'english':91,'mathematics':89,'science':83}
if 'english' in lee:
    lee.pop('english')
print(lee)

#29
lim = {'korean':94,'english':91,'mathematics':89,'science':83}
for i, j in lim.items():
    print(i, j)

#30
choi = {'korean':94,'english':91,'mathematics':89,'science':83}
result = {key for key, value in choi.items() if value >= 90}
print(result)

#31
yoo = {'korean':94,'english':91,'mathematics':89,'science':83}
sum = 0
for value in yoo.values():
    sum += value

average = sum / len(yoo)
print(average)