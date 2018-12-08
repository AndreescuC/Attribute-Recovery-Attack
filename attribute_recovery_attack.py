def compute_cooccurrence_matrix(tokens):
    return []


def compute_container(tokens, co_matrix):
    return []


def generate_subsets(set):
    return []


def compute_occurrences(set):
    pass


def compute_max_corelation(set):
    pass


def cardinal(entity):
    pass


def ceva(subsets, attributes, R, G, n):
    for subset in subsets:
        if compute_occurrences(subset) == n and compute_max_corelation(subset) == 0:
            for attribute in attributes:
                if cardinal(subset) != cardinal(attribute):
                    continue
                G[attribute] = G[attribute] | subset
                R = R | G[attribute]
                attributes = attributes.difference({attribute})
                print('Possible solution for cardinality %d is:' % cardinal(a))
                print(G[attribute])
                return


def attribute_recovery_attack(tokens, attributes, n):
    R = set()
    co_matrix = compute_cooccurrence_matrix(tokens)
    L = compute_container(tokens, co_matrix)
    sorted(L, key=lambda q: len(q))
    G = {k: set() for k in attributes}

    l = len(L)
    index = 0
    while index < l and attributes:
        L[index] = L[index].difference(R)
        subsets = generate_subsets(L[index])
        ceva(subsets, attributes, R, G, n)
        index += 1
    return R


def main():
    tokens = []
    attribute_recovery_attack(tokens)


if __name__ == '__main__':
    main()
