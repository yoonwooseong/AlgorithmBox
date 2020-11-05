def solution(p, n):
    hour = 0
    mini = 0
    seco = 0
    if n / 60 < 1:
        seco = n
    elif n / 60 >= 1 and n / 60 < 60:
        mini = n/60
        seco = n % 60
    else:
        hour = int(n/3600)
        mini = int((n % 3600)/60)
        seco = n - (3600*hour) - (60*mini)
    ch = int(p[3:5])
    cm = int(p[6:8])
    cs = int(p[9:11])
    if p[0:2] == "PM":
        ch += 12
    #"%02d" % sec
    rh = ch+hour
    rm = cm+mini
    rs = cs+seco
    if rs/60 > 1:
        rm += 1
    elif rs/60 == 1:
        rm += 1
        rs = 0
    if rm/60 > 1:
        rh += 1
    elif rm/60 == 1:
        rh += 1
        rm = 0
    if rh == 24:
        rh = 0

    print(ch, cm, cs)
    print(hour, mini, seco)
    print(rh, rm, rs)
    print("%02d" % rh + ":"+"%02d" % rm+":"+"%02d" % rs)

    return "%02d" % rh + ":"+"%02d" % rm+":"+"%02d" % rs


solution("PM 01:00:00", 7200)
