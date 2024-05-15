def solution(dirs):
    answer = 0
    dir_map = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    x, y = 5, 5
    visited_path = set()

    for way in dirs :
        nx, ny = x + dir_map[way][0], y + dir_map[way][1]
        if 0 <= nx < 11 and 0 <= ny < 11 :
            path_1 = (x, y, nx, ny)
            path_2 = (nx, ny, x, y) 
            if path_1 not in visited_path : 
                visited_path.add(path_1)
                visited_path.add(path_2)
                answer += 1
            x, y = nx, ny
        

    return answer