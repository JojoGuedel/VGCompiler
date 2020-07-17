class SyntaxKind:
    invalid_char_token = 0
    end_of_file_token = 101

    int_token = 102
    float_token = 103
    char_token = 104
    string_token = 105
    plus_token = 107
    minus_token = 108
    star_token = 109
    slash_token = 110
    double_star_token = 111
    double_slash_token = 112
    open_parenthesis_token = 113
    close_parenthesis_token = 114
    white_space_token = 115
    identifier_token = 116
    bang_token = 117
    double_ampersand_token = 118
    double_pipe_token = 119
    double_equals_token = 120
    not_equals_token = 121
    less_or_equals_token = 122
    greater_or_equals_token = 123
    less_than_token = 124
    greater_than_token = 125

    literal_expression = 200
    unary_expression = 201
    binary_expression = 202
    parenthesized_expression = 203

    true_keyword = 300
    false_keyword = 301

    @classmethod
    def str(cls, kind):
        if kind == cls.invalid_char_token:
            return "invalid_char_token"
        elif kind == cls.end_of_file_token:
            return "end_of_file_token"
        elif kind == cls.int_token:
            return "int_token"
        elif kind == cls.float_token:
            return "float_token"
        elif kind == cls.char_token:
            return "char_token"
        elif kind == cls.string_token:
            return "string_token"
        elif kind == cls.plus_token:
            return "plus_token"
        elif kind == cls.minus_token:
            return "minus_token"
        elif kind == cls.star_token:
            return "star_token"
        elif kind == cls.slash_token:
            return "slash_token"
        elif kind == cls.double_star_token:
            return "double_star_token"
        elif kind == cls.double_slash_token:
            return "double_slash_token"
        elif kind == cls.open_parenthesis_token:
            return "open_parenthesis_token"
        elif kind == cls.close_parenthesis_token:
            return "close_parenthesis_token"
        elif kind == cls.white_space_token:
            return "white_space_token"
        elif kind == cls.identifier_token:
            return "identifier_token"
        elif kind == cls.bang_token:
            return "bang_token"
        elif kind == cls.double_ampersand_token:
            return "double_ampersand_token"
        elif kind == cls.double_pipe_token:
            return "double_pipe_token"
        elif kind == cls.double_equals_token:
            return "double_equals_token"
        elif kind == cls.not_equals_token:
            return "not_equals_token"
        elif kind == cls.less_or_equals_token:
            return "less_or_equals_token"
        elif kind == cls.greater_or_equals_token:
            return "greater_or_equals_token"
        elif kind == cls.less_than_token:
            return "less_than"
        elif kind == cls.greater_than_token:
            return "greater_than"

        elif kind == cls.literal_expression:
            return "literal_expression"
        elif kind == cls.unary_expression:
            return "unary_expression"
        elif kind == cls.binary_expression:
            return "binary_expression"
        elif kind == cls.parenthesized_expression:
            return "parenthesized_expression"

        elif kind == cls.true_keyword:
            return "true_keyword"
        elif kind == cls.false_keyword:
            return "false_keyword"

        else:
            return f"invalid_syntax_kind: {kind}"

    @classmethod
    def get_binary_operator_precedence(cls, kind):
        if kind == cls.double_star_token or kind == cls.double_slash_token:
            return 6
        elif kind == cls.star_token or kind == cls.slash_token:
            return 5
        elif kind == cls.plus_token or kind == cls.minus_token:
            return 4
        elif kind == cls.less_than_token or kind == cls.greater_or_equals_token or kind == cls.double_equals_token or kind == cls.less_than_token or kind == cls.greater_than_token:
            return 3
        elif kind == cls.double_ampersand_token:
            return 2
        elif kind == cls.double_pipe_token:
            return 1
        else:
            return 0

    @classmethod
    def get_unary_operator_precedence(cls, kind):
        if kind == cls.plus_token or kind == cls.minus_token:
            return 7
        elif kind == cls.bang_token:
            return 6
        else:
            return 0

    @classmethod
    def get_keyword_kind(cls, text):
        if text == "true":
            return cls.true_keyword
        elif text == "false":
            return cls.false_keyword
        else:
            return cls.identifier_token
