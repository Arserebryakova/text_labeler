import spacy
from spacy import displacy


class TextLabelingWrapper:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def label_text(self, text, label_type):
        doc = self.nlp(text)
        if label_type == "ner":
            return self._label_ner(doc)
        elif label_type == "ling":
            return self._label_ling(doc)
        elif label_type == "ling_compact":
            return self._label_ling_compact(doc)
        raise Exception(f"Unkown label type {label_type}")

    def _label_ner(self, doc):
        colors = {
            "ORG": "linear-gradient(90deg, #41295a, #2f0743)",
            "ORDINAL": "linear-gradient(90deg, #2b1a1f, #4e0e29)",
            "MONEY": "linear-gradient(90deg, #373b44, #4286f4)",
            "DATE": "linear-gradient(90deg, #2c3e50, #4ca1af)",
        }
        options = {"colors": colors}
        return displacy.render(doc, style="ent", options=options)

    def _label_ling(self, doc):
        options = {
            "bg": "#212529",
            "color": "white"
        }
        return displacy.render(doc, style="dep", options=options)

    def _label_ling_compact(self, doc):
        options = {
            "compact": True,
            "bg": "#212529",
            "color": "white"
        }
        return displacy.render(doc, style="dep", minify=True, options=options)
