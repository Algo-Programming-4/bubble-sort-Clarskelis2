def bubble(Unsorted):
  for n in range(len(Unsorted)):
    for i in range(len(Unsorted) - 1):
      if Unsorted[i] > Unsorted[i + 1]:
        temp = Unsorted[i]
        Unsorted[i] = Unsorted[i + 1]
        Unsorted[i + 1] = temp
  return Unsorted
