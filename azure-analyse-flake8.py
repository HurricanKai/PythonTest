import re

filepath = 'flake8.log'
cnt = 0
with open(filepath) as fp:
    cnt = cnt + 1
    line = fp.readline()
    while line:
        print(line)
        r = re.search(r"(.?\/[^\/ :]*)+\/?:(\d*):(\d*): (\S*) (.*)", line)
        print(f"##vso[task.logissue type=error;sourcepath={r.group(1)};linenumber={r.group(2)};columnnumber={r.group(3)};code={r.group(4)}]{r.group(5)}")
        line = fp.readline()
if cnt > 0:
    exit(1)
else:
    exit(0)