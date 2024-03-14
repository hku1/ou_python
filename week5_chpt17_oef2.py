# Oefening 2
# In de implementatie van onze eigen subklasse van list ontbreekt nog de insert methode.
#
# Geef van die methode de documentatie en de implementatie.
#
# We geven hier nog eens de code zonder documentatie:


class SortedIntList(list):
    def __init__(self, initial_list: list[int]=[]):
        self._checklist(initial_list)
        self.__ascending = True
        super().__init__(initial_list)
        self.sort()

    def _check(self, el: int):
        if not isinstance(el, int):
            raise TypeError("Not an integer")
        return True

    def _checklist(self, l: list[int]):
        if not isinstance(l, list):
            raise TypeError("Argument must be a list with integers")
        for item in l:
            self._check(item)
        return True

    def __setitem__(self, i: int, item: int):
        self.append(item)

    def sort(self, key=None, reverse=False):
        if reverse:
            if self.__ascending:
                self.__ascending = False
            else:
                self.__ascending = True
        if self.__ascending:
            super().sort()
        else:
            super().sort(reverse=True)


    def append(self, item: int):
        self._check(item)
        super().append(item)
        self.sort()

    def extend(self, items: list[int]):
        self._checklist(items)
        super().extend(items)
        self.sort()

    def insert(self, index: int, item: int):
        self._check(item)
        self._check(index)
        super().insert(index, item)
        self.sort()


    def reverse(self):
        if self.__ascending:
            self.__ascending = False
        else:
            self.__ascending = True
        self.sort()


l = [5, 6, 9, 2]

sil = SortedIntList(l)

print(sil)

sil.insert(1,11)

print(sil)



sil.insert(2, 11)