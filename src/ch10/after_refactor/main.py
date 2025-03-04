from sets import Set, PersistentSet, PersistentObject, MemberContainer
from sets import T


def print_set(container_list: MemberContainer):
    for i in container_list:
        print(i)


def main() -> None:
    bs = Set[int]([1,2,3,4], 4)
    us = Set[str](['a', 'b', 'c'])
    ps = PersistentSet([PersistentObject(), PersistentObject()])
    print_set(bs)
    print("-----------")
    print_set(us)
    print("-----------")
    print_set(ps)



if __name__ == "__main__":
    main()