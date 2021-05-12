from sage.all import *

########
#Initiator random walk
########
def awalk(E,lA,lB,eA,eB,x,y,Gen01,Gen02):
    G = x*Gen01 + y*Gen02
    EE = E
    for i in range(0,eA):
        K = (lA**(eA-1-i))*G
        iso = EllipticCurveIsogeny(EE,K)
        EE = iso.codomain()
        G = iso(G)


    for i in range(0,eB):
        K = (lB**(eB-1-i))*G
        iso = EllipticCurveIsogeny(EE,K)
        EE = iso.codomain()
        G = iso(G)

    return EE,EE.gens()[0],EE.gens()[1]


########
#Public key generation. The last two input points are the other party's basis points. The first output is the image curve, the latter two are the the public basis point images.
########

def public(E,ll,e,m,n,P,Q,PP,QQ):
    G = m*P + n*Q
    EE = E
    Pi = PP
    Qi = QQ

    for i in range(0,e):
            K = (ll**(e-1-i))*G
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
        K = (ll**(e-1-i))*G
        iso = EllipticCurveIsogeny(EE,K)
        EE = iso.codomain()
        G = iso(G)

    return EE.j_invariant()

########
#Initiator public key generation
########

def publicA(E,mA,nA,lA,lB,eA,eB,Gen1A,Gen2A,Gen1B,Gen2B):
    return public(E,lA,eA,mA,nA,Gen1A,Gen2A,Gen1B,Gen2B)



########
#Responder public key generation
########

def publicB(E,mB,nB,lA,lB,eA,eB,Gen1A,Gen2A,Gen1B,Gen2B):
    return public(E,lB,eB,mB,nB,Gen1B,Gen2B,Gen1A,Gen2A)

########
#Initiator private key generation
########

def keyA(mA,nA,E,P,Q,lA,eA): #Where the outputs of the public key are E,P,Q respectively
    return key(E,lA,eA,mA,nA,P,Q)


########
#Responder private key generation
########

def keyB(mB,nB,E,P,Q,lB,eB):
    return key(E,lB,eB,mB,nB,P,Q)

########
#Exchange testing
########

def test(E,mA,nA,mB,nB,x,y,lA,lB,eA,eB,Gen01,Gen02):
    E1,Gen1,Gen2 = awalk(E,lA,lB,eA,eB,x,y,Gen01,Gen02)
    Gen1B = lA**eA * Gen1
    Gen2B = lA**eA * Gen2
    Gen1A = lB**eB * Gen1
    Gen2A = lB**eB * Gen2
    pA = publicA(E1,mA,nA,lA,lB,eA,eB,Gen1A,Gen2A,Gen1B,Gen2B)
    pB = publicB(E1,mB,nB,lA,lB,eA,eB,Gen1A,Gen2A,Gen1B,Gen2B)
    testkeyA = keyA(mA,nA,pB[0],pB[1],pB[2],lA,eA)
    testkeyB = keyB(mB,nB,pA[0],pA[1],pA[2],lB,eB)
    if testkeyA == testkeyB:
        return testkeyA,pA,pB,(E1,Gen1,Gen2),Gen1A,Gen2A,Gen1B,Gen2B
    else:
        return "something has gone wrong"

def main(lA,lB,eA,eB):
    p = (lA**(eA)) * (lB**(eB)) - 1
    F = GF(p**2)
    E0 = EllipticCurve([F(1), F(0)])
    Gen01 = E0.gens()[0]
    Gen02 = E0.gens()[1]
    ma,na = randint(1,lA**eA),randint(1,lA**eA)
    mb,nb = randint(1,lB**eB),randint(1,lB**eB)
    x,y = randint(1,E0.order()),randint(1,E0.order())
    key,pB,pA,E1,Gen1A,Gen2A,Gen1B,Gen2B = test(E0,ma,na,mb,nb,x,y,lA,lB,eA,eB,Gen01,Gen02)
    return E0,(F,F.polynomial()),E1,ma,na,mb,nb,Gen1A,Gen2A,Gen1B,Gen2B,pB,pA,key
