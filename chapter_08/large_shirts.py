def make_shirt(size='large', message='I love py!'):
    """概述要制作的T恤什么样。"""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')


make_shirt()
make_shirt(size='medium')
make_shirt('small', 'programmers')
