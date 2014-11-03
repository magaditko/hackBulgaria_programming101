class Student:

    def __init__(self, name, courses, available, github):
        self.name = name
        self.courses = courses
        self.available = available
        self.github = github

    def return_courses(self):
        result = []
        for course in self.courses:
            result.append(course['name'])
        return result

    def return_course_group_time(self):
        result = []
        for course in self.courses:
            result.append([course['name'], course['group']])
        return result

    def return_name(self):
        return self.name
