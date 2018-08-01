# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen.
# I have a .txt file for you, if you want to use it!
#
# Extra:
# Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count how many of each “category” of each image there are.
# This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images.
# Once you take a look at the first line or two of the file, it will be clear which part represents the scene category.
# To do this, you’re going to have to remember a bit about string parsing in Python 3.


def main():
    # first_file()
    second_file()


def first_file():

    name_dict = {}

    with open('nameslist.txt', 'r') as open_file:
        line = open_file.readline().strip()
        while line:
            if line not in name_dict:
                name_dict[line] = 1
            elif line in name_dict:
                name_dict[line] += 1
            line = open_file.readline().strip()
    print(name_dict)


def second_file():

    scene_dict = {}

    with open('Training_01.txt', 'r') as open_file:
        line = open_file.readline()[3:-26]
        while line:
            if line not in scene_dict:
                scene_dict[line] = 1
            elif line in scene_dict:
                scene_dict[line] += 1

            line = open_file.readline()[3:-26]
    print(scene_dict)


if __name__ == '__main__':
    main()
