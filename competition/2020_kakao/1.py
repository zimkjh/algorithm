import re


def step3(st):
    while True:
        new_st = st.replace("..", ".")
        if new_st == st:
            return new_st
        st = new_st


def step4(st):
    if st[0] == ".":
        st = st[1:]
    if st == "":
        return st
    if st[-1] == ".":
        st = st[:-1]
    return st


def step5(st):
    if st == "":
        return "a"
    return st


def step6(st):
    if len(st) > 15:
        st = st[:15]
    if st[-1] == ".":
        st = st[:-1]
    return st


def step7(st):
    if len(st) <= 2:
        while len(st) < 3:
            st += st[-1]
    return st


def solution(new_id):
    new_id = new_id.lower()
    new_id = "".join(re.findall("[a-z0-9\-_.]", new_id))
    new_id = step3(new_id)
    new_id = step4(new_id)
    new_id = step5(new_id)
    new_id = step6(new_id)
    new_id = step7(new_id)
    return new_id


print(solution("=.="))

## 2시 20분
