from rich.console import Console
from rich.table import Table
console=Console()
table=Table()
table.add_column("Name")
table.add_column("Marks")
table.add_row("Rahul","85")
table.add_row("Aman","92")
table.add_row("Rohit","78")
console.print(table)