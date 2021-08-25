# DES_Encryption_python
a python implementation of the Data Encryption Standard algorithm

The Data Encryption Standard (DES) is a symmetric-key block cipher published by the National Institute of Standards and Technology (NIST).
DES is an implementation of a Feistel Cipher. It uses 16 round Feistel structure. The block size is 64-bit. Though, key length is 64-bit, DES has an effective key length of 56 bits, since 8 of the 64 bits of the key are not used by the encryption algorithm (function as check bits only).

Since DES is based on the Feistel Cipher, all that is required to specify DES is :
  1. Round function
  2. Key schedule
  3. Any additional processing − Initial and final permutation

Round Function :

The heart of this cipher is the DES function, f. The DES function applies a 48-bit key to the rightmost 32 bits to produce a 32-bit output.

![Image of Yaktocat](https://github.com/noubhanidata/DES_Encryption_python/blob/d5e293cb08b3e98345a7031b8ae40574a5986904/images/round_function.jpg)

Key Generation : 

The round-key generator creates sixteen 48-bit keys out of a 56-bit cipher key. The process of key generation is depicted as 
![Image of Yaktocat](https://github.com/noubhanidata/DES_Encryption_python/blob/d5e293cb08b3e98345a7031b8ae40574a5986904/images/key_generation.jpg)

