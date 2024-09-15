"""
Mercenary Game main file
"""
from classes.player_service import PlayerService


class StartGame:
    """
    Go through the entire game
    """
    def __init__(self):
        # initialize the class object for the PlayerService class
        self.player_service = PlayerService()

    def greet_user(self):
        """
        Greet the user
        """
        print("Welcome to the mercenary game you piece of shit.")
    def run_game(self):
        """
        run the entire game
        """
        self.greet_user()
        self.player_service.get_new_player_info()


if __name__ == "__main__":
    game_obj = StartGame()
    game_obj.run_game()
