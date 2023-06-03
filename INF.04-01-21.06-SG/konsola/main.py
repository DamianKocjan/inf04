class Sorter:
  def __init__(self, array: list[int]):
    self.array = array

  def sort(self) -> list[int]:
    #########################################################
    # nazwa funkcji: sort
    # parametry wejściowe: -
    # wartość zwracana: list[int] - posortowana tablica
    # autor: <numer PESEL zdającego>
    #########################################################
    length = len(self.array)

    for i in range(length):
      maxIndex = self._max(i, length)

      self.array[i], self.array[maxIndex] = self.array[maxIndex], self.array[i]

    return self.array

  def _max(self, start: int, end: int) -> int:
    #########################################################
    # nazwa funkcji: max
    # parametry wejściowe: start - indeks od którego zaczynamy szukać
    #                      end   - indeks na którym kończymy szukać
    # wartość zwracana: int - indeks największego elementu w tablicy
    # autor: <numer PESEL zdającego>
    #########################################################
    maxIndex = start
    i = start

    while (i < end):
      if (self.array[i] > self.array[maxIndex]):
        maxIndex = i
      i += 1

    return maxIndex

ARRAY_SIZE = 10


def main():
  array = []

  print(f'Podaj {ARRAY_SIZE} elementow tablicy: ')

  for i in range(ARRAY_SIZE):
    array.append(int(input(f'Podaj {i+1} element: ')))

  sorter = Sorter(array)
  sorted = sorter.sort()

  print('Posortowana tablica: ')

  for i in range(ARRAY_SIZE):
    print(sorted[i])


if __name__ == '__main__':
  main()