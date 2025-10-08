from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# --- 1. Key Generation ---
# Generate a 2048-bit RSA key pair.
key = RSA.generate(2048)

# Extract the private key.
# It contains both the private and public components.
private_key = key.export_key()
print(private_key)
# print(privateKey)
private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAn2TzOLg8XPyJzdNfD4uiUOgRdCNVgZi16/taiGquXfOI5sax
V/Sg1lyVC2b+lRzGFFBUVawRVKiASH14j0PXga3M8d+sEl0ZfnGcnutlJrXTRysh
xhh8pUQ1jZpWNEV0TpkEtlM6ceY/V5JSAgFjh6mW6+yNOjjoqrxf/SfTwbhmsXTY
lbg5Y7rW1UOm+RbrzVWCO/y6FJgzZyKee7yi2SseFJdgVy7Swc9ZdamPSgKdONpn
ml8BldF1fwVc5IMveST6PdiYiMvXzFf6VFkjuu+3/Urn1XchUMx7SXPSqFs7ZF5A
xcqp14HMI+bIDq0NwTI7Uyy88i/zUZiVX80SeQIDAQABAoIBAEeY0t/BcevazBOW
RHb5I9nvxBdE392suNrdNtdcBCLTh8URrwtxKOXhBFnw054rJJZvVtJ8zfQXFDh7
k7HWqXDonsxuyh4dj5wKcG26Et+GgPbQ2wTebu7VarDGiL5GDG5ZsZIsZG5RHFa7
tPaNpSWE+fPTd8SVV32JzBwszaOP+ZwSwYz3WUNwW2qZibd+CN7Y4f4ZMtLLHoGg
EOMg/dcwGMYy+U9W+zSH9pkR4a3duFEQU8TBsvmaCPgMkPrd8AAXQVl4dOWUAksS
XZMGGb1cHoo07SRDZ6jFWCm4QcgDdc9o3GumZrQuxB0g2ilospGctI8aNCD+mqSU
yTuCjhkCgYEAxY+ch2bZn6WP+So9cfXdcDqKLval4rcnCmn9jerai0jgUXkEaz1z
x/cgohNByGketdX0T6ZQvG/NeuGxB9ULE56bEqW9XwXHGIajS5iwVRJvdp/A4RI/
HQoftpaPZtcMzoO2sl1pWVBTi/TUxDPP0UBDqbrezOzMJvnOhKzaKccCgYEAzosn
P1uzFSK77d6aIJ6g6aSN2lmJ95fmD6Q6uzXr6Q34iHqQt9L1RHguBP+B7bxIx1ex
Q+30osu0eRMZFaKMqL/8oV/X5ShuO9PvkWE9GzmA3WziTIfn2vwaxIhzcaRIpwxA
a5nWVABgSUxnMTZXWWPOSWr0okQnJ11pfIMw4b8CgYEAqtsGfjs+nkjq+IvFVBdU
CMk31GHPGQFYrDL565BerPK7vPoyDiS5Swi4mjKZQ59VxeBhR7kIPc9bH5isJ5/h
0nfqmPfpjJJMmzNlae2FIi2tZCPJBV1oY87rmlcfccst8jQK/rq2b11+w51bnMtK
QSeY3OMV6Jgp/tMv/aIXkuUCgYEAslfrmsTGfJCSb1HQCiyOy1AggJLiE92gdI8d
e3uS6Zj7qnUSsvfAes+/BOfPPAVhXmd1FC/LFisI+aao+UpzZF7qeDl3BVOE47ob
2Y96ISDlCc00Flsfs7IONvePn2f4p+1nTsH2FHCCs6f6Tr8aa4BHppNpCxgIKvB4
3l+1fKcCgYByiAU0iVY9CMqCl/FAQBwOnoPthL3zQKtPJZQmna5pXckx71+xoC0+
7JOFIEsGWseI5zMgLwyYjbPBkKHchuMM/9t8mNsfbvKTJnU2zR2QQR8f/i59+RB5
cBR/ySCC1CJmhFaL4Sj5COlAlAmmZu4jzUOcxl1UQLYF+8oO2dMhog==
-----END RSA PRIVATE KEY-----"""


public_key = key.publickey().export_key()
print(public_key)
public_key = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAppNAjM6uSx/rydKGK2ns
6wE5eR0wxQS6juTWUOTyuU3I7BGplRov1ru4mOgiWjLT1Ju7KVKKa+hmQQL6Mbha
w6bF0Dq0rtDw4Yg8e4Y3/mXsczRjTaKO1CnXwOOm67h7Psl7SAzByklGMBpspJK9
/u2F1CFMwH4978mzE8CjeGZxhWHeLCA6MGf5Y5K0/c24myTUAE9n4xJYr/Yi8DLQ
jLfgv+WQboagy5/KCfZ0zxjmkI5wq6bYOC0FJc6Mnvx8Q1r2PsL0vfN7dAihiSs2
q7lazKSsySibKvwhNMrnmoyAAqmTdCbPsKq9Zn/Wcf573T96jpT85PQqN7bE8PFD
5QIDAQAB
-----END PUBLIC KEY-----
"""
print(public_key)
