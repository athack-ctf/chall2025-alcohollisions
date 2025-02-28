import hashlib

with open("easterlabel.jpg", "rb") as f1:#rb=reading bytes
    # c1 = collision1
    c1 = bytearray(f1.read())#to write line 19
    original_md5_hash = hashlib.md5(c1).hexdigest() #hexdigest gives u string
    original_sha256_hash = hashlib.sha256(c1).hexdigest()
    print(f'{"md5":.<20}{original_md5_hash:>20}')
    print(f'{"sha256":.<20}{original_sha256_hash:>20}')

    # g1 = guess1 (assuming it's coll1 and looking for coll2)
    g1 = c1.copy()
    g1_size = len(g1)
    g1_block_start = g1_size - 128

    # Increment the 10th, and decrement the 74th byte of the "garbage" block
    g1[g1_block_start + 10 - 1] += 1
    g1[g1_block_start + 64 + 10 - 1] -= 1

    g1_md5 = hashlib.md5(g1).hexdigest()
    g1_sha256 = hashlib.sha256(g1).hexdigest()

    # g2 = guess2 (assuming it's coll2 and looking for coll1)
    g2 = c1.copy()
    g2_size = len(g2)
    g2_block_start = g2_size - 128

    # Increment the 10th, and decrement the 74th byte of the "garbage" block
    g2[g2_block_start + 10 - 1] -= 1
    g2[g2_block_start + 64 + 10 - 1] += 1

    g2_md5 = hashlib.md5(g2).hexdigest()
    g2_sha256 = hashlib.sha256(g2).hexdigest()

    if original_md5_hash == g1_md5:
        # We were given coll1, got collision2
        print("Had coll1, given coll2. Label found with:")
        print(f'{"md5":.<20}{g1_md5:>20}')
        print(f'{"sha256":.<20}{g1_sha256:>20}')
        with open("guess.jpg", "wb+") as f:
            f.write(g1)
        raise SystemExit(0)
    elif original_md5_hash == g2_md5:
        # We were given coll2, got collision1
        print("Had coll2, given coll1. Label found with:")
        print(f'{"md5":.<20}{g2_md5:>20}')
        print(f'{"sha256":.<20}{g2_sha256:>20}')
        with open("guess.jpg", "wb+") as f:
            f.write(g2)
        raise SystemExit(0)
    else:
        print("HUH?!")
        raise SystemExit(1)