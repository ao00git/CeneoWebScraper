def extract_element(dom_tree, selector, attribute=None):
    try:
        if attribute:
            if isinstance(attribute,str):
                return opinion.select(selector).pop(0)[attribute].strip()
            else:
                return [x.get_text().strip() for x in opinion.select(selector)]
        else:
            return opinion.select(selector).pop(0).get_text().strip()
    except IndexError:
        return None