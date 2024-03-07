class Pet:
    
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []
    
    def __init__(self, name, pet_type, owner=""):
        self.name = name
        if pet_type in Pet.PET_TYPES:
            self.pet_type=pet_type
        else:
            raise Exception
        self.owner = owner
        # Define a class variable all that stores all instances of the Pet class.
        Pet.all.append(self)
       
class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # return Pet.all
        return [pets for pets in Pet.all]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception
        pet.owner = self

    def get_sorted_pets(self):
        # Sort the Pet.all list by name
        sorted_pets = sorted(Pet.all, key=lambda pet: pet.name)
        return sorted_pets
        