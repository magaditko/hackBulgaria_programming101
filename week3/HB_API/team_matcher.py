import requests
import json
import random

from user import Student


class TeamMatcher:
    request = requests.get('https://hackbulgaria.com/api/students/', verify=False)

    def __init__(self):
        self.data = []
        self.set_students()
        self.courses = []
        self.set_all_courses()

    def set_students(self):
        
        content = json.loads(TeamMatcher.request.text)
        for student in content:
            self.data.append(Student(
                student['name'],
                student['courses'],
                student['available'],
                student['github']
            ))

    def set_all_courses(self):
        all_courses = []
        
        for student in self.data:
            all_courses.extend(student.return_courses())

        for value in all_courses:
            if value not in self.courses:
                self.courses.append(value)

    def print_courses(self):
        print('All Courses:')
        for c in enumerate(self.courses):
            print('[{}] {}'.format(c[0] + 1, c[1]))

    def students_from_course(self, course_id):
        if course_id >= 1 and course_id <= len(self.courses):
            result = []
            for student in self.data:
                for course in student.courses:
                    if course['name'] == self.courses[course_id - 1]:
                        result.append(student)
            return result

    def students_from_group(self, group_time, group):
        names = []
        for student in group:
            for course in student.courses:
                if course['group'] == group_time and student.available:
                    names.append(student.return_name())
        return names

    def match_teams(self, course_id, team_size, group_time):
        students = self.students_from_group(group_time,
                                            self.students_from_course(course_id))
        random.shuffle(students)
        teams = [students[i: i + int(team_size)] for i in range(0, len(students), int(team_size))]
        return teams

print('Hello, you can use one the following commands:')
print('list_courses - this lists all the courses that are available now.')
print('match_teams <course_id>, <team_size>, <group_time>\n')

matcher = TeamMatcher()
if TeamMatcher.request.status_code == 200:
    while(True):
        command = input()
        if command == 'list_courses':
            matcher.print_courses()
        elif 'match_teams' in command:
            command = command.split(' ')
            teams = matcher.match_teams(int(command[1]), int(command[2]), int(command[3]))

            for team in enumerate(teams):
                print("=" * 15)
                print('-- Team {} --:'.format(team[0] + 1))
                for name in team[1]:
                    print(name)
            break
        else:
            print('Sorry')
