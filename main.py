#### Fonction secondaire
"""
verifie si la chaine p est un palindrome
"""

TABLE=str.maketrans(
    "àâéèêëîïôùûüç",
    "aaeeeeiiouuuc"
    )

def alpha(p):
    """
    nettoye la chaine p
    """
    p=p.lower()
    test=p.translate(TABLE)
    b=""
    for c in test:
        if (c.isalpha() or c.isnumeric()):
            b+=c
    return b

def ispalindrome(p):
    """
    verifie si la chaine p est un palindrome
    """
    p =alpha(p)
    if len(p)==1:
        return True
    if p == "":
        return True
    if p[0]==p[-1]:
        return ispalindrome(p[1:-1])
    return False

#### Fonction principale


def main():
    """
    main
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        nettoye = alpha(s)
        print(s, ispalindrome(nettoye))


if __name__ == "__main__":
    main()
