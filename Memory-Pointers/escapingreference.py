class Course:
    def __init__(self, topic, learners):
        self.topic = topic
        self.learners = learners
def delete_first(items):
    del items[0]
def main():
    learners = ["A","B","C"]
    print("Learners:", learners)
    course = Course("Memory Management", learners)
    delete_first(learners)
    print("list in main:", learners)
    print("In course: ", course.learners)
    
if __name__ == "__main__":
    main()