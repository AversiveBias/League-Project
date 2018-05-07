import requests
import matplotlib.pyplot as py
'''
def requestSummonerData(region, summonerName, APIKey):

    #Here is how I make my URL.  There are many ways to create these.
    
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.4/summoner/by-name/" + summonerName + "?api_key=" + APIKey
    print(URL)
    #requests.get is a function given to us my our import "requests". It basically goes to the URL we made and gives us back a JSON.
    response = requests.get(URL)
    #Here I return the JSON we just got.
    return response.json()

def requestRankedData(region, ID, APIKey):
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.5/league/by-summoner/" + ID + "/entry?api_key=" + APIKey
    print(URL)
    response = requests.get(URL)
    return response.json()
    

def main():
    print("\nWhat up homie. Enter your region to get started")
    print("Type in one of the following regions or else the program wont work correctly:\n")
    print("NA or EUW (Note: You can add more regions by just changing up the URL!\n")

    #I first ask the user for three things, their region, summoner name, and API Key.
    #These are the only three things I need from them in order to get create my URL and grab their ID.

    region = str(input('Type in one of the regions above: '))
    summonerName = str(input('Type your Summoner Name here and DO NOT INCLUDE ANY SPACES: '))
    APIKey = str(input('Copy and paste your API Key here: '))

    #I send these three pieces off to my requestData function which will create the URL and give me back a JSON that has the ID for that specific summoner.
    #Once again, what requestData returns is a JSON.
    responseJSON  = requestSummonerData(region, summonerName, APIKey)
    
    ID = responseJSON[summonerName]['id']
    ID = str(ID)
    print(ID)
    responseJSON2 = requestRankedData(region, ID, APIKey)
    print (responseJSON2[ID][0]['tier'])
    print (responseJSON2[ID][0]['entries'][0]['division'])
    print (responseJSON2[ID][0]['entries'][0]['leaguePoints'])
main()
'''
#https://developer.riotgames.com/           go get your api key!
def requestSummonerData(region,summonerName,APIKey):
    URL = "https://"+region+".api.riotgames.com/lol/summoner/v3/summoners/by-name/"+summonerName+"?api_key="+APIKey
    response = requests.get(URL)
    return response.json()
def requestRankedData(region,summonerID,APIKey):
    URL = "https://"+region+".api.riotgames.com/lol/league/v3/positions/by-summoner/"+summonerID+"?api_key="+APIKey
    response = requests.get(URL)
    return response.json()
def printRankedData(region,summonerID,APIKey):
    rankedData = requestRankedData(region,summonerID,APIKey)
    print("XXXXXXXXXXXXXXXXXXXXXXXXX")
    for queue in rankedData:
        queueType = queue["queueType"]
        leagueName = queue["leagueName"]
        tier = queue["tier"]
        rank = queue["rank"]
        LP = str(queue["leaguePoints"])
        print(queueType)
        print(leagueName)
        print(tier+" "+rank+" "+LP+" LP")
        print("----------------------------")
def findSummonerProfile(region):
    summonerName = str(input("Enter summoner name"))
    while(summonerName is not ""):
        #APIKey=str(input("Enter API Key"))
        APIKey = "RGAPI-ee3f9db5-c1ea-4ca8-abfa-fcebca43bdc7"
        summonerInfo = requestSummonerData(region,summonerName,APIKey)
        print("Summoner Info: ",summonerInfo)
        summonerID = str(summonerInfo['id'])
        print("ID: ",summonerID)
        printRankedData(region,summonerID,APIKey)
        summonerName = str(input("Enter summoner name"))

def requestChampion(region):        #Something's wrong with this
    championID="420"
    print(region)
    URL="https://na1.api.riotgames.com/lol/static-data/v3/champions/"+championID+"?locale=en_US&api_key=RGAPI-2068e824-434d-4cd8-93d2-6bdd1fc4bb8c"
    response = requests.get(URL)
    data=response.json()
    print(data)




def getRegion():
    region=str(input("Enter region(NA, JP, BR, OC, EUN, EUW, TR, LA, RU, KR)"))
    region = region.upper()
    if (region =="NA" or region == "JP" or region == "BR" or region =="OC" or region == "EUN" or region == "EUW" or region == "TR"):
        region+="1"
    return region


region=getRegion().lower()
#requestChampion(region)
#region=getRegion().lower()
findSummonerProfile(region)
