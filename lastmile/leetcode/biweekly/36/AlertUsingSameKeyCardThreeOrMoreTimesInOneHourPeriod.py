from collections import defaultdict, Counter
from typing import List


class AlertUsingSameKeyCardThreeOrMoreTimesInOneHourPeriod:
    # def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
    #     timesDict = defaultdict(list)
    #
    #     for i in range(len(keyTime)):
    #         hour, min = keyTime[i].split(":")
    #         timesDict[hour].append(keyName[i])
    #         if min == '00':
    #             timesDict[str(int(hour) - 1)].append(keyName[i])
    #
    #     result = []
    #     for k, v in timesDict.items():
    #         counter = Counter(v)
    #         for ck, cv in counter.items():
    #             if cv >= 3:
    #                 result.append(ck)
    #     return result

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        personDict=defaultdict(list)
        for i in range(len(keyTime)):
            hour, min = keyTime[i].split(":")
            convert=int(hour)*60 + int(min)
            personDict[keyName[i]].append(convert)

        result=[]
        for k,v in personDict.items():
            if len(v)>=3:
                sortv=sorted(v)
                for i in range(len(sortv)-2):
                    if sortv[i+2]-sortv[i]<=60:
                        result.append(k)

        return sorted(set(result))

if __name__ == '__main__':
    init = AlertUsingSameKeyCardThreeOrMoreTimesInOneHourPeriod()
    print(init.alertNames(["daniel","daniel","daniel","luis","luis","luis","luis"], ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]))
    print(init.alertNames(keyName=["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"], keyTime=["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]))
    print(init.alertNames(keyName=["john", "john", "john"], keyTime=["23:58", "23:59", "00:01"]))
    print(init.alertNames(["leslie", "leslie", "leslie", "clare", "clare", "clare", "clare"],
                          ["13:00", "13:20", "14:00", "18:00", "18:51", "19:30", "19:49"]))
