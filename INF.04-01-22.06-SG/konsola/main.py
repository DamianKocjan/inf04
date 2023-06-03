import random


def search(array: list[int], element: int) -> int:
  #########################################################
  # nazwa funkcji: search
  # argumenty: array   - tablica w której szukamy
  #            element - element do wyszukania
  # typ zwracany: int, indeks elementu w tablicy
  # informacje: funkcja zwraca indeks elementu w tablicy
  #             poprzez przeszukiwanie z wartownikiem
  # autor: <numer PESEL zdającego>
  #########################################################
  array.append(element)

  i = 0
  while i != len(array) - 1:
    if (array[i] == element):
      break

    i += 1

  array.pop()
  return i


def generate_array(size: int) -> list[int]:
  #########################################################
  # nazwa funkcji: generate_array
  # argumenty: size - rozmiar tablicy do wygenerowania
  # typ zwracany: int[], wygenerowana tablica
  # informacje: funkcja zwraca tablicę o rozmiarze size z
  #             losowymi wartościami z zakresu 1-100
  # autor: <numer PESEL zdającego>
  #########################################################
  array = []
  for i in range(size):
    num = random.randint(1, 100)
    array.append(num)

  return array


ARRAY_SIZE = 100

def main():
  array = generate_array(ARRAY_SIZE)

  num = int(input("Podaj liczbę do wyszukania: "))
  index = search(array, num)

  print("Wygenerowana tablica:")
  print(*array, sep=", ")

  if (index == len(array)):
    print("Nie znaleziono elementu")
  else:
    print(f"Znaleziono element na pozycji {index}")


if __name__ == '__main__':
  main()
