#За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя
#пользоваться условной инструкцией if и циклами.

n = 100
m = 92
#print ((m+n-1)//n) 
# или print (abs(-m//n))
print (m//n+1-(m==n))