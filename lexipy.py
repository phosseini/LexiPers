from os import path
import pandas as pd
import shutil
import xml.etree.ElementTree as ET


class LexiPy:
    def __init__(self):
        self.src_path = 'data/adj-final.xml'
        self.copy_path = 'data/lexipers.xml'

        # creating a local copy of the lexicon if already doesn't exist
        try:
            if not path.exists(self.copy_path):
                shutil.copy(self.src_path, self.copy_path)
        except Exception as e:
            print("[log-constructor] detail: ", str(e))

        self.lexicon_columns = ["ID", "SynID", "POS", "Sense", "Gloss", "Example", "Label"]

    def read_lexicon(self, labels=[], read_original=False):
        """
        reading lexicon entries
        :param read_original: boolean: True if want to read the original lexicon, False, if the local copy.
        :param labels: list of labels as filter: "0": neutral, "-1": negative, "+1": positive.
        e.g. if only positive and neutral pass labels = ["+1", "0"]
        :return:
        """
        # creating an empty data frame
        df = pd.DataFrame(columns=self.lexicon_columns)

        try:
            # deciding which copy we want to read
            if not read_original and path.exists(self.copy_path):
                tree = ET.parse(self.copy_path)
            else:
                tree = ET.parse(self.src_path)
        except Exception as e:
            print("[log-read] detail: ", str(e))
            return df

        root = tree.getroot()
        for child in root:
            senses = child.attrib['Sense'].split(',')

            # filtering based on label
            if len(labels) == 0 or child.attrib['Label'] in labels:
                df = df.append([{'ID': child.attrib['ID'], 'SynID': child.attrib['SynID'], 'POS': child.attrib['POS'],
                                 'Sense': senses, 'Gloss': child.attrib['Gloss'], 'Example': child.attrib['Example'],
                                 'Label': child.attrib['Label']}], ignore_index=True)
        return df

    def update_labels(self, id_label):
        """
        updating label of synsets by their ID (not SynID)
        :param id_label: dictionary of ids and labels. E.g. {"1": "-1", "2": "+1"}
        :return:
        """
        try:
            tree = ET.parse(self.copy_path)
            root = tree.getroot()
            for child in root:
                if child.attrib["ID"] in id_label:
                    child.attrib["Label"] = id_label[child.attrib["ID"]]

            # writing new info into the local copy
            tree.write(open(self.copy_path, 'w'), encoding='unicode')
        except Exception as e:
            print("[log-update] detail: ", str(e))
