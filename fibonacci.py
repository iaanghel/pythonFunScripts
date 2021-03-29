def fibonacciGenerator():
    runFib = True
    while runFib:
        n = raw_input('How many numbers do you need? ')
        try:
            n = int(n)
            if n > 0:
                runFib = False
                series = [1]

                while len(series) < n:
                    if len(series) == 1:
                        series.append(1)
                    else:
                        series.append(series[-1] + series[-2])

                for i in range(len(series)):
                    series[i] = str(series[i])
            else:
                print ('enter a valid number')
        except:

            print ('enter a valid number')
    return ', '.join(series)


print (fibonacciGenerator())

