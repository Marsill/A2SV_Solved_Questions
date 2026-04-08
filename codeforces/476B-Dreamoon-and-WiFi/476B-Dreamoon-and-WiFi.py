def backtruck(i, step):
    if i == len(s2) and count == step:
        count2[0] += 1
        return
    if i >= len(s2):
        return
    if s2[i] == '?':
        backtruck(i+1, step+1)
        backtruck(i+1, step-1)

    elif s2[i] == "-":
        step -= 1
        i += 1
        backtruck(i, step)
    else:
        step += 1
        i += 1
        backtruck(i, step)

ques = s2.count("?")
backtruck(0, 0)
print(count2[0] / (pow(2, ques)))