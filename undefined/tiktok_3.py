def solve(ttl, queries):

    expires = dict()
    result = []

    for query in queries:
        q_arrr = query.split(' ')
        if q_arrr[0] == 'generate' or q_arrr[0] == 'renew':
            expires[q_arrr[1]] = ttl + int(q_arrr[2])
        elif q_arrr[0] == 'count':
            count = 0
            keys = list(expires.keys())
            for key in keys:
                if expires[key] >= q_arrr[1]:
                    count += 1
                else:
                    del expires[key]
            result.append(count)

    return result
