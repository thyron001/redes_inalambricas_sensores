import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import matplotlib.pyplot as plt
import re

class PlotterNode(Node):
    def __init__(self):
        super().__init__('plotter_node')
        self.subscription = self.create_subscription(
            String,
            'sensor_data',
            self.listener_callback,
            10)
        self.temperaturas = []
        self.timer = self.create_timer(5.0, self.generar_grafico)

    def listener_callback(self, msg):
        match = re.search(r'(\d+)', msg.data)
        if match:
            self.temperaturas.append(int(match.group(1)))
            self.get_logger().info(f'Dato recibido: {msg.data}')

    def generar_grafico(self):
        if not self.temperaturas:
            return
        plt.figure()
        plt.plot(self.temperaturas, marker='o', color='blue')
        plt.title('Temperatura del Sensor')
        plt.xlabel('Muestra')
        plt.ylabel('Temperatura (°C)')
        plt.grid(True)
        plt.savefig('/ros2_ws/data/sensor_plot.png')
        plt.close()
        self.get_logger().info('Grafico guardado en /ros2_ws/data/sensor_plot.png')

def main(args=None):
    rclpy.init(args=args)
    node = PlotterNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
