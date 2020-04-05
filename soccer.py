# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 19:08:28 2019

@author: MabuXayda
"""

import pandas as pd

_path = "F:/temp/soccer/soccer"

_path_Match = "MAtch.csv"
_path_Team = "MAtch.csv"
_path_Player = "MAtch.csv"
_path_Team_att = "MAtch.csv"
_path_Player_att = "MAtch.csv"

print(_path_Match)

match = pd.read_csv(_path + "/Match.csv", sep="\t")
country = pd.read_csv(_path + "/Country.csv", sep="\t")
country.columns = ["country_id", "country"]
match = pd.merge(country, match, on="country_id", how="right")

#league = pd.read_csv(_path + "/League.csv", sep="\t")
#league.columns = ["league_id", "country_id", "league"]
#match = pd.merge(league[["league_id", "league"]],
#                 match, on="league_id", how="right")
col = []
for i in range(1, 12):
    col.append("home_player_{}".format(i))

temp = match.sample(1000)

temp_m = pd.melt(temp, id_vars="home_team_api_id", value_vars=col, value_name="player_id")
temp_m2 = temp_m.groupby("home_team_api_id")["player_id"].value_counts().reset_index(name="count")
.reset_index(name="count")
temp_m3 = temp_m2.groupby(level=[0,1]).nlargest(2)
temp_m3 = temp_m2.groupby(["home_team_api_id", "player_id"]).nlargest(7)
    
def gen_KQ(temp):
    temp["KQ"] = "draw"
    temp.loc[temp["home_team_goal"] > temp["away_team_goal"], "KQ"] = "home_win"
    temp.loc[temp["home_team_goal"] < temp["away_team_goal"], "KQ"] = "home_lose"
    return temp
match = gen_KQ(match)
    
match["KQ"].value_counts()

sample = match.sample(1000)
sample = pd.merge(team[["home_team_api_id", "home_team"]], sample, on="home_team_api_id", how="right")
sample = pd.merge(team[["away_team_api_id", "away_team"]], sample, on="away_team_api_id", how="right")
sample.drop(["home_team_api_id", "away_team_api_id"], axis=1)

#%%
sample = match.sample(1000)
col_select = []
for i in range(1, 12):
    col_select.append("home_player_X{}".format(i))
    col_select.append("home_player_Y{}".format(i))
    col_select.append("away_player_X{}".format(i))
    col_select.append("away_player_Y{}".format(i))

match.drop(col_select, axis=1, inplace=True)

check = sample[col_select]
check.columns = check.columns.str.replace("home_player_", "")


#%%
player = pd.read_csv(_path + "/Player.csv", sep="\t")
player_att = pd.read_csv(_path + "/Player_Attributes.csv", sep="\t")
player_all = pd.merge(player, player_att, on="player_api_id", how="outer")

list_p = ["156546" , "45481" , "101586" , "292773" , "40662" , "10880" , "112471" , "171786" , "172346" , "25551" , "252969"]

from datetime import datetime
#import math

att_p = player_att[player_att["player_api_id"].isin(list_p)]
att_p["date"] = pd.to_datetime(att_p["date"], format="%Y-%m-%d")
att_p["diff_date"] = abs((att_p["date"] - datetime(2015, 1, 10)).dt.days)
att_p = att_p.sort_values("diff_date").drop_duplicates("player_api_id", keep="first")

mess = player_all[player_all["player_name"].str.contains("Messi")]
del(mess[["id_x", "id_y"]])

#%%
team = pd.read_csv(_path + "/Team.csv", sep="\t", encoding="latin-1")
#team.rename(columns={"team_api_id":"home_team_api_id",
#                     "team_long_name":"home_team"}, inplace=True)
team.rename(columns={"team_api_id":"away_team_api_id",
                     "team_long_name":"away_team"}, inplace=True)



team["team_long_name"].nunique()
dup = team[team["team_long_name"].duplicated(keep=False)]
team["team_long_name"].nunique()

team_att = pd.read_csv(_path + "/Team_Attributes.csv", sep="\t")

#%%
sample = player_all.sample(1000)
