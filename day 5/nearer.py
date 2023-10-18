"""Nearer"""

def near(alice, bob, ice):
    """-"""
    alice_ice = abs(ice - alice)
    bob_ice = abs(ice - bob)
    if alice_ice > bob_ice:
        print("Bob %d" % bob_ice)
    elif alice_ice < bob_ice:
        print("Alice %d" % alice_ice)
    else:
        print("Sundaes %d" % min(bob_ice, alice_ice))
near(int(input()), int(input()), int(input()))
