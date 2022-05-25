class Student:
    
    # A Student Object consctructor with default values
    # Given that the student object has no value for name, age, track and score attributes 
    # We set them to empty values
    def __init__(self, name = "", age = 0, tracks=[], score = 0.0):
        # initializing the attributes, where age is converted to int and score converted to float;
        self.name = name
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)
        
    # This method changes the name attribute of an object
    def change_name(self, new_name):
        self.name = new_name
    
    # This method changes the age attribute of an object
    def change_age(self, new_age):
        self.age = int(new_age)
    
    # This method adds an extra track to the track attribute of an object
    def add_track(self, new_track):
        self.tracks.append(new_track)
    
    # This method returns the score of an object  
    def get_score(self):
        return self.score
        



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
print(Bob.get_score())
