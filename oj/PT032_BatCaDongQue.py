duoc, mat, caAo = map(int,input().split())

def cach_1_timelimit(duoc, mat, caAo):
    soLanVot = 0
    while caAo > 0:
        if (caAo <= duoc):
            caAo = caAo - duoc
        else:
            caAo = caAo - (duoc - mat)
        soLanVot += 1

    return soLanVot

def cach_2(duoc, mat, caAo):
    moiLanBat = duoc - mat
    soCaConSauMoiLanBat = caAo - mat 
    soLanVot = (soCaConSauMoiLanBat // moiLanBat) + ( (soCaConSauMoiLanBat % moiLanBat) > 0)
    return soLanVot

def cach_3(duoc, mat, caAo):
    if (caAo-duoc)% (duoc-mat) !=0:
        d = (caAo-duoc)//(duoc-mat) + 2
    else:
        d = (caAo-duoc)//(duoc-mat) + 1
    
    return d

print(cach_2(duoc, mat, caAo))