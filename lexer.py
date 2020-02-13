#!/usr/bin/env python3
from token import Token

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.curr_char = ''
        self.char_idx = -1

    def get_next_char(self):
        self.char_idx += 1
        if self.char_idx < len(self.source_code):
            self.curr_char = self.source_code[self.char_idx] 
        else:
            self.curr_char = '\0'
    
    def read_next_char(self, next_char):
        self.get_next_char()
        if self.curr_char is not next_char:
            return False
        self.curr_char = ' '
        return True

    def create_new_num(self):
        num = ""
        if self.curr_char in ['*', '+']:
            num = self.curr_char
            self.get_next_char()
        else:
            while self.curr_char.isdigit():
                num += self.curr_char
                self.get_next_char()
        return num

    def create_new_ident(self):
        ident = ""
        while self.curr_char.isalpha():
            ident += self.curr_char
            self.get_next_char()
        return ident

    def create_new_str(self):
        str_val = ""
        self.get_next_char()
        while self.curr_char is not '\0' and self.curr_char is not '"':
            str_val += self.curr_char
            self.get_next_char()
        self.get_next_char()
        return str_val

    def lex(self):
        tokens = []
        while self.curr_char is not '\0':
            if self.curr_char.isalpha():
                tokens.append((Token.IDENT.name, self.create_new_ident()))
            elif self.curr_char.isdigit() or self.curr_char in ['*', '+']:
                tokens.append((Token.NUM.name, self.create_new_num()))
            elif self.curr_char is '(':
                tokens.append((Token.L_PAREN.name, self.curr_char))
                self.get_next_char()
            elif self.curr_char is ')':
                tokens.append((Token.R_PAREN.name, self.curr_char))
                self.get_next_char()
            elif self.curr_char is '"':
                tokens.append((Token.STRING.name, self.create_new_str()))
            elif self.curr_char in [' ', '\t', '\n', '']:
                self.get_next_char()
            elif self.curr_char is ',':
                tokens.append((Token.COMMA.name, self.curr_char))
                self.get_next_char()
            else:
                tokens.append((self.curr_char, self.curr_char))
                self.get_next_char()
        tokens.append((Token.EOF.name, ""))
        return tokens

