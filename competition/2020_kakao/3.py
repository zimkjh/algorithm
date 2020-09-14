def getScore(info):
    return int(info.split()[-1])


def solution(info, query):
    answer = []
    for q in query:
        tempAnswer = 0
        lang, job, period, soulNscore = q.split(" and ")
        soul, score = soulNscore.split()
        score = int(score)
        for i in info:
            if score > getScore(i):
                continue
            if lang != "-" and lang not in i:
                continue
            if job != "-" and job not in i:
                continue
            if period != "-" and period not in i:
                continue
            if soul != "-" and soul not in i:
                continue
            tempAnswer += 1
        answer.append(tempAnswer)
    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]
print(solution(info, query))
# 3시 (효율성 다 시간초과)

