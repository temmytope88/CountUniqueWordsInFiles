class Student:
    # [assignment] Skeleton class. Add your code here
    
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age =age
        self.tracks = tracks
        self.score =score
        pass
    def change_name(self, name):
        self.name = name
    def change_age(self, age):
        self.age = age
    def add_track(self, track):
        self.tracks.append(track)
    def get_score(self):
        return self.score
        



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
#print (Bob.name)
#print (Bob.score)
#print (Bob.tracks)
#print(Bob.score)

# Expected methods
Bob.change_name("Peter")
#print (Bob.name)
Bob.change_age(34)
#print (Bob.age)
Bob.add_track("UI/UX")
#print (Bob.tracks)
Bob.get_score()
print (Bob.get_score())