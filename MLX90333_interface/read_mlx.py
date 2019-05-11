import spidev
class mlxSensor:
    def __init__(self,csnum=1,rate=16000,delay=10000,bits=8):
        self.spicom = spidev.SpiDev()
        self.spicom.open(0, csnum)
        self.rate = rate
        self.delay=delay
        self.bits=bits

    def getData(self):
        rdata = self.spicom.xfer([255,255,255,255,255,255,255,255],self.rate,self.delay,self.bits)
        alpha = int((bin(rdata[1])<<8)+bin(rdata[2]))
        beta = int((bin(rdata[3])<<8)+bin(rdata[4]))
        return alpha,beta
if(__name__=="__main__"):
    mymlx = mlxSensor()
    while(True):
        print("alpha {} beta {}".format(mymlx.getData))