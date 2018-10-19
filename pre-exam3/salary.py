import urllib.request
import re


def name_to_url(name):
    if name[0] != name[0].lower():
        if ', ' in name:
            i1 = name.find(',')
            new_name1 = name[i1 + 2:].lower() + '-' + name[:i1].lower()
            return new_name1
        elif ' ' in name:
            new_name2 = []
            parts = name.split(' ')
            for part in parts:
                new_name2.append(part.lower())
            new_name2 = '-'.join(new_name2)
            return new_name2
    else:
        return str(name)
def report(name):
    try:
        url = 'http://cs1110.cs.virginia.edu/files/uva2016/'+ name_to_url(name)
        stream = urllib.request.urlopen(url)
        text = stream.read().decode('utf-8')

        title = re.compile('Job title: (.*)<br />')
        for match in title.finditer(text):
            job = match.group(1)
            if '&amp;' in job:
                job = job.replace('&amp;','&')
            if '&lt;' in job:
                job = job.repalce('<', '&lt;')
            if '&gt;' in job:
                job = job.repalce('>', '&gt;')


        compensation = re.compile('paytype.amount, (.*)\) %')
        for match in compensation.finditer(text):
            money = float(match.group(1))

        ranking = re.compile('rank</td><td>(.*) of 7,927</td></tr>')
        if ranking.search(text) != None:
            m = ranking.search(text)
            if ',' in m.group(1):
                new_rank = []
                parts = m.group(1).split(',')
                for part in parts:
                    new_rank.append(part)
                new_rank = ''.join(new_rank)
                rank = int(new_rank)
            else:
                rank = int(m.group(1))
        else:
            rank = 0

        return job, money, rank
    except:
        return None, 0, int(0)











#print(name_to_URL('Sullivan, Teresa'))
#print(name_to_URL('Teresa Sullivan'))
#print(name_to_URL('Polanowska-Grabow, Renata'))
#print(name_to_URL('Ali Reza Forghani Esfahani'))
#print(name_to_url('161048349'))
#report('Sullivan, Teresa')
#print(report('teresa-sullivan'))
#job, money, rank = report('teresa-sullivan')
