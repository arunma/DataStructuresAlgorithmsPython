from typing import List


class MakingFileNamesUnique:
    def getFolderNames(self, names: List[str]) -> List[str]:
        name_cnt = {}
        result = []
        for name in names:
            if name in name_cnt:
                count = name_cnt[name]
                curr_count = count + 1
                name_cnt[name] = curr_count
                out_name = "{}({})".format(name, curr_count)
                name_cnt[out_name] = 0
                result.append(out_name)
            elif '(' in name and name[:name.rindex('(')] in name_cnt:
                count = int(name[name.rindex('(') + 1:name.rindex(')')])
                name_cnt[name] = 0
                name_cnt[name[:name.rindex('(')]] = count
                result.append(name)
            elif name not in name_cnt:
                name_cnt[name] = 0
                result.append(name)
        return result


if __name__ == '__main__':
    init = MakingFileNamesUnique()
    print(init.getFolderNames(names=["pes", "fifa", "gta", "pes(2019)"]))
    print(init.getFolderNames(names=["gta", "gta(1)", "gta", "avalon"]))
    print(init.getFolderNames(names=["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]))
    print(init.getFolderNames(names=["wano", "wano", "wano", "wano"]))
    print(init.getFolderNames(names=["kaido", "kaido(1)", "kaido", "kaido(1)"]))
    print(init.getFolderNames(names=["m","t","y(4)","t","a","p","h","h","z","z(2)(2)","x(3)","h(4)(3)","l","z(1)","h","s(1)(2)","y(3)(2)","m(3)","i","h","u","j(1)(4)","q","j(1)","c","n(4)","k","s(1)(4)","p(2)","m","r(1)(4)","k(3)","d(3)(1)","e(4)"]))
                                   #["m","t","y(4)","t(1)","a","p","h","h(1)","z","z(2)(2)","x(3)","h(4)(3)","l","z(1)","h(2)","s(1)(2)","y(3)(2)","m(3)","i","h(3)","u","j(1)(4)","q","j(1)","c","n(4)","k","s(1)(4)","p(2)","m(4)","r(1)(4)","k(3)","d(3)(1)","e(4)"]
                                   #["m","t","y(4)","t(1)","a","p","h","h(1)","z","z(2)(2)","x(3)","h(4)(3)","l","z(1)","h(2)","s(1)(2)","y(3)(2)","m(3)","i","h(3)","u","j(1)(4)","q","j(1)","c","n(4)","k","s(1)(4)","p(2)","m(1)","r(1)(4)","k(3)","d(3)(1)","e(4)"]
    print(init.getFolderNames(names=["kaido", "kaido(1)", "kaido", "kaido(1)",
                                     "kaido(2)"]))  # ["kaido","kaido(1)","kaido(2)","kaido(1)(1)","kaido(2)(1)"]

