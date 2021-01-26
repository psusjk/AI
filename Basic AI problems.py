############################################################
# Section 1: Working with Lists
############################################################

def extract_and_apply(l, p, f):
    return [f(x) for x in l if p(x)]

def concatenate(seqs):
    return [s for u in seqs for s in u]

def transpose(matrix):
    lst=matrix
    num=len(lst)
    newlst=[]
    for i in range (len(lst[0])):
        sublst=[]
        counter=0
        while counter <= num-1:
            sublst.append(lst[counter][i])
            counter+=1
        newlst.append(sublst)
    return newlst

############################################################
# Section 2: Sequence Slicing
############################################################

def copy(seq):
    return seq[:]

def all_but_last(seq):
    return seq[:-1]

def every_other(seq):
    return seq[::2]

############################################################
# Section 3: Combinatorial Algorithms
############################################################

def prefixes(seq):
    ans=[]
    num=len(seq)
    for i in range(num+1):
        ans.append(seq[:i])
    return ans

def suffixes(seq):
    ans=[]
    num=len(seq)
    for i in range(num+1):
        ans.append(seq[i:])
    return ans

def slices(seq):
    ans=[]
    num=len(seq)
    for i in range(num):
        for j in range(1,num+1):
            if len(seq[i:j])>0:
                ans.append(seq[i:j])
    return ans

############################################################
# Section 4: Text Processing
############################################################

def normalize(text):
    return " ".join(text.lower().split())

def no_vowels(text):
    vowels =['a','e','i','o','u','A','E','I','O','U']
    for c in text:
        if c in vowels:
            text=text.replace(c,"")
    return text
    
def digits_to_words(text):
    numbers={"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
    result=""
    for i in text:
        if i in numbers.keys():
            result=result+numbers[i]+" "
    return result.strip()

def to_mixed_case(name):
    result=""
    result=result+lst[0].lower()
    num=len(lst)
    for i in range (1,num):
        lst[i].lower()
        result=result+lst[i].title()
    return result

############################################################
# Section 5: Polynomials
############################################################

class Polynomial(object):

    def __init__(self, polynomial):
        self.polynomial=tuple(polynomial)        

    def get_polynomial(self):
        return self.polynomial

    def __neg__(self):
        lst=[]
        for i in self.polynomial:
            (x,a)=i
            i=(-x,a)
            lst.append(i)
        return Polynomial(lst)

    def __add__(self, other):
        return Polynomial(self.polynomial+other.polynomial)

    def __sub__(self, other):
        other = - other
        return Polynomial(self.polynomial + other.polynomial)

    def __mul__(self, other):
        lst=[]
        for i in self.polynomial:
            (x,a)=i
            for j in other.polynomial:
                (y,b)=j
                coef=x*y
                power=a+b
                lst.append((coef,power))
        return Polynomial(lst)

    def __call__(self, x):
        return sum(i[0]*(x**i[1]) for i in self.polynomial)       
            
             

    def simplify(self):
        mydict={}
        lst=[]
        for i in self.polynomial:
            (x,a)=i
            if a not in mydict.keys():
                mydict[a]=x
            else:
                mydict[a]=mydict[a]+x
        if mydict[a] == 0:
            del mydict[a]
        dictsort=sorted(mydict.items(),key=lambda x:x[1],reverse=True)
        for j in dictsort:
            (t,r)=j
            lst.append((r,t))
        self.polynomial=tuple(lst)

    def __str__(self):
        pass


