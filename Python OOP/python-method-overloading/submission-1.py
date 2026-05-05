class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, first_text: str, second_text: str = None) -> str:
        if second_text is None:
            return first_text.upper()
        else:
            return first_text + second_text



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
