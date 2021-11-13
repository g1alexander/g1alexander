import json
import urllib3
from jinja2 import Environment, FileSystemLoader

# Cantidad maxima de posts a mostrar
MAX_POSTS = 5

# Setup
env = Environment(loader=FileSystemLoader("."))
http = urllib3.PoolManager()


def get_latest_posts(max_posts=5):
    r = http.request("GET", "./data.json")
    data = json.loads(r.data.decode("utf-8"))
    return data[0:max_posts]


hola = get_latest_posts(MAX_POSTS)

print(hola)

# def render_readme(data):
#     template = env.get_template("README.md.template")
#     render = template.render(**data)
#     with open("README.md", "w") as f:
#         f.write(render)


# # def main():


# # if __name__ == "__main__":
# #     main()

# latest_posts = get_latest_posts(MAX_POSTS)
# data = {"latest_post": latest_posts}
# render_readme(data)

# print(latest_posts)
