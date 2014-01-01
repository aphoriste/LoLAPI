import leagueoflegends

leagueOfLegends = leagueoflegends.leagueoflegends('YOUR-API-KEY')
champions = leagueOfLegends.champion('na').json()
for champion in champions['champions']:
	print champion['name']