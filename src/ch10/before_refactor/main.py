from sets import Set, BoundedSet, UnboundedSet, PersistentSet, PersistentObject
from sets import T


def print_set(container_list: Set):
    for i in container_list:
        print(i)


def main() -> None:
    bs = BoundedSet[int]([1,2,3,4], 4)
    us = UnboundedSet[str](['a', 'b', 'c'])
    ps = PersistentSet([PersistentObject(), PersistentObject()])
    print_set(bs)
    print("-----------")
    print_set(us)
    print("-----------")
    print_set(ps)



if __name__ == "__main__":
    main()