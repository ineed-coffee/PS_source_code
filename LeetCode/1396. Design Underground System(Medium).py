class UndergroundSystem:

    def __init__(self):
        self.travelers={}
        self.routes={}
        

    def checkIn(self, id_: int, stationName: str, t: int) -> None:
        self.travelers[id_]=(stationName,t)

    def checkOut(self, id_: int, stationName: str, t: int) -> None:
        start_s,start_t=self.travelers[id_]
        self.travelers[id_]=[]
        if not self.routes.get((start_s,stationName),0):
            self.routes[(start_s,stationName)]=[1,t-start_t]
        else:
            self.routes[(start_s,stationName)][0]+=1
            self.routes[(start_s,stationName)][1]+=(t-start_t)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if not self.routes.get((startStation,endStation),0):
            return 0
        cnt,times=self.routes[(startStation,endStation)]
        return times/cnt
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
