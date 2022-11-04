import sys
import pytest

sys.path.append("../src/sort_css_declarations")

import sort_css_declarations

from typing import Generator
from .expected_output_vars import EXPECTED_HTML_DICT 
from .expected_output_vars import EXPECTED_INCOMPLETE_HTML_DICT 

from .expected_output_vars import EXPECTED_HTML_ELEMS_ORDER 
from .expected_output_vars import EXPECTED_INCOMPLETE_HTML_ELEMS_ORDER

from .expected_output_vars import EXPECTED_ORDERED_HTML_ELEMS
from .expected_output_vars import EXPECTED_ORDERED_INCOMPLETE_HTML_ELEMS # HERE

from .expected_output_vars import EXPECTED_CSS_DICT 

from .expected_output_vars import EXPECTED_FORMATTED_CSS_DICT

from .expected_output_vars import EXPECTED_SORTED_CSS_WITHOUT_HTML
from .expected_output_vars import EXPECTED_SORTED_CSS_WITH_HTML
from .expected_output_vars import EXPECTED_SORTED_CSS_WITH_INCOMPLETE_HTML

from .expected_output_vars import EXPECTED_OUTPUT_WITHOUT_HTML
from .expected_output_vars import EXPECTED_OUTPUT_WITH_HTML

TEST_CSS_PATH = "./test_data/test_css.css"
TEST_HTML_PATH = "./test_data/test_html.html"
TEST_INCOMPLETE_HTML_PATH = "./test_data/test_incomplete_html.html"


def test_read_file():
    data = sort_css_declarations.read_file(TEST_CSS_PATH)
    assert isinstance(data, str)


def test_parse():

    with open(TEST_HTML_PATH, 'r', encoding='UTF-8') as file:
        html_str = file.read()

    test_output_dict = sort_css_declarations._parse(html_str)

    assert test_output_dict == EXPECTED_HTML_DICT 


def test_convert_html_to_dict():
    test_output_dict = sort_css_declarations.convert_html_to_dict(TEST_HTML_PATH)
    
    assert test_output_dict == EXPECTED_HTML_DICT

@pytest.mark.parametrize(
    ('input_x', 'expected'),
    (
        pytest.param(EXPECTED_HTML_DICT['html'], EXPECTED_HTML_ELEMS_ORDER, id='with full-fetched html'),
        pytest.param(EXPECTED_INCOMPLETE_HTML_DICT, EXPECTED_INCOMPLETE_HTML_ELEMS_ORDER, id="with incomplete html")

    )
)
def test_get_identifiers_in_order(input_x, expected):
    test_output_generator_complete = sort_css_declarations.get_identifiers_in_order(input_x)

    assert isinstance(test_output_generator_complete, Generator)
    assert tuple(test_output_generator_complete) == expected


@pytest.mark.parametrize(
    ('input_x', 'expected'),
    (
        pytest.param(TEST_HTML_PATH, EXPECTED_ORDERED_HTML_ELEMS, id='with full-fetched html'),
        pytest.param(TEST_INCOMPLETE_HTML_PATH, EXPECTED_ORDERED_INCOMPLETE_HTML_ELEMS, id="with incomplete html")

    )
)
def test_get_html_element_order(input_x, expected):
    test_output_tuple = sort_css_declarations.get_html_element_order(input_x)

    assert test_output_tuple == expected


def test_css_to_dict():

    TEST_CSS_PATH = "./test_data/test_css.css"

    with open(TEST_CSS_PATH, 'r', encoding='UTF-8') as file:
        css_content = file.read()

        test_output_dict = sort_css_declarations.css_to_dict(css_content)

        assert test_output_dict == EXPECTED_CSS_DICT


def test_format_css_dict():
    test_output_dict = sort_css_declarations.format_css_dict(EXPECTED_CSS_DICT)
    assert test_output_dict == EXPECTED_FORMATTED_CSS_DICT


def test_sort_css_by_keys():
    test_output_dict = sort_css_declarations.sort_css_by_keys(EXPECTED_FORMATTED_CSS_DICT)
    assert test_output_dict == EXPECTED_SORTED_CSS_WITHOUT_HTML


@pytest.mark.parametrize(
    ('input_x', 'expected'),
    (
        pytest.param(EXPECTED_ORDERED_HTML_ELEMS, EXPECTED_SORTED_CSS_WITH_HTML, id='with full-fetched html'),
        pytest.param(EXPECTED_ORDERED_INCOMPLETE_HTML_ELEMS, EXPECTED_SORTED_CSS_WITH_INCOMPLETE_HTML, id="with incomplete html")
    )
)
def test_sort_css_by_html(input_x, expected):
    test_output_dict = sort_css_declarations.sort_css_by_html(EXPECTED_FORMATTED_CSS_DICT, input_x)
    assert test_output_dict == expected

# PARAMETRIZE IT!
def test_generate_output_str():
    test_output_str = sort_css_declarations.generate_output_str(EXPECTED_SORTED_CSS_WITHOUT_HTML, {})
    assert test_output_str == EXPECTED_OUTPUT_WITHOUT_HTML
