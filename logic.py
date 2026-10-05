from math import comb

def Prob_Bernoulli(n,k,p):
    if not Formula(n,k,p):
        return 'Error:belowzero' 
    if not Prob_check(p):
        return 'Error:higher1'
    if k > n:
        return 'Error:notsatisfy_Bernoulli'
    return (comb(n,k))*(p**k)*((1-p)**(n-k))

def Prob_mult(A,B): 
    if not Formula(A,B):
        return 'Error:belowzero' 
    if not Prob_check(A,B):
        return 'Error:higher1'
    return A*B  

def Prob_add_incomp(A,B):
    if not Formula(A,B):
        return 'Error:belowzero' 
    if not Prob_check(A,B):
        return 'Error:higher1'
    if A+B > 1: 
        return 'Error:higher1_add'
    return A+B
    
def Prob_add_indep(A,B):
    if not Formula(A,B):
        return 'Error:belowzero' 
    if not Prob_check(A,B):
        return 'Error:higher1'
    return A + B -(A * B)
        
def Prob_add_dep(A,B,A0B):
    if not Formula(A,B,A0B):
        return 'Error:belowzero' 
    if not Prob_check(A,B,A0B):
        return 'Error:higher1'
    if ((A + B) - A0B) > 1:
        return 'Error:higher1_add'
    if ((A + B) - A0B) < 0:
        return 'Error:belowzero_add'
    return (A + B) - A0B
        
def Prob_check(*args): 
    for x in args:
        if x > 1:
            return False 
    return True

def Prob_at_least(p,n): 
    if not Formula(p,n):
        return 'Error:belowzero' 
    if not Prob_check(p):
        return 'Error:higher1'
    return (1-((1-p)**n))

def Formula(*args):
    for x in args:
        if x < 0:
            return False
    return True

def Prob_easy(m,n): 
    if Formula(m,n):
        if m<=n:
            return m/n
        else:
            return 'Error:notsatisfy_easy'
    return 'Error:belowzero'