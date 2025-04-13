'''
Name: Dylan Phoutthavong
Date: April 11th, 2025
Course: CSCI 3412
Task(s): Write your own Python program to web-scrape the CS department course pre-requisite information:...
'''
import requests
from bs4 import BeautifulSoup
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Scrape the CSCI course page
url = "https://catalog.ucdenver.edu/cu-denver/undergraduate/courses-a-z/csci/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Step 2: Parse the course blocks
coursesDict = {}
course_blocks = soup.find_all("div", class_="courseblock")

for block in course_blocks:
    title_tag = block.find("span", class_="text col-3 detail-code margin--tiny text--huge")
    extras_tag = block.find("div", class_="courseblockextra")
    
    if not title_tag or not extras_tag:
        continue

    # Normalize course code
    parts = title_tag.get_text(strip=True).split()
    if len(parts) >= 2:
        course_code = f"{parts[0].strip().upper()} {parts[1].strip()}"
    else:
        continue

    prereqs = []
    for a in extras_tag.find_all("a"):
        prereq = a.get_text(strip=True).upper()
        if prereq.startswith(("CSCI", "MATH", "PHYS")):
            prereqs.append(prereq)

    coursesDict[course_code] = {
        "title": title_tag.get_text(strip=True),
        "prerequisites": prereqs
    }

# Step 3: Write HTML table
html_table = """
<html><head><title>CS Courses</title></head><body>
<h1>CU Denver CS Courses and Prerequisites</h1>
<table border="1">
<tr><th>Course</th><th>Title</th><th>Prerequisites</th></tr>
"""

for course, info in coursesDict.items():
    prereq_str = ", ".join(info["prerequisites"])
    html_table += f"<tr><td>{course}</td><td>{info['title']}</td><td>{prereq_str}</td></tr>\n"

html_table += "</table></body></html>"

with open("CS_courses.html", "w") as f:
    f.write(html_table)

# Step 4: Create the graph
G = nx.DiGraph()
G.add_nodes_from(coursesDict.keys())

for course, info in coursesDict.items():
    for prereq in info["prerequisites"]:
        prereq = prereq.strip().upper()
        if prereq in coursesDict:
            G.add_edge(prereq, course)

# Step 5: Draw the graph
plt.figure(figsize=(20, 20))
pos = nx.spring_layout(G, k=0.2, iterations=50)
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=500)
nx.draw_networkx_edges(G, pos, arrows=True, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=8)
plt.title("CU Denver CSCI Course Prerequisites")
plt.axis('off')
plt.tight_layout()
plt.savefig("cs_course_graph.png")
plt.show()