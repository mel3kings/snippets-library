#!/usr/local/Caskroom/miniconda/base/bin/python

import os
import configparser

import sys


def split_into_chunks(text, chunk_size=2000):
    """Splits text into chunks of given size"""
    chunks = []
    words = text.split()
    current_chunk = []

    for word in words:
        if len(' '.join(current_chunk + [word])) <= chunk_size:
            current_chunk.append(word)
        else:
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

# Example usage
print("HELLLOOO.")
text = "What happens once you apply for cover of a pre-existing medical condition? Once you have completed our medical assessment, we will advise you of the outcome. Depending on your pre-existing medical condition(s), Allianz Global Assistance may either: a] agree in writing to include cover under your policy for your pre-existing medical condition(s) (an additional premium may be payable, and a medical excess may apply); or b] decline to include cover under your policy for your pre-existing medical condition(s); or c] decline to provide you with cover for any medical or hospital expenses, as well as for any other expenses arising from, related to or associated with any injury, illness or sickness suffered by you. Please note that if Allianz Global Assistance declines to provide you with cover as stated in point c] above, you will not be able to continue with your purchase; however there may be other options available such as: • you may be eligible to purchase our Non-Medical Plan - refer to the Table of Benefits on page 14 for details of the benefits available under this type of plan. Please call us on the sales and general enquiries number shown on the back cover of this PDS for further information; or • contacting the Insurance Council of Australia (ICA) - the ICA provides a referral service which is available on their website at www.insurancecouncil. com.au. Select ‘Find an Insurer’ to view a list of general insurers who may be able to provide insurance to suit your requirements. If you have any other questions about preexisting medical conditions, please call the sales and general enquiries number shown on the back cover of this PDS."
chunks = split_into_chunks(text)
print(chunks)

