from Compiler.Syntax.SyntaxKind import SyntaxKind


class Type:
    none_type = 0
    any_type = 1
    error_type = 2
    invalid_type = 3

    int_type = 10
    float_type = 11
    char_type = 12
    string_type = 13
    boolean_type = 14

    types = {
        SyntaxKind.int_token: int_type,
        SyntaxKind.float_token: float_type,
        SyntaxKind.char_token: char_type,
        SyntaxKind.string_token: string_type,
        SyntaxKind.true_keyword: boolean_type,
        SyntaxKind.false_keyword: boolean_type,
    }

    @classmethod
    def get_type(cls, syntax_kind):
        if syntax_kind in cls.types:
            return cls.types[syntax_kind]
        return cls.invalid_type

    @classmethod
    def str(cls, type):
        if type == cls.none_type:
            return "none_type"
        elif type == cls.any_type:
            return "any_type"
        elif type == cls.error_type:
            return "error_type"

        elif type == cls.int_type:
            return "int_type"
        elif type == cls.float_type:
            return "float_type"
        elif type == cls.char_type:
            return "char_type"
        elif type == cls.string_type:
            return "string_type"
        elif type == cls.boolean_type:
            return "boolean_type"
        else:
            return "invalid type"
