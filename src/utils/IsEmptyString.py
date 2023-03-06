def is_empty_string(value: str) -> str:
  return (
    type(value) != str
    or value == None
    or len(value) == 0
  )
