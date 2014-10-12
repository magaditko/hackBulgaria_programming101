def reduce_file_path(path):
    path = path.split('/')
    result = []
    for folder in path:
        if folder == "..":
            if result:
                result.pop()
        elif folder != "." and folder != "":
            result.append(folder)
    path = "/" + "/".join(result)
    return path


def main():
    print()
print(reduce_file_path("/"))
print(reduce_file_path("/srv/../"))
print(reduce_file_path("/srv/www/htdocs/wtf/"))
print(reduce_file_path("/srv/www/htdocs/wtf"))
print(reduce_file_path("/srv/./././././"))
print(reduce_file_path("/etc//wtf/"))
print(reduce_file_path("/etc/../etc/../etc/../"))
print(reduce_file_path("//////////////"))
print(reduce_file_path("/../"))
