N, Q = map(int, input().split())

queries = []
bool_str = []
res_str = ""


for i in input().split():
    if i == "true":
        bool_str.append(True)
    elif i == "false":
        bool_str.append(False)
    elif i == "or":
        bool_str.append("or")
    elif i == "and":
        bool_str.append("and")


for _ in range(Q):
    imp = input().split()

    queries.append((int(imp[0]), int(imp[1]), True if imp[2] == "true" else False))



def eval_q(bools):
    arr = bools.copy()

    # If there's no "or" at all, just return the single boolean or the result of all "and"s.
    if "or" not in arr:
        return eval(" ".join(str(x) for x in arr))  # or arr[0], if you already handled all "and"

    # Initial indices for the slice.
    # We'll keep reassigning these inside the loop as the array shrinks.
    try:
        first_or = arr.index("or")                # leftmost "or"
    except ValueError:
        # No "or" in arr => just return the bool
        return eval(" ".join(str(x) for x in arr))

    try:
        end = arr.index("or", first_or+1)         # second "or"
    except ValueError:
        end = len(arr)                            # or up to the end if no second "or"

    start = 0

    while len(arr) > 1:
        # Slice from 'start' up to 'end' (but not including 'end')
        segment = arr[start:end]

        if "or" not in segment:
            # Nothing to do in this segment, break out
            break

        # Split the segment around the first "or" *within* it
        local_or_idx = segment.index("or")
        seg1 = segment[:local_or_idx]
        seg2 = segment[local_or_idx+1:]

        # Evaluate whichever side is "shorter" first
        if len(seg1) < len(seg2):
            left_eval  = eval(" ".join([str(x) for x in seg1]))  # True/False in Python
            res = (left_eval == True)
            evaled_side = 1
        else:
            right_eval = eval(" ".join([str(x) for x in seg2]))
            res = (right_eval == True)
            evaled_side = 2

        # If that side is false, then do an OR with the other side
        if not res:
            if evaled_side == 1:
                # Re-eval seg2 for correctness (in case it has multiple tokens)
                seg2_eval = eval(" ".join([str(x) for x in seg2]))
                combined  = (False or seg2_eval)
                arr[start:end] = [combined]
            else:
                seg1_eval = eval(" ".join([str(x) for x in seg1]))
                combined  = (False or seg1_eval)
                arr[start:end] = [combined]
        else:
            # If the "shorter" side is True => the whole segment is True
            arr[start:end] = [True]

        # ---------------------------------------------------------
        # Now we have replaced arr[start:end] with a single boolean.
        # We must re-find the next 'or' boundaries for the next iteration.
        # ---------------------------------------------------------
        if "or" not in arr:
            break

        try:
            first_or = arr.index("or")
        except ValueError:
            break  # no more "or"s

        try:
            second_or = arr.index("or", first_or + 1)
        except ValueError:
            second_or = len(arr)

        # Recompute 'start' and 'end' for the next slice
        start = 0
        end   = second_or

    # When we leave the loop, arr should ideally be a single boolean or at least no more "or"
    # If there's still "and" left, Python's eval can handle that:
    return eval(" ".join([str(x) for x in arr]))



            
        




            
for query in queries:
    arr = []

    copy = bool_str.copy()

    copy[query[0]-1:query[1]] = [True]



    res = eval_q(copy)



    arr.append(res)


    copy = bool_str.copy()

    copy[query[0]-1:query[1]] = [False]



    res2 = eval_q(copy)


    arr.append(res2)


    if query[2] not in arr:
        res_str += "N"
    else:
        res_str += "Y"

print(res_str)
        





