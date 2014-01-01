import requests


class leagueoflegends:
	def __init__(self, apiKey):
		self.apiKey = apiKey
		return

	def genStandardDict(self):
		thisDict = {
			'api_key': self.apiKey
		}
		return thisDict

	def updateApiKey(self, apiKey):
		self.apiKey = apiKey
		return True

	def champion(self, region, freeToPlay=False):
		getParams = self.genStandardDict()
		if freeToPlay != False:
			getParams["freeToPlay"] = freeToPlay
		return requests.get("http://prod.api.pvp.net/api/lol/%s/v1.1/champion" % region, params=getParams)

	def game(self, region, summonerId, version="1.1"):
		getParams = self.genStandardDict()
		return requests.get("http://prod.api.pvp.net/api/lol/%s/v%s/game/by-summoner/%d/recent" % (region, version, summonerId), params=getParams)


	def league(self, region, summonerId, version="2.1"):
		getParams = self.genStandardDict()
		return requests.get("http://prod.api.pvp.net/api/%s/v%s/league/by-summoner/%d" % (region, version, summonerId), params=getParams)

	def stats_summary(self, region, summonerId, version="1.1", season=""):
		getParams = self.genStandardDict()
		if season != "":
			getParams["season"] = season
		return requests.get("http://prod.api.pvp.net/api/lol/%s/v%s/stats/by-summoner/%d/summary" % (region, version, summonerId), params=getParams)

	def stats_ranked(self, region, summonerId, version="1.1", season=""):
		getParams = self.genStandardDict()
		if season != "":
			getParams["season"] = season
		return requests.get("http://prod.api.pvp.net/api/lol/%s/v%s/stats/by-summoner/%d/ranked" % (region, version, summonerId), params=getParams)

	def summoner_masteries(self, region, summonerId, version="1.1"):
		getParams = self.genStandardDict()
		return requests.get("http://prod.api.pvp.net/api/lol/%s/v%s/summoner/%d/masteries" % (region, version, summonerId), params=getParams)

	def summmoner_runes(self, region, summonerId, version="1.1"):
		getParams = self.genStandardDict()
		return requests.get("http://prod.api.pvp.net/api/lol/%s/v%s/summoner/%d/runes" % (region, version, summonerId), params=getParams)

	def summoner_by_name(self, region, summonerName, version="1.1"):
		getParams = self.genStandardDict()
		return requests.get("http://prod.api.pvp.net/api/lol/%s/v%s/summoner/by-name/%s" % (region, version, summonerName), params=getParams)

	def summoner_by_id(self, region, summonerId, version="1.1"):
		getParams = self.genStandardDict()
		return requests.get("http://prod.api.pvp.net/api/lol/%s/v%s/summoner/%d" % (region, version, summonerId), params=getParams)

	def summoner_by_ids(self, region, summonerId, version="1.1"):
		getParams = self.genStandardDict()
		return requests.get("http://prod.api.pvp.net/api/lol/%s/v%s/summoner/%s/name" % (region, version, summonerId), params=getParams)

	def team(self, region, summonerId, version="1.1"):
		getParams = self.genStandardDict()
		return requests.get("http://prod.api.pvp.net/api/%s/v%s/team/by-summoner/%d" % (region, version, summonerId))