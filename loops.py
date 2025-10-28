"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    new_scores = []
    for scores in student_scores:
        new_scores.append(round(scores))
    return new_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    sum_fail = 0
    for scores in student_scores:
        if scores <= 40:
            sum_fail += 1
    return sum_fail


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    best = []
    for scores in student_scores:
        if scores >= threshold:
            best.append(scores)
    return best


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    grades = [41]
    step = round((highest - 41) / 4)
    for index in range(3):
        grades.append(grades[index] + step)
    return grades


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    rank:list[str] = []
    for index in range (1, len(student_scores) + 1):
    #     rank.append(str(i))
    #     rank.append(student_names[i-1])
    #     rank.append(student_scores[i-1])
        rank.append(f'{str(index)}. {student_names[index-1]}: {student_scores[index-1]}')
    return rank

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for item  in student_info:
        if 100 in item:
            return item
    return []

    # The first try
    # high = []
    # for i in range(len(student_info)):
    #     if '100' in student_info[i]:
    #         high.append(student_info[i])
    # return high

