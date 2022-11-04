import argparse
import logging
import re
from typing import Any
from typing import Dict
from typing import Generator
from typing import List
from typing import Tuple
from typing import Union

import bs4
import cssutils  # type: ignore

# To silence the warnings and error messages in stdout while using cssutils.parseString.
# It's not informative, doesn't affect the funcionality
# of the stylesheet and unnecessarly verbose.
cssutils.log.setLevel(logging.CRITICAL)


def read_file(path: str) -> str:

    with open(path, "r", encoding="UTF-8") as file:
        css_content = file.read()

    return css_content


def recurse(
    html_groups: Union[bs4.BeautifulSoup, Any], collector_dict: Dict[Any, Any]
) -> Dict[str, List[str | Dict[str, Any]] | Dict[str, str | List[Any]]]:
    "Recursively iterates the BeautifulSoup4.html_parse return."

    for group in html_groups:

        # MyPy cannot resolve properly the bs4 annotations.
        # "Re-cast" it as bs4.element.Tag solves complains
        # for the rest of the func.
        element: bs4.element.Tag = group  # type: ignore

        if not isinstance(group, str):

            if not element.name in collector_dict:
                collector_dict[element.name] = []

            tmp_collector: dict[str, Any] = {}

            if element.attrs:
                tmp_collector = {"attributes": element.attrs}

            collector_dict[element.name] += (recurse(group, tmp_collector),)

    return collector_dict


def _parse(
    html_string: str,
) -> Dict[str, List[str | Dict[str, Any]] | Dict[str, str | List[Any]]]:
    """Recursively parses the html_groups from BeautifulSoup4.html_parse and
    fetches to a hierarchical dictionary."""

    soup: bs4.BeautifulSoup = bs4.BeautifulSoup(html_string, "html.parser")

    child_ls: list[bs4.PageElement] = [child for child in soup.contents]

    return recurse(child_ls, {})


def convert_html_to_dict(
    path: str,
) -> Dict[str, List[Any] | Any]:
    "Converts html to dictionary calling on _parse function."
    return _parse(read_file(path))


def get_identifiers_in_order(
    html_dict: List[Dict[str, List[Any]]] | Dict[str, List[Any]]
) -> Generator[str, None, None]:
    """Starting from the body tag, recurses the html tree, and yield all the
    tags, IDs and class names."""

    start_node: List[Dict[str, List[Any]]] | Dict[str, List[Any]] = html_dict

    if isinstance(html_dict, list):
        if "body" in html_dict[0]:
            yield "body"
            start_node = html_dict[0]["body"]

    # Could be reduced with some smart move, but don't bother doing it. The
    # more explicit is, the easier is to debug.
    # ======================================================================
    if isinstance(start_node, list):
        for dictionary in start_node:
            for key, value in dictionary.items():

                if key == "attributes":
                    if "id" in value:
                        yield f"#{value['id']}"  # type: ignore
                    if "class" in value:
                        for class_name in value["class"]:  # type: ignore
                            yield f".{class_name}"

                if key != "attributes":
                    yield key

                if isinstance(value, list):
                    yield from get_identifiers_in_order(value)

    elif isinstance(start_node, dict):
        for key, value in start_node.items():

            if key == "attributes":
                if "id" in value:
                    yield f"#{value['id']}"  # type: ignore
                if "class" in value:
                    for class_name in value["class"]:  # type: ignore
                        yield f".{class_name}"

            if key != "attributes":
                yield key

            if isinstance(value, list):
                yield from get_identifiers_in_order(value)
    # ======================================================================


def get_html_element_order(path: str) -> Tuple[str, ...]:
    """Runs all the parsing and recursing functions, then returns the
    identifiers in the same order as in the html tree."""

    html_dict: Dict[str, List[Any] | Any] = convert_html_to_dict(path)

    identifiers_in_order: Generator[str, None, None]

    try:
        identifiers_in_order = get_identifiers_in_order(html_dict["html"])

    # If KeyError occurs, that means, that the HTML is only partial, not a
    # full-fetched HTML page.
    except KeyError:
        identifiers_in_order = get_identifiers_in_order(html_dict)

    identifiers_without_dups: Tuple[str, ...] = tuple(
        dict.fromkeys(identifiers_in_order)
    )

    return identifiers_without_dups


def css_to_dict(css_content: str) -> dict[str, dict[str, str]]:
    "Reads, parses, converts CSS to dictionary."

    css_dict: dict[str, dict[str, str]] = {}
    sheet: cssutils.css.cssstylesheet.CSSStyleSheet = cssutils.parseString(css_content)

    comment = ""

    for rule in sheet.cssRules:

        if type(rule) == cssutils.css.csscomment.CSSComment:
            comment = rule.cssText
        elif type(rule) == cssutils.css.CSSMediaRule:
            # The media queries will be processed in the media_rules_to_dict function.
            pass

        elif type(rule) == cssutils.css.CSSImportRule:

            if "/*IMPORTS*/" not in css_dict.keys():
                css_dict.setdefault("/*IMPORTS*/", {"comment": "", "props": ""})

            css_dict["/*IMPORTS*/"]["comment"] = ""
            css_dict["/*IMPORTS*/"]["props"] += f"{rule.cssText}\n"
        else:
            if rule.selectorText not in css_dict.keys():
                css_dict.setdefault(rule.selectorText, {"comment": "", "props": ""})

            css_dict[rule.selectorText]["comment"] = comment
            css_dict[rule.selectorText]["props"] = rule.style.cssText

            comment = ""

    return css_dict


def format_css_dict(
    css_dict: dict[str, dict[str, str]]
) -> dict[str, dict[str, str | list[str]]]:
    "Separates the string dump of properties into a list[str]."

    formated_css_dict: dict[str, dict[str, str | list[str]]] = {}

    for selectors, values in css_dict.items():

        split_properties: list[str] = re.split(";", values["props"])
        split_properties = [prop.replace("\n", "").strip() for prop in split_properties]

        if selectors == "/*IMPORTS*/":

            if "/*IMPORTS*/" not in formated_css_dict:
                imports: List[str] = [
                    prop.strip(";") for prop in values["props"].split("\n")
                ]
                formated_css_dict.setdefault(
                    "/*IMPORTS*/", {"comment": values["comment"], "props": imports}
                )

        else:

            for selector in selectors.split(","):

                selector = selector.strip()

                if selector not in formated_css_dict:
                    formated_css_dict.setdefault(
                        selector,
                        {"comment": values["comment"], "props": split_properties},
                    )

                else:
                    formated_css_dict[selector]["comment"] += values["comment"]  # type: ignore
                    formated_css_dict[selector]["props"] = [
                        *formated_css_dict[selector]["props"],
                        *split_properties,
                    ]

    return {
        key: {"comment": value["comment"], "props": sorted(value["props"])}
        for key, value in formated_css_dict.items()
    }


def sort_css_by_keys(
    css_dict: Dict[str, Dict[str, str | List[str]]]
) -> Dict[str, Dict[str, str | List[str]]]:
    """Orders the tags alphabetically, then ids, classes alphabetically.
    Return both as a merged dictionary."""

    imports: Dict[str, Dict[str, str | List[str]]] = {
        key: css_dict[key] for key in sorted(css_dict) if key == "/*IMPORTS*/"
    }

    tags: Dict[str, Dict[str, str | List[str]]] = {
        key: css_dict[key] for key in sorted(css_dict) if not key.startswith((".", "#"))
    }
    ids_classes: Dict[str, Dict[str, str | List[str]]] = {
        key: css_dict[key] for key in sorted(css_dict) if key.startswith((".", "#"))
    }

    return {**imports, **tags, **ids_classes}


def sort_css_by_html(
    css_dict: Dict[str, Dict[str, Any]], html_element_order: Tuple[str, ...]
) -> Dict[str, Dict[str, str | List[str]]]:
    """Loops through the html_element_order identifiers, and return the
    key-value from css_dict in the order of the identifiers."""

    result: Dict[str, Dict[str, str | List[str]]] = {}

    for html_elem in html_element_order:
        for css, value in css_dict.items():

            base_selector: str = list(filter(None, re.split(" |:", css)))[0].strip()

            if (
                # Split up the class or id from any selectors.
                base_selector == html_elem
                or base_selector == "html"
                or css.startswith((":", "*"))
                and css not in result
            ):
                result[css] = value

    return result


def media_rules_to_dict(
    css_content: str,
) -> Dict[str, List[Dict[str, str | List[str]]]]:
    """Reads, parses the css_content, searches for media query declarations,
    then converts them to dictionary."""

    # cssutils has poor documentation about how to get the @media specification
    # only, show this issue has been solved by regex for now.
    media_rule_token: re.Pattern = re.compile(r"(@media.*){")

    sheet: cssutils.css.cssstylesheet.CSSStyleSheet = cssutils.parseString(css_content)

    # Get all the media queries from the object blob.
    media_queries: List[cssutils.css.cssmediarule.CSSMediaRule] = [
        x for x in sheet if isinstance(x, cssutils.css.cssmediarule.CSSMediaRule)
    ]

    # Init the "collectors".
    media_rules_dict: Dict[str, List[Dict[str, str | List[str]]]] = {}
    comment: str = ""

    for m_query in media_queries:
        media_rule: str = re.findall(media_rule_token, m_query.cssText)[0]

        if media_rule not in media_rules_dict.keys():
            media_rules_dict.setdefault(media_rule, [])

        for css_rule in m_query:

            if type(css_rule) == cssutils.css.csscomment.CSSComment:
                comment = css_rule.cssText

            elif type(css_rule) == cssutils.css.CSSStyleRule:

                props_ls: List[str] = list(
                    map(lambda x: x.strip(";"), css_rule.style.cssText.split("\n"))
                )

                tmp: Dict[str, str | List[str]] = {}
                tmp["css_selector"] = css_rule.selectorText
                tmp["comment"] = comment
                tmp["props"] = props_ls

                media_rules_dict[media_rule].append(tmp)

                # Reset the "comment collector"
                comment = ""

    result: Dict[str, List[Dict[str, str | List[str]]]] = {}

    for key, value in media_rules_dict.items():

        if key not in result.keys():
            result.setdefault(key, [])

        for selector_dict in value:
            result[key].append(
                {
                    "css_selector": selector_dict["css_selector"],
                    "comment": selector_dict["comment"],
                    "props": sorted(selector_dict["props"]),
                }
            )

    return result


def sort_media_queries_by_html(
    media_rules_dict: Dict[str, List[Dict[str, str | List[str]]]],
    html_element_order: Tuple[str, ...],
) -> Dict[str, List[Dict[str, str | List[str]]]]:
    """Loops through the html_element_order identifiers, and return the
    key-value from media_rules_dict in the order of the identifiers."""

    result: Dict[str, List[Dict[str, str | List[str]]]] = {}

    for html_elem in html_element_order:

        for media, dict_ls in media_rules_dict.items():

            for selector_dict in dict_ls:

                base_selector: str = list(filter(None, re.split(" |:", selector_dict["css_selector"])))[0].strip()  # type: ignore

                if (
                    # Split up the class or id from any selectors.
                    base_selector == html_elem
                    or base_selector == "html"
                    or selector_dict["css_selector"].startswith((":", "*"))  # type: ignore
                    and media not in result
                ):
                    result[media] = dict_ls

    return result


def generate_output_str(
    css_dict: Dict[str, Dict[str, str | List[str]]],
    sorted_media_queries: Dict[str, List[Dict[str, str | List[str]]]],
) -> str:
    """Loops through the CSS and media query dictionary, then returns the content
    as a formated string."""

    result_str: str = ""

    for key, value in css_dict.items():

        if value["comment"]:
            result_str += f"\n{value['comment']}\n"
        else:
            result_str += "\n"

        # If they are import declarations..
        if key == "/*IMPORTS*/":
            result_str += f'{key}\n'

            for prop in list(filter(None, value["props"])):
                result_str += f"{prop};\n"

        # If they are normal CSS rules.
        else:
            result_str += f"{key} {{\n"

            for prop in value["props"]:
                result_str += f"    {prop};\n"

        if key != "/*IMPORTS*/":
            result_str += "}\n"

    for key, value in sorted_media_queries.items():  # type: ignore
        result_str += f"\n{key} {{"

        for selector_dict in value:

            if selector_dict["comment"]:  # type: ignore
                result_str += f"\n    {selector_dict['comment']}\n"  # type: ignore
            else:
                result_str += "\n"

            result_str += f'    {selector_dict["css_selector"]} {{\n'  # type: ignore

            for prop in selector_dict["props"]:  # type: ignore
                result_str += f"        {prop};\n"

            result_str += "    }\n"

        result_str += "}\n"

    return result_str


def main() -> None:

    parser = argparse.ArgumentParser(
        prog="sort_css",
        description="""Sorts CSS declarations. Without the
        "--by_html" it sorts first the tags alphabetically, then IDs and
        classes. """,
    )

    parser.add_argument(
        "filenames", metavar="target", nargs="*", help="CSS file's path."
    )

    parser.add_argument(
        "--by_html",
        action="store",
        type=str,
        help="Order CSS declarations by HTML's order.",
    )

    parser.add_argument(
        "-i",
        "--in_place",
        action="store_true",
        help="Edits file in-place.",
    )

    args = parser.parse_args()

    filenames: List[str] = args.filenames
    by_html: str = args.by_html
    in_place: bool = args.in_place

    for file_path in filenames:
        css_content: str = read_file(file_path)

        css_dict: Dict[str, Dict[str, str]] = css_to_dict(css_content)

        formated_css_dict: Dict[str, Dict[str, str | List[str]]] = format_css_dict(
            css_dict
        )

        media_rules_dict: Dict[
            str, List[Dict[str, str | List[str]]]
        ] = media_rules_to_dict(css_content)

        # Evaluates if --by_html is used and generates the formated
        # dictionaries correspondingly.
        # ===============================
        sorted_css: Dict[str, Dict[str, str | List[str]]]
        sorted_media_queries: Dict[str, List[Dict[str, str | List[str]]]]

        if by_html:
            ordered_html_elems: Tuple[str, ...] = get_html_element_order(by_html)

            sorted_css = sort_css_by_html(formated_css_dict, ordered_html_elems)
            sorted_media_queries = sort_media_queries_by_html(
                media_rules_dict, ordered_html_elems
            )

        else:
            sorted_css = sort_css_by_keys(formated_css_dict)
            sorted_media_queries = media_rules_dict
        # ===============================

        css_output: str = generate_output_str(sorted_css, sorted_media_queries)

        # ===============================
        if in_place:
            with open(file_path, "w", encoding="UTF-8") as file:
                file.write(css_output)
                print(f"{file_path} formated successfully!")
        else:
            print(css_output)
        # ===============================


if __name__ == "__main__":
    main()
