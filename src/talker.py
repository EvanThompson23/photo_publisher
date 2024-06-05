import rclpy # type: ignore
from rclpy.node import Node # type: ignore
from sensor_msgs.msg import CompressedImage # type: ignore
from cv_bridge import CvBridge # type: ignore
import numpy as np # type: ignore
import cv2 as cv # type: ignore

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.br = CvBridge()
        self.image = cv.imread("./PNGs/images.jpeg", cv.IMREAD_GRAYSCALE)
        self.publisher_ = self.create_publisher(CompressedImage, "IDK", 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
    def timer_callback(self):
        self.publisher_.publish(self.br.cv2_to_compressed_imgmsg(self.image))
        self.get_logger().info('Publishing photo')

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