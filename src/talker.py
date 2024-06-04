import rclpy # type: ignore
from rclpy.node import Node # type: ignore
from PIL import Image as img, ImageOps
from sensor_msgs.msg import Image # type: ignore
import numpy as np # type: ignore
import cv2 as cv # type: ignore

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        topic = input("Enter topic: ")
        image_RGB = img.open("./PNGs/images.jpeg")
        self.image = ImageOps.grayscale(image_RGB)
        self.publisher_ = self.create_publisher(Image, topic, 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Image()
        msg.height = self.image.height
        msg.width = self.image.width
        msg.encoding = "rgb8"
        msg.is_bigendian = False
        msg.step = 3 * self.image.width
        msg.data = np.array(self.image).tobytes()
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()