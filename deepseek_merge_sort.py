import pandas as pd

filename = 'E:/python/_test.csv'
filename3 = 'E:/python/res.csv'

def merge(sort, p, q, r):
    sort_lou = sort[p:q + 1]
    sort_up = sort[q + 1:r + 1]

    # Add sentinel values
    sort_lou.append({'DeviceId': float('inf')})
    sort_up.append({'DeviceId': float('inf')})

    i = j = 0
    for k in range(p, r+1):
        if sort_lou[i]['DeviceId'] <= sort_up[j]['DeviceId']:
            sort[k] = sort_lou[i]
            i += 1
        else:
            sort[k] = sort_up[j]
            j += 1

def merge_sort(sort, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(sort, p, q)
        merge_sort(sort, q + 1, r)
        merge(sort, p, q, r)

My = pd.read_csv(filename, skiprows=0, sep=',', on_bad_lines='skip', encoding='utf8')
My = My.drop(My.index[-1])
My_list = My.to_dict('records')
print(My_list)
merge_sort(My_list, 0, len(My_list) - 1)

# Convert the sorted list back to a DataFrame
My_res = pd.DataFrame(My_list)

# Save the sorted DataFrame to a CSV file
My_res.to_csv(filename3, index=False)