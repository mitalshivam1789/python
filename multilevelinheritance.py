class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    def isdance(self):
        return f"Yes I can dance {self.dance} o of times."

class Grandson(Son):
    dance = 6
    def isdance(self):
        return f"I can dance much better then dad as Ican dance {self.dance} times."
darry = Dad()
larry = Son()
harry = Grandson()
print(harry.isdance())
print(harry.basketball)