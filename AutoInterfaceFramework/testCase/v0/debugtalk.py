from parameters.section import Section
import os

version = os.getcwd().split("/")[-1]

section = Section(version)

def key():
    return section.key(version)