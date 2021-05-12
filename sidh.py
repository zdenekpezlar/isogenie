from sage.all import *


########
#Public key generation. The last two input points are the other party's basis points. The first output is the image curve, the latter two are the the public basis point images.
########



def public(E,ll,e,m,n,P,Q,PP,QQ):
    G = m*P + n*Q
    EE = E
    Pi = PP
    Qi = QQ

    for i in range(0,e):
        K = G
        for j in range(0,e-i-1):
            K = ll*G
            
        iso = EllipticCurveIsogeny(EE,K)
        EE = iso.codomain()
        Pi = iso(Pi)
        Qi = iso(Qi)
        G = iso(G)

    return EE, Pi, Qi


########
#Private key generation. The input curve is the other party's image curve. The last two input points are the public points.
########


def key(E,ll,e,m,n,P,Q):
    G = m*P + n*Q
    EE = E

    for i in range(0,e):
        K = G
        for j in range(0,e-i-1):
            K = ll*G
            
        iso = EllipticCurveIsogeny(EE,K)
        EE = iso.codomain()
        G = iso(G)
    return EE.j_invariant()


########
#Initiator public key generation
########

def publicA(E,mA,nA,lA,lB, eA, eB,Gen1A,Gen2A,Gen1B,Gen2B):
    return public(E,lA,eA,mA,nA,Gen1A,Gen2A,Gen1B,Gen2B)

########
#Responder public key generation
########

def publicB(E,mB,nB,lA,lB, eA, eB,Gen1A,Gen2A,Gen1B,Gen2B):
    return public(E,lB,eB,mB,nB,Gen1B,Gen2B,Gen1A,Gen2A)

########
#Initiator private key generation
########

def keyA(mA,nA,E,P,Q,lA,lB, eA, eB): #Where the outputs of the public key are E,P,Q respectively
    return key(E,lA,eA,mA,nA,P,Q)


########
#Responder private key generation
########

def keyB(mB,nB,E,P,Q,lA,lB, eA, eB):
    return key(E,lB,eB,mB,nB,P,Q)

########
#Exchange testing
########

def test(E,mA,nA,mB,nB,lA,lB, eA, eB,Gen1A,Gen2A,Gen1B,Gen2B):
    pB = publicB(E,mB,nB,lA,lB, eA, eB,Gen1A,Gen2A,Gen1B,Gen2B)
    pA = publicA(E,mA,nA,lA,lB, eA, eB,Gen1A,Gen2A,Gen1B,Gen2B)
    testkeyA = keyA(mA,nA,pB[0],pB[1],pB[2],lA,lB, eA, eB)
    testkeyB = keyB(mB,nB,pA[0],pA[1],pA[2],lA,lB, eA, eB)
    if testkeyA == testkeyB:
        return testkeyA,pB,pA
    else:
        return "something has gone wrong"

def main(lA,lB, eA, eB):
    p = (lA**(eA)) * (lB**(eB)) - 1
    F=  GF(p**2)
    E = EllipticCurve([F(1), F(0)])
    Gen1A = E.gens()[0] #l_A**(eA) torsion generators
    Gen2A = E.gens()[1]
    for i in range(0,eB-1):
        Gen1A = lB*Gen1A
        Gen2A = lB*Gen2A 
    Gen1B = E.gens()[0] #l_B**(eB) torsion generators
    Gen2B = E.gens()[1] 
    for i in range(0,eA-1):
        Gen1B = lA*Gen1B
        Gen2B = lA*Gen2B 
    ma,na = randint(1,lA**eA),randint(1,lA**eA)
    mb,nb = randint(1,lB**eB),randint(1,lB**eB)
    key,pB,pA = test(E,ma,na,mb,nb,lA,lB, eA, eB,Gen1A,Gen2A,Gen1B,Gen2B)
    return E,(F,F.polynomial()),ma,na,mb,nb,Gen1A,Gen2A,Gen1B,Gen2B,pB,pA,key
