import heapq
import random

n,m = input().split()
n = int(n)
m = int(m)

H = []
n_out = [[] * n for i in range(n)]

for j in range(m):
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    n_out[a].append((b,c))
    n_out[b].append((a,c))

raiz = random.randint(0,n-1)
for(x,c) in n_out[raiz]:
    heapq.heappush(H, (c,raiz,x))

n_edges = 0
custo_tot = 0
marcados = [raiz]
arv_ger_min = []

while n_edges < n-1:
    while True:
        (c,a,b) = heapq.heappop(H)
        if b not in marcados:
            break
    marcados.append(b)
    print(a,b)
    print(marcados)
    custo_tot += c
    arv_ger_min.append((a,b))
    n_edges += 1
    for (x,c) in n_out[b]:
        if x not in marcados:
            heapq.heappush(H,(c,b,x))

print(custo_tot)
print(arv_ger_min) #teste