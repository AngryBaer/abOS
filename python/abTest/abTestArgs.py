



def return_tuples():
    return 'one', 'two', 'three'


def take_tuples(*args):
    print(args)



if __name__ == '__main__':
    print(return_tuples())
    take_tuples(return_tuples())



