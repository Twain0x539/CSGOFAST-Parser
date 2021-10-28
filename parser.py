from time import time

from Parsers import CSGOFastParser



if __name__ == "__main__":
    parser = CSGOFastParser()
    history_output_path = "./train.csv"
    money_info_output_path = "./bets.csv"
    history_latest_parse_time = 0
    cooldown = 1200


    while(True):
        current_time = time()
        if(current_time - history_latest_parse_time > cooldown):
            history_latest_parse_time = current_time
            history_data = parser.parse_history()
            with open(history_output_path, "a+") as file:
                for line in history_data:
                    for element in line:
                        file.write(element)
                        file.write(',')
                    file.write('\n')
            print('History updated')
        current_game_info = parser.parse_current_game()
        if int(current_game_info[0]) < 1 or int(current_game_info[0]) == 25:
            with open(money_info_output_path, "a+") as file:
                for element in current_game_info[1:]:
                    file.write(element)
                    file.write(',')
                file.write('\n')
            print('Bets info updated')

