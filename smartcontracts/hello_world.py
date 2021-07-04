from boa3.builtin import NeoMetadata, metadata, public
from boa3.builtin.interop.storage import put, get

@public
def Main() -> bool:
    put('hello', 'world')
    return True

@public
def hello() -> str:
    return bytes.to_str(get('hello'))