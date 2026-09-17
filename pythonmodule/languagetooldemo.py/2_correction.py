import language_tool_python

tool = language_tool_python.LanguageTool("en-US")

text = "I has a book."
corrected = tool.correct(text)

print("Original:", text)
print("Corrected:", corrected)
