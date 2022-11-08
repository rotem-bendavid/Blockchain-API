import requests, json

#returns latest block height
def LatestBlockHeight():
    latest_block_url = "https://blockchain.info/latestblock"
    response = requests.get(latest_block_url)
    if (response.status_code != 404):
        latest_block = response.json()
        return(latest_block['height'])

#gets block height and returns it's TS
def GetTS(blockHeight):
    block_url = "https://blockchain.info/block-height/"+str(blockHeight)+"?format=json"
    response = requests.get(block_url)
    if (response.status_code != 404):
        block = response.json()
        if (block['blocks'] == []):
            return GetTS(LatestBlockHeight())
        return block['blocks'][0]['time']
