import tracemalloc
class Course:
    def __init__(self, topic, learners):
        self.topic = topic
        self.learners = learners
class Course_Restricted:
    __slots__=["topic","learners"]
    def __init__(self, topic, learners):
        self.topic = topic
        self.learners  = learners
learners = ["C","A"]
c = Course("python",learners)
cr = Course_Restricted("Java",learners)
c.level = "beginner"
tracemalloc.start()
objs = [Course_Restricted("python",learners)for i in range (1000)]
print("Course Restricted:" , tracemalloc.get_traced_memory())
tracemalloc.start()
objs = [Course("python", learners) for i in range(200000)]
print("Course:" , tracemalloc.get_traced_memory())