"""Netflix"""

def premium(display, download):
    """419 / pack"""
    need_dis = display // 4
    need_down = download // 4
    if display % 4: #if display % 4 != 0
        need_dis += 1
    if download % 4:
        need_down += 1
    return max(need_dis, need_down)

def standard(display, download):
    """349 / pack"""
    need_dis = display // 2
    need_down = download // 2
    if display % 2:
        need_dis += 1
    if download % 2:
        need_down += 1
    return max(need_dis, need_down)

def basic():
    """279 / pack"""
    return max(need_dis, need_down)

def netflix():
    """-"""
    screen = int(input())
    download = int(input())
    unlimit = input()
    watch = input()
    labtv = input()
    hdava = input()
    ultraava = input()

    ultra = premium(screen, download)
    u_prize = ultra * 419
    hdv = standard(screen, download)
    h_prize = hdv * 349
    lab = basic(screen, download)
    l_prize = lab * 279
    mobile = max(screen, download)
    m_prize = mobile * 99
    
netflix()
