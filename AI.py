def sort_dict_list(data, key):
    try:
        return sorted(data, key=lambda item: item.get(key))
    except Exception as e:
        print("Sort failed:", e)
        return data
