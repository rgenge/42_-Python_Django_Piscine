def swap_dict(d):
    return {v: k for k, v in d.items()}

def my_sort():
    d = {
    'Hendrix' : '1942',
    'Allman' : '1946',
    'King' : '1925',
    'Clapton' : '1945',
    'Johnson' : '1911',
    'Berry' : '1926',
    'Vaughan' : '1954',
    'Cooder' : '1947',
    'Page' : '1944',
    'Richards' : '1943',
    'Hammett' : '1962',
    'Cobain' : '1967',
    'Garcia' : '1942',
    'Beck' : '1944',
    'Santana' : '1947',
    'Ramone' : '1948',
    'White' : '1975',
    'Frusciante': '1970',
    'Thompson' : '1949',
    'Burton' : '1939',
    }
    prev = 0
    prevname = 0
    it = -1
    sorted_dict = sorted(d.items(), key=lambda x:x[1])
    for i in sorted_dict:
        it = it + 1
        if i[1] == prev:
            if prevname > i[0]:
                prov = sorted_dict[it - 1]
                sorted_dict[it - 1] = sorted_dict[it]
                sorted_dict[it] = prov
        prev = i[1]
        prevname = i[0]
    converted_dict = dict(sorted_dict)
    for i in sorted_dict:
        print(i[0])

if __name__ == '__main__':
    my_sort()