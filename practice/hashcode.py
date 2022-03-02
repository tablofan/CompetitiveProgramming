from collections import defaultdict
import heapq

def main():
    c = defaultdict(dict)
    status = defaultdict(int)

    contributors, projects = map(int, input().split())

    for _ in range(contributors):
        name, skills = input().split()
        status[name] = 0
        for _ in range(int(skills)):
            skill, level = input().split()
            c[skill][name] = int(level)
    for i in c:
        c[i] = {k: v for k, v in sorted(c[i].items(), key=lambda item: item[1])}

    p = []
    for _ in range(projects):
        inp = input().split()
        skills = []
        for _ in range(int(inp[4])):
            i = input().split()
            skills.append([i[0],int(i[1])])
        project = [inp[0], int(inp[1]), int(inp[2]), int(inp[3]), skills]
        p.append(project)

    time = 0
    pres = []
    cres = []
    while p:
        removed = set()
        for projectname, days, score, bestbefore, skills in p:

            if score+bestbefore-(time+days)<=0:
                removed.add(projectname)
            else:
                l = len(skills)
                curr = []
                for skill,level in skills:
                    for name,v in c[skill].items():
                        if v>=level and not status[name] and name not in curr:
                            curr.append(name)
                            break
                if len(curr)>=l:
                    for i in curr:
                        status[i] = days
                    removed.add(projectname)
                    pres.append(projectname)
                    cres.append(" ".join(curr))

        p = [i for i in p if i[0] not in removed]
        try:
            val = min(i for i in status.values() if i)
        except:
            break
        time += val
        for i in status:
            status[i] = max(0, status[i]-val)
    print(len(pres))
    for i in range(len(pres)):
        print(pres[i])
        print(cres[i])

if __name__ == "__main__":
    main()