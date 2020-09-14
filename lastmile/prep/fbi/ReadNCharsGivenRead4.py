from typing import List


class ReadNCharsGivenRead4:
    def __init__(self):
        self.queue=[]

    def read(self, buf: List[str], n: int) -> int:
        i=0
        while i<n:
            if self.queue:
                buf[i]=self.queue.pop(0)
                i+=1
            else:
                temp=['']*4
                tot_read=read4(temp)
                if tot_read==0:
                    break

                self.queue+=temp
        return i



if __name__ == '__main__':
    init = ReadNCharsGivenRead4()
    print(init.read([], 4))
