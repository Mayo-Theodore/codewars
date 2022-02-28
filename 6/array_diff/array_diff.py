class ArrayDiff():

    def integers_only(self, a, b):
        if all(isinstance(e, (int, float)) for e in a) and all(isinstance(e, (int, float)) for e in b) :
            pass
        else:
            return "List must only contain integers"

    def check_length(self, a, b):
        if len(a) or len(b) > 5:
            return "List must contain a maximum of 5 integers"
    
    def difference(self, a, b):
        for x in b:
            while x in a:
                a.remove(x)
        return a
