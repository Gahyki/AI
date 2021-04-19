class PNT:
    def __init__(self, total_tokens):
        self.total_tokens: int = total_tokens
        self.all_tokens = [i+1 for i in range(self.total_tokens)]
        self.depth = 0 # number of moves made
        self.recent_choice = 0

    def getfactors(self, number):
        # TO DO
        factors = []
        for i in range(1, number + 1):
            if i == 1 and i in self.all_tokens:
                factors.append(i)

            if i % number == 0 and i in self.all_tokens:
                factors.append(i)
        return factors

    def getmultiples(self, number):
        multiples = []
        for i in range(1, self.total_tokens):
            if i*number in self.all_tokens:
                multiples.append(i*number)
        return multiples

    def neighbors(self):
        all_neighbors = []
        if self.depth == 0:
            for i in range(self.total_tokens//2):
                if (i+1) % 2 == 1:
                    all_neighbors.append(i+1)
        else:
            all_neighbors = list(set(self.getmultiples(self.recent_choice) + self.getfactors(self.recent_choice)))
        return all_neighbors

    def take_token(self, token_value, player):
        while token_value not in self.all_tokens:
            print("The token " + str(token_value) + " is already taken by a player.")
            token_value = input("Here are your choices:\n" + str(self.all_tokens) + "\nPlease select a new token: ")

        if self.depth % 2 == 0:
            print("Player MAX has successfully taken the token " + str(token_value) + ".")
            player.ls_taken_tokens.append(token_value)
            self.all_tokens.remove(token_value)
        else:
            print("Player MIN has successfully taken the token " + str(token_value) + ".")
            player.ls_taken_tokens.append(token_value)
            self.all_tokens.remove(token_value)




