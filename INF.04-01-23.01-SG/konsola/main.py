def nwd(a: int, b: int) -> int:
  """
  **********************************************
  nazwa funkcji: nwd
  opis funkcji: funkcja zwraca największy wspólny dzielnik dwóch liczb
  parametry: a - pierwsza liczba całkowita
  nazwa parametru b - druga liczba całkowita
  zwracany typ i opis: int, największy wspólny dzielnik
  autor: 00000000000
  ***********************************************
  """
  while (a != b):
    if (a > b):
      a -= b
    else:
      b -= a
  return a


def main():
  a = int(input("Podaj a: "))
  b = int(input("Podaj b: "))

  print(f"Największy wspólny dzielnik {a} i {b}, to {nwd(a, b)}")


if __name__ == "__main__":
  main()
