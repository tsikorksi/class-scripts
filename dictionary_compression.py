# simple dictionary compression algorithm


def pattern_analysis(sample):
    pattern_dictionary = {}
    half = int(len(sample)/2)
    for i in range(2, half):
        for j in range(0, len(sample), i):
            pattern = sample[j:j + i]
            count = 0
            for k in range(0, len(sample)):
                if sample[j:k] == pattern:
                    count += 1
            if count > 2:
                pattern_dictionary.update({pattern: j})

    print(pattern_dictionary)
    return pattern_dictionary


pattern_analysis("testetstaiurfpiutaiuryajgafkuhstywqjkighduhgfd")
