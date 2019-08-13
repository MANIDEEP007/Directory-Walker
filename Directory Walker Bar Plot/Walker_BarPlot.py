'''Module that calculates count of various files present'''
import os
import webbrowser

PATH = str(input("Enter PATH to be traversed: "))
if PATH[-1] == '/':
    PATH = PATH[0:-1]
print("Collecting Data. Please wait for some time")
COUNT_LIST = []

#Based on the need Give file types and Corresponding correct extension
COUNT_TYPES = ["'Python File'", "'Python Compiled Files'", "'XML Files'", \
    "'LOG Files'", "'Yang Files'", "'Shell Scripts'", "'Text Files'"]
COUNT_EXT = ["py", "pyc", "xml", "log", "yang", "sh", "txt"]
COUNT_EXT.append("Others")
COUNT_TYPES.append("'Others'")

for i in COUNT_TYPES:
    COUNT_LIST.append(0)

for root, direc, files in os.walk(PATH):
    for f in files:
        try:
            index = COUNT_EXT.index(f.split(".")[-1])
            COUNT_LIST[index] += 1
        except ValueError:
            COUNT_LIST[-1] += 1
TOTAL_FILES = sum(COUNT_LIST)
for i in range(0, len(COUNT_LIST)):
    COUNT_LIST[i] = str(COUNT_LIST[i])
X_DATA = "[" + ",".join(COUNT_TYPES) + "]"
Y_DATA = "[" + ",".join(COUNT_LIST) + "]"
print("Collected Data!!")


def html_writer():
    '''Function to Generate HTML File for Bar Plot'''
    print("Preparing HTML File.Please wait for some time")
    html_file = open("BarPlot.html", "w")
    html_top_str = '''
	<html>
	<head>
		<title>''' + PATH.split("/")[-1] + '''</title>
		<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
	</head>
	<body>
		<h3 align = "center">'''+ PATH.split("/")[-1] + " BarPlot"+ " [ Total Files: "+\
                 str(TOTAL_FILES) +" ]"+'''</h3>
		<div id="myDiv"><!-- Plotly Bar chart will be drawn inside this DIV --></div>
		<script>
					var data = [
						{
						x: '''
    html_middle_str = X_DATA + ''',y:''' + Y_DATA + ''','''
    html_bottom_str = "type:'bar'"+'''
						}
					];
					Plotly.newPlot('myDiv', data);
		</script>
	</body>
	</html>'''
    html_str = html_top_str + html_middle_str + html_bottom_str
    html_file.write(html_str)
    print("Prepared HTML File. Opening it!!")
html_writer()
webbrowser.open('file://' + os.path.realpath("BarPlot.html"))
