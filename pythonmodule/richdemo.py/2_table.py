from rich.table import Table
from rich.console import Console
table = Table(title="Student Data")
table.add_column("Name")
table.add_column("Marks")
table.add_row("Ajay", "80")
table.add_row("Rahul", "75")
Console().print(table)
