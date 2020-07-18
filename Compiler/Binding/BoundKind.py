from Compiler.Type import Type


class BoundKind:
    unary_expression = 100
    literal_expression = 101
    binary_expression = 102
    variable_expression = 103
    variable_assignment_expression = 104

    identity = 200
    negation = 201
    logical_not = 202

    addition = 300
    subtraction = 301
    multiplication = 302
    division = 303
    power = 304
    root = 305
    logical_and = 306
    logical_or = 307
    double_equals = 308
    not_equals = 309
    less_or_equals = 310
    greater_or_equals = 311
    less_than = 312
    greater_than = 313

    _unary_result_types = {
        (Type.int_type, identity): Type.int_type,
        (Type.int_type, negation): Type.int_type,
        (Type.float_type, identity): Type.float_type,
        (Type.float_type, negation): Type.float_type,

        (Type.boolean_type, logical_not): Type.boolean_type
    }

    _binary_result_types = {
        # numbers
        (Type.int_type, addition, Type.int_type): Type.int_type,
        (Type.int_type, subtraction, Type.int_type): Type.int_type,
        (Type.int_type, multiplication, Type.int_type): Type.int_type,
        (Type.int_type, division, Type.int_type): Type.int_type,
        (Type.int_type, power, Type.int_type): Type.int_type,
        (Type.int_type, root, Type.int_type): Type.int_type,

        (Type.int_type, double_equals, Type.int_type): Type.boolean_type,
        (Type.int_type, not_equals, Type.int_type): Type.boolean_type,
        (Type.int_type, less_or_equals, Type.int_type): Type.boolean_type,
        (Type.int_type, greater_or_equals, Type.int_type): Type.boolean_type,
        (Type.int_type, less_than, Type.int_type): Type.boolean_type,
        (Type.int_type, greater_than, Type.int_type): Type.boolean_type,

        (Type.int_type, addition, Type.float_type): Type.float_type,
        (Type.int_type, subtraction, Type.float_type): Type.float_type,
        (Type.int_type, multiplication, Type.float_type): Type.float_type,
        (Type.int_type, division, Type.float_type): Type.float_type,
        (Type.int_type, power, Type.float_type): Type.float_type,
        (Type.int_type, root, Type.float_type): Type.float_type,

        (Type.int_type, double_equals, Type.float_type): Type.boolean_type,
        (Type.int_type, not_equals, Type.float_type): Type.boolean_type,
        (Type.int_type, less_or_equals, Type.float_type): Type.boolean_type,
        (Type.int_type, greater_or_equals, Type.float_type): Type.boolean_type,
        (Type.int_type, less_than, Type.float_type): Type.boolean_type,
        (Type.int_type, greater_than, Type.float_type): Type.boolean_type,

        (Type.float_type, addition, Type.int_type): Type.float_type,
        (Type.float_type, subtraction, Type.int_type): Type.float_type,
        (Type.float_type, multiplication, Type.int_type): Type.float_type,
        (Type.float_type, division, Type.int_type): Type.float_type,
        (Type.float_type, power, Type.int_type): Type.float_type,
        (Type.float_type, root, Type.int_type): Type.float_type,

        (Type.float_type, double_equals, Type.int_type): Type.boolean_type,
        (Type.float_type, not_equals, Type.int_type): Type.boolean_type,
        (Type.float_type, less_or_equals, Type.int_type): Type.boolean_type,
        (Type.float_type, greater_or_equals, Type.int_type): Type.boolean_type,
        (Type.float_type, less_than, Type.int_type): Type.boolean_type,
        (Type.float_type, greater_than, Type.int_type): Type.boolean_type,

        (Type.float_type, addition, Type.float_type): Type.float_type,
        (Type.float_type, subtraction, Type.float_type): Type.float_type,
        (Type.float_type, multiplication, Type.float_type): Type.float_type,
        (Type.float_type, division, Type.float_type): Type.float_type,
        (Type.float_type, power, Type.float_type): Type.float_type,
        (Type.float_type, root, Type.float_type): Type.float_type,

        (Type.float_type, double_equals, Type.float_type): Type.boolean_type,
        (Type.float_type, not_equals, Type.float_type): Type.boolean_type,
        (Type.float_type, less_or_equals, Type.float_type): Type.boolean_type,
        (Type.float_type, greater_or_equals, Type.float_type): Type.boolean_type,
        (Type.float_type, less_than, Type.float_type): Type.boolean_type,
        (Type.float_type, greater_than, Type.float_type): Type.boolean_type,

        # string
        (Type.string_type, addition, Type.string_type): Type.string_type,
        (Type.string_type, addition, Type.char_type): Type.string_type,

        (Type.char_type, addition, Type.string_type): Type.string_type,

        (Type.string_type, multiplication, Type.int_type): Type.string_type,
        (Type.int_type, multiplication, Type.string_type): Type.string_type,

        (Type.string_type, double_equals, Type.string_type): Type.boolean_type,
        (Type.string_type, not_equals, Type.string_type): Type.boolean_type,

        (Type.char_type, double_equals, Type.string_type): Type.boolean_type,
        (Type.char_type, not_equals, Type.string_type): Type.boolean_type,

        (Type.string_type, double_equals, Type.char_type): Type.boolean_type,
        (Type.string_type, not_equals, Type.char_type): Type.boolean_type,

        # char
        (Type.char_type, addition, Type.char_type): Type.string_type,

        (Type.string_type, multiplication, Type.int_type): Type.char_type,
        (Type.int_type, multiplication, Type.string_type): Type.char_type,

        (Type.char_type, double_equals, Type.char_type): Type.boolean_type,
        (Type.char_type, not_equals, Type.char_type): Type.boolean_type,

        # boolean
        (Type.boolean_type, logical_and, Type.boolean_type): Type.boolean_type,
        (Type.boolean_type, logical_or, Type.boolean_type): Type.boolean_type,

        (Type.boolean_type, double_equals, Type.boolean_type): Type.boolean_type,
        (Type.boolean_type, not_equals, Type.boolean_type): Type.boolean_type,
    }

    @classmethod
    def str(cls, kind):
        if kind == cls.unary_expression:
            return "unary_expression"
        elif kind == cls.literal_expression:
            return "literal_expression"
        elif kind == cls.binary_expression:
            return "binary_expression"

        elif kind == cls.identity:
            return "identity"
        elif kind == cls.negation:
            return "negation"
        elif kind == cls.logical_not:
            return "logical_not"

        elif kind == cls.addition:
            return "addition"
        elif kind == cls.subtraction:
            return "subtraction"
        elif kind == cls.multiplication:
            return "multiplication"
        elif kind == cls.division:
            return "division"
        elif kind == cls.power:
            return "power"
        elif kind == cls.root:
            return "root"
        elif kind == cls.logical_and:
            return "logical_and"
        elif kind == cls.logical_or:
            return "logical_or"
        elif kind == cls.double_equals:
            return "double_equals"
        elif kind == cls.not_equals:
            return "not_equals"
        elif kind == cls.less_or_equals:
            return "less_or_equals"
        elif kind == cls.greater_or_equals:
            return "greater_or_equals"
        elif kind == cls.less_than:
            return "less_than"
        elif kind == cls.greater_than:
            return "greater_than"

    @classmethod
    def resolve_unary_type(cls, syntax_kind, bound_operator_kind):
        if (syntax_kind, bound_operator_kind) in cls._unary_result_types:
            return cls._unary_result_types[(syntax_kind, bound_operator_kind)]
        return None

    @classmethod
    def resolve_binary_type(cls, left_syntax_kind, bound_operator_kind, right_syntax_kind):
        if (left_syntax_kind, bound_operator_kind, right_syntax_kind) in cls._binary_result_types:
            return cls._binary_result_types[(left_syntax_kind, bound_operator_kind, right_syntax_kind)]
        else:
            return None
