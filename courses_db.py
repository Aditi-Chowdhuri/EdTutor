def read_data(fb):
    data=fb.get("/", "courses")
    cname_arr = data.keys()
    return cname_arr, data
