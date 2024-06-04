import rclpy # type: ignore
from rclpy.node import Node # type: ignore
from sensor_msgs.msg import Image # type: ignore
from cv_bridge import CvBridge #type: ignore
import cv2 #type: ignore

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        topic = input("Enter topic: ")
        self.subscription = self.create_subscription(
            Image,
            topic,
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.bridge = CvBridge()

    def listener_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding="8UC3")
            if cv_image is not None:
                cv2.imshow("Received Image", cv_image)
                cv2.waitKey(1)
                # Save the image
                filename = 'received_image.jpg'
                cv2.imwrite(filename, cv_image)
                self.get_logger().info(f"Image saved as {filename}")
            else:
                self.get_logger().warning("Received image is None")
        except Exception as e:
            self.get_logger().error(f"Error processing image: {str(e)}")


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
