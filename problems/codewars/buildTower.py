def tower_builder(n_floors):
    '''
    https://www.codewars.com/kata/576757b1df89ecf5bd00073b
    '''

    tower = []
    
    max_size = (n_floors - 1) * 2 + 1
    
    for i in range(n_floors):
        stars = 2 * i + 1
        spaces = (max_size - stars) // 2
        
        floor = ' ' * spaces
        floor += '*' * stars
        floor += ' ' * spaces
        
        tower.append(floor)
        
    return tower