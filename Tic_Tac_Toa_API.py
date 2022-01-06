from flask import Flask, request
from Tic_Tac_Toa import player_details

app = Flask(__name__)

game_players_details = []


@app.route("/details", methods=["POST"])
def details():
    players_details = request.get_json()
    game_players_details.append(players_details["player1"])
    game_players_details.append(players_details["symbol1"])
    game_players_details.append(players_details["player2"])
    game_players_details.append(players_details["symbol2"])

    return f"Players_Names: {players_details['player1'], players_details['player2']} \n" \
           f"Players_symbol: {players_details['symbol1'], players_details['symbol2']}"


@app.route("/play", methods=["POST"])
def play():
    winner = player_details(game_players_details[0], game_players_details[1], game_players_details[2],
                            game_players_details[3])

    if winner == game_players_details[1]:
        # return f"Players_Names = {player1_name, player2_name} \n" \
        #        f"Players_Symbol = {player1_symbol, player2_symbol} \n" \
        return f"The winner of the game 'TIC-Tac-Toa' is '{game_players_details[0]}' \n" \
               f"{game_players_details.clear()}"
    if winner == game_players_details[3]:
        # return f"Players_Names = {player1_name, player2_name} \n" \
        #        f"Players_Symbol = {player1_symbol, player2_symbol} \n" \
        return f"The winner of the game 'TIC-Tac-Toa' is '{game_players_details[2]}' \n" \
               f"{game_players_details.clear()}"


app.run(host="0.0.0.0", port=3000, debug=True)
