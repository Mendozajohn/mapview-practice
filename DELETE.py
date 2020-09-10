import sys

from kivy.base import runTouchApp
from kivy.lang import Builder

if __name__ == '__main__' and __package__ is None:
    from os import path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


root = Builder.load_string(
    """
#:import sys sys
#:import MapSource kivy_garden.mapview.MapSource
MapView:
    lat: 50.6394
    lon: 3.057
    zoom: 13
    map_source: MapSource(sys.argv[1], attribution="") if len(sys.argv) > 1 else "osm"
    MapMarkerPopup:
        lat: 50.6394
        lon: 3.057
        popup_size: dp(230), dp(130)
        Bubble:
            BoxLayout:
                orientation: "horizontal"
                padding: "5dp"
                AsyncImage:
                    source: "https://scontent.fmnl17-1.fna.fbcdn.net/v/t1.0-9/97391292_1435478759991103_6175061857997422592_o.jpg?_nc_cat=100&_nc_sid=09cbfe&_nc_ohc=f-mPvs123EUAX_PV_vM&_nc_ht=scontent.fmnl17-1.fna&oh=6200a082c19b01175ab4776cb4680e81&oe=5F817D1F"
                    mipmap: True
                Label:
                    text: "[b]Lille[/b]\\n1 154 861 hab\\n5 759 hab./km2"
                    markup: True
                    halign: "center"
    MapMarkerPopup:
        lat: 50.6594
        lon: 3.057
        popup_size: dp(230), dp(130)
        Bubble:
            BoxLayout:
                orientation: "horizontal"
                padding: "5dp"
                AsyncImage:
                    source: "https://scontent.fmnl17-1.fna.fbcdn.net/v/t1.0-9/97391292_1435478759991103_6175061857997422592_o.jpg?_nc_cat=100&_nc_sid=09cbfe&_nc_ohc=f-mPvs123EUAX_PV_vM&_nc_ht=scontent.fmnl17-1.fna&oh=6200a082c19b01175ab4776cb4680e81&oe=5F817D1F"
                    mipmap: True
                Label:
                    text: "[b]Lille[/b]\\n1 154 861 hab\\n5 759 hab./km2"
                    markup: True
                    halign: "center" 
"""
)

runTouchApp(root)
