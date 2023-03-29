from world_cup_teams import *
import random

def generate_group_stage(ratings, teams):
  group_stage = []

  #Group stages based on real template from Qatar 2022 WC
  group_A = [ratings["qatar"], ratings["ecuador"], ratings["senegal"], ratings["netherlands"], teams[teams.index("qatar")], teams[teams.index("ecuador")], teams[teams.index("senegal")], teams[teams.index("netherlands")]]
  group_stage.append(group_A)
  group_B = [ratings["england"], ratings["iran"], ratings["usa"], ratings["wales"], teams[teams.index("england")], teams[teams.index("iran")], teams[teams.index("usa")], teams[teams.index("wales")]]
  group_stage.append(group_B)
  group_C = [ratings["argentina"], ratings["saudi arabia"], ratings["mexico"], ratings["poland"], teams[teams.index("argentina")], teams[teams.index("saudi arabia")], teams[teams.index("mexico")], teams[teams.index("poland")]]
  group_stage.append(group_C)
  group_D = [ratings["france"], ratings["australia"], ratings["denmark"], ratings["tunisia"], teams[teams.index("france")], teams[teams.index("australia")], teams[teams.index("denmark")], teams[teams.index("tunisia")]]
  group_stage.append(group_D)
  group_E = [ratings["spain"], ratings["costa rica"], ratings["germany"], ratings["japan"], teams[teams.index("spain")], teams[teams.index("costa rica")], teams[teams.index("germany")], teams[teams.index("japan")]]
  group_stage.append(group_E)
  group_F = [ratings["belgium"], ratings["canada"], ratings["morocco"], ratings["croatia"], teams[teams.index("belgium")], teams[teams.index("canada")], teams[teams.index("morocco")], teams[teams.index("croatia")]]
  group_stage.append(group_F)
  group_G = [ratings["brazil"], ratings["serbia"], ratings["switzerland"], ratings["cameroon"], teams[teams.index("brazil")], teams[teams.index("serbia")], teams[teams.index("switzerland")], teams[teams.index("cameroon")]]
  group_stage.append(group_G)
  group_H =[ratings["portugal"], ratings["ghana"], ratings["uruguay"], ratings["south korea"], teams[teams.index("portugal")], teams[teams.index("ghana")], teams[teams.index("uruguay")], teams[teams.index("south korea")]]
  group_stage.append(group_H)

  return group_stage

#Main function that calculates odds and what team will have a better cahnce of winning. Does this by picking a random float number then compaing it to the odds of a team
def play_match(team1, team2, team1_name, team2_name):
  odds_team1_win = team1 - 69
  odds_team2_win = team2 - 69
  total_odds = odds_team1_win + odds_team2_win
  odds_of_drawing_min = total_odds / 2 - 2
  odds_of_drawing_min = odds_of_drawing_min / total_odds * 100
  odds_of_drawing_max = total_odds / 2 + 2
  odds_of_drawing_max = odds_of_drawing_max / total_odds * 100
  percent_chance_team1_win = odds_team1_win / total_odds * 100
  random_winner = random.uniform(0, 100)
  if random_winner >= odds_of_drawing_min and random_winner <= odds_of_drawing_max:
    winner = [team1_name, team2_name]
  elif random_winner <= percent_chance_team1_win:
    winner = [team1_name]
  else:
    winner = [team2_name]

  return winner

#Calculates points for whatever teams are in that bracket (group stage has 4 teams, rest have 2)
def calculate_points(group, winner):
  if len(winner) == 2:
    for i in winner:
      group[i] += 1
  else:
    for x in winner:
      group[x] += 3

#Finds most points out of a bracket. Used to find out what team will move forward
def find_most_points(group, team_ratings):
  highest_team_points = -1
  highest_team = ""
  for team in group:
    if group[team] > highest_team_points:
      highest_team_points = group[team]
      highest_team = team
    elif group[team] == highest_team_points:
      if team_ratings[team] > team_ratings[highest_team]:
        highest_team_points = group[team]
        highest_team = team
  return highest_team

def generate_next_bracket(round_of_16, team, team_ratings):
  round_of_16.update({team : team_ratings[team]})
  
def generate_round_16_games(all_teams, team):
  list_of_matches = []
  #Winner of Group A vs 2nd Place Group B
  list_of_matches.append([all_teams[team[0]], all_teams[team[3]], team[0], team[3]])
  #Winner of Group B vs 2nd Place Group A
  list_of_matches.append([all_teams[team[1]], all_teams[team[2]], team[1], team[2]])
  #Winner of Group C vs 2nd Place Group D
  list_of_matches.append([all_teams[team[4]], all_teams[team[7]], team[4], team[7]])
  #Winner of Group D vs 2nd Place Group C
  list_of_matches.append([all_teams[team[5]], all_teams[team[6]], team[5], team[6]])
  #Winner of Group E vs 2nd Place Group F
  list_of_matches.append([all_teams[team[8]], all_teams[team[11]], team[8], team[11]])
  #Winner of Group F vs 2nd Place Group E
  list_of_matches.append([all_teams[team[9]], all_teams[team[10]], team[9], team[10]])
  #Winner of Group G vs 2nd Place Group H
  list_of_matches.append([all_teams[team[12]], all_teams[team[15]], team[12], team[15]])
  #Winner of Group H vs 2nd Place Group G
  list_of_matches.append([all_teams[team[13]], all_teams[team[14]], team[13], team[14]])
  
  return list_of_matches

def generate_quarter_final_games(all_teams, team):
  list_of_matches = []
  #Winner of First Game vs Winner of Third Game
  list_of_matches.append([all_teams[team[0]], all_teams[team[2]], team[0], team[2]])
  #Winner of Fifth Game vs Winner of Seventh Game
  list_of_matches.append([all_teams[team[4]], all_teams[team[6]], team[4], team[6]])
  #Winner of Second Game vs Winner of Fourth Game
  list_of_matches.append([all_teams[team[1]], all_teams[team[3]], team[1], team[3]])
  #Winner of Sixth Game vs Winner of Eigth Game
  list_of_matches.append([all_teams[team[5]], all_teams[team[7]], team[5], team[7]])
  
  return list_of_matches

def generate_semi_final_games(all_teams, team):
  list_of_matches = []
  #Winner of Games 1 and 2
  list_of_matches.append([all_teams[team[0]], all_teams[team[1]], team[0], team[1]])
  #Winner of Games 3 and 4
  list_of_matches.append([all_teams[team[2]], all_teams[team[3]], team[2], team[3]])
  
  return list_of_matches

def generate_the_finals(all_teams, team):
  return[[all_teams[team[0]], all_teams[team[1]], team[0], team[1]]]

#Plays through each match using 2 teams and updates that groups dictionary
def play_through_match(bracket, list, dict, team_ratings):
  for match in bracket:
    bracket_points = {
      match[2] : 0,
      match[3] : 0
    }
    winner_of_match = play_match(match[0], match[1], match[2], match[3])
    calculate_points(bracket_points, winner_of_match)
    winner_of_match_team = find_most_points(bracket_points, team_ratings)
    list.append(winner_of_match_team)
    generate_next_bracket(dict, winner_of_match_team, team_ratings)

#Takes a dictionary of odds of all teams winning world cup and one specific team and prints that teams odds
def print_all_team_odds(wc_winner_all_teams, team):
  wc_winner_all_teams[team] /= 100
  print(f"\033[0;34m{team.capitalize()}\033[0m has a \033[1;32m{wc_winner_all_teams[team]}%\033[0m to win the 2022 FIFA World Cup!")
  wc_winner_all_teams[team] *= 100

def check_input(prompt, list_options):
  while True:
    print(prompt)
    #Gets user input in stipped and lower case form
    user_input = input(" ").lower().strip()
    #Checks if input is in the list of valid menu options
    if user_input in list_options:
      #Returns input if it is
      return user_input.lower().strip()
    else:
      #Else the while True runs again
      print("That was not one of the options! Try again")

def check_country(prompt, teams):
  while True:
    print(prompt)
    #Gets user input in stipped and lower case form
    user_input = input(" ").lower().strip()
    #Checks if input is in the list of valid menu options
    if user_input in teams:
      #Returns input if it is
      return user_input.lower().strip()
    else:
      #Else the while True runs again
      print("Sorry, it looks like that is not a country, or they did not qualify for the 2022 World Cup... Try again!")

#Creates graph using square symbols to make a visual graph of most likely players to win
def create_graph(dict, names):
  #3 letter codes for each team in order of team names list as this will make the graph look more even
  three_letter_dict = {
    "BRA" : 0,
    "BEL" : 0,
    "FRA" : 0,
    "ARG" : 0,
    "ENG" : 0,
    "ESP" : 0,
    "NED" : 0,
    "POR" : 0,
    "DEN" : 0,
    "GER" : 0,
    "CRO" : 0,
    "MEX" : 0,
    "URU" : 0,
    "SUI" : 0,
    "USA" : 0,
    "SEN" : 0,
    "WAL" : 0,
    "IRN" : 0,
    "SRB" : 0,
    "MAR" : 0,
    "JPN" : 0,
    "POL" : 0,
    "KOR" : 0,
    "TUN" : 0,
    "CRC" : 0,
    "AUS" : 0,
    "CAN" : 0,
    "CMR" : 0,
    "ECU" : 0,
    "QAT" : 0,
    "KSA" : 0,
    "GHA" : 0
  }
  list_three_letters = []
  for key in three_letter_dict:
    list_three_letters.append(key)
  
  for i in dict:
    three_letter_dict[list_three_letters[names.index(i)]] = dict[i]

  #Prints one box for each "% point" they have of winning
  for x in three_letter_dict:
    #Change the 10 to make the graph bars longer or shorter. Longer is more accurate
    num_of_symbol = int(three_letter_dict[x]) // 10
    print(f"{x}: {'■' * num_of_symbol}")
  print("\n")

#Previous winners of all WC
def previous_winners():
  previous_winners_dict = {
    "2018" : "France",
    "2014" : "Germany",
    "2010" : "Spain",
    "2006" : "Italy",
    "2002" : "Brazil",
    "1998" : "France",
    "1994" : "Brazil",
    "1990" : "Germany",
    "1986" : "Argentina",
    "1982" : "Italy",
    "1978" : "Argentina",
    "1974" : "West Germany",
    "1970" : "Brazil",
    "1966" : "England",
    "1962" : "Brazil",
    "1958" : "Brazil",
    "1954" : "Germany",
    "1950" : "Uruguay",
    "1938" : "Italy",
    "1934" : "Italy",
    "1930" : "Uruguay"
  }

  print(" ")
  #User can see all previous winners or just winner of an inputted year
  if input("View all previous winners [v]\nOr enter anything else to view a certain year").strip().lower() == "v":
    print("\n")
    for year in previous_winners_dict:
      print(f"Winner of \u001b[35m{year}\033[0m World Cup: \033[0;34m{previous_winners_dict[year]}\033[0m")
    print("\n")
      
  else:
    allowed_input = True
    while allowed_input:
      print(" ")
      user_input = input("What year would you like to see the winner for?:\n")
  
      if user_input in previous_winners_dict:
        print(f"\nWinner of \u001b[35m{user_input}\033[0m World Cup: \033[0;34m{previous_winners_dict[user_input]}\033[0m \n")
        allowed_input = False
      else:
        print("Looks like that wasn't a year that a World Cup was held on... Try Again\n")

#Main world cup sim that will output one team. This is used 10 000 times later to clacualte a larger sample size for probability
def world_cup_simulator():
  team_ratings = {}
  
  for team in world_cup_teams:
    #Finds team name from list of name using index of list in world_cup_teams
    team_name = names_of_teams[world_cup_teams.index(team)]
    #Team rating starts at 0
    total_team_rating = 0
    #Goes through each player
    for player in team:
      #Gets their ova rating
      player_rating = team[player]
      #Adds it to total rating for team
      total_team_rating += player_rating
    #Takes average team rating by adding all players rating and dividing by number of players(11)
    ova_team_rating = total_team_rating // len(team)
    #Adds country name and their overall rating as a key value pair to the final dictionary of teams
    team_ratings.update({team_name : ova_team_rating})
  
  group_stage = generate_group_stage(team_ratings, names_of_teams)
  
  round_of_16_teams = {}
  round_of_16_names = []
  
  for group in group_stage:
    group_stage_points = {
      group[4] : 0,
      group[5] : 0,
      group[6] : 0,
      group[7] : 0
    }
    winners_list = []
    #Team 1v2
    winner_game1 = play_match(group[0], group[1], group[4], group[5])
    winners_list.append(winner_game1)
    #Team 3v4
    winner_game2 = play_match(group[2], group[3], group[6], group[7])
    winners_list.append(winner_game2)
    #Team 1v3
    winner_game3 = play_match(group[0], group[2], group[4], group[6])
    winners_list.append(winner_game3)
    #Team 2v4
    winner_game4 = play_match(group[1], group[3], group[5], group[7])
    winners_list.append(winner_game4)
    #Team 1v4
    winner_game5 = play_match(group[0], group[3], group[4], group[7])
    winners_list.append(winner_game5)
    #Team 2v3
    winner_game6 = play_match(group[1], group[2], group[5], group[6])
    winners_list.append(winner_game6)
  
    for winner in winners_list:
      calculate_points(group_stage_points, winner)
  
    first_place = find_most_points(group_stage_points, team_ratings)
    del group_stage_points[first_place]
    second_place = find_most_points(group_stage_points, team_ratings)
    generate_next_bracket(round_of_16_teams, second_place, team_ratings)
    generate_next_bracket(round_of_16_teams, first_place, team_ratings)
    round_of_16_names.append(first_place)
    round_of_16_names.append(second_place)
  
  round_of_16 = generate_round_16_games(round_of_16_teams, round_of_16_names)
  
  final_8_list = []
  quarter_final_dict = {}
  #Main match function finds winner of game
  play_through_match(round_of_16, final_8_list, quarter_final_dict, team_ratings)
  quarter_finals = generate_quarter_final_games(quarter_final_dict, final_8_list)
  
  final_4_list = []
  semi_final_dict = {}
  #Main match function finds winner of game
  play_through_match(quarter_finals, final_4_list, semi_final_dict, team_ratings)
  semi_finals = generate_semi_final_games(semi_final_dict, final_4_list)
  
  final_2_list = []
  finals_dict = {}
  #Main match function finds winner of game
  play_through_match(semi_finals, final_2_list, finals_dict, team_ratings)
  the_finals = generate_the_finals(finals_dict, final_2_list)
  
  final_1_list = []
  useless_dict = {}
  #Main match function finds winner of game
  play_through_match(the_finals, final_1_list, useless_dict, team_ratings)
  world_cup_winner = final_1_list[0]
  return world_cup_winner

#Intro
print("Welcome to the 2022 FIFA World Cup Simulator! In this program, you will be able to generate a simulation that gives you the probability of each country from this years World Cup winning the championship! This works by running through a simulation 10 000 times and using the winners from each simulation to convert them into an overall % chance that each team will win.\n\n You can choose to either generate all 10 000 games, run through just one simulation, view the probabilities of one team winning, view the proabilites of all teams winning, or exit.\n")

games_generated = False
#Main menu that runs until user exits
while True:
  user_menu_input = check_input("Generate All 10 000 Games [c]\nGenerate Just One Simulation [s]\nView The Proabability A Country Will Win [v]\nView All Probabilities Of Countries [a]\nView The Team Most Likely To Win [w]\nCreate A Graph With All Probabilities [g]\nView A Country's Starting Lineup & Their Ratings [x]\nView All Previous World Cup Winners [u]\nExit [e]", ["v", "a", "g", "s", "e", "x", "w", "c", "u"])

  #Prints all teams odds of winning WC
  if user_menu_input == "a":
    if games_generated == True:
      print("\n")
      for team in wc_winner_all_teams:
        print_all_team_odds(wc_winner_all_teams, team)
      print("\n")
    else:
      print("\nTo view probabilites, you must generate the 10 000 games first\n")

  #User can see one teams odds of winning
  elif user_menu_input == "v":
    if games_generated == True:
      country_input = check_country("\nWhat Country Would You Like To See?:", names_of_teams)
      print("\n")
      print_all_team_odds(wc_winner_all_teams, country_input)
      print("\n")
    else:
      print("\nTo view probabilites, you must generate the 10 000 games first\n")

  #User must generate all of these games and odds before other actions. Restricted using a variable and boolean value
  elif user_menu_input == "c":
    wc_winner_all_teams = {}
    for team in world_cup_teams:
      #Finds team name from list of name using index of list in world_cup_teams
      team_name = names_of_teams[world_cup_teams.index(team)]
      #Team rating starts at 0
      team_wins = 0
      #Adds team name and number of times won so far (0) to dict as key value pair
      wc_winner_all_teams.update({team_name : team_wins})

    #Larger sample size used 10 000 times for more accurate odds of teams winning
    for i in range(10000):
      possible_world_cup_winner = world_cup_simulator()
      wc_winner_all_teams[possible_world_cup_winner] += 1
    games_generated = True
    print("\n")

  #Only runs through sim once and not 10 000 times
  elif user_menu_input == "s":
    single_winner = world_cup_simulator()
    print(f"\nThe winner of this World Cup Simulation is: \033[0;34m{single_winner.capitalize()}\033[0m\n")

  #User can see the 11 players starting for a team
  elif user_menu_input == "x":
    user_input_country = check_country("\nWhat Country Would You Like To See?:", names_of_teams)
    print(f"The starting line up for \033[0;34m{user_input_country.capitalize()}\033[0m\n is:\n")

    team = world_cup_teams[names_of_teams.index(user_input_country)]
    for player in team:
      print(f"\033[0;31m{player}\033[0m with a rating of \033[0;35m{team[player]}\033[0m Overall")
    print("\n")

  #Prints most likely team to win WC
  elif user_menu_input == "w":
    if games_generated == True:
      most_likely_team = max(wc_winner_all_teams, key = wc_winner_all_teams.get)
      print(" ")
      print_all_team_odds(wc_winner_all_teams, most_likely_team)
      print(" ")
    else:
      print("\nTo view probabilites, you must generate the 10 000 games first\n")

  #Creates histrogram type thing to visualize results
  elif user_menu_input == "g":
    if games_generated == True:
      graph = create_graph(wc_winner_all_teams, names_of_teams)
    else:
      print("\nTo view probabilites, you must generate the 10 000 games first\n")

  #Function is called that prints previous winners of other WC
  elif user_menu_input == "u":
    previous_winners()

  #Main loop is broken and code ends with bye bye message.
  else:
    print("Bye Bye!")
    break