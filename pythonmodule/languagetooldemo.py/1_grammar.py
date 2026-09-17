import language_tool_python

tool = language_tool_python.LanguageTool("en-US")

text = "He go to school every day."
matches = tool.check(text)

print("Mistakes found:", len(matches))

for match in matches:
    print(match.message)
