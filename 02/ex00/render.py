import sys
import os
import re


def render():
    if len(sys.argv) != 2:
        sys.exit("Type 2 arguments")
    input = sys.argv[1]
    path = os.getcwd() + "/" + input

    if not os.path.isfile(path):
        sys.exit('Type a valid file')
    
    if not input.endswith('.template'):
        sys.exit("Extension must be .template")
    settings_file = open("settings.py", 'r').readlines()

    input_list = []
    input_list_2 = []
    counter = -1
    for i in settings_file:
        counter = counter + 1
        new = i.split('=')[0].strip()
        input_list.append(new)
        if (new != ''):
            new = "{" + new + "}"
        input_list_2.append(new)
    output_list = {}
    counter = -1

    for i in settings_file:
        counter = counter+1
        if i[:3] == input_list[counter][:3]:
            res_name = i.partition(input_list[counter])[2]
            res_name = str(res_name)
            res_name = re.split("=", res_name)[-1].strip('\n').strip()
            output_list[counter] = res_name  
    html = open(input, 'r').read()
    counter = 0

    while (counter < 7):
        if(input_list_2[counter]):
            html = re.sub(input_list_2[counter], output_list[counter], html)
            html = html.replace('"', '')
        counter += 1
    input = input[:-9]
    output = input + '.html'
    f = open(output, 'w')
    f.write(html)

if __name__ == "__main__":
    render()
