import ImageProcessing
import timeit

# code snippet to be executed only once
mysetup = "import ImageProcessing"

# code snippet whose execution time is to be measured
mycode = "ImageProcessing.grab_screen()"

# timeit statement
totaltime = timeit.timeit(setup=mysetup,
                    stmt=mycode,
                    number=1000)

print(totaltime)
print(totaltime/1000)
