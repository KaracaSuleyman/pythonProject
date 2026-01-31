
class MagicMethod(list):
    def __add__(self, other):
        if len(self) != len(other):
            return 'Farkli uzunluklar toplanmaz'
        else:
            result=MagicMethod()
            for i in range(len(self)):
                result.append(self[i]+other[i])
        return result

    def __sub__(self, other):
        if len(self) != len(other):
            return 'Farkli uzunluklar toplanmaz'
        else:
            result=MagicMethod()
            for i in range(len(self)):
                result.append(self[i]-other[i])
        return result

    def __eq__(self, other):
        if sum(self) == sum(other):
            return True
        return False

    def __abs__(self):
        result=MagicMethod()
        for i in self:
            if i >=0:
                result.append((i))
            else:
                result.append(-1*i)
        return result


list1=MagicMethod([2,-6,5,])
list2=MagicMethod([-4,8,-1,])


print(list1+list2)
print(list1-list2)
print(list1==list2)
print(abs(list1))
print(abs(list2))