import random
class Sorting():

    def merge_sort(self,lst):
        def merge_lst(lst_a,lst_b):
            length_a=len(lst_a)
            length_b=len(lst_b)
            lst=[]
            i=j=0
            while i <length_a and j<length_b:
                if lst_a[i]<lst_b[j]:
                    lst.append(lst_a[i])
                    i+=1
                else:
                    lst.append(lst_b[j])
                    j+=1
            if i==length_a:
                lst+=lst_b[j:]
            else:
                lst += lst_a[i:]
            return lst

        def recursive(lst):
            if len(lst) <= 1:
                return lst
            mid=len(lst)//2
            lst_a=recursive(lst[:mid])
            lst_b=recursive(lst[mid:])
            return merge_lst(lst_a,lst_b)

        return recursive(lst)



lst=list(range(15))
random.shuffle(lst)

print('before:',lst)
s=Sorting()
lst=s.merge_sort(lst)

print('after:',lst)