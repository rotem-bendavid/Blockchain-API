import api.modules.api, math

#find the TS's block height or last block height before TS
def FindLastBlockBeforeTS (ts):
    firstBlock = 0
    lastBlock = api.modules.api.LatestBlockHeight()

    #edge cases
    if (api.modules.api.GetTS(firstBlock) > ts):
        return 'None'
    if (api.modules.api.GetTS(lastBlock) <= ts):
        return lastBlock

    #find the right digit of TS's block heigt for each digit, uses binary search
    blockHeight = 0
    lastBlockDigitLength = int(math.log10(lastBlock)+1)
    for i in reversed(range(lastBlockDigitLength)):
        val = binarySearch(i,blockHeight,ts)
        blockHeight += int(val*math.pow(10,i))
    return int(blockHeight)

#find k that TS's block height is between k*math.pow(10,i) to (k+1)*math.pow(10,i)
def binarySearch(i,blockHeight,ts):
    low = 0
    high = 9
    while (low < high):
        #searches in range of low index and low index+1
        lowHeight = CalculateIndex(blockHeight,low,i)
        lowPlusOneHeight = CalculateIndex(blockHeight,low+1,i)
        if (IsInRange(lowHeight,lowPlusOneHeight,ts)):
            return low

        #searches in range of high index and high index+1
        highHeight = CalculateIndex(blockHeight,high,i)
        highPlusOneHeight = CalculateIndex(blockHeight,high+1,i)
        if (IsInRange(highHeight,highPlusOneHeight,ts)):
            return high

        #cuts search range in half to first or second half
        middle = math.floor((low+high)/2)
        middleHeight = CalculateIndex(blockHeight,middle,i)
        if (api.modules.api.GetTS(middleHeight) > ts):
                high=middle
                low += 1
        else:
            low=middle
            high -= 1

#calculate block height with given params (for creating range)
def CalculateIndex (blockHeight,num,i):
    return int(blockHeight+(num*math.pow(10,i)))

#returns if TS is in range of two block heights
def IsInRange(height,heightPlusOne,ts):
    if (api.modules.api.GetTS(height) <= ts and api.modules.api.GetTS(heightPlusOne) > ts):
        return True
    return False