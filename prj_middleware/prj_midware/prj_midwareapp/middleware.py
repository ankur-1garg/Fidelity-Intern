def middleware(get_response):
    print("One time initialization")
    def my_function(request):
        print('process before request')
        res =get_response(request)
        print(res)
        print("process after response")
        return res
    return my_function