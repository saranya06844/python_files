def main():
    def check_scope():
        def do_local():
            test="it's local"
        def do_non_local():
            nonlocal test
            test="it's a non local"
            print("it's a non local function",test)
        def do_global():
            global test
            test="it's a global"

        do_non_local()
        test="default"
        print("test value after test:", test)
        do_non_local()
        print("test value after calling non local function:",test)
        do_global()
        print("test value after calling do_global:",test)

    check_scope()
    print("test value calling from main funciton:", test)
main()
print("test value calling from main:",test)