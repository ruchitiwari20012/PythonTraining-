def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec


@dec1

#just writing it with @ than also it works
def who_is_ruchi():
    print("Ruchi is a good girl")

#who_is_ruchi = dec1(who_is_ruchi)
who_is_ruchi()