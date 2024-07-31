FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_data(data)


def get_data():
    subjects = []
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')
        print(parts)
        parts[2] = int(parts[2])
        print(parts)
        subjects.append(parts)
        print(subjects)
    input_file.close()
    return subjects

def display_data(data):
    """Display data to looks good."""
    for subjects in data:
        print(f"{subjects[0]} is taught by {subjects[1]} and has {subjects[2]} students.")


main()