#                                  Merge Sort Algorithm 

def fusion(l1,l2):
    if(not l1):return l2
    if (not l2):return l1
    if(l1[0]<l2[0]):
        print([l1[0]] + fusion(l1[1:],l2))
        return [l1[0]] + fusion(l1[1:],l2)
    print([l2[0]] + fusion(l1,l2[1:]))
    return [l2[0]] + fusion(l1,l2[1:])

def AlgotriFusion(l):
   if(len(l)==1):return l
   else:
        N = len(l)//2
        leftlist = AlgotriFusion(l[0:N])
        rightlist = AlgotriFusion(l[N:])
        a = fusion(leftlist,rightlist)
   return a

listeEntiers = [12, -5, 7, 3, 19, 0, -8, 14, 22, 1, 6, -3, 17, 9, 4, 15]
print(AlgotriFusion(listeEntiers))



        
    