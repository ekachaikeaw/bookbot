def get_num_words(content):
    word_list = content.split()
    return len(word_list)

def get_chars_dict(content):
    ch_dict = {}
    for ch in content:
        lower_ch = ch.lower()
        if lower_ch not in ch_dict:
            ch_dict[lower_ch] = 1
        else:
            ch_dict[lower_ch] += 1
    return ch_dict