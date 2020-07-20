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
    equals_token = 126
    plus_equals_token = 127
    minus_equals_token = 128
    star_equals_token = 129
    slash_equals_token = 130

    literal_expression = 200
    unary_expression = 201
    binary_expression = 202
    parenthesized_expression = 203
    variable_expression = 204
    assignment_expression = 205
    additional_assignment_expression = 206

    true_keyword = 300
    false_keyword = 301

    str = {
        invalid_char_token: "invalid_char_token",
        end_of_file_token: "end_of_file_token",

        int_token: "int_token",
        float_token: "float_token",
        char_token: "char_token",
        string_token: "string_token",
        plus_token: "plus_token",
        minus_token: "minus_token",
        star_token: "star_token",
        slash_token: "slash_token",
        double_star_token: "double_star_token",
        double_slash_token: "double_slash_token",
        open_parenthesis_token: "open_parenthesis_token",
        close_parenthesis_token: "close_parenthesis_token",
        white_space_token: "white_space_token",
        identifier_token: "identifier_token",
        bang_token: "bang_token",
        double_ampersand_token: "double_ampersand_token",
        double_pipe_token: "double_pipe_token",
        double_equals_token: "double_equals_token",
        not_equals_token: "not_equals_token",
        less_or_equals_token: "less_or_equals_token",
        greater_or_equals_token: "greater_or_equals_token",
        less_than_token: "less_than_token",
        greater_than_token: "greater_than_token",
        equals_token: "equals_token",
        plus_equals_token: "plus_equals_token",
        minus_equals_token: "minus_equals_token",
        star_equals_token: "star_equals_token",
        slash_equals_token: "slash_equals_token",

        literal_expression: "literal_expression",
        unary_expression: "unary_expression",
        binary_expression: "binary_expression",
        parenthesized_expression: "parenthesized_expression",
        variable_expression: "variable_expression",
        assignment_expression: "assignment_expression",
        additional_assignment_expression: "additional_assignment_expression",

        true_keyword: "true_keyword",
        false_keyword: "false_keyword",
    }

    value = {
        plus_token: "+",
        minus_token: "-",
        star_token: "*",
        slash_token: "/",
        double_star_token: "**",
        double_slash_token: "//",
        open_parenthesis_token: "(",
        close_parenthesis_token: ")",
        bang_token: "!",
        double_ampersand_token: "&&",
        double_pipe_token: "||",
        double_equals_token: "==",
        not_equals_token: "!=",
        less_or_equals_token: "<=",
        greater_or_equals_token: ">=",
        less_than_token: "<",
        greater_than_token: ">",
        equals_token: "=",
        plus_equals_token: "+=",
        minus_equals_token: "-=",
        star_equals_token: "*=",
        slash_equals_token: "/=",
        true_keyword: "true",
        false_keyword: "false",
    }

    @classmethod
    def kind_exists(cls, kind):
        if kind in cls.str:
            return cls.str[kind]
        else:
            return None

    @classmethod
    def value_exists(cls, kind):
        if kind in cls.value:
            return cls.value[kind]
        else:
            return None

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
