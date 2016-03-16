'''
Created on 16.03.2016

@author: Yingxiong
'''
from kivy.garden.graph import Graph, MeshLinePlot
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class CanvasApp(App):

    @property
    def cracking_wid(self):
        graph = Graph(x_ticks_minor=5,
                      x_ticks_major=100, y_ticks_major=100,
                      y_grid_label=True, x_grid_label=True, padding=5,
                      x_grid=True, y_grid=True, xmin=0, xmax=1000, ymin=0, ymax=1000)
        self.rect = MeshLinePlot(color=[1, 0, 0, 1])
        self.rect.points = self.draw_rect(500, 500, 400, 400)
        graph.add_plot(self.rect)
        return graph

    @staticmethod
    def draw_rect(x, y, l, w):
        return [(x - l / 2., y - w / 2.), (x + l / 2., y - w / 2.), (x + l / 2., y + w / 2.), (x - l / 2., y + w / 2.), (x - l / 2., y - w / 2.)]

    def on_touch_move(self, touch):
        self.rect.points = self.draw_rect(touch.x, touch.y, 400, 400)

    def build(self):
        root = BoxLayout(orientation='vertical')
        root.on_touch_move = self.on_touch_move
        root.add_widget(self.cracking_wid)
        return root
if __name__ == '__main__':
    CanvasApp().run()
