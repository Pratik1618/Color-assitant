
import requests


def get_combinations(scheme, palette_no, colors_no):

    combinations = []

    scheme_s = str(scheme)
    palette_no_s = str(palette_no)
    colors_no_s = str(colors_no)

    url = f"https://random-palette-generator.p.rapidapi.com/palette/{scheme_s}/{palette_no_s}/{colors_no_s}"

    headers = {
        "X-RapidAPI-Host": "random-palette-generator.p.rapidapi.com",
        "X-RapidAPI-Key": "484c82a95dmsh9f58039e4cd4478p1ce421jsn0ace37def898"
    }

    response = requests.request("GET", url, headers=headers)

    output = response.json()

    output_data = output.get('data')


    for i in output_data:
        single_combination = i['palette']
        combinations.append(single_combination)

    return combinations

