import ImageProcessing
import timeit

def testAutoGui():
    mysetup = "import ImageProcessing"
    mycode = "ImageProcessing.autoguiCapture()"

    totaltime = timeit.timeit(setup=mysetup,
                        stmt=mycode,
                        number=1000)
    print(mycode)
    print(totaltime)
    print(totaltime/1000)
    print("")

def testDxcam():
    mysetup = "import ImageProcessing"
    mycode = "ImageProcessing.dxCamCapture()"

    totaltime = timeit.timeit(setup=mysetup,
                              stmt=mycode,
                              number=1000)

    print(mycode)
    print(totaltime)
    print(totaltime / 1000)
    print("")
def testMss():
    mysetup = "import ImageProcessing"
    mycode = "ImageProcessing.mssCapture()"

    totaltime = timeit.timeit(setup=mysetup,
                              stmt=mycode,
                              number=1000)

    print(mycode)
    print(totaltime)
    print(totaltime / 1000)
    print("")

if __name__ == '__main__':
    testAutoGui()
    testDxcam()
    testMss()