from datetime import timedelta


def toTime(string):
    h, m, s = map(int, string.split(":"))
    return timedelta(hours=h, minutes=m, seconds=s)


def toAnswer(time):
    time = str(time)
    h, m, s = time.split(":")
    if len(h) == 1:
        h = "0" + h
    if len(m) == 1:
        m = "0" + m
    if len(s) == 1:
        s = "0" + s
    return h + ":" + m + ":" + s


def solution(play_time, adv_time, logs):
    logs = sorted(logs)
    play_time = toTime(play_time)
    adv_time = toTime(adv_time)
    answerTime = 0
    answerL = [[timedelta(0), min(adv_time, play_time), timedelta(0)]]
    maxTime = timedelta(0)

    for log in logs:
        startTime, endTime = map(toTime, log.split("-"))
        nowAnswerL = []
        index = 0
        while index < len(answerL):
            if answerL[index][1] > startTime:
                durationTime = min(answerL[index][1], endTime) - startTime
                answerL[index][2] += durationTime
                maxTime = max(maxTime, answerL[index][2])
            # max 아닌애들 버리기 (이미 다 더한 애들 중)
            elif answerL[index][2] < maxTime:
                del answerL[index]
                index -= 1
            index += 1

        nowAnswerL.append(startTime)
        nowAnswerL.append(startTime + adv_time)
        nowAnswerL.append(min(startTime + adv_time, endTime) - startTime)
        maxTime = max(maxTime, nowAnswerL[2])
        answerL.append(nowAnswerL)
    print(answerL)
    for answer in answerL:
        if answer[2] == maxTime:
            return toAnswer(answer[0])
    # return toAnswer(answerTime)


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play_time, adv_time, logs))

# play_time = "99:59:59"
# adv_time = "25:00:00"
# logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
# print(solution(play_time, adv_time, logs))

# 실패 + 시간초과 (6/31)

