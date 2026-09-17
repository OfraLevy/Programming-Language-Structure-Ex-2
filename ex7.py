def clean_spaces(text):
    return text.strip()

def capitalize_text(text):
    return text.title()


def add_stars(text):
    return "***" + text + "***"


def create_pipeline():
    return lambda x: x


def add_to_pipeline(pipeline_fn, new_fn):
    return lambda x: new_fn(pipeline_fn(x))


if __name__ == '__main__':
    pipeline = create_pipeline()

    pipeline = add_to_pipeline(pipeline, clean_spaces)
    pipeline = add_to_pipeline(pipeline, capitalize_text)
    pipeline = add_to_pipeline(pipeline, add_stars)

    text = input("enter text:\n")

    if not text.strip():
        print("invalid input")
    else:
        print(pipeline(text))