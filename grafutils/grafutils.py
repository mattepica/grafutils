from grafanalib._gen import DashboardEncoder
import grafanalib.core as G
import json

class Dashboard(G.Dashboard):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.x = 0
        self.y = 0
        self.rowHeight = 0

    def add_panel(self, panel):
        if ( 24 - self.x ) < panel.width:
            self.x = 0
            self.y = self.y + self.rowHeight
            self.rowHeight = 0
        if self.rowHeight < panel.height:
            self.rowHeight = panel.height
        panel.gridPos = G.GridPos(x=self.x, y=self.y, w=panel.width, h=panel.height)
        panel.id= len(self.panels)
        self.panels = self.panels + [panel]
        self.x = self.x + panel.width

    def __str__(self):
        return json.dumps(
            self.to_json_data(),
            sort_keys=True,
            indent=2,
            cls=DashboardEncoder,
        )

class TimeSeries(G.TimeSeries):
    def __init__(self, width, height, **kwargs):
        super().__init__(
            **kwargs
        )
        self.width = width
        self.height = height

class Text(G.Text):
    def __init__(self, width, height, **kwargs):
        super().__init__(
            transparent = True,
            **kwargs
        )
        self.width = width
        self.height = height
