import grafutils as gu

d = gu.Dashboard(title="Hello").auto_panel_ids()

for x in range(4):
    d.add_panel(gu.Text(width=8,height=4,title=f"test{x}",description="test"))

print(d)
