# sbm3qh & mto3hr & jl4nq

def ellipsis(s):
    return s[:2]+"..."+s[len(s)-2:]

print(ellipsis("computer science"))

def eighteen(s):
    return s[0]+str((len(s)-2))+s[-1]

print(eighteen("computer science"))

def allit(s, t):
    s = s.lower()
    t = t.lower()
    if (s[0]== 'a' or s[0]== 'e' or s[0]== 'i' or s[0]== 'o' or s[0]== 'u') or (t[0]== 'a' or t[0]== 'e' or t[0]== 'i' or t[0]== 'o' or t[0]== 'u'):
        return False
    elif s[0] == t[0]:
        return True
    else:
        return False

print(allit("exciting", "excit"))

def between(s,t):
    if t in s[s.find(t)+len(t):s.find(s[-1])]:
        return s[s.find(t)+len(t):s.find(t, s.find(t)+len(t), s.find(s[-1]))]
    else:
        return ""

print(between("quick", "u"))




