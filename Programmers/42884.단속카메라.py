def solution(routes):
    routes.sort(key=lambda x:x[1])
    cctv=set()
    for route in routes:
        if any([ True for point in cctv if point>=route[0]]):
            continue
        cctv.add(route[1])
    return len(cctv)
