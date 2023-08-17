# Check if a point belongs to a secp256k1 curve

# secp256k1 domain parameters
Pcurve = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 -1 # The proven prime
Acurve = 0 # These two defines the elliptic curve. y^2 = x^3 + Acurve * x + Bcurve
Bcurve = 7
Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
GPoint = (int(Gx),int(Gy)) # This is our generator point.
N=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141 # Number of points in the field

left_side = (Gy ** 2) % Pcurve
right_side = ((Gx ** 3) + Acurve + Bcurve) % Pcurve

print("left side:", left_side)

print("right side:", right_side)

if left_side == right_side:
    
    print("Verified!")
