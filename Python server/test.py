import jinja2


f = open("test.html.j2", "r")

env = jinja2.Environment( loader=jinja2.FileSystemLoader('.'))
tmp = env.get_template("test.html.j2")


data = []
f = open("data.txt","r")
for line in f:
    line = line.strip()
    data.append(line.split(','))

out = tmp.render(data=data)
print(out)
