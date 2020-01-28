import pandas as pd
import xml.etree.ElementTree as et


class LexiPy:
    def __init__(self):
        self.lexicon_path = 'data/adj-final.xml'
        self.lexicon_columns = ["ID", "SynID", "POS", "Sense", "Gloss", "Example", "Label"]

    def read_synsets(self, labels=[]):
        """
        reading lexicon entries
        :param labels: list of labels: "0": neutral, "-1": negative, "+1": positive.
        e.g. if only positive and neutral pass labels = ["+1", "0"]
        :return:
        """
        # creating an empty data frame
        df = pd.DataFrame(columns=self.lexicon_columns)
        tree = et.parse(self.lexicon_path)
        root = tree.getroot()
        for child in root:
            senses = child.attrib['Sense'].split(',')

            # filtering based on label
            if len(labels) == 0 or child.attrib['Label'] in labels:
                df = df.append([{'ID': child.attrib['ID'], 'SynID': child.attrib['SynID'], 'POS': child.attrib['POS'],
                                 'Sense': senses, 'Gloss': child.attrib['Gloss'], 'Example': child.attrib['Example'],
                                 'Label': child.attrib['Label']}], ignore_index=True)
        return df
