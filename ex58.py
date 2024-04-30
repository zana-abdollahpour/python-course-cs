def combine_words(word, **kwargs):
    return kwargs.get("prefix", "") + word + kwargs.get("suffix", "")


def combine_words2(word, **kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word


print(combine_words("child"))
print(combine_words("child", prefix="man"))
print(combine_words("child", suffix="ish"))
