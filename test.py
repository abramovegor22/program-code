def category_stat(data_file):
    from csv import reader as r
    myfile = open(data_file, encoding='utf-8')
    txt = myfile.read()
    myfile.close()
    result = []
    with open(data_file, "r", newline="", encoding='utf-8') as file:
        reader = r(file)
        for row in reader:                       
            if row.count("product_code") > 0: continue
            result.append( ( row[1], txt.count("," + str(row[1]) + ","), txt.count("," + str(row[1]) + ",1" ) ) ) 
    result.sort()         
    from itertools import groupby
    sort_result = [a for a, _ in groupby(result)]
    sort_result.sort()
    return sort_result

stat = category_stat('category_stat_1.csv')
print('\n'.join(str(i) for i in stat))
