"""
Function to replace text in a text file
"""


def replace_txt(filename, sea_txt, rep_txt):
    """
    :param filename: Filename of the text file.
    :param sea_txt: Searched text.
    :param rep_txt: Text that is insert instead of 'sea_txt'
    :return: None
    """
    # Opening text file in read only mode using the open() function
    with open(filename, 'r') as file:
        data = file.read()
        data = data.replace(sea_txt, rep_txt)

    # Opening our text file in write only mode to write the replaced content
    with open(filename, 'w') as file:
        file.write(data)
