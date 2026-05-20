import re
RUBY_RE = re.compile(r'\|([^《]+)《([^》]+)》')

def define_env(env):
    # マクロはここに書く
    @env.macro
    def asred(comment):
        return f'<span style=color:#FF0000;>{comment}</span>'
