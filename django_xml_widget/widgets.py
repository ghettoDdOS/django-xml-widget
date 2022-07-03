from django import forms


class XMLTreeViewWidget(forms.Widget):
    template_name = "xml-tree-view.html"

    class Media:
        js = (
            "js/simpleXML.js",
            "js/jquery-3.6.0.min.js",
        )
        css = {"all": ("css/simpleXML.css")}
