n = int(input("Digite um numero"))
div = 0
for i in range(1, n):
    if n % i == 0:
        div = div + 1
        if div > 1:
          break
if div > 1:
  print("não é primo")
else:
  print("é primo")


