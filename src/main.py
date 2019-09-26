from datafetch.fetch_data import DataFetch


master_flag = {
            -1: 'test space',
        }[-1]

if __name__ == '__main__':
    if master_flag == 'test space':
        a = DataFetch()
