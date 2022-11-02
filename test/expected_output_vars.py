EXPECTED_HTML_DICT = {
    "html": [
        {
            "attributes": {"lang": "en"},
            "head": [
                {
                    "meta": [
                        {"attributes": {"charset": "UTF-8"}},
                        {
                            "attributes": {
                                "http-equiv": "X-UA-Compatible",
                                "content": "IE=edge",
                            }
                        },
                        {
                            "attributes": {
                                "name": "viewport",
                                "content": "width=device-width, initial-scale=1.0",
                            }
                        },
                    ],
                    "link": [
                        {
                            "attributes": {
                                "rel": ["stylesheet"],
                                "href": "./css/style.css",
                            }
                        }
                    ],
                    "title": [{}],
                }
            ],
            "body": [
                {
                    "div": [
                        {
                            "attributes": {"class": ["banner-container"]},
                            "h3": [{"u": [{}]}],
                        },
                        {
                            "attributes": {"class": ["form-container"]},
                            "div": [
                                {
                                    "attributes": {"class": ["form-wrapper"]},
                                    "form": [
                                        {
                                            "attributes": {
                                                "action": "index.php",
                                                "method": "post",
                                                "enctype": "multipart/form-data",
                                            },
                                            "div": [
                                                {
                                                    "attributes": {
                                                        "class": ["upload-field"]
                                                    },
                                                    "label": [
                                                        {
                                                            "attributes": {
                                                                "for": "file"
                                                            },
                                                            "u": [{}],
                                                        }
                                                    ],
                                                    "input": [
                                                        {
                                                            "attributes": {
                                                                "type": "file",
                                                                "name": "file",
                                                            }
                                                        }
                                                    ],
                                                },
                                                {
                                                    "attributes": {
                                                        "class": ["submit-wrapper"]
                                                    },
                                                    "button": [
                                                        {
                                                            "attributes": {
                                                                "class": ["button"],
                                                                "type": "submit",
                                                                "name": "upload",
                                                            }
                                                        }
                                                    ],
                                                },
                                            ],
                                        }
                                    ],
                                }
                            ],
                        },
                        {
                            "attributes": {
                                "id": "test_id",
                                "class": ["output-container"],
                            },
                            "div": [
                                {"attributes": {"class": ["output-wrapper"]}, "p": [{}]}
                            ],
                        },
                    ]
                }
            ],
        }
    ]
}

EXPECTED_INCOMPLETE_HTML_DICT = {
    "div": [{"attributes": {"class": ["banner-container"]}, "h3": [{"u": [{}]}]}]
}

EXPECTED_HTML_ELEMS_ORDER = (
    "body",
    "div",
    ".banner-container",
    "h3",
    "u",
    ".form-container",
    "div",
    ".form-wrapper",
    "form",
    "div",
    ".upload-field",
    "label",
    "u",
    "input",
    ".submit-wrapper",
    "button",
    ".button",
    "#test_id",
    ".output-container",
    "div",
    ".output-wrapper",
    "p",
)

EXPECTED_INCOMPLETE_HTML_ELEMS_ORDER = ("div", ".banner-container", "h3", "u")


EXPECTED_ORDERED_HTML_ELEMS = (
    "body",
    "div",
    ".banner-container",
    "h3",
    "u",
    ".form-container",
    ".form-wrapper",
    "form",
    ".upload-field",
    "label",
    "input",
    ".submit-wrapper",
    "button",
    ".button",
    "#test_id",
    ".output-container",
    ".output-wrapper",
    "p",
)

EXPECTED_ORDERED_INCOMPLETE_HTML_ELEMS = ("div", ".banner-container", "h3", "u")

EXPECTED_CSS_DICT = {
    ".banner-container": {"comment": "", "props": "background: #BEBEBE"},
    ".output-container, .submit-wrapper, .form-container, .form-wrapper, .banner-container": {
        "comment": "",
        "props": "display: flex;\njustify-content: center;\nalign-items: center",
    },
    ".form-wrapper": {
        "comment": "",
        "props": "border: 1px solid black;\nborder-radius: 5px;\nmargin: 0.8rem 0 0 0;\nbackground: rgb(218, 226, 218);\nbackground: linear-gradient(90deg, rgba(218, 226, 218, 1) 26%, rgba(199, 199, 209, 1) 100%, rgba(0, 255, 23, 1) 100%);\npadding: 1rem",
    },
    ".upload-field": {
        "comment": "",
        "props": "display: grid;\njustify-content: center;\nalign-items: center",
    },
    ".button": {
        "comment": "",
        "props": "align-items: center;\nborder: 1px solid #787878;\nborder-radius: 12px;\nbox-shadow: transparent 0 0 0 3px, rgba(18, 18, 18, 0.1) 0 6px 20px;\nbox-sizing: border-box;\ncolor: #121412;\ncursor: pointer;\ndisplay: inline-flex;\nfont-family: Inter, sans-serif;\nfont-size: 1rem;\nfont-weight: 500;\njustify-content: center;\nline-height: 1;\nmargin: 0.8rem 0 0 0;\noutline: none;\npadding: 0.8rem 1rem;\ntext-align: center;\ntext-decoration: none;\ntransition: box-shadow 0.2s, -webkit-box-shadow 0.2s;\nwhite-space: nowrap;\nuser-select: none",
    },
    ".button:hover": {
        "comment": "",
        "props": "box-shadow: #C0C0C0 0 0 0 3px, transparent 0 0 0 0",
    },
    ".output-container": {"comment": "", "props": "padding: 2rem"},
    ".output-wrapper": {"comment": "", "props": "width: 35rem"},
    ".output-wrapper p": {"comment": "/*TEST COMMENT*/", "props": "text-align: center"},
    ".radio-btn-wrapper": {
        "comment": "",
        "props": "display: flex;\njustify-content: space-between;\nwidth: 100%",
    },
}

EXPECTED_FORMATTED_CSS_DICT = {
    ".banner-container": {
        "comment": "",
        "props": [
            "align-items: center",
            "background: #BEBEBE",
            "display: flex",
            "justify-content: center",
        ],
    },
    ".output-container": {
        "comment": "",
        "props": [
            "align-items: center",
            "display: flex",
            "justify-content: center",
            "padding: 2rem",
        ],
    },
    ".submit-wrapper": {
        "comment": "",
        "props": ["align-items: center", "display: flex", "justify-content: center"],
    },
    ".form-container": {
        "comment": "",
        "props": ["align-items: center", "display: flex", "justify-content: center"],
    },
    ".form-wrapper": {
        "comment": "",
        "props": [
            "align-items: center",
            "background: linear-gradient(90deg, rgba(218, 226, 218, 1) 26%, rgba(199, 199, 209, 1) 100%, rgba(0, 255, 23, 1) 100%)",
            "background: rgb(218, 226, 218)",
            "border-radius: 5px",
            "border: 1px solid black",
            "display: flex",
            "justify-content: center",
            "margin: 0.8rem 0 0 0",
            "padding: 1rem",
        ],
    },
    ".upload-field": {
        "comment": "",
        "props": ["align-items: center", "display: grid", "justify-content: center"],
    },
    ".button": {
        "comment": "",
        "props": [
            "align-items: center",
            "border-radius: 12px",
            "border: 1px solid #787878",
            "box-shadow: transparent 0 0 0 3px, rgba(18, 18, 18, 0.1) 0 6px 20px",
            "box-sizing: border-box",
            "color: #121412",
            "cursor: pointer",
            "display: inline-flex",
            "font-family: Inter, sans-serif",
            "font-size: 1rem",
            "font-weight: 500",
            "justify-content: center",
            "line-height: 1",
            "margin: 0.8rem 0 0 0",
            "outline: none",
            "padding: 0.8rem 1rem",
            "text-align: center",
            "text-decoration: none",
            "transition: box-shadow 0.2s, -webkit-box-shadow 0.2s",
            "user-select: none",
            "white-space: nowrap",
        ],
    },
    ".button:hover": {
        "comment": "",
        "props": ["box-shadow: #C0C0C0 0 0 0 3px, transparent 0 0 0 0"],
    },
    ".output-wrapper": {"comment": "", "props": ["width: 35rem"]},
    ".output-wrapper p": {
        "comment": "/*TEST COMMENT*/",
        "props": ["text-align: center"],
    },
    ".radio-btn-wrapper": {
        "comment": "",
        "props": ["display: flex", "justify-content: space-between", "width: 100%"],
    },
}

EXPECTED_SORTED_CSS_WITHOUT_HTML = {
    ".banner-container": {
        "comment": "",
        "props": [
            "align-items: center",
            "background: #BEBEBE",
            "display: flex",
            "justify-content: center",
        ],
    },
    ".button": {
        "comment": "",
        "props": [
            "align-items: center",
            "border-radius: 12px",
            "border: 1px solid #787878",
            "box-shadow: transparent 0 0 0 3px, rgba(18, 18, 18, 0.1) 0 6px 20px",
            "box-sizing: border-box",
            "color: #121412",
            "cursor: pointer",
            "display: inline-flex",
            "font-family: Inter, sans-serif",
            "font-size: 1rem",
            "font-weight: 500",
            "justify-content: center",
            "line-height: 1",
            "margin: 0.8rem 0 0 0",
            "outline: none",
            "padding: 0.8rem 1rem",
            "text-align: center",
            "text-decoration: none",
            "transition: box-shadow 0.2s, -webkit-box-shadow 0.2s",
            "user-select: none",
            "white-space: nowrap",
        ],
    },
    ".button:hover": {
        "comment": "",
        "props": ["box-shadow: #C0C0C0 0 0 0 3px, transparent 0 0 0 0"],
    },
    ".form-container": {
        "comment": "",
        "props": ["align-items: center", "display: flex", "justify-content: center"],
    },
    ".form-wrapper": {
        "comment": "",
        "props": [
            "align-items: center",
            "background: linear-gradient(90deg, rgba(218, 226, 218, 1) 26%, rgba(199, 199, 209, 1) 100%, rgba(0, 255, 23, 1) 100%)",
            "background: rgb(218, 226, 218)",
            "border-radius: 5px",
            "border: 1px solid black",
            "display: flex",
            "justify-content: center",
            "margin: 0.8rem 0 0 0",
            "padding: 1rem",
        ],
    },
    ".output-container": {
        "comment": "",
        "props": [
            "align-items: center",
            "display: flex",
            "justify-content: center",
            "padding: 2rem",
        ],
    },
    ".output-wrapper": {"comment": "", "props": ["width: 35rem"]},
    ".output-wrapper p": {
        "comment": "/*TEST COMMENT*/",
        "props": ["text-align: center"],
    },
    ".radio-btn-wrapper": {
        "comment": "",
        "props": ["display: flex", "justify-content: space-between", "width: 100%"],
    },
    ".submit-wrapper": {
        "comment": "",
        "props": ["align-items: center", "display: flex", "justify-content: center"],
    },
    ".upload-field": {
        "comment": "",
        "props": ["align-items: center", "display: grid", "justify-content: center"],
    },
}

EXPECTED_SORTED_CSS_WITH_HTML = {
    ".banner-container": {
        "comment": "",
        "props": [
            "align-items: center",
            "background: #BEBEBE",
            "display: flex",
            "justify-content: center",
        ],
    },
    ".form-container": {
        "comment": "",
        "props": ["align-items: center", "display: flex", "justify-content: center"],
    },
    ".form-wrapper": {
        "comment": "",
        "props": [
            "align-items: center",
            "background: linear-gradient(90deg, rgba(218, 226, 218, 1) 26%, rgba(199, 199, 209, 1) 100%, rgba(0, 255, 23, 1) 100%)",
            "background: rgb(218, 226, 218)",
            "border-radius: 5px",
            "border: 1px solid black",
            "display: flex",
            "justify-content: center",
            "margin: 0.8rem 0 0 0",
            "padding: 1rem",
        ],
    },
    ".upload-field": {
        "comment": "",
        "props": ["align-items: center", "display: grid", "justify-content: center"],
    },
    ".submit-wrapper": {
        "comment": "",
        "props": ["align-items: center", "display: flex", "justify-content: center"],
    },
    ".button": {
        "comment": "",
        "props": [
            "align-items: center",
            "border-radius: 12px",
            "border: 1px solid #787878",
            "box-shadow: transparent 0 0 0 3px, rgba(18, 18, 18, 0.1) 0 6px 20px",
            "box-sizing: border-box",
            "color: #121412",
            "cursor: pointer",
            "display: inline-flex",
            "font-family: Inter, sans-serif",
            "font-size: 1rem",
            "font-weight: 500",
            "justify-content: center",
            "line-height: 1",
            "margin: 0.8rem 0 0 0",
            "outline: none",
            "padding: 0.8rem 1rem",
            "text-align: center",
            "text-decoration: none",
            "transition: box-shadow 0.2s, -webkit-box-shadow 0.2s",
            "user-select: none",
            "white-space: nowrap",
        ],
    },
    ".button:hover": {
        "comment": "",
        "props": ["box-shadow: #C0C0C0 0 0 0 3px, transparent 0 0 0 0"],
    },
    ".output-container": {
        "comment": "",
        "props": [
            "align-items: center",
            "display: flex",
            "justify-content: center",
            "padding: 2rem",
        ],
    },
    ".output-wrapper": {"comment": "", "props": ["width: 35rem"]},
    ".output-wrapper p": {
        "comment": "/*TEST COMMENT*/",
        "props": ["text-align: center"],
    },
}

EXPECTED_SORTED_CSS_WITH_INCOMPLETE_HTML = {
    ".banner-container": {
        "comment": "",
        "props": [
            "align-items: center",
            "background: #BEBEBE",
            "display: flex",
            "justify-content: center",
        ],
    }
}


EXPECTED_OUTPUT_WITHOUT_HTML = """\n.banner-container {\n    align-items: center;\n    background: #BEBEBE;\n    display: flex;\n    justify-content: center;\n}\n\n.button {\n    align-items: center;\n    border-radius: 12px;\n    border: 1px solid #787878;\n    box-shadow: transparent 0 0 0 3px, rgba(18, 18, 18, 0.1) 0 6px 20px;\n    box-sizing: border-box;\n    color: #121412;\n    cursor: pointer;\n    display: inline-flex;\n    font-family: Inter, sans-serif;\n    font-size: 1rem;\n    font-weight: 500;\n    justify-content: center;\n    line-height: 1;\n    margin: 0.8rem 0 0 0;\n    outline: none;\n    padding: 0.8rem 1rem;\n    text-align: center;\n    text-decoration: none;\n    transition: box-shadow 0.2s, -webkit-box-shadow 0.2s;\n    user-select: none;\n    white-space: nowrap;\n}\n\n.button:hover {\n    box-shadow: #C0C0C0 0 0 0 3px, transparent 0 0 0 0;\n}\n\n.form-container {\n    align-items: center;\n    display: flex;\n    justify-content: center;\n}\n\n.form-wrapper {\n    align-items: center;\n    background: linear-gradient(90deg, rgba(218, 226, 218, 1) 26%, rgba(199, 199, 209, 1) 100%, rgba(0, 255, 23, 1) 100%);\n    background: rgb(218, 226, 218);\n    border-radius: 5px;\n    border: 1px solid black;\n    display: flex;\n    justify-content: center;\n    margin: 0.8rem 0 0 0;\n    padding: 1rem;\n}\n\n.output-container {\n    align-items: center;\n    display: flex;\n    justify-content: center;\n    padding: 2rem;\n}\n\n.output-wrapper {\n    width: 35rem;\n}\n\n/*TEST COMMENT*/\n.output-wrapper p {\n    text-align: center;\n}\n\n.radio-btn-wrapper {\n    display: flex;\n    justify-content: space-between;\n    width: 100%;\n}\n\n.submit-wrapper {\n    align-items: center;\n    display: flex;\n    justify-content: center;\n}\n\n.upload-field {\n    align-items: center;\n    display: grid;\n    justify-content: center;\n}\n"""

EXPECTED_OUTPUT_WITH_HTML = """\n.banner-container {\n    align-items: center;\n    background: #BEBEBE;\n    display: flex;\n    justify-content: center;\n}\n\n.form-container {\n    align-items: center;\n    display: flex;\n    justify-content: center;\n}\n\n.form-wrapper {\n    align-items: center;\n    background: linear-gradient(90deg, rgba(218, 226, 218, 1) 26%, rgba(199, 199, 209, 1) 100%, rgba(0, 255, 23, 1) 100%);\n    background: rgb(218, 226, 218);\n    border-radius: 5px;\n    border: 1px solid black;\n    display: flex;\n    justify-content: center;\n    margin: 0.8rem 0 0 0;\n    padding: 1rem;\n}\n\n.upload-field {\n    align-items: center;\n    display: grid;\n    justify-content: center;\n}\n\n.submit-wrapper {\n    align-items: center;\n    display: flex;\n    justify-content: center;\n}\n\n.button {\n    align-items: center;\n    border-radius: 12px;\n    border: 1px solid #787878;\n    box-shadow: transparent 0 0 0 3px, rgba(18, 18, 18, 0.1) 0 6px 20px;\n    box-sizing: border-box;\n    color: #121412;\n    cursor: pointer;\n    display: inline-flex;\n    font-family: Inter, sans-serif;\n    font-size: 1rem;\n    font-weight: 500;\n    justify-content: center;\n    line-height: 1;\n    margin: 0.8rem 0 0 0;\n    outline: none;\n    padding: 0.8rem 1rem;\n    text-align: center;\n    text-decoration: none;\n    transition: box-shadow 0.2s, -webkit-box-shadow 0.2s;\n    user-select: none;\n    white-space: nowrap;\n}\n\n.button:hover {\n    box-shadow: #C0C0C0 0 0 0 3px, transparent 0 0 0 0;\n}\n\n.output-container {\n    align-items: center;\n    display: flex;\n    justify-content: center;\n    padding: 2rem;\n}\n\n.output-wrapper {\n    width: 35rem;\n}\n\n/*TEST COMMENT*/\n.output-wrapper p {\n    text-align: center;\n}\n"""
