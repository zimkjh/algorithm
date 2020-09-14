import re
def getScore(info):
    return int(info.split()[-1])


def solution(info, query):
    # info 정리
    infoD = {}
    for i in info:
        nowI = i.split()
        score = int(nowI[-1])
        keyInfo = " ".join(nowI[:-1])
        if keyInfo in infoD:
            infoD[keyInfo] += [score]
        else:
            infoD[keyInfo] = [score]
    for key in infoD:
        infoD[key] = sorted(infoD[key])

    answer = []
    for q in query:
        tempAnswer = 0
        lang, job, period, soulNscore = q.split(" and ")
        soul, score = soulNscore.split()
        score = int(score)
        regexStr = ""
        if lang == "-":
            regexStr += ".+ "
        else:
            regexStr += (lang + " ")
        if job == "-":
            regexStr += ".+ "
        else:
            regexStr += (job + " ")
        if period == "-":
            regexStr += ".+ "
        else:
            regexStr += (period + " ")
        if soul == "-":
            regexStr += ".+"
        else:
            regexStr += soul

        # dict와 비교
        for key in infoD:
            if re.search(regexStr, key):
                tempAnswer += len([x for x in infoD[key] if x >= score])
        answer.append(tempAnswer)
    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
# query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
#          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
#          "- and - and - and - 150"]
query = ["- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]
print(solution(info, query))
# 3시 (효율성 다 시간초과)

