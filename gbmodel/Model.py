# Base class containing the functions
# Use pass to implement the function definitions in other models
class Model():
    def breeds(self):
        """
        Retrieves all dog breeds
	      :return: A JSON object containing a list of all dog breeds
        """
        pass

    def a_breed(self, breed):
        """
        Retrieves an image from a specified breed, max 10
        :param breed: String
        :return: A JSON object containing URLs of random images based on the specified breed
        """
        pass
