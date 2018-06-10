import re


if __name__ == "__main__":

    pattern = r"\S+\s-\s-\s\[(?:23\/Mar\/2009:09:0[1-9]:0[4-9]|23\/Mar\/2009:[1-2][0-9]:\d{2}:\d{2}|2[4-8]\/Mar\/2009:\d{2}:\d{2}:\d{2}|28\/Mar\/2009:)\s\S+\s\S(?:GET)(?:\s\S)+"
    number_of_matched_requests = 0
    read_lines = 0

    with open("log") as file:
        for line in file:
            read_lines += 1
            if re.match(pattern, line):
                number_of_matched_requests += 1
                print(re.findall(pattern, line))

    print("\nNumber of all read lines: %d" % read_lines)
    print("\nNumber of all GET between 23/Mar/2009 and 28/Mar/2009 : %d" % number_of_matched_requests)
