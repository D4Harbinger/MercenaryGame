"""
Player Service
"""


class PlayerService:

    def __init__(self):
        """
        initialize class variables
        """
        # track the current player
        self.player = {
            'name': '',
            'rank': 1,
            'cash': 250.0,
            'arsenal': ['Knife',],
            'current_contract': None,
            'contracts_completed': 0,
            'xp': 0.0
        }
        # track the ranks
        self.ranks = {
            1: {'title': 'Rookie', 'xp_required': 0},
            2: {'title': 'Silver Killer', 'xp_required': 600},
            3: {'title': 'Gold Killer', 'xp_required': 1200},
            4: {'title': 'True Hunter ☠️', 'xp_required': 2400}
        }

    def get_new_player_info(self):
        """
        Get the name of the new mercenary
        """
        self.player['name'] = input('Please Enter your mercenary name: ')
        print(f'Name: {self.player["name"]}')
