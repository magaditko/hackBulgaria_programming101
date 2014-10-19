def reduce_file_path(path):
    path = path.replace(" ", "")
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
