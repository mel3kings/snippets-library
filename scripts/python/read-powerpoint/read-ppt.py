#!/usr/local/Caskroom/miniconda/base/bin/python

import os
import pptx


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


def main():
    process_file("/Users/melchor_tatlonghari/Box Sync/Local_working_folder/")


def process_file(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if filename.endswith(".pptx"):
            text = get_text_from_ppt(os.path.join(file_path))
            print(text)
        elif os.path.isfile(file_path):
            continue
        else:
            process_file(file_path)


# if __name__openai_key = "YOUR_OPENAI_KEY_HERE"

if __name__ == "__main__":
    main()
