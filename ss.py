from rich import print
from rich.progress import track

print("[bold cyan]Starting program...[/bold cyan]")

for i in track(range(5), description="Working"):
    pass

print("[bold green]Done![/bold green] ✅")
