import sys

indent = '    '


def is_line_empty(line):
    return len(line.strip()) != 0


def get_filename(filename):
    return filename.replace('.dsl', '.py')


def get_content(filename):
    return open(filename).read()


def split_lines(content):
    return content.split('\n')


def underscore_to_camel_case(word):
    words = word.split('_')
    result = ''
    for word in words:
        result += word.capitalize()
    return result


def line_to_case(line):
    line = line.split(' -> ')
    line[1] = line[1].split(' == ')

    result = 'self.assert'
    if line[1][1] == 'True':
        result += 'True({}, {})'.format(line[1][0], line[0])
    elif line[1][1] == 'False':
        result += 'False({}, {})'.format(line[1][0], line[0])
    else:
        result += 'Equal({}, {}, {})'.format(line[1][1], line[1][0], line[0])
    return result


def unline(content):
    return "\n".join(content)


def get_class_line(filename):
    class_name = underscore_to_camel_case(filename[:-4])
    class_line = 'class {}(unittest.TestCase):'.format(class_name)
    return class_line


def main():
    l = []
    l.append('import unittest')
    l.append(' ')
    filename = sys.argv[1]
    contents = get_content(filename)
    lines = split_lines(contents)
    without_empty_lines = list(filter(is_line_empty, lines))
    for line in without_empty_lines:
        if 'import' in line:
            l.append(line)
            l.append(' ')
            l.append(' ')
            without_empty_lines.remove(line)
    l.append(get_class_line(filename))
    l.append(indent + without_empty_lines[0])
    without_empty_lines.remove(without_empty_lines[0])
    for index, line in enumerate(without_empty_lines):
        l.append(indent + 'def testCase{}(self):'.format(index + 1))
        l.append(indent + indent + line_to_case(line))
        l.append(' ')
    l.append('if __name__ == \'__main__\':')
    l.append(indent + 'unittest.main()')

    ul = unline(l)
    print(ul)
        

if __name__ == '__main__':
    main()        
