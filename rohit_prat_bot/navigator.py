class Navigator:
    def __init__(self, image_paths):
        self.image_paths = image_paths
        self.index = 0

    def current_image(self):
        return self.image_paths[self.index]

    def next_image(self):
        self.index = (self.index + 1) % len(self.image_paths)
        return self.current_image()

    def previous_image(self):
        self.index = (self.index - 1) % len(self.image_paths)
        return self.current_image()
