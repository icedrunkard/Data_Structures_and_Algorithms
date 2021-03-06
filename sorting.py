import random


class Sorting():

    def merge_sort(self, lst):
        def merge_lst(lst_a, lst_b):
            length_a = len(lst_a)
            length_b = len(lst_b)
            lst = []
            i = j = 0
            while i < length_a and j < length_b:
                if lst_a[i] < lst_b[j]:
                    lst.append(lst_a[i])
                    i += 1
                else:
                    lst.append(lst_b[j])
                    j += 1
            if i == length_a:
                lst += lst_b[j:]
            else:
                lst += lst_a[i:]
            return lst

        def recursive(lst):
            if len(lst) <= 1:
                return lst
            mid = len(lst) // 2
            lst_a = recursive(lst[:mid])
            lst_b = recursive(lst[mid:])
            return merge_lst(lst_a, lst_b)

        return recursive(lst)

    def quick_sort(self, lst):
        if len(lst) <= 1:
            return lst
        return self.quick_sort([x for x in lst[1:] if x < lst[0]]) + \
               lst[:1] + \
               self.quick_sort([x for x in lst[1:] if x >= lst[0]])

    def insert_sort(self, lst):
        for i in range(len(lst)):
            x = lst[i]
            j = i
            while j > 0 and lst[j - 1] > x:
                lst[j] = lst[j - 1]
                j -= 1
            lst[j] = x
        return lst

    def bubble_sort(self, lst):
        for i in range(len(lst))[::-1]:
            swap = False
            for j in range(i):
                if lst[j + 1] < lst[j]:
                    lst[j + 1], lst[j] = lst[j], lst[j + 1]
                    swap = True
            if not swap: break
        return lst

    def shell_sort(self,lst):
        step=len(lst)//3
        while step>0:
            for i in range(step,len(lst)):
                while i>=step and lst[i-step]>lst[i]:
                    lst[i],lst[i-step]=lst[i-step],lst[i]
                    i-=step
            step=step//3
        return lst

lst = list(range(15))
random.shuffle(lst)
lst=[7, 13, 10, 5, 8, 1, 4, 9, 0, 3, 6, 2, 14, 11, 12]
print('before:', lst)
s = Sorting()
lst = s.shell_sort(lst)

print('after:', lst)
