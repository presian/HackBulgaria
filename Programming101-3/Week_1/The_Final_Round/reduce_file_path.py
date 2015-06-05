def double_slash_remover(path):
    return path.replace("//", "/")


def string_splitter(path):
    return path.split("/")


def empty_string_remover(path_entities):
    return [x for x in path_entities if x != ""]


def point_checker(path_entity):
    if path_entity != ".." and path_entity != ".":
        return True
    return False


def result_maker(path_entities):
    result = []
    for i in range(0, len(path_entities) - 1):
        if path_entities[i + 1] != ".." and point_checker(path_entities[i]):
            result.append(path_entities[i])
    if len(result) > 0:
        if point_checker(path_entities[-1]):
            result.append(path_entities[-1])
    return "/" + "/".join(result)


def reduce_file_path(path):
    path = double_slash_remover(path)
    path_entities = string_splitter(path)
    path_entities = empty_string_remover(path_entities)
    return result_maker(path_entities)


def main():
    print(reduce_file_path("/"))
    print(reduce_file_path("/srv/../"))
    print(reduce_file_path("/srv///www/htdocs/wtf/"))
    print(reduce_file_path("/srv/www/htdocs/wtf"))
    print(reduce_file_path("/srv/./././././"))
    print(reduce_file_path("/etc//wtf/"))
    print(reduce_file_path("/etc/../etc/../etc/../"))
    print(reduce_file_path("//////////////"))
    print(reduce_file_path("/../"))
    print(reduce_file_path(
        "/home//radorado/code/./hackbulgaria/week0/../"))


if __name__ == '__main__':
    main()
