
class NATO:
    def __init__(self):
        self.nato_charset = self.initialize_charset()

    def initialize_charset(self):
        self.nato_charset = {}
        self.nato_charset['a'] = 'alpha'
        self.nato_charset['b'] = 'bravo'
        self.nato_charset['c'] = 'charlie'
        self.nato_charset['d'] = 'delta'
        self.nato_charset['e'] = 'echo'
        self.nato_charset['f'] = 'foxtrot'
        self.nato_charset['g'] = 'golf'
        self.nato_charset['h'] = 'hotel'
        self.nato_charset['i'] = 'india'
        self.nato_charset['j'] = 'juliett'
        self.nato_charset['k'] = 'kilo'
        self.nato_charset['l'] = 'lima'
        self.nato_charset['m'] = 'mike'
        self.nato_charset['n'] = 'november'
        self.nato_charset['o'] = 'oscar'
        self.nato_charset['p'] = 'papa'
        self.nato_charset['q'] = 'quebec'
        self.nato_charset['r'] = 'romeo'
        self.nato_charset['s'] = 'sierra'
        self.nato_charset['t'] = 'tango'
        self.nato_charset['u'] = 'uniform'
        self.nato_charset['v'] = 'victor'
        self.nato_charset['w'] = 'whiskey'
        self.nato_charset['x'] = 'xray'
        self.nato_charset['y'] = 'yankee'
        self.nato_charset['z'] = 'zulu'
        return self.nato_charset


    def alter_chars(self, msg):
        """
        Formats the input string by changing each character to its NATO equivalent.

        :param msg:
            Input string to encrypt.
        
        Returns:
            A string with required changes.
            0 if input is not string.
        """

        if not isinstance(msg, str):
            return 0

        out = ''
        # msg = msg.lower()

        for char in msg:
            if char.lower() in self.nato_charset.keys():
                out += self.nato_charset[char.lower()]
            else:
                out += '/'
        return out
