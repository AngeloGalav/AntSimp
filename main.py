from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ColorProperty
from layout_classes import *

# load layout file
Builder.load_file('layout/layout.kv')

class GridCell(Widget):
    color = ColorProperty('#ffffff')
    # Change cell's color to pencil_color on a touch event
    # collides on press or drag (_move)
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.color = App.get_running_app().pencil_color
            return True
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            self.color = App.get_running_app().pencil_color
            return True
        return super().on_touch_move(touch)


class MainApp(App):
    pencil_color = ColorProperty('#ff0000ff')

    def build(self):
        self.title = "Stigmergy Simulation"
        self.icon = "res/ant.png"
        root = RootWidget()
        grid = root.ids.grid
        print(root.ids)
        for i in range(grid.rows * grid.cols):
            grid.add_widget(GridCell())
        return root

if __name__ == '__main__':
    MainApp().run()
