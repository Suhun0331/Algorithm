a, b = map(int,input().split())
maxx = 0
minn = 0
m_a = a
m_b = b
i_a = a
i_b = b
while True:
    if m_a>m_b:
        m_b += b
    elif m_a<m_b:
        m_a += a
    else:
        maxx = m_a
        break

lst_a = []
lst_b = []

for i in range(1, a+1):
    if i_a%i==0:
        lst_a.append(i)

for i in range(1, b+1):
    if i_b%i==0:
        lst_b.append(i)

for i in lst_b:
    if i in lst_a:
        if minn < i:
            minn = i
print(minn)
print(maxx)