import rclpy # type: ignore
from rclpy.node import Node # type: ignore
from sensor_msgs.msg import CompressedImage # type: ignore
from cv_bridge import CvBridge #type: ignore
import cv2 #type: ignore
from sys import getsizeof

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.br = CvBridge()
        self.subscription = self.create_subscription(
            CompressedImage,
            "IDK",
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.bridge = CvBridge()

    def listener_callback(self, msg):
        self.get_logger().info('Receiving Photo')
        print(type(msg))
        print(getsizeof(msg))
        img = self.br.compressed_imgmsg_to_cv2(msg)
        print(type(img))
        print(getsizeof(img))
        cv2.imwrite('./PNGs/recieved.jpeg', img)
        

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
