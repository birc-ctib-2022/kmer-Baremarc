"""Computing kmers of a string."""


def kmer(x: str, k: int) -> list[str]:
    """
    Computer all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

    FIXME: do you want more tests here?
    """
    ...
    kmer_list=[x[i:i+k] for i in range(0,len(x),k)]

    return kmer_list


def unique_kmers(x: str, k: int) -> list[str]:
    """
    Computer all unique k-mers of x.

    FIXME: do you want more tests here?
    """
    ...
    all_kmers=kmer(x,k)
    kmers=[]
    for i in all_kmers:
        if i not in kmers:
            kmers.append(i)
        
    return kmers
        

def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    Computer all k-mers of x and count how often they appear.

    FIXME: do you want more tests here?
    """
    ...
    # first we need to count the amount of occurences of the key and then apply the value after by using insert.
    the_kmers=kmer(x,k)
    countings=[]
    for numbers in the_kmers:
        countings.append(the_kmers.count(numbers))
    i=0
    while the_kmers:
        the_kmers.insert(i,countings[i])
        i+=1

    return the_kmers

print(count_kmers('agtagtcg', 3))

