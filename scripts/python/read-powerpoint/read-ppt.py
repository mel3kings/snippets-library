#!/usr/local/Caskroom/miniconda/base/bin/python

import os
import pptx
import configparser
import requests


def get_text_from_ppt(ppt_path):
    prs = pptx.Presentation(ppt_path)
    print("=====processing file: {}".format(ppt_path))
    text = []
    for slide in prs.slides:
        slide_id = prs.slides.index(slide)
        text.append("Title: {} slide: {}".format(ppt_path, slide_id))
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    text.append(run.text)
    return '\n'.join(text)


def process_file(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if filename.endswith(".pptx"):
            text = get_text_from_ppt(os.path.join(file_path))
            return text
        elif os.path.isfile(file_path):
            continue
        else:
            process_file(file_path)


def send_to_open_ai(text, api_key):
    prompt = 'Give me a synthesize paragraph from the following text: {}'.format(text)
    data = {'prompt': prompt, 'max_tokens': 500}
    headers = {'Authorization': 'Bearer {}'.format(api_key)}
    response = requests.post('https://api.openai.com/v1/engines/text-davinci-003/completions', json=data,
                             headers=headers)
    raw_response = response.json()
    ai_response = raw_response["choices"][0]["text"]
    return ai_response


def main():
    config = configparser.ConfigParser()
    config.read('properties.ini')
    directory_ = config['DEFAULT']['Local_Directory']
    print("reading: {}".format(directory_))
    response = process_file(directory_)
    ai_response = send_to_open_ai(response, config['DEFAULT']['API_KEY'])
    print(ai_response)


# if __name__openai_key = "YOUR_OPENAI_KEY_HERE"

if __name__ == "__main__":
    main()
